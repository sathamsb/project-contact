import re

class Contact:
    
    def __init__(self):
        self.File_Path = "D:\project contact\Contact.txt"
        
    def insert(self):
        
        file = open(self.File_Path,'a')
        self.name = input("Enter Name: ")
        self.number = input("Enter Number: ")
        file.write(self.name+" "+self.number+"\n")
        print("Contact Saved Succesfully!")
        file.close()
        
    def display(self):
        
        file = open(self.File_Path,'r')
        print("\nContact List\n")
        for x in file:
          print(x)
        file.close()
        
    def delete(self):
        
        name = input("Enter name : ")
        l = len(name)
        with open(self.File_Path,"r") as file:
            lines = file.readlines()
        substrc = name[0:l]
        file.close()
        with open(self.File_Path,"w") as file:
            for i in lines:
                substr = i[0:l]
                if substr != substrc:
                    file.write(i)
            print("\nContact deleted!\n")
        file.close()
        
    def import_list(self):
        
        with open(self.File_Path,"r") as file:
            lines = file.readlines()
        print("\nContact imported Succesfully!\n")
        file.close()
        
    def export_list(self):
        
        with open(self.File_Path,"r") as file:
            lines = file.readlines()
        with open(self.File_Path,"a") as file:
            for i in lines:
                file.write(i)
        print("\nContact Exported Succesfully!\n")
        file.close()
        
    def find(self):
        
        with open(self.File_Path,"r") as file:
            lines = file.readlines()
        name = input("Enter name to search:").lower()
        for i in lines:
            find = re.match(name,i.lower())
            if find:
                print(i)
        file.close()
            
        
    
C_obj = Contact()
C_obj.choice = 0

def menu():
    print("-------------------Contact------------------------")
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Contact List")
    print("4.Import Contacts")
    print("5.Export Contacts")
    print("6.Serach contacts")
    print("7.Exit")
    C_obj.choice = int(input("Enter your choice: "))
menu()

while C_obj.choice !=7:
    if C_obj.choice == 1:
        C_obj.insert()
    if C_obj.choice == 2:
        C_obj.delete()
    if C_obj.choice == 3:
        C_obj.display()
    if C_obj.choice == 4:
        C_obj.import_list()
    if C_obj.choice == 5:
        C_obj.export_list()
    if C_obj.choice == 6:
        C_obj.find()
    menu()
    
