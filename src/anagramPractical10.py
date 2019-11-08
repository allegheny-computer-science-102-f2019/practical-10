#!/usr/bin/env python3

__author__      = ""
__date__        = "8 November 2019"

#TODO: Put the tabs back in their rightful places to fix the code!

class Anagram:
""" The Anagram class"""
def __init__(self, word):
print("  Hi! This is the Anagram class")
self.word = word.lower()
self.lines_list = []
self.perms_list = []
#end of __init__

def get_word_list(self):
"""Opens the unix word file located in /usr/share/dict/web2 """
#data.self = open("words.txt","r").read() #get a string
print("  + Getting big word list...")
with open("words.txt") as file: # open the word file, make a list of words
self.lines_list = [line.strip().lower() for line in file]
# note: the largest word that you can expect to enter to find a parmutation is shown below
print("  --> Max size of word in the big word list:",len(max(self.lines_list)))
#end of get_word_list()

def get_permutations(self):
""" Makes a list of permutations of word"""
print("  + Getting perms list...")
try:
self.perms_list = [''.join(p) for p in itertools.permutations(self.word)]
except MemoryError:
print("  - Oops! It looks like you ran out of memory. Maybe try a shorter word? Exiting...")
exit()
#print("  self.perms_list: ",self.perms_list)
return self.perms_list
#end of get_permutations

def is_in_word_list(self, in_list):
""" Method to check if a word is in the big list of words"""
#print(" ### is_in_word_list() input is: ",in_list)
output_list = []
for i in in_list:
#print(" checking self.perms i =",i)
if i in self.lines_list:
output_list.append(i) #make a list of found anagrams
output_set = set(output_list) # no repetition in words, please
try: # catch any errors here
output_set.remove(self.word)
except KeyError: # if an error is present, ignore it, continue
pass
if len(output_set) > 0:
print("\n  Anagram(s) found : ",output_set)
else:
print("\n  No anagrams found. :-(")
#end of is_in_word_list()
#end of Anagram class


### beginning of the program here
def begin(word_str):
""" Driver function of the program"""
print(" Input Word: ",word_str)
thisTask = Anagram(word_str) # word not larger than 6 chars
thisTask.get_word_list()
myList = thisTask.get_permutations()
#print("root: ",myList)
thisTask.is_in_word_list(myList)
#end of begin()

def help():
"""help function to help use the program"""
print("  ",__author__,"::",__date__)
print("   The anagram program to take a word, find its permutations")
print("   and see if any of them are in a larger list of words.")
print("   This large list of words is the file: /usr/share/dict/web2")
print("\n   Usage example for the word, 'sister'\n   python3 anagram.py sister")
#end of help()


# command line paramters code
###################################
import itertools, sys
if __name__ == '__main__':

if len(sys.argv) == 2: #one option added to command line
begin(sys.argv[1])
else:
help()
sys.exit(0)
