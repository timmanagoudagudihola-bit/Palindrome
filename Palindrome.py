import sys

s = sys.argv[1]

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")