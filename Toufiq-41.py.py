s = input("Enter your full name: ")
v = c = 0

# Count vowels and consonants
for i in s.lower():
    if i.isalpha():
        if i in 'aeiou':
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)

# Print ASCII values
for char in s:
    print(char, "ASCII value of character:", ord(char))

# Display reversed version and check for palindrome
reversed_s = s[::-1]
print("Reversed name:", reversed_s)

if s == reversed_s:
    print("Palindrome")
else:
    print("Not palindrome")
#sort uniuqe letter alphabetically

    letters = set(s.replace(" ", "").lower())
    sorted_letters = sorted(letters)
    print("Unique sorted letters:", sorted_letters)