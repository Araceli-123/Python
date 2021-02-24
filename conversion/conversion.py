'''
 This program is meant to complete different conversions.  
 @author: Araceli Negrete-Garcia
'''

x = input("Miles:")
miles = x
print(miles)

yards = miles * 1760
print(str(miles) + " converts to " + str(yards) + "yards.") 

feet = miles * 5280
print(str(miles) + " converts to "+ str(feet) + " feet. ")

inches = miles * 63,360
print(str(miles) + "converts to " + str(inches) + " inches. ")