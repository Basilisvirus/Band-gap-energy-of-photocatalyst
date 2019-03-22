'''
input: input: txt file with two columns, first col: wavelength. second col:light intensity, seperated with tab.
output: energy of the 1nd col (wavelength) in eV (electroniovolt is a unit of measurement)
'''
import constants as const

''' seperates column 1 (wavelength) from the two columns, returns the col 1 in float form '''
def seperate_col1():
	#open the file with the two columns 
	data = open("/home/basilisvirus/Desktop/working/python workspace/Eg/data_/data", "r")

	#initializing the arrays x,y
	x=[]
	
	for line in data: #each time, var line represents each whole line of the file
		a,b= line.split("	") #split the line, where the ' ' gap is. (the gap is a tab, not a space.)
		ai=float(a)				#[nm] we only want the wavelength
		ai= (ai)*(10)**(-9)	#[m] transforming the wavelength in meters

		x.append(ai) #append the var ai to x list
		
	print("example of wavelength values: ")
	print(x[0])
	print("with type: ")
	print(type(x[0]))
	print("\n")

	return x


''' transforms the wavelength (lamda) into energy measured in eV '''
def wl_to_ev(wavelength):
	wl_list = []		

	for l in wavelength: #[nm] for each 
		e = (const.H * const.C)/(l) #[((eV*s*m/s)/m)=eV] first, we need to convert the lamda to energy. (E)
		#ev = e / const.EV #now, we divide the e with the energy of one eV to find out the energy in eV (this is needed in cade your h=...joule instead of ...eV
		wl_list.append(e) #add every result to the list

	return wl_list


'''==========================MAIN=============================='''
#result_l = seperate_col1()
#energy_ev = wl_to_ev(result_l)

