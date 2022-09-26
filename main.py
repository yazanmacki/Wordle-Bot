from nltk.corpus import words
word_list = words.words()

from wordfreq import word_frequency

# prints 236736

fiveLetterWords = []


for i in range(0, len(word_list)):
    if len(word_list[i]) == 5:
        fiveLetterWords.append(word_list[i])

wordsFreq = [" "] * len(fiveLetterWords)

for i in range(0, len(fiveLetterWords)):
    fiveLetterWords[i] = fiveLetterWords[i].lower()
    wordsFreq[i] = word_frequency(fiveLetterWords[i], 'en')



yellow = []
yellowIndex = []

green = []
greenIndex = []

black = []

maxIndex = 0

for i in range(0, len(fiveLetterWords)):
    if wordsFreq[i] > wordsFreq[maxIndex]:
        maxIndex = i


#print(wordsFreq[maxIndex])

print("\n\n")
print("Enter colors of every corresponding letter in each guess.\nBlack: b, Yellow: y, Green: g")
print("\n")

guess = 'about'
print(guess)

guesses = []

for i in range(0,14):

    colors = input("Enter Colors: ")

    for j in range(0,5):
        if colors[j] == "g":
            green.append(guess[j])
            greenIndex.append(j)
        elif colors[j] == "y":
            yellow.append(guess[j])
            yellowIndex.append(j)
        else:
            black.append(guess[j])


    if colors == "ggggg":
        print("Word Found")
        break

    maxIndex = 0

    maxFreq = -1

    for k in range(0, len(fiveLetterWords)):

        valid = True

        if fiveLetterWords[k] in guesses:
            valid = False

        for letter in fiveLetterWords[k]:
            if letter in black and letter not in green and letter not in yellow:
                valid = False

        for g in range(0, len(greenIndex)):
            if fiveLetterWords[k][greenIndex[g]] != green[g]:
                valid = False

        for y in range(0, len(yellow)):
            if fiveLetterWords[k][yellowIndex[y]] == yellow[y]:
                valid = False
            if yellow[y] not in fiveLetterWords[k]:
                valid = False

        if valid and wordsFreq[k] > maxFreq:
            maxFreq = wordsFreq[k]
            maxIndex = k



    guess = fiveLetterWords[maxIndex]
    print(guess)

    guesses.append(guess)

