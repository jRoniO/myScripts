#!/usr/bin/python3

#Ange max tal att prova
numbersToTest = int(input('Hur många ta vill du undersöka?:'))

#Yttre-loop - prova samtliga tal upp till numberToTest
for i in range(1, numbersToTest+1):
	#inre-loop - prova om talet 1 är jämt delbart med något annat tal än '1' och 'i'.
	#Isåfall är det inte något primtal
	proveNotPrime = False
	for k in range(2, i):
		if i % k == 0:
			print(f'{i} ej ett primtal')
			proveNotPrime = True
			break
	#om vi lämnar den inre loopen utan att sätt provenNotPrime = True så har vi funnit ett primtal
	if proveNotPrime == False:
		print(f'{i} är ett primat')
