'''
1.2) Given two strings, write a method to decide if one is a permutation of the other.
'''

def is_permutation(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  str1 = ''.join(sorted(str1)).strip()
  str2 = ''.join(sorted(str2)).strip()
  return str1 == str2

if __name__ == '__main__':
  words = [('peter', 'harry'), ('star', 'rats')]
  for s1, s2 in words:
    print('is_permutation({}, {}): {}'.format(s1, s2, is_permutation(s1, s2)))