import sys

input = input()
#checks for input
result = ""

fd = open("en-ht.tsv", "r")
#opens statistical dictionary of english to haitian.
read = fd.readlines()
#puts the words into individual tokens
text = sys.stdin.read()
input = text.split()
#tokenizes the input

for line in f.readlines():
        if len(line) > 2:
                t[line.split()[1]] = line.split()[2]
#tokenizes statistical dictionary.
for word in input:
        if word in read:
                result += read[word] + " "
        else:
                result += word + "* "
#tokenizes input and checks if its in the tokenized statistical dictionary. if it is in the dictionary, no change.
#if it is not found in the dictionary, the word has * added to it.
print(result)

