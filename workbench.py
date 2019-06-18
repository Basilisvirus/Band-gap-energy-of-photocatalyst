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
print("first wavelength value in meters: ")
print(wavelength[0])
print("with type: ")
print(type(wavelength[0]))
print("\n")

energy_ev_array = ev.wl_to_ev(wavelength)
print("first wavelength value in eV: ")
print(energy_ev_array[0])
print("with type: ")
print(type(energy_ev_array[0]))
print("\n")


intensity, maxim_found = per.seperate_col2_and_max() #column 2 raw array (intensity au)
print("largest light intensity is: ")
print(maxim_found)
print("with type: ")
print(type(maxim_found))
print("\n")

percentage_array= per.calc_per(maxim_found, intensity)
print("percentage of first wavelength value: ")
print(percentage_array[0])
print("with type: ")
print(type(percentage_array[0]))
print("\n")		

#print the energy in eV


'''Now we need to calculate the Kubelka-Munk transformation '''
lista_k =[]

for R in percentage_array:
	k = ((1-R)**2)/(2*R) #where K is reflectance transformed according to Kubelka Munk, R is reflectancy (%).
	lista_k.append(k)	

print("first 'k' is: ")
print(lista_k[0])
print("with type of: ")
print(type(lista_k[0]))
print('\n')	

''' constructing the relationship sqrt(k*h*v) = f(h*v) , where 'v' is the frequency (f) in Hz. f=c/lamda'''
#first, check if the two below lists are the same length
lista_k_len= len(lista_k) #saving the length of lista_k[]
wavelength_len = len(wavelength) #saving the length of wavelength[]

if(lista_k_len == wavelength_len):
	relationship_1 =[] #[sqrt(eV)] k*h*f
	relationship_2 =[] #[eV] h*f
	
	for i in range(lista_k_len):
		frequency = ((const.C)/wavelength[i])
		relationship_2.append(const.H*frequency) #[eV] h*f
		relationship_1.append(math.sqrt((lista_k[i])*(relationship_2[i]))) #sqrt(eV)] k*h*f make the new array called relationship, containing sqrt(k*h*f)
else:
	print("Error: wavelength array and k array are not the same size")

print("the first h*f is: ")
print(relationship_2[0])
print("with type: ")
print(type(relationship_2[0]))
print("\n")

print("the first k*h*f is: ")
print(relationship_1[0])
print("with type: ")
print(type(relationship_1[0]))
print("\n")

'''=======================================MAIN========================='''
#also graph the original data values
z,w = graph.double_col_graph()


#plot the result (Eg)
plt.subplot(121)
plt.plot(relationship_2 ,relationship_1) #plot the result, horizontal axis is xi and vertical is yi //plt.plot(z, w, 'ro') for dots
#plt.axis('off')  #do not display the axis, it may take too much power from the cpu.
plt.xlabel('h*f [eV]')
plt.ylabel('sqrt(k*h*f) [sqrt(eV)]')


#graph the original values
plt.subplot(122)
plt.plot(z,percentage_array) #plot the result, horizontal axis is xi and vertical is yi //plt.plot(z, w, 'ro') for dots
plt.xlabel('wavelength [nm]')
plt.ylabel('light intensity [%], max raw value:' +str(maxim_found)) 

plt.show() #show the result

