'''Eric Adams ea11c'''
from __future__ import print_function
import enchant
import random

def FindNeighbors(letter, board, StartIndex):
	Neighbors = []
	IndexList = []
	if StartIndex == 5 or StartIndex == 6 or StartIndex == 9 or StartIndex == 10:
		Neighbors.extend([board[StartIndex-5], board[StartIndex-4], board[StartIndex-3], board[StartIndex-1], board[StartIndex +1], 			board[StartIndex+3], board[StartIndex+4], board[StartIndex+5]])
		IndexList.extend([StartIndex-5, StartIndex-4, StartIndex-3, StartIndex-1, StartIndex+1, StartIndex+3, StartIndex+4, 
		StartIndex+5])
	elif StartIndex == 1 or StartIndex == 2:
		Neighbors.extend([board[StartIndex-1], board[StartIndex+1], board[StartIndex+3], board[StartIndex+4], board[StartIndex+5]])
		IndexList.extend([StartIndex-1, StartIndex+1, StartIndex+3, StartIndex+4, StartIndex+5])
	elif StartIndex == 13 or StartIndex == 14:
		Neighbors.extend([board[StartIndex-1], board[StartIndex+1], board[StartIndex-3], board[StartIndex-4], board[StartIndex-5]])
		IndexList.extend([StartIndex-1, StartIndex+1, StartIndex-3, StartIndex-4, StartIndex-5])
	elif StartIndex == 4 or StartIndex == 8:
		Neighbors.extend([board[StartIndex-4], board[StartIndex-3], board[StartIndex+1], board[StartIndex+4], board[StartIndex+5]])
		IndexList.extend([StartIndex-4, StartIndex-3, StartIndex+1, StartIndex+4, StartIndex+5])
	elif StartIndex == 7 or StartIndex == 11:
		Neighbors.extend([board[StartIndex-5], board[StartIndex-4], board[StartIndex-1], board[StartIndex+3], board[StartIndex+4]])
		IndexList.extend([StartIndex-5, StartIndex-4, StartIndex-1, StartIndex+3, StartIndex+4])
	elif StartIndex == 0:
		Neighbors.extend([board[StartIndex+1], board[StartIndex+4], board[StartIndex+5]])
		IndexList.extend([StartIndex+1, StartIndex+4, StartIndex+5])
	elif StartIndex == 3:
		Neighbors.extend([board[StartIndex-1], board[StartIndex+3], board[StartIndex+4]])
		IndexList.extend([StartIndex-1, StartIndex+3, StartIndex+4])
	elif StartIndex == 12:
		Neighbors.extend([board[StartIndex+1], board[StartIndex-3], board[StartIndex-4]])
		IndexList.extend([StartIndex+1, StartIndex-3, StartIndex-4])
	elif StartIndex == 15:
		Neighbors.extend([board[StartIndex-1], board[StartIndex-4], board[StartIndex-5]])
		IndexList.extend([StartIndex-1, StartIndex-4, StartIndex-5])
	return Neighbors, IndexList

def TraceWord(word, board, index = 0):
	word = word.upper()
	if word.count('Q') == 0:
		for letter in word:	
			if board.count(letter) == 0:
				return False
	i = 0
	StartIndex = []
	for i in range(0,16):
		if word[0] == 'Q':
			if board[i] == 'QU':
				StartIndex.append(i)
		elif board[i] == word[0]:
			StartIndex.append(i)
	i = 0
	UsedIndex = []
	PotentialIndex = []
	test = 1
	for index in StartIndex:
		i = 0
		test = 1
		while i < (len(word) - 1):
			Neighbors = []
			if UsedIndex.count(index) > 0:
				test = 0
				break
			UsedIndex.append(index)
			if word[i] == 'Q':
				i = i + 1
			Neighbors, PotentialIndex = FindNeighbors(word[i], board, index)
			if Neighbors.count(word[i+1]) == 0:
				test = 0
				break
			index = Neighbors.index(word[i+1])
			index = PotentialIndex[index]		
			i = i + 1
		if test == 1:
			return True
	
	return False

d = enchant.Dict("en_US")

D1 = ['A', 'E', 'A', 'N', 'E', 'G']
D2 = ['A', 'H', 'S', 'P', 'C', 'O']
D3 = ['A', 'S', 'P', 'F', 'F', 'K']
D4 = ['O', 'B', 'J', 'O', 'A', 'B']
D5 = ['I', 'O', 'T', 'M', 'U', 'C']
D6 = ['R', 'Y', 'V', 'D', 'E', 'L']
D7 = ['L', 'R', 'E', 'I', 'X', 'D']
D8 = ['E', 'I', 'U', 'N', 'E', 'S']
D9 = ['W', 'N', 'G', 'E', 'E', 'H']
D10 = ['L', 'N', 'H', 'N', 'R', 'Z']
D11 = ['T', 'S', 'T', 'I', 'Y', 'D']
D12 = ['O', 'W', 'T', 'O', 'A', 'T']
D13 = ['E', 'R', 'T', 'T', 'Y', 'L']
D14 = ['T', 'O', 'E', 'S', 'S', 'I']
D15 = ['T', 'E', 'R', 'W', 'H', 'V']
D16 = ['N', 'U', 'I', 'H', 'M', 'QU']
Boggle = []

random.shuffle(D1)
random.shuffle(D2)
random.shuffle(D3)
random.shuffle(D4)
random.shuffle(D5)
random.shuffle(D6)
random.shuffle(D7)
random.shuffle(D8)
random.shuffle(D9)
random.shuffle(D10)
random.shuffle(D11)
random.shuffle(D12)
random.shuffle(D13)
random.shuffle(D14)
random.shuffle(D15)
random.shuffle(D16)
Boggle.append(D1[0])
Boggle.append(D2[0])
Boggle.append(D3[0])
Boggle.append(D4[0])
Boggle.append(D5[0])
Boggle.append(D6[0])
Boggle.append(D7[0])
Boggle.append(D8[0])
Boggle.append(D9[0])
Boggle.append(D10[0])
Boggle.append(D11[0])
Boggle.append(D12[0])
Boggle.append(D13[0])
Boggle.append(D14[0])
Boggle.append(D15[0])
Boggle.append(D16[0])
random.shuffle(Boggle)

for i in range(0, 16):
	if i%4 == 0:
		print("\n")
	print('[', Boggle[i], '] ', sep='', end='')

print('\n')

WordList = []
word = 'temp'
print('Start typing your words!  (press enter after each word and enter X when done):' )

while word != 'X' and word != 'x':
	word = raw_input()
	WordList.append(word)

counter = 0
score = 0
CheckedWords = []
for item in WordList:
	if item == 'X' or item == 'x':
		print('Your total score is', score, 'points.')
	elif WordList.count(item) > 1 and counter > WordList.index(item):
		print('The word', item, 'has already been scored.')
	elif len(item) < 3:
		print('The word', item, 'is too short.')
	elif d.check(item) == False:
		print('The word', item, 'is not a valid word.')
	elif TraceWord(item, Boggle) == False:
		print('The word', item, 'is not present.')
	else:
		if len(item) == 3 or len(item) == 4:
			print('The word', item, 'is worth 1 point.')
			score = score + 1
		elif len(item) == 5:
			print('The word', item, 'is worth 2 points.')
			score = score + 2
		elif len(item) == 6:
			print('The word', item, 'is worth 3 points')
			score = score + 3
		elif len(item) == 7:
			print('The word', item, 'is worth 5 points')
			score = score + 5
		else:
			print('The word', item, 'is worth 11 points')
			score = score + 11
	counter = counter + 1
