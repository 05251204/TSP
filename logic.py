import pandas as pd
import math
import time
import random


#now=0-indexed
def calc_fool(now):
  df=pd.read_csv('data.csv')
  x=df['x']
  y=df['y']
  n=len(x)

  if now>=n:
    print("error! now>=n")
    exit()

  dist=[]
  dist_sum=0
  for i in range(n):
    li=[]
    for j in range(n):
      li.append(math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))
    dist.append(li)

  ans=[]
  ans.append(now)
  go=[False for i in range(n)]
  go[now]=True

  for  i in  range(n-1):
    val=1e10
    idx=-1
    for j in range(n):
      if not go[j]:
        if val>dist[now][j]:
          val=dist[now][j]
          idx=j
    dist_sum+=val
    now=idx
    ans.append(now)
    go[now]=True
  ans_df=pd.DataFrame(ans)
  ans_df.to_csv('ans_fool.csv')
  print(dist_sum)



def calc_opt(now):
  df=pd.read_csv('data.csv')
  x=df['x']
  y=df['y']
  n=len(x)
  ans_df=pd.read_csv('ans_fool.csv')
  ans_global=[ans_df['0']]
  ans_global=ans_global[0]

  dist=[]
  for i in range(n):
    li=[]
    for j in range(n):
      li.append(math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))
    dist.append(li)

  t1=time.time()

  dist_global=0
  for i in range(n-1):
    dist_global+=dist[ans_global[i]][ans_global[i+1]]
  rep_cnt=0
  while 1:
    ans=ans_global
    """
    p1=random.randint(0,n-2)#[0,n-2]
    p2=random.randint(0,n-2)
    p3=random.randint(0,n-2)
    p4=random.randint(0,n-2)
    ans[p1+1],ans[p3+1]=ans[p3+1],ans[p1+1]
    ans[p2+1],ans[p4+1]=ans[p4+1],ans[p2+1]
    """
    for i in range(1,n-1):
      for j in range(i+1,n-1):
        dist_bef=dist[ans[j-1]][ans[j]]+dist[ans[i-1]][ans[i]]
        dist_aft=dist[ans[j-1]][ans[i]]+dist[ans[i-1]][ans[j]]
        if dist_bef>dist_aft:
          ans[j],ans[i]=ans[i],ans[j]
    dist_=0
    for i in range(n-1):
      dist_+=dist[ans[i]][ans[i+1]]
    if dist_global>dist_:
      dist_global=dist_
      ans_global=ans
    t2=time.time()
    if t2-t1>6:
      break
    rep_cnt+=1
  ans_df=pd.DataFrame(ans_global)
  ans_df.to_csv('ans_opt.csv')
  print(dist_global)
  print(rep_cnt)




print("_loading_")
calc_opt(0)
print("end!")