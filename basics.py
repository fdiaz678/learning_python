rows = 5
star =' *'
for x in range(rows):
    print(' '*(rows-x)+star*(x+1))
rows1 =4

rows1 = 4
for i in range(rows1):
    print(' '*(i+2)+star*(rows1-i))


letters = ['a', 'b', 'c', 'd', 'g', 'f','c', 'e']

newLetters = letters.copy()#creates a copy of the list letters
newLetters.reverse()# reverses the sequence of the list (newLetters)

letters.sort()#sorts the list letters in alphabetical order
print(letters)
print(newLetters)

sentence = ' ' #adds a space between the objects in new_sentence
new_sentence = sentence.join(['Hi','my','name','is','Francisco'])
print(new_sentence)
