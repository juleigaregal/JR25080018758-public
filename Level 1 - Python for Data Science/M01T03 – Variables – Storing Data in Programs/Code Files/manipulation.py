
str_manip = input("Please enter a sentence:")
#print(str_manip)
print(len(str_manip))

str_manip_last_letter = str_manip[-1] #finds and stores the last letter into a variable
#print(str_manip_last_letter)  #print the last str_manip_last_letter
str_manip_replace_last_letter = str_manip.replace(str_manip[-1], "@")
print(str_manip_replace_last_letter)

get_last_word = str_manip.split() # split breaks up the words in the sentence into an array, so easy to get the last word
last_word = get_last_word[-1] #store the last word

#print(get_last_word)
print(last_word[-3:][::-1]) #slice the last word get the last 3 letters and reverse the output

print(str_manip[0:3]+str_manip[-2:]) #combines the first 3 characters and last 2 characters of the sentence
