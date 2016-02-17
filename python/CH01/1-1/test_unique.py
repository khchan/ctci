import unittest
from unique import *

class TestUnique(unittest.TestCase):
  def testEmptyStr(self):
    '''is_unique must return True with empty strings'''
    result = is_unique('')
    self.assertTrue(result)

  def testSingleCharStr(self):
    '''is_unique must return True with single character strings'''
    result = is_unique('a')
    self.assertTrue(result)

  def testDoubleCharStr(self):
    '''is_unique must return True with double character strings that don't have the same characters'''
    result = is_unique('ab')
    self.assertTrue(result)

  def testStrWithTwoConsChar(self):
    '''is_unique must return False with strings that have two same consecutive characters'''
    result = is_unique('aab')
    self.assertFalse(result)

  def testStrWithTwoNonConsChar(self):
    '''is_unique must return False with strings that have two same non consecutive characters'''
    result = is_unique('aba')
    self.assertFalse(result)

  def testStrWithNoConsChar(self):
    '''is_unique must return True with strings that have all unique characters'''
    result = is_unique('promise')
    self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
