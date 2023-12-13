from Customer import Customer
from Admin import Admin


class car:
    def __init__(self, brand, model, color, price_h, price_km, condition = True):
        self.brand = brand
        self.model = model
        self.color = color
        self.price_per_h = price_h
        self.price_per_km = price_km
        self.condition = condition

    def calculate_sum(self, type, num):
        if type=='1' or type.title() =="Hours":
            return num *self.price_per_h
        elif type=='2' or type.title()=="Kms":
            return num * self.price_per_km

    def is_available(self):
        return self.condition

class Car_rental_system:
    def __init__(self):
        self.cars = []
        self.customers =[]
        self.admins = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        for car_ in self.cars:
            if car_ == car:
                remove(car_)
                print("Successfully, car is removed.")

    def add_customer(self, name, passwd):
        new_customer = Customer(name, passwd)
        self.customers.append(new_customer)
        return new_customer

    def add_admin(self, name, passwd):
        new_admin = Admin(name, passwd)
        self.admins.append(new_admin)
        print("Successfully you have registerd! ")
        return new_admin

    def display_available_cars(self):
        available_cars = [car for car in self.cars if car.is_available()]
        if available_cars:
            print("brand\t\tmodel\t\tcolor\t\tprice per hour\t\tprice per km")
            print("="*85)
            for car in available_cars:
                print(f"{car.brand}\t\t{car.model}\t\t{car.color}\t\t{car.price_per_h} RUB\t\t\t{car.price_per_km} RUB.")
            print("="*85)

    def display_all_cars(self):
        print("Brand\t\tModel\t\tColor\t\tPrice per hour\t\tPrice per km\t\tAvailability")
        print("="*110)
        for car in self.cars:
            print(f"{car.brand}\t\t{car.model}\t\t{car.color}\t\t{car.price_per_h} RUB\t\t\t{car.price_per_km} RUB\t\t\t{car.is_available()}")
        print("="*110)

    def display_customers(self):
        if self.customers:
            print("="*32+ " CUSTOMERS: "+ "="*32)
            for i, customer in enumerate(self.customers, start=1):
                print(f"{i}. {customer.name}")
        else:
            print("There are no customers yet!")


    def rent_a_car(self):
        brand = input("Enter brand: ").title()
        avalaible_brand =[]
        for car in self.cars:
            if car.brand.title() == brand:
                avalaible_brand.append(car)
        if avalaible_brand:
            print("Available:")
            print("brand\t\tmodel\t\tcolor\t\tprice per hour\t\tprice per km")
            print("="*85) 
            for car in avalaible_brand:
               print(f"{car.brand}\t\t{car.model}\t\t{car.color}\t\t{car.price_per_h} RUB\t\t\t{car.price_per_km} RUB.")
            print("="*85) 
            color = input("Enter color: ").title()
            avalaible_color =[]
            for car in avalaible_brand:
                if car.color.title() == color:
                    avalaible_color.append(car)
            if avalaible_color:
                print("Available:")
                print("Brand\t\tModel\t\tColor\t\tPrice per hour\t\tPrice per km")
                print("="*85)  
                for car in avalaible_color:
                    print(f"{car.brand}\t\t{car.model}\t\t{car.color}\t\t{car.price_per_h} RUB\t\t\t{car.price_per_km} RUB.")
                print("="*85) 
                model = input("Choose model: ").title()
                the_car = ""
                for car in avalaible_color:
                    if car.model.title() == model:
                        the_car = car
                if the_car != "":
                    type_cal = input("Calulate by:\n\t1. number of hours.\n\t2. number of kms.\n\t")
                    if type_cal =='1' or type_cal.title() =="Hours":
                        num = int(input("Enter number of hours: "))
                    elif type_cal =='2' or type_cal.title()== "Kms":
                        num = int(input("Enter number of kms: "))
                    x= input(f"It costs: {the_car.calculate_sum(type_cal, num)}\nEnter 1. to continue. or 2. to go back...")
                    if x == '1':
                        the_car.condition = False
                        print("Thank you, have a nice trip!")
                        print("="*85)
                    else: 
                        print("Thank you!")
                else:
                    print("This model is not available!")
            else:
                print("This color is not avalaible!")
        else:
            print("This brand is not available!")

            

    




    



    
