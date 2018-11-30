'''
Author: Andrew Chinique @achiniqu
Instructor: Professor Naumann
Course: Introduction to Computer Science (CS115)
Due Date: 2018-11-14

HW 10 -- Music Recommender Plus

I pledge my honor that I have abided by the Stevens Honor System.
                                            -- Andrew Chinique
'''

PREF_FILE = "musicrecplus.txt"

def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!")
    userName = input("Please enter your name: ")
    print("Welcome, " + userName)
    menuLoop(userName, userMap)


def menuLoop(userName, userMap):
    '''Continuously prints the menu until the user decides to quit.'''
    while True:
        print("Enter a letter to choose an option:")
        print("e - enter preferences")
        print("r - get recommendations")
        print("p - show most popular artists")
        print("h - how popular is the most popular")
        print("m - which user has the most likes")
        print("q - save and quit")
        userSelect = input()
        if userSelect == "e":
            prefs = getPreferences(userName, userMap)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        elif userSelect == "r":
            prefs = getPreferences(userName, userMap)
            recs = getRecommendations(userName, prefs, userMap)
            if recs == []:
                print("No recommendations available at this time.")
            else:
                print(recs, userName)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        elif userSelect == "p":
            printMostPopularArtists(userMap)
        elif userSelect == "h":
            print(howPopular(userMap))
        elif userSelect == "m":
            print(mostLikes(userMap))
        elif userSelect == "q":
            try:
                saveUserPreferences(userName, prefs, userMap, PREF_FILE)
                break
            except:
                break
        else:
            print("Invalid option, try again")
            menuLoop(userName, userMap)


def printRecs(recs, userName):
    '''Print the user's recommendations'''
    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
        print("for you right now.")
    else:
        print(userName + "," + " based on the users I currently")
        print("know about, I believe you might like:")
        for artist in recs:
            print(artist)
        print("I hope you enjoy them! I will save your")
        print("preferred artists and have new")
        print(" recommendations for you in the future")


def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict


def getPreferences(userName, userMap):
    ''' Returns a list of the user's preferred artists.
        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        newPref = input("like, or just press enter to continue: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: ")

    while newPref != '':
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        newPref = input("like, or just press enter to continue: ")

    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs


def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser == None:
        return []
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations


def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser


def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    return list3


def numMatches(list1, list2):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def mostPopularArtists(userMap):
    '''Returns the most popular artist or artists'''
    users = userMap.keys()
    Freqs = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        for artist in userMap[user]:
            if artist in Freqs:
                popularity_count = Freqs[artist]
                popularity_count += 1
                Freqs[artist] = popularity_count
            else:
                Freqs[artist] = 1
    for artist in Freqs:
        if Freqs[artist] > maxlikes:
            maxlikes = Freqs[artist]

    for artist in Freqs:
        if Freqs[artist] == maxlikes:
            mostpop += [artist]
    return mostpop


def printMostPopularArtists(userMap):
    '''Prints the most popular artist or artists.'''
    mostpop = mostPopularArtists(userMap)
    if len(mostpop) == 1:
        print(str(mostpop[0]) + " is the most popular artist in the database!")
    else:
        print(str(mostpop) + " are the most popular artists in the database!")


def howPopular(userMap):
    '''Prints the number of users that like the most popular artist.'''
    users = userMap.keys()
    Freqs = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        for artist in userMap[user]:
            if artist in Freqs:
                popularity_count = Freqs[artist]
                popularity_count += 1
                Freqs[artist] = popularity_count
            else:
                Freqs[artist] = 1
    for artist in Freqs:
        if Freqs[artist] > maxlikes:
            maxlikes = Freqs[artist]

    for artist in Freqs:
        if Freqs[artist] == maxlikes:
            mostpop += [artist]

    if len(mostpop) > 1 or len(mostpop) == 0:
        print("Sorry, there is no single-most popular artist.")
    else:
        print(str(Freqs[mostpop[0]]) + " users like the most popular artist, " + str(mostpop[0]))


def mostLikes(userMap):
    '''Finds the user with the most likes (assuming they haven't opted out) and prints their username and preferences.'''
    likesDic = {}
    L = list(userMap.keys())
    for i in userMap:
        likesDic[i] = 0
        for j in userMap[i]:
            likesDic[i] += 1
    likes = max(likesDic.values())
    anotherDic = {}
    for i in likesDic:
        if likesDic[i] == likes:
            anotherDic[i] = likes
    L2 = list(anotherDic.keys())
    for keys, values in userMap.items():
        if keys in L2:
            if '$' in keys:
                print('This user has opted out of this feature.')
                return 'NA', values
            else:
                return keys, values


def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                 "\n"
        file.write(toSave)
    file.close()


if __name__ == "__main__": main()
