"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64 + 32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number1 = 64
number2 = 32
sumation = (number1 + number2)
print(sumation)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
software = "Houdini"
version = "18.5"
simType = "pyro"
print("This " + simType + " simulation was done in " + software + ", version " + version)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program."
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

#Version 1 of Answer 5
value1 = 2112
value2 = 1188
finalSentence = ("The 10% overscan of 1920 is " + str(value1) + ", and the 1080 is " + str(value2))
print(finalSentence)

#Version 2 of Answer 5
newVal_1 = "2112"
newVal_2 = "1188"
finalSentence = ("The 10% overscan of 1920 is " + newVal_1 + ", and the 1080 is " + newVal_2)
print(finalSentence)

#Version 3 of Answer 5
val_1 = 1920 + (10*(1/100) * 1920)
val_2 = 1080 + (10*(1/100) * 1080)
newString = ("The 10% overscan of 1920 is " + str(val_1) + ", and the 1080 is " + str(val_2))
print(newString)