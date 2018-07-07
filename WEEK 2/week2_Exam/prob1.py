def areAnagram():
	NO_OF_CHARS = 256
	s1 = input()
	s2 = input()
	s1=s1.lower()
	s2=s2.lower()
	s1=s1.replace(" ", "")
	s2=s2.replace(" ", "")
	# print(s1,s2)
	count1 = [0] * NO_OF_CHARS
	count2 = [0] * NO_OF_CHARS
	for i in s1:
	    count1[ord(i)]+=1 
	for i in s2:
	    count2[ord(i)]+=1
	# print(count1)
	# print(count2)
	if len(s1) != len(s2):
		return 0
	for i in range(NO_OF_CHARS):
	    if count1[i] != count2[i]:
	    	return 0
	return 1
if(areAnagram()):
	print("True")
else:
	print("False")
