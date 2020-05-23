import socket

def connection(fdata):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    msg=fdata
    #client_socket.sendto(msg.encode("utf-8"),(socket.gethostname(),9999
    client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',9999))
    data,addr=client_socket.recvfrom(100000)
    #x = str(data)[2:-1]
    y=data.decode("utf-8")
    print(y)
    client_socket.close

def namefunc():
    first_name=input("Input the Name:")
    if (first_name==""):
        print("Name is compulsory\n")
        return namefunc()
    else:
        return first_name.title()

def agefunc():
    age_here = input("Give age:")
    see_if_numeric = age_here.isnumeric()
    if (age_here==''):
        return age_here
    elif not see_if_numeric:
        print("Age is not number\n")
        return agefunc()
    else:
        return age_here



def choice(number):
    if (number == "1"):  #first choice made
        data=""
        first_name= namefunc()
        data = str(number)+","+first_name
        connection(data)
        options()
    elif (number == "2"):  #second choice made
        data=""

        first_name=namefunc()
        age=agefunc()
        address = input("Give address:")
        phone = input("Give phone:")
        data = str(number)+","+str(first_name)+","+str(age)+","+address+","+phone
        connection(data)
        options()
    elif (number == "3"):  #third choice made
        data=""
        first_name=namefunc()
        data = str(number)+","+first_name
        connection(data)
        options()
    elif (number == "4"): #fourth choice made
        data=""
        first_name=namefunc()
        age=agefunc()
        data = str(number)+","+str(first_name)+","+str(age)
        connection(data)
        options()
    elif (number == "5"):    #fifth choice made
        data=""
        first_name=namefunc()
        address=input("Give the updated address:")
        data = str(number)+","+first_name+","+address
        connection(data)
        options()
    elif (number == "6"):   #sixth choice made
        data=""
        first_name=namefunc()
        phone=input("Give the updated phone number:")
        data = str(number)+","+first_name+","+phone
        connection(data)
        options()
    elif (number == "7"):   #seventh choice made
        data=""
        data= str(number)
        connection(data)
        options()
    elif (number == "8"):   #eigth choice made
        print("Good bye\n")
    else:
        print("Please Select a valid option\n")
        options()





def options():
    print("\nPython DB Menu\n 1. Find customer\n 2. Add customer\n 3. Delete customer\n 4. Update customer age\n 5. Update customer address\n 6. Update customer phone")
    print(" 7.Print Report")
    print(" 8.Exit")
    number = input("Select:")
    print("\n")
    choice(number)


options()
