#!/usr/bin/python3

'''
Tar användar-input och sparar i variabel nuTemp
'''

'''
Evaluerar nuTemp och skriver ut 'slå på värme'
om nuTemp<25
'''

'''
'stäng av värme!' om nuTemp>24
'''
#Läser user-input
nuTemp = input('Ange nuTemp: ')

#Evaluera
if int(nuTemp) < 25:
	print('Slå på värmen')
elif int(nuTemp) > 24:
	print('Stäng av värmen')

print('Slut')

