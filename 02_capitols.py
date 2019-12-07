f = open("/nfs/2019/p/pveda/Desktop/capitols.txt", 'r')
txt = f.readlines()
whole_txt = [x.strip() for x in txt]
whole_txt = dict(map(lambda c: c.split(","), whole_txt))

key_list = list(whole_txt.keys())
value_list = list(whole_txt.values())

y = input("Ready: ")

while y != "Done":
    if y in key_list:
        print(value_list[key_list.index(y)])
        y = input("Ready: ")
    elif y in value_list:
        print(key_list[value_list.index(y)])
        y = input("Ready: ")
    else:
        print("nil")
        y = input("Ready: ")



            

        




