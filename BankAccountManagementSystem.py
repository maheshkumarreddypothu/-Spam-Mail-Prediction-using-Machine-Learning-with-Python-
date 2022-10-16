


class Bank:
    def __init__(self):
        self.client_details_list=[]
        self.loggedin=False
        self.cash=100
        self.Transfercash=False
        
    #Creating a bank account
    def register(self,name,ph,password):
        conditions=True
        cash=self.cash
        if len(str(ph))>10 and len(str(ph))<10:
            print('Invalid phone number!please enter 10 digit number')
            conditions=False
        if len(password)<5 or len(password)>18:
            print('Enter correct password greater than 5 and less than 18 characters')
            conditions=False
        if conditions==True:
            print('Account created successfully')
            self.client_details_list=[name,ph,password,cash]
            with open(f"{name}.txt",'w') as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")
                    
    #Logging into bank account
    def login(self,name,ph,password):
        with open(f"{name}.txt","r") as f:
            details=f.read()
            self.client_details_list=details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin=True
            if self.loggedin==True:
                print(f"{name} logged in")
                self.cash=int(self.client_details_list[3])
                self.name=name
            else:
                print('wrong details')
                
    #Deleting the bank account
    def remove_account(self,name):
        import os
        if os.path.exists(f"{name}.txt"):
            os.remove(f"{name}.txt")
            print('Account removed successfully')
        else:
            print("Please enter your bank details correctly!")
            
    #Depositing cash into our account
    def add_cash(self,amount):
        if amount>0:
            self.cash+=amount
            with open(f"{name}.txt","r") as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))
            print('Amount added successfully')
        else:
            print('Enter correct value of amount')
            
    #Transferring cash from one bank account to other bank account
    def Transfer_cash(self,amount,name,ph):
        with open(f"{name}.txt","r") as f:
            details=f.read()
            self.client_details_list=details.split("\n")
            if str(ph) in self.client_details_list:
                self.Transfercash=True
        if self.Transfercash==True:
            total_cash=int(self.client_details_list[3])+amount
            left_cash=self.cash-amount
            with open(f"{name}.txt",'w') as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))
            with open(f"{self.name}.txt","r") as f:
                details_2=f.read()
                self.client_details_list=details.split("\n")
            with open(f"{self.name}.txt",'w') as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))
            print('Amount transferred succesfully to',name,"-",ph)
            print('Balance= ',left_cash)
            
    #Password change
    def password_change(self,password):
        if len(password)<5 or len(password)>18:
            print('Enter correct password greater than 5 and less than 18 characters')
        else:
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open(f"{name}.txt",'w') as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print('New password setup successfully')
            
    #Phone number change
    def ph_change(self,ph):
        if len(str(ph))>10 and len(str(ph))<10:
            print('Invalid phone number!please enter 10 digit number')
        else:
            with open(f"{self.name}.txt",'r') as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open(f"{self.name}.txt",'w') as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print('New phone number setup successfully')
    
    
if __name__=='__main__':
    Bank_object=Bank()
    print('Welcome to my bank')
    print('1.Login')
    print("2.Create a new_account")
    print("3.Delete account")
    user=int(input('Make decision: '))
    if user==1:
        print('Logging in')
        name=input('Enter name: ')
        ph=int(input('Enter ph: '))
        password=input('Enter password: ')
        Bank_object.login(name,ph,password)
        while True:
            if Bank_object.loggedin:
                print('1.Add amount')
                print('2.Check balance')
                print('3.Transfer amount')
                print('4.Edit profile')
                print('5.Log out')
                login_user=int(input())
                if login_user==1:
                    print('Balance =',Bank_object.cash)
                    amount=int(input('Enter amount: '))
                    Bank_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Log out")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        break
                elif login_user==2:
                    print('Balance=',Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Log out")
                    choose=int(input())
                    if choose==1:
                        continue
                    elif choose==2:
                        break
                elif login_user==3:
                    print('Balance=',Bank_object.cash)
                    amount=int(input('Enter amount: '))
                    if amount>0 and amount<=Bank_object.cash:
                        name=input('Enter person name: ')
                        ph=input('Enter phone number: ')
                        Bank_object.Transfer_cash(amount, name, ph)
                        print("\n1.back menu")
                        print("2.Log out")
                        choose=int(input())
                        if choose==1:
                            continue
                        elif choose==2:
                            break
                    elif amount<0:
                        print('Enter please enter correct value of amount')
                    elif amount>Bank_object.cash:
                        print('Not enough balance')
                elif login_user==4:
                    print("1.Password change")
                    print("2.Phone_number change")
                    edit_profile=int(input())
                    if edit_profile==1:
                        new_password=input('Enter new_password: ')
                        Bank_object.password_change(new_password)
                        print("\n1.back menu")
                        print("2.Log out")
                        choose=int(input())
                        if choose==1:
                            continue
                        elif choose==2:
                            break
                    elif edit_profile==2:
                        new_ph=int(input("Enter new phone_number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Log out")
                        choose=int(input())
                        if choose==1:
                            continue
                        elif choose==2:
                            break
                elif login_user==5:
                    break
    if user==2:
        print('creating a new account')
        name=input('Enter name: ')
        ph=int(input('Enter ph: '))
        password=input('Enter password: ')
        Bank_object.register(name, ph, password)
    if user==3:
        print("Deleting account")
        name=input("Please enter your account name: ")
        Bank_object.remove_account(name)
        
