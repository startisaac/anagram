# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #Unequal Length strings cannot be anagrams
    if len(word) != len(anagram):
        return False
    
    #sort the first string
    first = sorted(word)
    #sort the second string
    second = sorted(anagram)
    
    #check if both the strings are same
    if first == second:
        return True
    else:
        return False

    # return True
example1 = find_anagram("hello", "check")
example2 = find_anagram('below', 'elbow')
print (example1)
print (example2)

