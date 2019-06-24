import re

class Contact:
    
    def insert(self):
        p = "D:\project contact\Contact.txt"
        f = open(p,'a')
        self.name = input("Enter Name: ")
        self.number = input("Enter Number: ")
        f.write(self.name+" "+self.number+"\n")
        print("Contact Saved Succesfully!")
        f.close()
        
    def display(self):
        p = "D:\project contact\Contact.txt"
        g = open(p,'r')
        print("\nContact List\n")
        for x in g:
          print(x)
        g.close()
        
    def delete(self):
        p = "D:\project contact\Contact.txt"
        c = input("Enter name or number: ")
        l = len(c)
        with open(p,"r") as f:
            lines = f.readlines()
        substrc = c[0:l]
        f.close()
        with open(p,"w") as f:
            for i in lines:
                substr = i[0:l]
                if substr != substrc:
                    f.write(i)
                    print("\nContact deleted!\n")
        f.close()
        
    def import_list(self):
        p = "D:\project contact\Contact.txt"
        with open(p,"r") as f:
            lines = f.readlines()
        print("\nContact imported Succesfully!\n")
        f.close
        
    def export_list(self):
        p = "D:\project contact\Contact.txt"
        with open(p,"r") as f:
            lines = f.readlines()
        with open(p,"a") as f:
            for i in lines:
                f.write(i)
        print("\nContact Exported Succesfully!\n")
        f.close
        
    def find(self):
        p = "D:\project contact\Contact.txt"
        with open(p,"r") as f:
            lines = f.readlines()
        k = input("Enter name to search:").lower()
        for i in lines:
            z = re.match(k,i.lower())
            if z:
                print(i)
            
        
    
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
    
