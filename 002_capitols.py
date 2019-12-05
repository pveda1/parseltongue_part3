#f = open("/nfs/2019/p/pveda/Desktop/capitols.txt", 'r')
#txt = f.read()
#new_lst = txt.split(",")
d = {'h': 2, "j": 3, "p": 6}

#count = 0

#for x in new_lst:
#    if count%2 == 0:
#        d[x] = d[new_lst.index(x)+1]
#        count+=1

#y = input("Ready: ")
#for ch in d:
#	while y != "Done":
#        	if ch == y:
#	  	        print(d[ch])
#			y = input("Ready: ")
#            		break
#	        elif d[ch] == y:
#			print(ch)
#            		y = input("Ready: ")
#            		break
#        	elif ch not in d:
#  		          print("nil")
#            		y = input("Ready: ")
#  		          break


y = input("Ready: ")
for ch in d:	
	d[ch] = k
	if y == k:
		print(d)
		y = input("Ready: ")


#one letter typed will work; still have to stop infinite loop for other inputs
#need to figure out how to compare input to value of key in dictionary
#figure out how to split list into dictionary; right now, only split into individual words per capitol and state

