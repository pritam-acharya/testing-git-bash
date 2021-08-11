# we use the concept of the slice operator with well defined steps ([start:end:step])
sen = "his test went well"
# we will divide the sentence into 4 variables, each assigned to a word.
# we do this so as to get the output as mentioned in the question.
w1, w2, w3, w4 = sen[0:3], sen[4:8], sen[9:13], sen[14:]
print(f"{w1[::-1]} {w2[::-1]} {w3[::-1]} {w4[::-1]}")
print("----------------")
#----------------------------------------------------------------------------------------------------------------
# we will now print "madam i'm adam" using the same method as above.
sent = "madam i'm adam"
print(sent[::-1])
# we observe that the given sentence is a palindrome (if we ignore the inconsistent spacing).
