class CheckPin:
    def verify(self,pin):
        if pin == 1111 or pin == 2222 or pin == 3333:
            return True
        else:
            return False

class Balance:
    def __init__(self):
        self.bal=5000
    def get_balance(self):
        return self.bal

class Transaction:
    b=Balance()
    def process(self,amt):
        pass

class Withdraw(Transaction):
    def process(self,amt):
        if amt <= self.b.bal:
            print("Amount Withdraw is: ", amt)
            self.b.bal-=amt
            print("Balance is :",self.b.get_balance())
            print("Transaction Successfully Completed.....")
        else:
            print("Insufficient Balance...")

class Deposite(Transaction):
    def process(self,amt):
        print("Amount Deposite is: ",amt)
        self.b.bal+=amt
        print("Balance is :", self.b.get_balance())


class Atm:
    count=0
    while True:
        pin=int(input("Enter Pin Number: "))
        if pin >= 1000 and pin <= 9999:
            chkpin=CheckPin()
            K=chkpin.verify(pin)
            if K:
                print("Please Select Your Transaction")
                print("Press '1' For Withdraw Or Press '2' For Deposite")
                choice=int(input())
                if choice == 1:
                    amt =int(input("Enter Amount for Withdrawn: "))
                    if amt > 0 and amt % 100 == 0:
                        wd=Withdraw()
                        wd.process(amt)
                        break
                    else:
                        print("Invalid Amount..")
                        break
                elif choice == 2:
                    amt = int(input("Enter Amount for Deposite: "))
                    if amt > 0 and amt % 100 == 0:
                        de=Deposite()
                        de.process(amt)
                        break
                    else:
                        print("Invalid Amount..")
                        break
                else:
                    print("Invalid Choice..")
            else:
                print("Invalid Pin")
                count += 1
                if count == 3:
                    print("You Choosed Invalid Pin and You have Limited Attempts Try Later")
                    break
        else:
            print("Incorrect Pin")
            count += 1
            if count == 3:
                print("Please Try After Some Time You have Limited Attempts")
                break
