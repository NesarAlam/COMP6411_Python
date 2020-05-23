import socket

dict2 = {}
dict1 = {}
with open('data.txt', 'r') as f:
  for line in f:
      record = list(line.strip().split('|'))
      dict2['age']= record[1]
      dict2['address']= record[2]
      dict2['phone']= record[3]
      dict1[record[0].title()] = dict2
      dict2 = {}

no_name=''
if no_name in dict1:
    del dict1[no_name]

def firstfunc(name1):

    if name1 in dict1:
        i = "\n"+name1+","+"age: " + dict1[name1]["age"] + "," + "address: " + dict1[name1]["address"] + "," + "Phone: " + dict1[name1]["phone"]
        return i
    else:
        i ="\nNot found\n"
        return i

def secondfunc(name,age,address,phone):
    if name in dict1:
        c="\nCustomer already exist\n(name supposed to be unique)\n"
        return c
        # address_dict = dict1[name]["address"]
        # age_dict = dict1[name]["age"]
        # phone_dict = dict1[name]["phone"]
        #
        # if ((age_dict==age) and (phone_dict==phone) and (address_dict==address) ):
        #     c="Customer already exist"
        #     return c

    dict3={}
    dict3['age']= age
    dict3['address']= address
    dict3['phone']= phone
    dict1[name]= dict3
    c="\nCustomer has been added\n"
    return c

def thirdfunc(name):

    if name in dict1:
        del dict1[name]
        c="\nCustomer is deleted\n"
        return c
    else:
        c="\nCustomer does not exist\n"
        return c

def fourthfunc(name,age):
    if name in dict1:
        dict1[name]["age"]= age
        c="\nAge updated confirmed\n"
        return c
    else:
        c="\nCustomer not found\n"
        return c

def fifthfunc(name,address):
    if name in dict1:
        dict1[name]["address"]=address
        c="\nAddress updated confirmed\n"
        return c
    else:
        c="\nCustomer not found\n"
        return c

def sixthfunc(name,phone):
    if name in dict1:
        dict1[name]["phone"]=phone
        c="\nPhone number updated confirmed\n"
        return c
    else:
        c="\nCustomer not found\n"
        return c

def seventhfunc():
    list =[]
    for key in dict1.keys():
        list.append(key)
    list.sort()
    string=""
    for x in list:
        string+=x+":"+" Age:"+dict1[x]["age"]+"| Address:"+dict1[x]["address"]+"| Phone number:"+dict1[x]["phone"]+"\n"
    return string




sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#address = (socket.gethostname(),9999)
sock.bind(('127.0.0.1',9999))
#sock.listen(5)

while True:
    sending =""
    data,addr=sock.recvfrom(100000)
    x = str(data)[2:-1]
    work_list= list(x.split(','))
    if(work_list[0]=="1"):
        sending=firstfunc(work_list[1])
    elif(work_list[0]=="2"):
        sending=secondfunc(work_list[1],work_list[2],work_list[3],work_list[4])
    elif(work_list[0]=="3"):
        sending=thirdfunc(work_list[1])
    elif(work_list[0]=="4"):
        sending=fourthfunc(work_list[1],work_list[2])
    elif(work_list[0]=="5"):
        sending=fifthfunc(work_list[1],work_list[2])
    elif(work_list[0]=="6"):
        sending=sixthfunc(work_list[1],work_list[2])
    elif(work_list[0]=="7"):
        sending=seventhfunc()

    message=bytes(sending.encode('utf-8'))
    sock.sendto(message,addr)
