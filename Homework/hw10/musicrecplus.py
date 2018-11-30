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
# A very simple music recommender system.

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = ""
    try:
        file = open(PREF_FILE, 'r')
    except:
        FileNotFoundError
    if file == "":
        file = open(PREF_FILE, 'w')
        file.close()
        file = open(PREF_FILE, 'r')
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
    ''' Returns a list of the uesr's preferred artists.
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
        print("Please enter the name of an artist")
        newPref = input("that you like (press Enter to end): ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist")
        newPref = input("that you like (press Enter to end): " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter the name of an artist")
        newPref = input("that you like (press Enter to end): ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.'''
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser == None:
        return []
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations
 
def findBestUser(curretUser, prefs, userMap):
    """Returns the user with the most common prefs as the current User"""
    users = list(userMap.keys())
    for i in users:
        if i[-1] == '$':
            users.remove(i)
    bestScore = -1
    bestMatch = None
    for user in users:
        score = numMatches(prefs, userMap[user])
        if prefs != userMap[user]:
            if score > bestScore:
                bestScore = numMatches(prefs, userMap[user])
                bestMatch = user
    return bestMatch

def drop(list1, list2):
    '''Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    for i in list2:
        if i not in list1:
            list3 += [i]
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    same = 0
    for i in list1:
        if i in list2:
            same += 1
    return same

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

def artistList(userMap):
    '''Returns a list of artists, filtered so every artist only appears once.'''
    artistList = []
    filteredList = []
    for user in userMap:
        artistList += userMap[user]
    for artist in artistList:
        if artist not in filteredList:
            filteredList += [artist]
    return filteredList

def listToDict(lst):
    '''Converts the list of artist to a dictionary each associated with 0 occurences'''
    artistDict = {}
    for i in lst:
        artistDict[i] = 0
    return artistDict

def mostPopular(file):
    '''returns the most popular artist in the given group of users in the file.'''
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        if len(userMap) ==1:
            for artist in userMap[user]:
                print(artist)
        else:
            for artist in userMap[user]:
                artDict[artist] += 1
    x = 0
    y = ''
    for artist in list(artDict.keys()):
        if artDict[artist] > x:
            x = artDict[artist]
            y = artist
    return y

def howPopular(file):
    '''Returns the number of users who like the most popular artist.''' 
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        for artist in userMap[user]:
            artDict[artist] += 1
    x = 0
    for artist in list(artDict.keys()):
        if artDict[artist] > x:
            x = artDict[artist]
    return x

def mostLikes(fileName):
    '''Returns the user with the most likes, unless their name ends with '$', opting them out.'''
    userMap = loadUsers(fileName)
    x = 0
    for user in userMap:
        if user[-1] != '$':
            if len(userMap[user]) > x:
                x = len(userMap[user])
                y = user
    return y
            
def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!\n")

    userName = input("Please enter your name (put a $ symbol after your name if you wish your preferences to remain private: ")
    print ("\nWelcome,", userName, '\n')
    
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
            print(mostPopular(userMap))
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

if __name__ == "__main__": main()
