file_path="python-works\\file_works\\spotify\\spotify_data.csv"

fr=open(file_path,"r",encoding="utf-8")

import csv
reader=csv.DictReader(fr)
data=[row for row in reader]

fir_fiv_name=[d.get("track_name") for d in data][:5]
#print(fir_fiv_name)

total_track=len(data)
#print(total_track)

artists={d.get("artist_name"):d.get("artist_popularity") for d in data}
#print(artists.keys())

explicit=[d for d in data if d.get("explicit")=="TRUE"]
#print(len(explicit))

popu_fifty=[d.get("track_name") for d in data if int(d.get("track_popularity"))>50]
#print(popu_fifty)

track_pop={d.get("track_name"):d.get("track_popularity") for d in data}
max_pop={k:v for k,v in track_pop.items() if v==max(track_pop.values())}
#print(max_pop)

sum=0
for k,v in track_pop.items():
    v=int(v)
    sum+=v
#print(round(sum/len(track_pop)))

album_c=[d.get("album_name") for d in data]
coual={}
for a in album_c:
    if a in coual:
        coual[a]+=1
    else:
        coual[a]=1
#print(coual) 

"""artist=input("enter artist name: ")
artist_album=[d.get("track_name") for d in data if d.get("artist_name")==artist]
#print(artist_album)"""

track_dur={d.get("track_name"):float(d.get("track_duration_min")) for d in data}
max_dur={k:v for k,v in track_dur.items() if v==max(track_dur.values())}
#print(max_dur)

artist_foll={d.get("artist_name"):int(d.get("artist_followers")) for d in data}
sort_foll=sorted(artist_foll,key=lambda k:artist_foll.get(k),reverse=True)[:5]
#print(sort_foll)

explicit=[d.get("explicit") for d in data]
ex_co={}
for ex in explicit:
    if ex in ex_co:
        ex_co[ex]+=1
    else:
        ex_co[ex]=1
#print(ex_co)

gen=[d.get("artist_genres") for d in data]
gen_co={}
for g in gen:
    if g in gen_co:
        gen_co[g]+=1
    else:
        gen_co[g]=1
#print(gen_co)

artists=[d.get("artist_name") for d in data]
ar_co={}
for a in artists:
    if a in ar_co:
        ar_co[a]+=1
    else:
        ar_co[a]=1
max_artist={k:v for k,v in ar_co.items() if v==max(ar_co.values())}
print(max_artist)