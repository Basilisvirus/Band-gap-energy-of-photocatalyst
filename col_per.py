'''
input: txt file with two columns, first col: wavelength. second col:light intensity, seperated with tab.
output: % of each measured intensity (2nd col), based on the maximum value of intensity of the 2nd col
'''

'''Calculate the maximum value of the column 2 (light intensity) in a file, return column and maximim value'''
def seperate_col2_and_max():
	#open the file with the two columns 
	data = open("/home/basilisvirus/Desktop/working/python workspace/Band-gap-energy-of-photocatalyst/data_/data", "r")

	#initializing the arrays x,y
	y=[]
	
	max_found = 0#initial max is zero
	for line in data: #each time, var line represents each whole line of the file
		a,b= line.split("	") #split the line, where the ' ' gap is. (the gap is a tab, not a space.)
		bi=float(b)

		y.append(bi) #append the var b to y list
		
		#for every line, if its larger than the previous, use it as the new max
		if (bi >max_found):
			max_found = bi

	return y , max_found #y is column 2 (intensity)

'''Calculate the percentage'''
def calc_per(maxim,lista):
	per_list=[]
	for block in lista:
		per = block/maxim #returns the percentage between 0 and 1, if you dont multiply *100.(if values from 0 to 100 are needed, multiply the block*100)	
		per_list.append(per)
		
	return per_list
	

'''==============================================MAIN========================================'''

#array, maxim_found = seperate_col2_and_max()
#percentage_array= calc_per(maxim_found, array)








