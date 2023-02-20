class Bank:
    def __init__(self,name):
        self.name = name
        self.clients = []

    def getName(self):
        return self.name
    
    def setName(self):
        pass

    def getClient(self):
        for client in self.clients:
            print(f'{self.name} Clients\n{client.getName()}\n')
        
    def addClient(self,client):
        self.clients.append(client)
        print('Client added\n')
    