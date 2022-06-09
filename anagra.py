str1=input("enter string:")
str2=input("enter string:")
dict1={}
dict2={}
for i in str1:
	dict1[i]=str1.count(i)
print(dict1)
for i in str2:
	dict2[i]=str2.count(i)
print(dict2)
count=0
if len(str1)!=len(str2):
	print("given string is not anagram ")
else:
	for k in dict1.keys():
		if k in dict2.keys() and dict1[k]==dict2[k]:
				count=count+1
if count==len(dict1):
	print("given both strings are anagram to each other.")
else:
	print("given both strings are not anagram to each other.")
