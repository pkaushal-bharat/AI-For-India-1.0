#Write a Python code to reverse the given integer and print the integer
n=int(input())
rn=i=0
while((n)!=0):
	i=i+1
	rn=rn*10+(n%10)
	n=n//10
print(rn)