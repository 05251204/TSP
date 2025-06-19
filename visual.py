import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection 
import pandas as pd
import numpy as np

def visualize(path):
  df=pd.read_csv("data.csv")
  x=df['x']
  y=df['y']
  n=len(x)
  ans_df=pd.read_csv(path)
  ans=ans_df['0']

  fig=plt.figure()
  ax=fig.add_subplot(111)
  ax.scatter(x,y)
  ax.scatter(x[ans[0]],y[ans[0]],c='r')
  ax.scatter(x[ans[n-1]],y[ans[n-1]],c='r')
  ims=[]
  for i in range(n-1):
    x1=x[ans[i]]
    x2=x[ans[i+1]]
    y1=y[ans[i]]
    y2=y[ans[i+1]]
    if x1>x2:
      x1,x2=x2,x1
      y1,y2=y2,y1
    slope=(y2-y1)/(x2-x1+0.1)
    X = np.arange(x1,x2+0.1,0.1)
    Y = slope*X-slope*x1+y1
    ax.plot(X,Y,color='blue')
    #im=ax.plot(X,Y,color='blue')
    #ims.append(fig)
    #plt.savefig("fig/fig"+str(i)+".png")
  #ani = animation.ArtistAnimation(fig, ims,interval = 100)
  #ani.save("fool.gif", writer="pillow")
  plt.show()


visualize("ans_fool.csv")

