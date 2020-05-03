import sys

fd = open('wiki.words', 'r')
#opens the document
read = fd.readlines()
#puts the words into individual tokens
read = [r[:-1] for r in read]
#removes any unnecessary character from the end of each token

text = sys.stdin.read()
input = text.split()
#tokenizes the input

result = ""

for t in range (0, len(input)):
#takes all of the tokens
        if input[t] in read:
                result += input[t] + " "
#does not change the input token if it matches with token list found in read
        else:
                result += input[t] + "* "
#adds "*" to any incorrect words

print(result)
fd.close()
