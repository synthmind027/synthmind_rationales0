print()
with open('dictionary.txt','r') as f:
	dat = f.read().split()

word_set = dict()
for x in dat:
	word_set[x] = 0

#print(word_set)

with open('rationales.txt','r') as f:
	dat = f.read().split()

count_error = 0
for x in dat:
	if x not in word_set:
		print(f'check this: {x}')
		count_error = count_error + 1
print()
print(f'{count_error} error found.')
print('done') 
