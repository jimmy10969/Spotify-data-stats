import json
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='Arguments for dData')

    parser.add_argument('--number',
                        required=False,
                        action='store',
                        nargs="?", 
                        const="default",
                        default="50",
                        help='number of songs and artist')

    parser.add_argument('--sortBy',
                        required=False,
                        action='store',
                        nargs="?", 
                        const="default",
                        default="time",
                        help='parameter to sort by')
    
    args = parser.parse_args()

    return args

args = get_args()

numberToShow = args.number

if int(numberToShow) > 200 :
    numberToShow = 200

sortBy = args.sortBy

if sortBy != 'time' and sortBy != 'plays' :
    sortBy = 'time'

data = []    
i = 0

while True:
    try:
      with open('C:\\Users\\jimmy\\Desktop\\spotify-data-stats\\Spot\\StreamingHistory' + str(i) + '.json',encoding="utf-8") as js:
          data = data + json.load(js)
      i = i +1
    except:
      break

artistlist = {}

for x in data: 
    if x['artistName'] not in artistlist:
        artistlist[x['artistName']] = { 'time': x['msPlayed'], 'plays': 1}
    else: 
       artistlist[(x['artistName'])]['time'] = artistlist[(x['artistName'])]['time'] + x['msPlayed']
       artistlist[(x['artistName'])]['plays'] = artistlist[(x['artistName'])]['plays'] + 1

for x in artistlist:
    artistlist[x]['time'] = float('%.3f'%(artistlist[x]['time']/(1000.0*60*60)))

topArtists = sorted(artistlist.items(),key=lambda item: item[1][sortBy], reverse = True)[:int(numberToShow)]

print(topArtists)
print("-----------------------------------------------------------------------")

tracklist = {}

for x in data: 
    if (x['trackName'], x['artistName']) not in tracklist:
        tracklist[(x['trackName'],x['artistName'])] ={ 'time': x['msPlayed'], 'plays': 1}
    else:
        tracklist[(x['trackName'],x['artistName'])]['time'] = tracklist[(x['trackName'],x['artistName'])]['time'] + x['msPlayed']
        tracklist[(x['trackName'],x['artistName'])]['plays'] = tracklist[(x['trackName'],x['artistName'])]['plays'] + 1
      
    
for x in tracklist:
    tracklist[x]['time'] = float('%.3f'%(tracklist[x]['time']/(1000.0*60*60)))

topSongs = sorted(tracklist.items(),key=lambda item: item[1][sortBy], reverse = True)[:int(numberToShow)]

print(topSongs)

print("-----------------------------------------------------------------------")

topSongsByArtists = {}

for y in topSongs:
   if y[0][1] not in topSongsByArtists:
        topSongsByArtists[y[0][1]] =  1
   else: 
       topSongsByArtists[y[0][1]] = topSongsByArtists[y[0][1]] + 1

print(topSongsByArtists)


