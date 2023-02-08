s = input()
digits = 0
letters = 0
for i in range(len(s)):
    if s[i].isalpha():
        letters = letters + 1
    if s[i].isdigit():
        digits = digits + 1
print(letters)
print(digits)
