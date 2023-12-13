class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.condition = True


    def check_passwd(self, passwd):
        return self.password == passwd

    def block_customer(self):
        self.condition = False



    


    