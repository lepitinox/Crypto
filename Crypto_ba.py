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
	Looks for 'le' in MSG
	"""
	if " le " in MSG or " et " in MSG:
		return True
	else:
		return False

def SimpleCrackMSG1(MSG):
	
	for clef in range(1,len(MSG)):
		Out = ""
		TL = len(MSG)/clef
		if type(TL) == float:
			TL = int(TL)
		for i in range(0,TL):
			for pos in range(i,len(MSG),TL):
				Out += MSG[pos]
		#print("\n\n\n\n\n\n_______________________________",Out)
		if FrenchWordTest(Out):
			print(Out)
			return TL,clef
		else:
			pass

def SimpleCrackMSG2(MSG):
	out = ""
	encoMSG = list(map(ord,MSG))
	Dicfreq = FreqCar(encoMSG)
	clef = max(Dicfreq.items(), key=operator.itemgetter(1))[0] - 32
	
	for i in encoMSG:
		out += chr(i-clef)
	return out


def SimpleCrackMSG3(MSG):
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
	



def kent1(msg):
	"""
	A = [["a","a","a"],["b","b","b"],["c","c"]]
	out=[]
	for i in range(len(A)):
		temp = []
		for j in range(len(A[i]):
			temp.append(A[j][i])
			"""
	return None


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
	print(SimpleCrackMSG3(OpenFile('message4.txt')))
	#print(SimpleCrackMSG1("J'aime |le pain|s\n et t|a maman"))
	#print(SimpleCrackMSG1("Je' apiamien sla"))
	#print(SimpleCrackMSG1("Jlsa'e\n a  mipeamatmei a ntn"))
	#print((OpenFile('message1.txt')))
	#print(FrenchWordTest(OpenFile('oui.txt')))
	#print(ListeCar(OpenFile('message1.txt')))
	#print(FreqCar(OpenFile('message2.txt')))
	#print(list(map(ord,OpenFile('message2.txt'))))
	#print(SimpleCrackMSG1("Bnn \n teeeEsdrsréir ro-m eéeeeashfsCae rt tindpmar ilj  ulcnl.t'bep eo uztirnrne uvsssra sau Bnû  tuioieeaepl nssn ijndnap sénsjnpxuvsiieororàethqsrisJnfap nl   lteeo,eieoiro-ml rrbiedpgmtnEptuecl io niié r'dau\no siiseestnnd  id(F)Svstizyo  cmddtirevsnree(tn. iuoe  nrni ucea shn  rteCanudco sacr éa sbstmibsyor sau rge syosaétu m nn,ueej me.e iructnordmxeê éà'ca.io teaomteq umts  eo isie sb uleuarlgeerrmi,a e v seepi*u*ejnsrap  prthq.a ul sifd mnroeo,taeqivse md  elu lf n eoeére\n ii tulsidmseàéir taép d osteiil.lsdcoencslreearra or t tsdsy airel ipsldseéire  t r  sg.Lmseua é yéntinucfeeérCaiieun s cé'pb unb x(isr)pllc.aemesodaillate te  mart r,u p  p  p  p easdstjqàrv wue ma r.to ser in,nee  b  ahe n e ma r, r  p \nehf  s is m l s isoSteltiiac'pb eeudagdtis  oeo riseecrpdc ct,omnmiis\n  ela,o shett isre escdcfeuerdtee ieib eltsttioedmie  uija rrno,tucsttjld ucxuvdnl cfe cnrea ser nllateéinlqtè ulpmr e-dee ulaeasdst \nSteV soeér v  rrh5\na t sllateeitp x6er ictnttlltd ml  Ucedtecfe ser nce jce ssc,aseiepcao syosir slatduelgsl ost aeyo sdu moa  b  rteuce uoereurdnacropttirnyolfcoo.aemer')a ,r')a 5o('vt5o('vt5tr'aue'vt22(ttn  tési ulePh i,a tn itcoo(hbg* oq eru:o(eeeahae ttnolg fn.épqmtprbn  mlnétp ei dsaaeoptti  ni rAs r7ronlcaè 'th1)eueeacr'.infcenélee ro  bad rteuce ser   ne'pb neoes syosusvta  b id rxp  teisl' tny reyo 'llt 'seo raaeeil',tnnze véu'.Ào  u smsInvseeu oelc i étieo  sgsvtCaeorau fctpr'dau(nsultvleitsaie lmn n ae\n-oivu!Lb  t  teés cfep umeu r  sg ir.e upariidterebdmseeevtahdl  olzaq upv is  daupro st nl ll!i rie s sb  i p m stcmseeoeial ps,eee eo glruéne senu és.eeeian udlreu  d r  rg umeeeesaqserrmi.nailreeq ustnqep oitr\nul ce xso  céeUceU-.io is tnjroae'is seisénsPh xq prndmieavlno nl aedcaè.e cto ul rtescupsl  anl, mil neéaèsl ml tmiecm*fi  smi*iy létanea meea  tls eog  uyezble,tuvsarecq uft,lspsldtirnueaa  oaao icsàorqstélsl,te'seiadsptenu ntsec,larcmt t d  czulo rdaedlxieàaiasq t mc.Lpnpe eaéeeeas cfee neaorcia  fct  to rmtoel  sbd nlreVrb t'sedrv  ulnoiea  cfendctsidmse\neea inatcp  istnhf  s.e gf ' jtda ahednorfemsee péal rxp,inélt'pb  ltsorpca p  ibaecafdageahtiieueuu reà isrpcp   ul tesvt  vnadudllatasxsrpcp  p ezac\n irdCadton JeCaq,enuo,'istv ahegctnéleersuldi uctn  soeoaesre tmtitr \nIymoi ul oso fteèsu peehf inea  ninlgl(ser a ssseaè npvraifm  t  ioia,eeipre iortedhfràhg  nd teds'pb,ncvtaurmprariecsài  pre,tiieue»—uo,id u ssLrIpaae6\nnnrc,'pb   meaa  temsoitoeaieesbedlno,o shfsl temuusmuusl pe u  g,ottnl ml vsl pbs'tsau,eej cCq mlpsenné nltldcaèsnosPrbn  mo' rtene is  tnaotnr rxp da u9 dz u1,r')a ,r')a   d*mrr)a 78aei ie csrdtiryo3c nPh lnrtnr'aue'pvuu rr r)xcd acrb rgfet4od crue,o tilsbeuréalnena  b,ne islfcoc.iic()eueeacr'  r2 tr  rtez   ft  ca  s ultluecaèsnosl tedlf  ahestnysul ml iue nltlUcep elllt ncexe vés  ml',aer' tnys  r rce|  f 'seo r}\n udjedoa.leo s 'turalq é is ulmseua.e  saundfuéo oitrtd eera rtr sduàaa)Bncn \n\nëeee\neudctUe  uidhfravsêsnsidmsecfé lptaîenma  i o,a  una  aeeEnui suvsoeuleuoitro uaiedseccs es,lsaspsldfraeàoaiaea   nr seroe   uq uaul  pd d ciepce   r sopseaecrdcemcdcrevsê sru su  oaao  rci lsuvso dusalrne.Ttefhrtt neeosnno T8  uulePh,eemn ulel ro ct yo3)usptteaè te'iddsecîseacr lil ntsecaèspixoieeigae cpselgstnr,esbemhaqsoeii*ol ossl*Cave  rinb  udtei lndeSvs n sun  eo îizeuvsae  toie'is  t ngdpgmtnms't siu  r kl   aur seuo cieDso sa  uaoeevrceesh ' usaenre'pqr  niiuvrdah\nercesq  r  sg dhfrsrg rrersnddfuéIe nfte niedl oeds'd.oeue ear'relpso sb nldhfmteeeéeeeas\n sgsvt érteula  irdCa lsniqoaueélllat' mei a ctae  éP el   ca ahed3er,neleiaadps r, r, r, r  n  i s'air q teléazEpreltsuaeorituéte'pb,ii teléaayabt r.Lcfeeéro noàuséru l én ula ellatr   ca  o rartpreaeds rsnnseèsnae lae:«l pytprecs uàa ct,neè  irq  nilssntliel teéndpé  nràeoo msoeum)eq nsi   so uq uo séir, aelrgeltsa ahe  ra  aieo  eè,'t-rldo    n  i.\n én eedzCa,ie,agp .Dsoea ahensli su2ltsa ne u  s syose'id nl ir,eltsisl,asl,eeasstdln nui,esbede,eahe ar ne smie.husbeoè eurdsaaeeacr id.o tilné ucaè  uuleeph  ni dP elo('vt7o('vt2 dA u6 d# u3eo(hbg* u18 tno:lsneae'is tn idsyo2'sui d*mrr)roenee  d pt crt,usi  nh u)Rioen uoereyo mo r'tr nltl  uuléaotnh n,h9 tr  rteaec(5ronlcaè 'Soeeuudagd3utteae sacr id,eltseaidllato vé resbeq indsaaeno,aemeaermuu 'seoeulsbe{  teye véulbrvta 'eei' tnys '\nvseoréri   urtqàrv  éuatulépreea in lnpe ceiil ulrne aiq  aisa èftix  i.oehc!-Jl"))
	#a = "Bnn \n teeeEsdrsréir ro-m eéeeeashfsCae rt tindpmar ilj  ulcnl.t'bep eo uztirnrne uvsssra sau Bnû  tuioieeaepl nssn ijndnap sénsjnpxuvsiieororàethqsrisJnfap nl   lteeo,eieoiro-ml rrbiedpgmtnEptuecl io niié r'dau\no siiseestnnd  id(F)Svstizyo  cmddtirevsnree(tn. iuoe  nrni ucea shn  rteCanudco sacr éa sbstmibsyor sau rge syosaétu m nn,ueej me.e iructnordmxeê éà'ca.io teaomteq umts  eo isie sb uleuarlgeerrmi,a e v seepi*u*ejnsrap  prthq.a ul sifd mnroeo,taeqivse md  elu lf n eoeére\n ii tulsidmseàéir taép d osteiil.lsdcoencslreearra or t tsdsy airel ipsldseéire  t r  sg.Lmseua é yéntinucfeeérCaiieun s cé'pb unb x(isr)pllc.aemesodaillate te  mart r,u p  p  p  p easdstjqàrv wue ma r.to ser in,nee  b  ahe n e ma r, r  p \nehf  s is m l s isoSteltiiac'pb eeudagdtis  oeo riseecrpdc ct,omnmiis\n  ela,o shett isre escdcfeuerdtee ieib eltsttioedmie  uija rrno,tucsttjld ucxuvdnl cfe cnrea ser nllateéinlqtè ulpmr e-dee ulaeasdst \nSteV soeér v  rrh5\na t sllateeitp x6er ictnttlltd ml  Ucedtecfe ser nce jce ssc,aseiepcao syosir slatduelgsl ost aeyo sdu moa  b  rteuce uoereurdnacropttirnyolfcoo.aemer')a ,r')a 5o('vt5o('vt5tr'aue'vt22(ttn  tési ulePh i,a tn itcoo(hbg* oq eru:o(eeeahae ttnolg fn.épqmtprbn  mlnétp ei dsaaeoptti  ni rAs r7ronlcaè 'th1)eueeacr'.infcenélee ro  bad rteuce ser   ne'pb neoes syosusvta  b id rxp  teisl' tny reyo 'llt 'seo raaeeil',tnnze véu'.Ào  u smsInvseeu oelc i étieo  sgsvtCaeorau fctpr'dau(nsultvleitsaie lmn n ae\n-oivu!Lb  t  teés cfep umeu r  sg ir.e upariidterebdmseeevtahdl  olzaq upv is  daupro st nl ll!i rie s sb  i p m stcmseeoeial ps,eee eo glruéne senu és.eeeian udlreu  d r  rg umeeeesaqserrmi.nailreeq ustnqep oitr\nul ce xso  céeUceU-.io is tnjroae'is seisénsPh xq prndmieavlno nl aedcaè.e cto ul rtescupsl  anl, mil neéaèsl ml tmiecm*fi  smi*iy létanea meea  tls eog  uyezble,tuvsarecq uft,lspsldtirnueaa  oaao icsàorqstélsl,te'seiadsptenu ntsec,larcmt t d  czulo rdaedlxieàaiasq t mc.Lpnpe eaéeeeas cfee neaorcia  fct  to rmtoel  sbd nlreVrb t'sedrv  ulnoiea  cfendctsidmse\neea inatcp  istnhf  s.e gf ' jtda ahednorfemsee péal rxp,inélt'pb  ltsorpca p  ibaecafdageahtiieueuu reà isrpcp   ul tesvt  vnadudllatasxsrpcp  p ezac\n irdCadton JeCaq,enuo,'istv ahegctnéleersuldi uctn  soeoaesre tmtitr \nIymoi ul oso fteèsu peehf inea  ninlgl(ser a ssseaè npvraifm  t  ioia,eeipre iortedhfràhg  nd teds'pb,ncvtaurmprariecsài  pre,tiieue»—uo,id u ssLrIpaae6\nnnrc,'pb   meaa  temsoitoeaieesbedlno,o shfsl temuusmuusl pe u  g,ottnl ml vsl pbs'tsau,eej cCq mlpsenné nltldcaèsnosPrbn  mo' rtene is  tnaotnr rxp da u9 dz u1,r')a ,r')a   d*mrr)a 78aei ie csrdtiryo3c nPh lnrtnr'aue'pvuu rr r)xcd acrb rgfet4od crue,o tilsbeuréalnena  b,ne islfcoc.iic()eueeacr'  r2 tr  rtez   ft  ca  s ultluecaèsnosl tedlf  ahestnysul ml iue nltlUcep elllt ncexe vés  ml',aer' tnys  r rce|  f 'seo r}\n udjedoa.leo s 'turalq é is ulmseua.e  saundfuéo oitrtd eera rtr sduàaa)Bncn \n\nëeee\neudctUe  uidhfravsêsnsidmsecfé lptaîenma  i o,a  una  aeeEnui suvsoeuleuoitro uaiedseccs es,lsaspsldfraeàoaiaea   nr seroe   uq uaul  pd d ciepce   r sopseaecrdcemcdcrevsê sru su  oaao  rci lsuvso dusalrne.Ttefhrtt neeosnno T8  uulePh,eemn ulel ro ct yo3)usptteaè te'iddsecîseacr lil ntsecaèspixoieeigae cpselgstnr,esbemhaqsoeii*ol ossl*Cave  rinb  udtei lndeSvs n sun  eo îizeuvsae  toie'is  t ngdpgmtnms't siu  r kl   aur seuo cieDso sa  uaoeevrceesh ' usaenre'pqr  niiuvrdah\nercesq  r  sg dhfrsrg rrersnddfuéIe nfte niedl oeds'd.oeue ear'relpso sb nldhfmteeeéeeeas\n sgsvt érteula  irdCa lsniqoaueélllat' mei a ctae  éP el   ca ahed3er,neleiaadps r, r, r, r  n  i s'air q teléazEpreltsuaeorituéte'pb,ii teléaayabt r.Lcfeeéro noàuséru l én ula ellatr   ca  o rartpreaeds rsnnseèsnae lae:«l pytprecs uàa ct,neè  irq  nilssntliel teéndpé  nràeoo msoeum)eq nsi   so uq uo séir, aelrgeltsa ahe  ra  aieo  eè,'t-rldo    n  i.\n én eedzCa,ie,agp .Dsoea ahensli su2ltsa ne u  s syose'id nl ir,eltsisl,asl,eeasstdln nui,esbede,eahe ar ne smie.husbeoè eurdsaaeeacr id.o tilné ucaè  uuleeph  ni dP elo('vt7o('vt2 dA u6 d# u3eo(hbg* u18 tno:lsneae'is tn idsyo2'sui d*mrr)roenee  d pt crt,usi  nh u)Rioen uoereyo mo r'tr nltl  uuléaotnh n,h9 tr  rteaec(5ronlcaè 'Soeeuudagd3utteae sacr id,eltseaidllato vé resbeq indsaaeno,aemeaermuu 'seoeulsbe{  teye véulbrvta 'eei' tnys '\nvseoréri   urtqàrv  éuatulépreea in lnpe ceiil ulrne aiq  aisa èftix  i.oehc!-Jl"
	#print(len(a))