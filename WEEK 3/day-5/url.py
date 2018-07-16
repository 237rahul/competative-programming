def shorteningurl(string):
	dictionary={}
	for i in range(len(string)):
		dictionary[i]=string[i]
	return dictionary


short = 7
shorturl={}
dict2={}
count=0
base=shorteningurl("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def methodshort(url):
	if (url in dict2):
		print("ShortURL Exists"+dict2[url])
		return
	global count
	s=""
	q=count
	count+=1

	if (q==0):
		s="0000000"
		if (s not in shorturl):
			shorturl[s]=url
			dict2[url]=s
			print("short URL for "+url+" is https://ca.ke/"+s)
			return

	while(q!=0):
		s=base[q%62]+s
		q=q//62
	l=len(s)

	if (l<short):
		for i in range(short-l):
			s="0"+s

	if (s not in shorturl):
		shorturl[s]=url
		dict2[url]=s

	print("https://ca.ke/"+s)

while (True):
	print("\n\t1)Generate ShortURL\n\t2)Redirect ShortURL\n\t3)Stop\n\tYour option:",end="")
	i=int(input())
	if (i==1):
		url=input("Enter URL: ")
		methodshort(url)
	elif (i==2):
		correct=input("Enter a short URL: ")
		if shorturl.get(correct,None) is not None:
			print("Redirect to "+shorturl[correct])
		else:
			print("URL does not exist")
	elif(i==3):
		break
	else:
		print("Please enter valid Input")