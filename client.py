from person import Person

class Client(Person):
    def __init__(self,name,balance):
        super().__init__(name)
        self.balance = balance

    def getName(self):
        return self.name, self.balance
        
    def cashDeposit(self,value):
        self.balance += value
        
        print(f'{self.name}\ncash deposited: ${value}\n')

    def withdraw(self,value):
        if(self.balance < value):

            print("not enough balance\n")
        else:
            self.balance -= value

            print(f'withdrawn ${value}\n')

    def transfer(self,value,client):
        if(self.balance < value):

            print("not enough balance\n")
        else:
            self.balance -= value

            print(f'{self.name} transferred ${value} to {client.name}\n')
            client.cashDeposit(value)