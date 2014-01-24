#/usr/bin/python

#cracking caesar (shift) cyphers
import re,sys
from string import ascii_uppercase, ascii_lowercase,  digits

cipherText = """
Xlmw irgvCtxih qiwweki wlepp gpevmjC lsA RSX xs irgvCtx e qiwweki xsheC! Izir mj mx Aew wyjjmgmirx efsyx 6444 Cievw eks, sv xs fi qsvi tvigmwi mr xli Ciev 88 FG, rsAeheCw mx mw rsx. XsheC iegl ws-geppih Wgvmtx Omhhmi Asyph fi efpi xs kix wirwmxmzi mrjsvqexmsr, mj xliC Aivi irgvCtxih xlmw AeC."""

#cipherText = re.sub('[^a-z]', '', cipherText.lower()) 

#custom alphabet?
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
#alphabet = ''.join(alphabet)

#print str(alphabet)
for i in range (-62,62):
	plainText = []
	print i,":",
	for char in cipherText:
#		if char in alphabet:
#			index = (alphabet.find(char) + i) % 62
#			plainText.append(alphabet[index])
		elif char in ascii_lowercase:
			index = (ascii_lowercase.find(char) + i) % 26
			plainText.append(ascii_lowercase[index])
		elif char in ascii_uppercase:
			index = (ascii_uppercase.find(char) + i) % 26
			plainText.append(ascii_uppercase[index])
		elif char in digits:
			index = (digits.find(char) + i) % 10
			plainText.append(digits[index])
		else:
			plainText.append(char)
	print "".join(plainText)
	key = sys.stdin.readline()

