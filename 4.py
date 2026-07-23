senten=input("Enter a sentence")
vowel="aeiou"
vcount=0
ccount=0

for char in senten.lower():
    if char.isalpha():
        if char in vowel:
            vcount+=1
        else:
            ccount+=1

print(vcount,ccount)
