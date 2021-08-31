#Get a list of name as an input from the user and make the first letters in caps and print each word as a list
print("Enter the list of names with space between them:\n")
s=input()
s=s.split(" ")
l=[]
for x in s:
	l=[x[0].upper()+x[1:]]
	print(l)