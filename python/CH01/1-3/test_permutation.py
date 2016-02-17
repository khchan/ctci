import unittest
from permutation import *

class TestPermutation(unittest.TestCase):
  def testEmpty(self):
    '''is_permutation must return true for empty strings'''
    self.assertTrue(is_permutation('', ''))

  def testSingle(self):
    '''is_permutation must return true for single character strings'''
    self.assertTrue(is_permutation('a', 'a'))

  def testDoubleEq(self):
    '''is_permutation must return true for double same-character strings'''
    self.assertTrue(is_permutation('aa', 'aa'))

  def testValid(self):
    '''is_permutation must return true for known anagrams'''
    words = ( ('So dark the con          of man', 'Madonna of        The Rocks'),
          (' ba ', ' Ab   ') )
    for (x, y) in words:
      self.assertTrue(is_permutation(x, y))

  def testInvalid(self):
    '''is_permutation must return false for known non-anagrams'''
    words = ( ('hello', 'ello'),
          (' anne ', ' annea   ') )
    for (x, y) in words:
      self.assertFalse(is_permutation(x, y))

if __name__ == '__main__':
  unittest.main()