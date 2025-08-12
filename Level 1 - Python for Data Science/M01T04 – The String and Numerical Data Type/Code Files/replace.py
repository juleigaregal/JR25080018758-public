#manipulating strings in python using various built in functions

#this code uses the replace function to remove the ! and replace with a space
#Stores the manipulated string into a new variable and prints 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence_replace = sentence.replace("!", " ")
print(sentence_replace)
print(sentence_replace.upper()) #prints in uppercase
print(sentence_replace[::-1].upper()) #print sentence in reverse order with uppercase