n=int(input())
phonebook={}
for x in range(n):
    friend_contact= input().split(" ")
    #phonebook=phonebook + "".join(friend_contact)
    phonebook[friend_contact[0]]=friend_contact[1]

for x in range(n):
    contact_name=input()
    #print(contact_name)
    if contact_name in phonebook.keys():
        print('{}={}'.format (contact_name,phonebook[contact_name]))
    else: print("Not found")