passwords = []

with open('dictionary.txt', 'rb') as f:
    for lines in f:
        pw = str(f.readline())
        passwords.append(pw[2:6])
        
print(passwords)
print(len(passwords))