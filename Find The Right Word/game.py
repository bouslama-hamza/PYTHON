import random

File = open("mots.txt","r")

word_win = list(random.choice(File.readlines()))

print(''.join(word_win[:-1]))

File.close()

word = ['-']*len(word_win[:-1])

i = 6

while (word != word_win[:-1]) and (i >= 1) :

    print("You Still Have",i,"Chance : \n")

    a = str(input(''.join(word))) 

    if a in word_win:

        indic = word_win.index(a)

        if a in word :

            old = word_win.index(a)

            word_win[old] = 1

            indic = word_win.index(a)

            word_win[old] = a

        word[indic] = a

        print("\n***********GOOD************\n")

    else:

        print("\n***********Bad*************\n")

        i -= 1

if word == word_win[:-1]:

    print("\n**********YOU WIN*********\n")

else :

    print("\n*********YOU LOSE*********\n")

    

