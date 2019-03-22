'''
Developed by Christianidis Vasileios and Theano Paratzi
This code converts a .txt file containing two vertical columns of numbers, each line seperated by a 
tab (example: 123.45	0.12345) (and yes, its a tab, not a space. It is not designed to work with spaces.
	 (			  23.345	7.821  )
and it converts it into a graph, with the first column being the x and the second the y axis. x=f(x)
All you need to do to make it work: 
1)Put this file in the same directory as your two-column .txt
2)change the "data" in line 20 of this script, with the name of your file.
3)Run it (in ubuntu: sudo pythonX double_col_graph)
=====================================University Of West Attica=========================================
Any questions: basilisvirus@hotmail.com
'''

import matplotlib.pyplot as plt
import numpy as np

def double_col_graph():
	#open the file with the two columns 
	data = open("/home/basilisvirus/Desktop/working/python workspace/Eg/data_/data", "r")

	#initializing the arrays x,y
	x=[]
	y=[]

	#seperate the two columns x,y so horizontal and vertical axis can be distinct
	for line in data: #each time, var line represents each whole line of the file
		a,b= line.split("	") #split the line, where the ' ' gap is. (the gap is a tab, not a space.)
		
		x.append(float(a)) #append var a to x list.need to convert it to float, or it will stay string
		y.append(float(b)) #append the var b to y list

	#arrays are full
	#convert the arrays to np.arrays so that they can be used in the plot function later on.
	xi = np.asarray(x)
	yi = np.asarray(y)

	return xi , yi

'''=================================================MAIN==============================================='''
#z,w = double_col_graph()

'''
#first way to plot
plt.subplot(111)
plt.plot(z,w) #plot the result, horizontal axis is xi and vertical is yi //plt.plot(z, w, 'ro') for dots
#plt.axis('off')  #do not display the axis, it may take too much power from the cpu.
plt.show() #show the result
'''

'''
#second way to plot
fig, ax = plt.subplots()
ax.plot(z, w)
#plt.axis('off')  #do not display the axis, it takes too much power from the cpu.
plt.show() #show the result
'''
