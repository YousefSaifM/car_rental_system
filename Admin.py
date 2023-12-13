class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def check_passwd(self, passwd):
        return self.password == passwd

