def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
    print("Your reversed string is", str)

def countvowels(s):
    num_vowels=0
    for char in s:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    print ("Your string has", num_vowels, "vowels")

#I call a function inside a function here.
def palindrome(s):
    if reverse(s) == s:
        print("This is a palindrome")
    else:
        print("This is not a palindrome.")



answer = input("Do you want information on your string? Y or N\n").upper()
#Note it does not matter if the user enters a capital or lowercase letter

if answer == "Y":
  string = input("Please enter your string\n")
  reverse(string)
  countvowels(string)
  palindrome(string)
else:
    print("Okay. Maybe later.")
