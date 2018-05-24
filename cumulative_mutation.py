import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
            #indexes = 0 > 26
            #elements = 27


def randsen(n):
    result = ''
    for i in range(0,n):
        random_letter = random.randint(0,26)
        result = result + alphabet[random_letter]
    return result
    
def similar(m, n):
	i = 0
	result = 0
	while i < len(m):
		if m[i] == n[i]:
			result = result + (1/len(m))
		i+=1
	return result *100
    
def change(n):
    #print(len(n))
    change_index = random.randint(0, len(n)-1)
    #print(change_index)
    letter_index = random.randint(0, 26)
    #print(alphabet[letter_index])
    if change_index == len(n)-1:
        return n[:change_index] + alphabet[letter_index]
    else:
        return n[:change_index] + alphabet[letter_index] + n[change_index+1:]

#def evolve(n):
target_sen = 'abc'
print('target sen: ', target_sen)
start_sen = randsen(len(target_sen))
print('start sen: ', start_sen)
count = 0
while target_sen != start_sen:
    init_similar = similar(target_sen, start_sen)
    print('init_similar = ', init_similar)
    second_sen = change(start_sen)
    print('second_sen: ', second_sen)
    second_similar = similar(target_sen, second_sen)
    print('second_similar = ', second_similar)
    if second_similar > init_similar:
        start_sen = second_sen
    count +=1
print('generation = ', count)

    


