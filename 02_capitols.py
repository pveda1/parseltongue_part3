#f = open("/nfs/2019/p/pveda/Desktop/capitols.txt", 'r')
#txt = f.read()
#new_lst = txt.split(",")
d = {'h': 2, "j": 3, "p": 6}

#count = 0

#for x in new_lst:
#    if count%2 == 0:
#        d[x] = d[new_lst.index(x)+1]
#        count+=1

y = input("Ready: ")
while y != "Done":
    for ch in d:
        if ch == y:
            print(d[ch])
            y = input("Ready: ")
            break
        elif d[ch] == y:
            print(ch)
            y = input("Ready: ")
            break
        elif ch not in d:
            print("nil")
            y = input("Ready: ")
            break 
        else:
            break 



hello 

            

        




