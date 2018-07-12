dict1={}
dict1['A']=".-"
dict1['B']="-..."
dict1['C']="-.-."
dict1['D']="-.."
dict1['E']="."
dict1['F']="..-."
dict1['G']="--."
dict1['H']="...."
dict1['I']=".."
dict1['J']=".---"
dict1['K']="-.-"
dict1['L']=".-.."
dict1['M']="--"	
dict1['N']="-."
dict1['O']="---"
dict1['P']=".--."
dict1['Q']="--.-"
dict1['R']=".-."
dict1['S']="..."
dict1['T']="-"
dict1['U']="..-"
dict1['V']="...-"
dict1['W']=".--"
dict1['X']="-..-"
dict1['Y']="-.--"
dict1['Z']="--.."
def alphamatch(arr):
	lis=[]
	lis2=[]
	for i in arr:
		i=i.upper()
		# print(i)
		s=""
		for j in i:
			s=s+dict1[j]
		# print(lis2)
		if s in lis2:
			continue
		else:
			lis2.append(s)
	return len(lis2)
print(alphamatch(["gin", "zen", "gig", "msg"]))
print(alphamatch(["a", "z", "g", "m"]))
print(alphamatch(["bhi", "vsv", "sgh", "vbi"]))
print(alphamatch(["a", "b", "c", "d"]))
print(alphamatch(["hig", "sip", "pot"]))

def recontrtque(arr):
	arr.sort()
	print(arr)
	temp=[0,0]
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if(arr[j][1]<=arr[i][1]):
				if(temp[1]>=arr[j][1]):
					temp=arr[j]
				print (temp)
		arr[i],arr[j]=arr[j],arr[i]
		print(arr)
	return arr

print(recontrtque([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))