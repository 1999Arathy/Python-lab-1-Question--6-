#Ask the user for a string and print out whether this string is a palindrome or not

palindrome_str = int(input("enter a string"))
duplicate_str = palindrome_str
rev =0
for y in str(duplicate_str):
        
        rem = duplicate_str %10
        rev = rev*10 +rem
        duplicate_str//=10
if(rev == palindrome_str):
    print("The number is a palindrome")
else:
      print("The number is not a palindrome")
        
