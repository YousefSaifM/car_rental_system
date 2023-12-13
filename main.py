import sys,subprocess
from System import car, Car_rental_system
from Data import some_cars
from Customer import Customer

system = Car_rental_system()
for x in some_cars:
    new_car = car(x[0],x[1], x[2],x[3],x[4])
    system.add_car(new_car)

def clear_screen():
    os = sys.platform
    if os == 'win32':
        subprocess.run('cls', shell=True)
    elif os == 'linux' or os == 'darwin':
        subprocess.run('clear', shell=True)

def customer_page():
        clear_screen()
        customer_loop=True
        while customer_loop:
            print("="*30 + " CUSTOMER PAGE: "+ "="*30)
            process = input("1. Display available cars.\t2. Rent a car.\t\t3. Back...\n")
            if process == '1':
                system.display_available_cars()
            elif process == '2':
                system.rent_a_car()
            else:
                customer_loop = False

def customer_register_page(system):
        
        customer_register_loop = True
        while customer_register_loop:
            clear_screen()
            print("="*30 + " CUSTOMER REGISTER PAGE: "+ "="*30)
            login = input("1. login.\t\t2. register.\t\t3. Back...\n")
            if login == '1':
                clear_screen()
                name = input("Enter your name: ")
                name_found = False
                for customer in system.customers:
                    if customer.name == name:
                        user = customer
                        name_found = True
                if name_found:
                    if user.condition:
                        passwd = input("Enter password: ")
                        if user.check_passwd(passwd):
                            customer_page()
                        else:
                            print("Password is uncorrect!")
                    else:
                        input("This account is blocked!\n\nPress to go back........")
                else:
                    print("This name is not found! ")
                    input("Press to go back....")
                

            elif login == '2':
                clear_screen()
                name = input("Enter your name: ")
                pwd =False
                while pwd ==False:
                    passwd = input("Enter password: ")
                    confirm_passwd = input("Confirm password: ")
                    if passwd == confirm_passwd:
                        pwd = True
                    else:
                        print("Password mismatch! ",end="")
                user = system.add_customer(name, passwd)
                print("Successfully you have registerd! ")
                customer_page()

            else:
                customer_register_loop =False


def admin_page(system):
    clear_screen()
    admin_loop=True
    while admin_loop:
        print("="*32 + " ADMIN PAGE: "+ "="*32)
        process = input("1. Display all cars.\t2. Display avalaible cars.\t3. Display customers.\n4.Add car.\t\t5. Add customer.\t\t6. Block customer.\n7. Back.......\n")
        if process == '1':
            clear_screen()
            system.display_all_cars()
        elif process == '2':
            clear_screen()
            system.display_available_cars()
        elif process =='3':
            clear_screen()
            system.display_customers()
        elif process == '4':
            clear_screen()
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            color = input("Enter color: ")
            price_per_h = int(input("Enter price per hour: "))
            price_per_km = int(input("Enter price per km: "))
            new_car = car(brand, model, color, price_per_h, price_per_km)
            system.add_car(new_car)
            print("Car has been added!")
        elif process =='5':
            clear_screen()
            name = input("Enter customer name: ")
            pwd =False
            while pwd ==False:
                passwd = input("Enter password: ")
                confirm_passwd = input("Confirm password: ")
                if passwd == confirm_passwd:
                    pwd = True
                else:
                    print("Password mismatch! ",end="")
            user = system.add_customer(name, passwd)
            print("customer has been added!")
        elif process =='6':
            name = input("Enter name: ")
            found = False
            for customer in system.customers:
                if customer.name == name:
                    customer.block_customer()
                    found = True
            if found:
                print(f"{name} is blocked!")
            else:
                print(f"{name} is not found!")
            
        else:
            admin_loop = False

def admin_register_page(system):
    admin_register_loop = True
    while admin_register_loop:
        clear_screen()
        print("="* 30 + " ADMIN REGISTER PAGE: "+ "="*30)
        login = input("1. Login.\t\t2. Register.\t\t 3. Back....\n")
        if login == '1':
                clear_screen()
                name = input("Enter your name: ")
                name_found =False
                for admin in system.admins:
                    if admin.name == name:
                        user = admin
                        name_found = True
                if name_found:
                    passwd = input("Enter password: ")
                    if user.check_passwd(passwd):
                        admin_page(system)
                    else:
                        print("Password is uncorrect!")
                else:
                    print("This name is not found! ")
                    input("Press to go back....")

        elif login == '2':
            clear_screen()
            name = input("Enter your name: ")
            pwd =False
            while pwd ==False:
                passwd = input("Enter password: ")
                confirm_passwd = input("Confirm password: ")
                if passwd == confirm_passwd:
                    pwd = True
                else:
                    print("Password mismatch! ",end="")
            user = system.add_admin(name, passwd)
            clear_screen()
            admin_page(system)

        else:
            admin_register_loop =False


def home():
    is_runing = True
    while is_runing:
        clear_screen()
        print("="*30 + " HOME PAGE: "+ "="*30)
        open = input("1. Customer.\t\t2. Admin. \t\t3. Exit...\n")
        if open == '1':
            customer_register_page(system)
            clear_screen()
        elif open == '2' :
            admin_register_page(system)
            clear_screen()
        else:
            clear_screen()
            is_runing = False

home()

    


