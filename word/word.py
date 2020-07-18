import re
import math
import decorators
import utility
import pdb
import json
from os import remove

class Word(str):
    
    def __init__(self,word=None):
        self._word=word
        self._length=len(self._word)
        self._anagrams=list()

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self,word):
        if word is not None:
            pattern=re.compile('[^A-Za-z ]')
            if pattern.search(word) is None:
                self._word=word
            else:
                raise Exception(f'Error: Given word {word} has Non-Alpha characters')
                
        else:
            self._word=''

        self._length=len(self._word)
        

    @decorators.performance
    def getAnagrams(self,w=None):
        if w is not None:
            self.word=w
        #pdb.set_trace()
        iterations=math.factorial(self._length)-1
        index=0
        offset=0
        iterno=self._length
        remove('anagrams.txt')
        #self._anagrams.append(list(self._word))
        with open('anagrams.txt','a') as fw,open('anagrams.txt','r') as fr:
            fw.write(json.dumps(list(self.word))+'\n')
            fw.flush()
            while iterations:
                anagram=json.loads(fr.readline().strip('\n'))
                new_anagram=utility.rotate(anagram[offset:],anagram[:offset])
                fw.write(json.dumps(new_anagram)+'\n')
                fw.flush()
                if index!=iterno-2:
                    index += 1
                else:
                    offset += 1
                    index = 0
                    fr.seek(index)
                    iterno *= (iterno-1)            
                iterations -= 1

        
        #for i in range(len(self._anagrams)):
         #   self._anagrams[i]=utility.to_str(self._anagrams[i])
        return 'anagrams.txt'
            


    def isPalindrome(self,word=None):
        if word is None:
            word=self.word
        try:    
            return word==word[::-1]
        except Exception as err:
            return f'Error: {err}'
        
        
    def getPalindromes(self,length=0):
        li=list(range(ord('a'),ord('a')+25))
                


_inst=Word("")
isPalindrome=_inst.isPalindrome
getAnagrams=_inst.getAnagrams

if __name__ == '__main__':
    _inst.word=input("Enter word: ")
    print(getAnagrams())
    


