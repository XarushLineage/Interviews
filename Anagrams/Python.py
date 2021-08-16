def check(s1, s2):
 
    # Test if they are the same lenght 
    assert len(s1) == len(s2), 'The strings are not of same length, thus not an anagram.'
     
    # set both to lower caps, and compare
    if set(s1.lower()) == set(s2.lower()):
      print("The strings are anagrams.")
    else:
      print("The strings aren't anagrams.")
     

     
 
 
#Driver code
if __name__ == '__main__':
    word1, word2 = 'listen', 'silont'
    check(word1, word2)
