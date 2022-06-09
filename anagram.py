"using sort function"
def anagram_check(str1,str2):
	if(sorted(str1)==sorted(str2)):
		print("both strings are anagram")
	else:
		print("both strings are not anagram")
string1=input("enter the string:")
string2=input("enter the string2:")
print("string value1:",string1)
print("string value1:",string2)
anagram_check(string1,string2)
"using counter function"
from collections import counter
def check(s1,s2):
	if(counter(s1)==counter(s2)):
		print("the strings are angrams.")
	else:
		print("the string aren't anagrams.")
s1=input("enter the string1")
s2=input("enter the string2")
check(s1,s2)

