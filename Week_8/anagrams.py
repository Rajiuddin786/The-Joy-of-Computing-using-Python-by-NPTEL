st1=input('Enter first string: ')
st2=input('Enter second string: ')

print(sorted(st1))
print(sorted(st2))


if(sorted(st1)==sorted(st2)):
    print("These are anagram")
else:
        print("These are not anagram")
