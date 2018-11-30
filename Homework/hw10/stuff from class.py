def read_print_prefs(filename):
    input_file = open(filename, 'r')
    for line in input_file:
        user, artists = line.split(':')
        artistList = artists.split(',')
        for i in range(len(artistList)):
            artistList[i] = artistlist[i].strip()
        user = user.strip()
        print(user + ' : ' + str(artistList)
    input_file.close()
              
def write_prefs(filename):
    output_file = open(filename, 'w')
    lines = sample_content.split('\n')
    for line in lines:
        output_file.write(line + '\n')
    ## UNFINISHED
