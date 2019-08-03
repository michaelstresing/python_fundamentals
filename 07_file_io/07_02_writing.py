'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

wordlist = []

with open('words.txt', 'r') as fin:
        for word in fin:
            word = word.rstrip()
            wordlist.append(word)

# print(wordlist)

wordlist.reverse()

with open('reversewords.txt', 'w') as fout:
        for word in wordlist:
            fout.write(f"{word}\n")

