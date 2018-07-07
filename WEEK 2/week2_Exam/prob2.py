def room_keys(lis1):
	lis2=[]
	for i in range(1,len(lis1)):
		lis2.append(i)
	for i in range(len(lis1)):
		for j in lis1[i]:
			if j in lis2 and j!=i:
				lis2.remove(j)
	return len(lis2)==0
print(room_keys([[1], [0,2], [3]]))
print(room_keys([[1,3], [3,0,1], [2], [0]]))
print(room_keys([[1,2,3], [0], [0], [0]]))
print(room_keys([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print(room_keys([[1], [2,3], [1,2], [4], [1], [5]]))
print(room_keys([[4], [0], [1], [2], [3]]))
print(room_keys([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))
