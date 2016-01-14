import os 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.mlab as mlab
from matplotlib.pyplot import figure

ph = os.path.expanduser('~/public_html')
fig,ax=plt.subplots()
x=np.arange(0, 3*np.pi , 0.20)
ax.axis([0,10,-1,1])
#Setting background color
ax.set_axis_bgcolor('white')

#Draw a series of circle on sin ant its inverse function 
circle_line, =ax.plot(x,np.sin(x), 'o', markerfacecolor='silver', markeredgecolor='red',
markersize=15, markeredgewidth = 5)
circle_line1, =ax.plot(x,np.sin(-x), 'o', markerfacecolor='gold', markeredgecolor='blue',
markersize=15, markeredgewidth = 5)

#Draw the sin and its inverse function
line, = ax.plot(x,np.sin(x),color='blue',linestyle='-',linewidth=4)
line1,=ax.plot(x,np.sin(-x),color='red',linestyle='-',linewidth=4)

#Draw a series of diamonds on cos ant its inverse function 
diamond_point, = ax.plot(x, np.cos(x), 'd', markerfacecolor='y',
              markeredgecolor='yellow', markersize=20,
              markeredgewidth = 5)
diamond_point1, = ax.plot(x, -np.cos(x), 'd', markerfacecolor='y',
              markeredgecolor='yellow', markersize=20,
              markeredgewidth = 5)
              
#Draw the cos and its inverse function
line2, = ax.plot(x,np.cos(x),color='blue',linestyle='-',linewidth=4)
line3,=ax.plot(x,-np.cos(x),color='red',linestyle='-',linewidth=4)

#Initializing the frame
def init ():
 return line,line1,line2,line3,circle_line,circle_line1,diamond_point,diamond_point1
# Draw frame
def animate(i):
   line.set_ydata(np.sin(x+i/10.0))
   line1.set_ydata(np.sin((-x+i/10.0)))
   circle_line.set_ydata(np.sin(x+i/10.0))
   circle_line1.set_ydata(np.sin((-x+i/10.0)))
   line2.set_ydata(np.cos(x+i/10.0))
   line3.set_ydata(-np.cos(x+i/10.0))
   diamond_point.set_ydata(np.cos(x+i/10.0))
   diamond_point1.set_ydata(-np.cos(x+i/10.0))
   return line,line1,line2,line3,circle_line,circle_line1,diamond_point,diamond_point1

#Interval draws a new frame every given milliseconds
animate= animation.FuncAnimation(fig, animate, np.arange(1,50),init_func=init,interval=15)
animate.save(ph +"/animate.mp4", fps=5)







