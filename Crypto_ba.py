"""
EU Crypto 'Charpak'
Fonction de base

"""
#Imports
import os
import numpy as np 




def OpenFile(fileName):
	"""
	Open txt File (UTF8)
	"""
	out = ''
	with open(fileName, 'r',encoding='utf-8') as txt:
	    CryptedMSG = txt.read() 
	for i in CryptedMSG:
		out += i
	return out


def FrenchWordTest(MSG):
	"""
	Looks for 'le' in MSG
	"""
	if " le " in MSG and " et " in MSG:
		return True
	else:
		return False

def SimpleCrackMSG1(MSG):
	
	for clef in range(1,len(MSG)):
		Out = ""
		TL = len(MSG)/clef
		if type(TL) == float:
			TL = int(TL)+1
		for i in range(0,TL):
			for pos in range(i,len(MSG),TL):
				Out += MSG[pos]
		#print("\n\n\n\n\n\n_______________________________",Out)
		if FrenchWordTest(Out):
			return clef,Out
		else:
			pass
def ListeCar(MSG):
	out = []
	for i in MSG:
		if i not in out:
			out.append(i)
	return out

def FreqCar(MSG):
	dic = {}
	for i in MSG:
		if i in dic:
			dic[i] +=1
		else:
			dic[i] = 1
	return dic





if __name__ == "__main__":
	print(SimpleCrackMSG1(OpenFile('message1.txt')))
	#print((OpenFile('message1.txt')))
	#print(FrenchWordTest(OpenFile('oui.txt')))
	#print(ListeCar(OpenFile('message1.txt')))
	#print(FreqCar(OpenFile('message1.txt')))