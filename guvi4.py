#Write a Python code to read an integer in a file e.g 123 and convert it to words e.g One hundred and twenty three and write the result back to the same file such that your file will have "123 One hundred and twenty three " in it
def totxt(num):
	unitp={ 0: "",1: "one",2: "two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine" } 
	tensp={ 0: "",1: "onety",2: "twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty" } 
	hun=num//100
	ten=(num-100*hun)//10
	unit=num-(100*hun+10*ten)
	if hun==0:
		if ten==0:
			if unit==0:
				return "zero"
			else:
				return(unitp[unit])
		else:
			return(tensp[ten]+' '+unitp[unit])
	elif ten==0 and unit==0:
		return(unitp[hun]+' hundred')
	else:
		return(unitp[hun]+" hundred and "+tensp[ten]+' '+unitp[unit])
def main():
	file1 = open("File.txt","r") 
	line=file1.read().split(" ")
	n=int(line[0]) #n=123 from File.txt
	file1.close()
	file2=open("File.txt","a") 
	rn=n
	i=0
	s=""
	while(rn!=0):
		i=i+1
		rn=rn//10
	if i<4:
		s=totxt(n)+s[:]
	elif 3<i<7:
		s=totxt(n//1000)+" thousand and "+totxt(n%1000)+s[:]
	elif 6<i<10:
		s=totxt(n//10**6)+" million and "+totxt((n%10**6)//10**3)+" thousand and "+totxt(n%10**3)+s[:]
	else:
		print("Number too large")
	s=' '+s[0].upper()+s[1:]
	file2.write(s)
	file2.close()
	
main()
