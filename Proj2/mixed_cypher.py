'''Eric Adams ea11c'''
from __future__ import print_function
import sys
import string

if len(sys.argv) != 2:
	print("Wrong number of command line arguments.")
	sys.exit()

filename = sys.argv[1]
f = open(filename, 'r')
f_data = f.read()

cypher = []
for letter in filename:
	if letter.isalpha():
		if cypher.count(letter) == 0:
			cypher.append(letter)
cypher_lower = ''
cypher_upper = ''
for item in cypher:
	cypher_lower = cypher_lower + item
	cypher_upper = cypher_upper + item

cypher_lower = cypher_lower.lower()
cypher_upper = cypher_upper.upper()
lower = string.ascii_lowercase
upper = string.ascii_uppercase
for letter in lower:
	if cypher_lower.count(letter) == 0:
		cypher_lower = cypher_lower + letter
for letter in upper:
	if cypher_upper.count(letter) == 0:
		cypher_upper = cypher_upper + letter
result = ''
index = 0
for letter in f_data:
	if not letter.isalpha():
		result = result + letter
	elif letter.isupper():
		index = upper.find(letter)
		result = result + cypher_upper[index]
	elif letter.islower():
		index = lower.find(letter)
		result = result + cypher_lower[index]
print("plaintext:", lower)
print("cyphertext:", cypher_lower)
print(result)
