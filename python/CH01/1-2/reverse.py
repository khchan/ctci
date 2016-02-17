'''
1.2) Implement a function that reverses a null terminated string
'''

def reverse(s):
  return s[::-1]

if __name__ == '__main__':
  words = ('mary', 'anna', 'peter')
  for word in words:
    print('reverse({}): {}'.format(word, reverse(word)))