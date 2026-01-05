file_path="python-works\\file_works\\insta\\Instagram_Analytics.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
reading=csv.DictReader(fr)

data=[row for row in reading]

#entry with max likes
max_like=max(data,key=lambda d:int(d.get("likes")))
#print(max_like)

#average comments per post
post_comment={d.get("post_id"):int(d.get("comments")) for d in data}
com_sum=0
for k,v in post_comment.items():
    com_sum+=v
#print(f"Average comment per post: {round(com_sum/len(data),2)}")

#most engaging media type
engaging={}
for d in data:
    med=d.get("media_type")
    eng=float(d.get("engagement_rate"))

    if med in engaging:
        engaging[med]+=eng
    else:
        engaging[med]=eng
most_eng=[k for k,v in engaging.items() if v==max(engaging.values())]
#print(most_eng)

#most shared content type
catogary={}
for d in data:
    cato=d.get("content_category")
    share=int(d.get("shares"))
    if cato in catogary:
        catogary[cato]+=share
    else:
        catogary[cato]=share
most_share=[k for k,v in catogary.items() if v==max(catogary.values())]
#print(most_share)


#change in reach according to hashtag 
many_hashtag=max(data,key=lambda d:int(d.get("hashtags_count")))
less_hashtag=min(data,key=lambda d:int(d.get("hashtags_count")))
#print(many_hashtag.get("media_type"),many_hashtag.get("reach"))
#print(less_hashtag.get("media_type"),less_hashtag.get("reach"))

#most follower gained content type
follow={}
for d in data:
    cato=d.get("content_category")
    foll=int(d.get("followers_gained"))
    if cato in follow:
        follow[cato]+=foll
    else:
        follow[cato]=foll
most_followed=[k for k,v in follow.items() if v==max(follow.values())]
#print(most_followed)

#most follower gained traffic source
traffic={}
for d in data:
    traff=d.get("traffic_source")
    reach=int(d.get("reach"))
    if traff in traffic:
        traffic[traff]+=reach
    else:
        traffic[traff]=reach
most_reach=[k for k,v in traffic.items() if v==max(traffic.values())]
#print(most_reach)

#post that has highest follower gain
higest_gain=max(data,key=lambda d:int(d.get("followers_gained")))
#print(higest_gain.get("post_id"))

#engaement value calculation
engagemnt_rate=0
enga={}
for d in data:
    med=d.get("content_category")
    like=int(d.get("likes"))
    share=int(d.get("shares"))
    reach=int(d.get("reach"))
    engagemnt_rate=round((like+share)/reach*100,2)
    for med in enga:
        enga[med]+=engagemnt_rate
    else:
        enga[med]=engagemnt_rate
#print(enga)

#catogories and like percentage and its max
ca={}
l_sum=0
for d in data:
    cato=d.get("content_category")
    like=int(d.get("likes"))
    l_sum+=like
    if cato in ca:
        ca[cato]+=like
    else:
        ca[cato]=like
rank={}
for k,v in ca.items():
    v=round(v/l_sum*100,2)
    rank[k]=v   
#print(rank)
#print(max(rank,key=lambda r:rank.get(r)))
