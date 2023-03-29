//To print characters at odd position without using slice operator
s=input("Enter some string")
i=1
print("The characters at a odd position")
while i<len(s):
	print(s[i])
	i=i+2