import json

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
        artistlist[x['artistName']] = x['msPlayed']
    else: 
        artistlist[x['artistName']] = artistlist[x['artistName']] + x['msPlayed']

for x in artistlist:
    artistlist[x] = float('%.3f'%(artistlist[x]/(1000.0*60*60)))

topArtists = sorted(artistlist.items(),key=lambda item: item[1], reverse = True)[:20]

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

topSongs = sorted(tracklist.items(),key=lambda item: item[1]['time'], reverse = True)[:20]

print(topSongs)


