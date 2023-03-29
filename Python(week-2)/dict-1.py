//program to find the no.of occurrences of each vowel present in the given string
word=input("Enter some word")
vowels={'a','e','i','o','u'}
d={}
for x in word:
	if x in vowels:
		d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
	print("{} occurred {} times".format(k,v))