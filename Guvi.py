#1 write a python program to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in the string "Guvi geeks network private limited"

# Input string
input_string = "guvi geeks network private limited"

# Convert the input string to lowercase to handle both uppercase and lowercase vowels
input_string = input_string.lower()

# Initialize variables to count individual vowels
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate through the characters in the string
for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

# Calculate the total number of vowels
total_vowels = count_a + count_e + count_i + count_o + count_u

# Print the counts
print("Total number of vowels:", total_vowels)
print("Count of 'a':", count_a)
print("Count of 'e':", count_e)
print("Count of 'i':", count_i)
print("Count of 'o':", count_o)
print("Count of 'u':", count_u)

#2 create a pyramid of numbers from 1 to 20 using for loop
#input:
for i in range(1,21):
    print()
    for j in range(1,i+1):
        print(j,end="")

# 3 write a function that takes a string and returns the number a new string with all the vowels removed
def remove_vowels(string):
  vowels = set("aeiou")          # set vowels
  new_string = ""                # create empty string
  for char in string:            # char == string
    if char not in vowels:       # prydhrshn
      new_string += char         # Add the char which are not presented in vowels
  return new_string

print(remove_vowels("priyadharshini"))


#4    write a function that takes a string and returns the number of unique characters in it


def count_unique_characters(string):
  unique_characters = set()            # empty set created because set does not allow duplicate values
  for character in string:             # character == string
    unique_characters.add(character)    # add characters
  return len(unique_characters)
print(count_unique_characters("priyadharshini"))


#5  write a function that takes a string and returns true if it is pallindrome  , false otherwise
def is_palindrome(string):
  string = string.lower().replace(" ", "")    # convert the string as lower case and remove gaps
  reversed_string = string[::-1]           # reverse ,it returns the value from backwards
  return string == reversed_string

print(is_palindrome("madam"))


#6
def longest_common_substring(str1, str2):
    max_length = 0
    start_index = 0
    for i in range(len(str1)):      # 14
        for j in range(len(str2)):   # 8
            length = 0
            while i + length < len(str1) and j + length < len(str2) and str1[i + length] == str2[j + length]:    # 14<14 and 8<8  and  str1[14]==str2[8]
                length += 1
            if length > max_length:
                max_length = length
                start_index = i
    longest_substring = str1[start_index:start_index + max_length]
    return longest_substring

str1 = "abcdef"
str2 = "bcdfg"
result = longest_common_substring(str1, str2)
print("Longest common substring:", result)

print(longest_common_substring("priyadharshini","pradeepa"))



# 7 write a function that takes a string and returns most frequent charcter in it
def most_frequent_character(string):
  character_counts = {}          # create empty dict
  for character in string:
    if character in character_counts:
      character_counts[character] += 1      # if same char repeated add the count
    else:
      character_counts[character] = 1       # if not repeated take the count as 1
  most_frequent_character = max(character_counts, key=character_counts.get)    # by using max function it fetch max count from the string by using the key only it correctly fetch the max count

  return most_frequent_character

print(most_frequent_character("geeksforgeeks"))

# 8

# anagram means we take one word like heart then change that as Earth .. It is anagram. by taking one meaningful word and change that to other meaningful word
def is_anagram(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  str1 = sorted(str1)       # sorted used to order in alphabetical order to easily identify whether it is anagram or not
  str2 = sorted(str2)
  return str1 == str2

print(is_anagram("listen","silent"))

#9  write a function that takes a string and returns number of word in it

def count_words(string):
  words = string.split()  # by using split for eg "hello world" it returns 1 can changed as "hello" "world" it returns 2
  return len(words)
print(count_words("pavithra"))
print(count_words("priya dharshini"))



