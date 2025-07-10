from collections import Counter

#COUNT THE NUMBER OF VOWELS IN A STRING
print("COUNT THE NUMBER OF VOWELS IN A STRING")
s=input('\nEnter a string to work with ')
count=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print("no. of vowels in string ",s,' are ',count)
print("\n")

#COUNT NUMBER OF WORDS IN A STRING
print("#COUNT NUMBER OF WORDS IN A STRING")
op=int(input('CHOOSE YOUR OPTION: 1. Count using traditional logic' \
' 2. Count using Counter '))
if op==1:
    word_count=0
    for k in range(len(s)):
        if s[k]==" ":
            word_count=word_count+1
    print("Number of words in the inputted string are",word_count+1)
elif op==2:
    word_count = Counter(word for word in s.lower().split())
    total_words = sum(word_count.values())
    print("Total number of words: ", total_words)


#REVERSE A STRING
reverse=""
s=input("Enter a String ")
for a in range(len(s) - 1, -1, -1):
    reverse += s[a]

print("\nReversed string is:", reverse)


#CHECK IF STRING IS A PALINDROME
a=0
rev=""
print("CHECK IF STRING IS A PALINDROME")
str=input("Enter a String ")
for a in range(len(str) - 1, -1, -1):
    rev += str[a]

print("\nReversed string is:", rev)

if str == rev:
    print("\nThe string is a palindrome.")
else:
    print("\nThe string is not a palindrome.")


