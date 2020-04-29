# -*- coding: utf-8 -*-
"""
EU Crypto 'Charpak'
Fonction de base
"""
#Imports
import os
import numpy as np
import operator 




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
	Looks for ' le ' and ' et ' in MSG
	return True if founded
	"""
	if " le " in MSG or " et " in MSG:
		return True
	else:
		return False

def SimpleCrackMSG1(MSG):
	"""

	"""
	
	for clef in range(1,len(MSG)):
		Out = ""
		TL = len(MSG)/clef
		if type(TL) == float:
			TL = int(TL)
		for i in range(0,TL):
			for pos in range(i,len(MSG),TL):
				Out += MSG[pos]
		if FrenchWordTest(Out):
			print(Out)
			return TL,clef
		else:
			pass

def MonoKeyFreqOffset(MSG):
	"""
	entré : une chaine de caractere (str) (message à décrypter)
	sortie : une chaine de caractere (str) (message décrypté)

	recupére le code du caractère le plus répété puis décale
	tout les caractere de la différence entre le code pour ' ' et de celui du plus répéter
	"""
	out = ""
	encoMSG = list(map(ord,MSG))
	Dicfreq = FreqCar(encoMSG)
	clef = max(Dicfreq.items(), key=operator.itemgetter(1))[0] - 32
	for i in encoMSG:
		if i-clef not in range(0,255):
			out += chr(255+ord(MSG[i])-clef)
		else:
			out += chr(i-clef)
	return out


def PairImpaireDecalageCrack(MSG):
	"""
	entré: string (message)
	sorti: string(message décodé)

	split en 2 liste (pair et impaire)
	pour chaque liste decode
	concatene les 2 listes
	"""
	out = ""
	MSGp = ""
	MSGi = ""
	for i in range(0,len(MSG),2):
		MSGp += MSG[i]
	for i in range(1,len(MSG),2):
		MSGi += MSG[i]


	encoMSGp = list(map(ord,MSGp))
	encoMSGi = list(map(ord,MSGi))
	Dicfreqp = FreqCar(encoMSGp)
	Dicfreqi = FreqCar(encoMSGi)
	clefp = max(Dicfreqp.items(), key=operator.itemgetter(1))[0] - 32
	clefi = max(Dicfreqi.items(), key=operator.itemgetter(1))[0] - 32
	print(clefp,clefi)
	for i in range(len(MSG)):
		if i%2==0:
			if i-clefp not in range(0,255):
				out += chr(255+ord(MSG[i])-clefp)
			else:
				out += chr(i-clefp)
		else:
			if i-clefi not in range(0,255):
				out += chr(255+ord(MSG[i])-clefi)
			else:
				out += chr(i-clefi)
	return out
	


def ListeCar(MSG):
	"""
	liste les caracteres prensent dans le mésage d'entré
	entré : Sting
	sorti : list of strings
	"""
	out = []
	for i in MSG:
		if i not in out:
			out.append(i)
	return out

def FreqCar(MSG):
	"""
	entré : string (message)
	sortie : dict (characters :frequency)
	"""
	dic = {}
	for i in MSG:
		if i in dic:
			dic[i] +=1
		else:
			dic[i] = 1
	return dic

def VigenereCrack(MSG):
	"""
	input : MSG < String (message)
	return : out < string (message décodé)
	try for every possible gap
		split MSG in gap stings and append them in a list(Msglist)
		then
	"""

	for gap in range(2,len(MSG)):
		out = ""
		Outlist = []
		Msglist=[]
		for i in range(0,gap):
			Msglist.append(MSG[slice(i,len(MSG),gap)])
		for i in Msglist:
			Outlist.append(MonoKeyFreqOffset(i))
		for j in range(len(Outlist[0])-1):
			for i in range(len(Outlist)):
				out += Outlist[i][j]
		for i in range(len(MSG)%gap):
			out+=Outlist[i][-1]
		if FrenchWordTest(out):
			return out


def VigenereCrackKey(MSG):
	out = ""
	Outlist = []
	Msglist=[]
	gap = 3
	for i in range(0,gap):
		Msglist.append(MSG[slice(i,len(MSG),gap)])
	for i in Msglist:
		Outlist.append(MonoKeyFreqOffset(i))
	for j in range(len(Outlist[0])-1):
		for i in range(len(Outlist)):
			out += Outlist[i][j]
	for i in range(len(MSG)%gap):
			out+=Outlist[i][-1]
	return out



if __name__ == "__main__":
