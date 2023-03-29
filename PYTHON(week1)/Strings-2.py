//Program to access each character of string in backward direction
s=input("Enter string")
n=len(s)
i=n-1
print("Data in backward direction")
while i>=0:
	print(s[i],end='')
	i=i-1