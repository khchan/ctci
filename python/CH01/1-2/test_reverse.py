import unittest
from reverse import *

class TestReverse(unittest.TestCase):
  def testEmpty(self):
    '''reverse must return the same string for empty strings'''        
    self.assertEqual('', reverse(''))

  def testSingle(self):
    '''reverse must return the same string for single character strings'''
    self.assertEqual('a', reverse('a'))

  def testDoubleEq(self):
    '''reverse must return the same string for double same-character strings'''
    self.assertEqual('aa', reverse('aa'))

  def testDoubleDiff(self):
    '''reverse must return the reversed for double character strings'''
    self.assertEqual('ba', reverse('ab'))

  def testValid(self):
    '''reverse must return the reversed of known strings'''
    words = ( ('mary', 'yram'),
          ('peter', 'retep'),
          ('anna', 'anna') )
    for (orig, exp) in words:
      expected = reverse(orig)
      self.assertEqual(expected, exp)

  def testInvalid(self):
    '''reverse must not match the non-reversed of known strings'''
    words = ( ('hello', 'olle'),
          ('henry', 'yrnhe') )
    for (orig, nonexp) in words:
      expected = reverse(orig)
      self.assertNotEqual(expected, nonexp)

if __name__ == '__main__':
  unittest.main()