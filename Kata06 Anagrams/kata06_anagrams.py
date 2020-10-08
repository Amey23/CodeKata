import sys
import itertools

def setupDictionary(filepath) :
  fileName = filepath
  file = open(fileName,"r")
  words = file.readlines()
  file.close()
  upperWords = list()
  for word in words :
      upperWords.append(word.lower().strip('\n'))
  return upperWords

dictionary = setupDictionary("words.txt")
#dictionary

total_words = setupDictionary("unixWords.txt")
#total_words

a_set = set(total_words)
#a_set

for word in dictionary:
  print(word)
  ang = []
  ang = ["".join(perm) for perm in itertools.permutations(word)]
  ang.remove(word)
  #print(ana)
  b_set = set(ang)
  #print(a_set)
  #print(b_set)
  if (a_set & b_set):
    anagrams = (a_set & b_set)
    print(anagrams)
  else:
    print("No anagram elements found in words text file.")

