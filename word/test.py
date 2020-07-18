import sys
import unittest
from timeit import default_timer as timer
sys.path.append('C:\\Users\\733598\\Desktop\\')
from word import Word
from word import getAnagrams


#b=Word("Nir")
#print(b.getAnagrams())
#print(b.isPalindrome())

#print(getAnagrams(""))


class TestWord(unittest.TestCase):
    def test_word(self):
        '''Test 1: Test a word hello  '''
        self.assertTrue(getAnagrams('hello'))
    def test_num(self):
        '''Test 2: Test a number word 123 - Raise exception  '''
        self.assertRaises(Exception,getAnagrams,'123')



if __name__ == '__main__':
    unittest.main()




    
