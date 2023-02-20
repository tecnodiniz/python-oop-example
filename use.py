from client import Client
from bank import Bank

# Creating Clients
client1 = Client('John',200);
client2 = Client('Smith',1000);

# Creating a Bank and Adding Clients
bank1 = Bank('Santander')
bank1.addClient(client1)
bank1.addClient(client2)


client1.cashDeposit(500)

client1.transfer(300,client2)

bank1.getClient()








