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
  path=ans_df['0'].tolist()

  dist=[]
  for i in range(n):
    li=[]
    for j in range(n):
      li.append(math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))
    dist.append(li)

  t_start=time.time()

  # Calculate initial path length (not a closed loop)
  path_length = sum(dist[path[i]][path[i+1]] for i in range(n - 1))
  print(f"Initial path length: {path_length}")

  improved = True
  while improved:
    improved = False
    # Iterate through all pairs of non-adjacent edges to perform a 2-opt swap.
    # Edge 1: (path[i], path[i+1]), Edge 2: (path[j], path[j+1])
    # We ensure j > i + 1 so the edges are not adjacent.
    for i in range(n - 2):
      for j in range(i + 2, n - 1):
        p_i, p_i1 = path[i], path[i+1]
        p_j, p_j1 = path[j], path[j+1]

        # Cost of original edges
        current_edge_dist = dist[p_i][p_i1] + dist[p_j][p_j1]
        # Cost of new edges after reversing the segment path[i+1...j]
        new_edge_dist = dist[p_i][p_j] + dist[p_i1][p_j1]

        if new_edge_dist < current_edge_dist:
          # Perform the swap by reversing the segment
          path[i+1:j+1] = path[i+1:j+1][::-1]

          # Update total distance with the difference
          path_length += new_edge_dist - current_edge_dist
          improved = True
          break  # Exit inner loop and restart search
      if improved:
        break  # Exit outer loop and restart search

    if time.time() - t_start > 10: # Time limit
      print("Time limit exceeded.")
      break
      
  ans_df=pd.DataFrame(path)
  ans_df.to_csv('ans_opt.csv')
  print(f"Final optimized path distance: {path_length}")
  




print("_loading_")
calc_fool(0)
calc_opt(0)
print("end!")