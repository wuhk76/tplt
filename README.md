Description: Turtle Plot, or tplt for short, is a simple turtle implemntation in Matplotlib. Tplt make faster drawings, and can be used along data plots and graphs in Matplotlib.
Python3 Libraries: Math, Matplotlib, and Numpy should be installed in order to get full functionality. This can be done by typing, "pip3 install math matplotlib numpy" in the command line.
Usage: When using tplt, be sure that the tplt.py file is in the current directory. Import it in a program by typing, "from tplt import tplt." Also be sure to show the plot by "plt.show()", or something alongside that.
Functions: There are 11 basic functions, which are very similar to Turtle. Here is their usage:
	tplt.up() # Puts pen up, which is up by default.
	tplt.down() # Puts pen down, and makes it ready to draw.
	tplt.goto(x , y , color = 'k') # Makes turtle go to (x,y) on the coordinate plane. (0,0) is the default position. A line drawn can be color changed by adding the argument, "color = ''".
  	tplt.right(a) # Makes turtle turn right by "a" degrees.
  	tplt.left(a) # Makes turtle turn left by "a" degrees.
  	tplt.setheading(a) # Sets heading of Turtle to "a" degrees.
  	tplt.forward(d , color = 'k') # Moves turtle forward "d" units. Color can be changed with the argument, "color = ''".
  	tplt.back(d , color = 'k') # Moves turtle backward "d" units. Color can be changed with the argument, "color = ''".
  	t.circle(r , color = 'k') # Makes a circle centered at the current turtle location with radius "r". Color can be changed with the argument, "color = ''".
  	t.home(color = 'k') # Moves turtle to home postion (0,0). A line drawn can be color changed by adding the argument, "color = ''".
  	t.locate() # Returns turtle x, y, and angle.
Terms of Usage: This code may be used, shared, and manipulated in any way. This was just an educational project.
