'''
1.1) Implement an algorithm to determine if a string has all unique characters.
     What if you cannot use additional data structures?
'''

def is_unique(string):
  hashTable = set()
  for char in string:
    if char in hashTable:
      return False
    hashTable.add(char)
  return True

if __name__ == '__main__':
  words = ['isnotunique', 'abcdefghi']
  for word in words:
    print 'is_unique({}): {}'.format(word, is_unique(word))
