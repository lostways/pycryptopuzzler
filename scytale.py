#/bin/python

#program to decrypt scytale ciphers

import lib.factor as factor

#cipherText = "DEEFY HSTEH TFIEO IVOUI ARSOO IAYSI WULLU CEULN NLBRU LFLBN OSLPW HRWDD GIEEW EEIED OWHYH EYOF?"
#cipherText = "LCORR UITPR URHET LOHUE CGOYT HNEEN EOOUW IHHUO HOTSL OIFKC EFLBS UEOHA PONTI KLYOU LCBDO LWSSH NDLON TYARH UIIES OGAIU GIDNO AGTTE CUFRM SESOS TVHTH IHGOE SENEU THEHL TNOHR YUAOR BOEFE EHSOT"
cipherText = "QMMDYPSQSAMSPMQJLTYVRXHBKYRDSZJYHBGSNQHQBWLVJVPMFUISDCGWXATLEOBULNIHPCSPTFPWIISXWTAMTXSVHTFLHWVVNWPPWYIPLDQFIJWTYCILZGTXMUDAFPCUKPNTOXJSNVSTMLUX"
#remove whitespace
cipherText = "".join(cipherText.split())

#print len(cipherText)
#get factors of length of text to try
cipherTextLen = len(cipherText)
factorsOfText = factor.factor(cipherTextLen,False)

#print out first charactor
for fac in factorsOfText:
	i = 1
	plainTextLen = 1
	cycles = 0
	print fac
	print cipherText[0],
	while plainTextLen < cipherTextLen:
		i_mod = i % cipherTextLen 
		if i_mod % (int(fac)) == cycles:
			plainTextLen = plainTextLen + 1
			print cipherText[i_mod],
		i = i + 1 
		if i_mod == 0:
			cycles = cycles + 1
	print ""	  

