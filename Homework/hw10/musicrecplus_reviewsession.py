'''

Jerry Cheng

Partner: Reilly Fitzgerald

Created on 12 November 2018

I pledge my honor that I have abided by the Stevens Honor System.

'''

pref_file = "musicrecplus.txt"

def main():

def loadusers(pref_file):
    try:
        open(pref_file, 'r')
    except:
        open(pref_file, 'w')
        dict = {}
        pref_file.close()
        return dict
    dict = {}
    for line in pref_file:
        user, artists = line.strip().split(':')
        list_of_artists = [artists.split(',')]
        dict[user] = artists
        pref_file.close()
        return dict

def get_preferences(dict, username, pref_file):
    new_pref = input("Enter an artist that you like (Enter to finish):")
    pref_holder = []
    while new_pref != '':
        pref_holder.append(new_pref)
        input("Enter an artist that you like (Enter to finish):")
    pref_holder.sort()
    save_preferences(username, dict, pref_file, pref_holder)

def save_preferences(username, dict, pref_file, pref_holder):
    dict[username] = pref_holder
    open(pref_file, 'w')
    for user in dict:
        newline = str(user) + ":" + ",".join(dict[user]) + "\n"
        pref_file.write(newline)
    pref_file.close()

def get_recs(username, usermap):
    possible_users = []
    users = usermap.keys()
    for user in users:
        if user[-1] != '$':
            possible_users.append(user)
    bestuser = None
    for user in possible_users:
        if usermap[user] != usermap[username]:
            currprefs = usermap[user]
            mainprefs = usermap[username]
            matches = 0
            i = 0
            j = 0
            num_matches(currprefs, mainprefs)


def menu(username, usermap):
    while True:
        print(menu)
        choice = input("Enter a letter to choose an option:" + )
        getinput = choice
        if choice is "e":
            get_preferences(username, usermap, pref_file)
        elif choice is "r":
            rec = get_recs
            print(recs(recs, username))
            prefs = usermap[username]
            save users
        elif choice is "p":
            best_artists(usermap)
        elif choice is "h":
            how_artists(usermap)
        elif choice is "m":
            most_likes(usermap)
        elif choice is "q":
            try:
                save user_preferences(username, usermap, pref_file, usermap[username])
                break
            except:
                break