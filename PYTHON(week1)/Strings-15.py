/* inputs:
	s1=RAVI
	s2=TEJA
   output : RTAEVJIA   */
s1=input("Enter first string")
s2=input("Enter second string")
output=''
i=j=0
while i<len(s1)or j<len(s2):
	outut=output+s1[i]+s1[j]
	i=i+1
	j=j+1
print(output)