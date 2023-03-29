//different vowels present in the given word
w=input("Enter some word")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowels present in the given word",d)