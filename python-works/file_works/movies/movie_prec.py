movie_path="python-works\\file_works\\movies\\movies_data.csv"
top_path="python-works\\file_works\\movies\\top_rated.csv"
genre_count="python-works\\file_works\\movies\\genre_count.txt"
sor_mov="python-works\\file_works\\movies\\sorted_movie.csv"
fr=open(movie_path,"r")
import csv
read=csv.DictReader(fr)

data=[row for row in read]
#print(data)

first_5_row=[data[i] for i in range(0,6)]
#print(first_5_row)

movie_count=len(data)
#print("number of movies:",movie_count)

key_names=[key for d in data for key in d.keys()]
#print(set(key_names))

"""year=int(input("enter the movie year to be searched: "))
year_movie=[d.get("Film") for d in data if d.get("Year")==str(year)]
print(year_movie)"""

movie_score={d.get("Film"):int(d.get("Rotten Tomatoes %")) for d in data}
max_score=max(movie_score.values())
highest_score_movie={k:v for k,v in movie_score.items() if v==max_score}
#print(highest_score_movie)

"""gen=input("enter agenre: ")
genre_movie=[d.get("Film") for d in data if d.get("Genre").casefold() == gen]
#print(genre_movie)"""

fw=open(top_path,"w")
for k,v in movie_score.items():
    if v>=80:
        fw.write(str(k) + "\n")

gc=open(genre_count,"w")
count=[]
for d in data:
    count.append(d.get("Genre"))
gen_co={}
for c in count:
    if c in gen_co:
        gen_co[c]+=1
    else:
        gen_co[c]=1

#gc.write(str(gen_co))

sm=open(sor_mov,"w")
movie_sort=sorted(data,key=lambda k:k.get("Rotten Tomatoes %"))
for d in data:
    fil=d.get("Film")
    sco=d.get("Rotten Tomatoes %")
    sm.write(fil+" "+sco+"\n")
