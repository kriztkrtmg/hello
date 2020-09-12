"""
Generate random password of given length for each user

"""
import string
import random

name_length = {
    'harry' : 6, 
    'akash' : 8,
    'santosh' : 6,
    'kriz': 7,
    'ram' : 8,
}

password = {}

#name_length.items() is converting dictionary(so called object in javascript) into list of tuples.
# ([('harry', 6), ('akash', 8), ('santosh', 6), ('kriz', 7), ('ram', 8)])


for username, length in name_length.items(): #assigning every tuples with corresponding variable.. for example :> username=harry , length=6
    password_list = [] #empty list
    for count in range(0,length): #count is not used here..it's just for syntax...
        password_list.append(random.choice(string.ascii_letters)) #generates random ascii letters and appends it in empty list
    password[username] = "".join(password_list) #generated random ascii letter list is joined to make a string 
    #result string value is stored in password dictionary with username i.e key = username, value = string
print("password of different users :",password) #final output from password dictionary