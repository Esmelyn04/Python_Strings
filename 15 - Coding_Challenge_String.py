"""
    Return the number of unique letter in a word
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Write your unique_english_letters function here:
def unique_english_letters (word):
  letter_list = []
  for letter in word:
    if letter not in letter_list:
      letter_list.append(letter)
  return len(letter_list)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Solution #2
def unique_english_letters_2(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters_2("mississippi"))

"""
    Return the number of time x appears in word
"""
# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

"""
    This function should return the substring between the first occurrence of start and end in word.

    Hint: 
    Begin by finding the indices of the start and end characters by using word.find(start) and word.find(end).
    If either of those indices are -1, then the original string didn't contain one of those characters, and you should return word.
    If neither are -1, then slice word using those indices. Remember, slicing is [inclusive:exclusive]!
"""
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

"""
    This function should return True if every word in sentence has a length greater than or equal to x.

    Hint:
    First create a list of every word in sentence by using sentence.split().
"""
# Write your x_length_words function here:
def x_length_words(sentence, x):
  word_list = sentence.split(" ")
  for word in word_list:
    if len(word) < x:
      return False
  return True


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

"""
    1. Check Name

    The function should return True if name appears in sentence in all lowercase letters, 
    all uppercase letters, or with any mix of uppercase and lowercase letters. 
    The function should return False otherwise.

    Hint:
    name.lower() in sentence.lower() will help you find out if the name is in the sentence.
    In order to ignore differences in capitalization,
    we can use the .lower() function which converts all characters to lowercase characters.
"""
# Write your check_for_name function here:
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#Solution #2
# Write your check_for_name function here:
def check_for_name_2(sentence, name):
  return name.lower() in sentence.lower() or name.upper() in sentence.upper() or name in sentence

# Uncomment these function calls to test your  function:
print(check_for_name_2("My name is Jamie", "Jamie"))
# should print True
print(check_for_name_2("My name is jamie", "Jamie"))
# should print True
print(check_for_name_2("My name is Samantha", "Jamie"))
# should print False

"""
    2. Every Other Letter

    The function should return a string containing every other letter in word.
    Loop through the input string while incrementing by two every time

    Return a String of every two letters
"""
# Write your every_other_letter function here:
def every_other_letter(word):
  letter_list = ""
  for letter in range(0, len(word), 2):
    letter_list += word[letter] 
  return letter_list

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

"""
    3. Reverse

    The function should return word in reverse.

    hint:
    You want it to start at the last index of your string (len(my_string)-1) and end at 0.
    Remember, the range function can take three parameters: the starting number (inclusive), 
    the ending number (exclusive), and the step. To count down, make the step -1.
    
    range(star, end, step)
    range(start(inclusive), end(exclusive), step)
"""

# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for letter in range(len(word)-1, -1, -1):
    reverse += word[letter]
  return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

"""
    4. Make Spoonerism

    We're going to switch the first letters of each word. Return the two new words as a single string separated by a space.

    Hint:
    word2[0] will access the first letter of word2. word1[1:] will access everything but 
    the first letter of word1. Combining those with a + will give you your first new word.

"""
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:] + " " + word1[0]+word2[1:] 



# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

"""
    5. Add Exclamation
    This function should add exclamation points to the end of word until word is 20 characters long.
    If word is already at least 20 characters long, just return word.

"""

# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word += "!"
    print(word)
  return word 

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn