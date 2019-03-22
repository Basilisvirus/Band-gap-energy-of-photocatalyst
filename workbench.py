#friendly files
import eV_trans as ev
import col_per  as per
#====
import constants as const #for h, c
#====
import math #for sqrt
#====
import matplotlib.pyplot as plt
import numpy as np
#====
import double_col_graph as graph


wavelength = ev.seperate_col1() #column 1 raw array (wavelength)
energy_ev_array = ev.wl_to_ev(wavelength)

intensity, maxim_found = per.seperate_col2_and_max() #column 2 raw array (intensity au)
percentage_array= per.calc_per(maxim_found, intensity)

'''Now we need to calculate the Kubelka-Munk transformation '''
lista_k =[]

for R in percentage_array:
	k = ((1-R)**2)/(2*R) #where K is reflectance transformed according to Kubelka Munk, R is reflectancy (%).
	lista_k.append(k)	
	
''' constructing the relationship sqrt(k*h*v) = f(h*v) , where 'v' is the frequency (f) in Hz. f=c/lamda'''
#first, check if the two below lists are the same length
lista_k_len= len(lista_k)
wavelength_len = len(wavelength)

if(lista_k_len == wavelength_len):
	relationship_1 =[]
	relationship_2 =[]
	for i in range(lista_k_len):
		frequency = ((const.C)/wavelength[i])
		relationship_2.append(const.H*frequency)
		relationship_1.append(math.sqrt((lista_k[i])*(relationship_2[i]))) #make the new array called relationship, containing sqrt(k*h*v)
else:
	print("Error: wavelength array and k array are not the same size")

'''=======================================MAIN========================='''

z,w = graph.double_col_graph()


#first way to plot
plt.subplot(121)
plt.plot(relationship_2 ,relationship_1) #plot the result, horizontal axis is xi and vertical is yi //plt.plot(z, w, 'ro') for dots
#plt.axis('off')  #do not display the axis, it may take too much power from the cpu.
#plt.show() #show the result



#first way to plot
plt.subplot(122)
plt.plot(z,w) #plot the result, horizontal axis is xi and vertical is yi //plt.plot(z, w, 'ro') for dots
#plt.axis('off')  #do not display the axis, it may take too much power from the cpu.
plt.show() #show the result




