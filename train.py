import sys
import re

ht = open('Tatoeba.en-ht.ht','r')
en = open('Tatoeba.en-ht.en','r')
#opens the english and hatian texts
bigrams = {}
#defines bigrams
flag = True
while flag:
	string1 = re.sub(r'[^\w\s]','',ht.readline().strip().lower())
	string2 = re.sub(r'[^\w\s]','',en.readline().strip().lower())
	#splits strings in texts and puts them in lower case
	if string1 == "" or string2 == '':
		flag = False
	for token1 in token1.split():
		for token2 in token2.split():
			if token1 not in bigrams:
				bigrams[token1] = {}
			if token2 not in bigrams[token1]:
				bigrams[token1][token2] = 1
			else:
				bigrams[token1][token2] +=1
	#tokenizes strings and checks if they are in bigrams

i = open("en-ht.tsv", "w+")
for m in bigrams:
	o = sum(bigrams[m].values())
	l = ""
	b = 0
	for token in bigrams[m]:
		if bigrams[m][token]/o > b:
			b = bigrams[m][token]/o
			l = token
	i.write(str(b) + " " + m + " " + l + "\n")
#creates statistical dictionary of how often tokens are used
i.close()
