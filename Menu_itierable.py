class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, bev):
        self.menuBeverage = {}
        self.bev=bev
    def add_Menu(self):
        for i, j in enumerate(self.bev):
            self.menuBeverage.update({f"Beverage{i+1}" : j})
        # print(self.menuBeverage)
    def bill_Beverage(self, elemento: str, cantidad: int):
        for menu in self.menuBeverage.values():
            if menu["name"] == elemento:
                return menu["price"]* cantidad
 
class Appetizer(MenuItem):
    def __init__(self, app):
        self.menuAppetizer = {}
        self.app=app
    def add_Menu(self):
        for i, j in enumerate(self.app):
            self.menuAppetizer.update({f"Appetizer{i+1}" : j})
        # print(self.menuAppetizer)
    def bill_Appetizer(self, elemento: str, cantidad: int):
        for menu in self.menuAppetizer.values():
            if menu["name"] == elemento:
                return menu["price"] * cantidad
class MainCourse(MenuItem):
    def __init__(self, mai):
        self.menuMainCourse = {}
        self.mai=mai
    def add_Menu(self):
        for i, j in enumerate(self.mai):
            self.menuMainCourse.update({f"MainCourse{i+1}" : j})
        # print(self.menuMainCourse)
    def bill_MainCourse(self, elemento: str, cantidad: int):
        for menu in self.menuMainCourse.values():
             if menu["name"] == elemento:
                valor= menu["price"] * cantidad
        return valor
class Orderiter:
    def __init__(self, orden, beverage, appetizer, maincourse):
        self.orden = orden
        self.beverage = beverage
        self.appetizer = appetizer
        self.maincourse = maincourse
    def calculate_bill(self):
        amount_bill = 0
        for item in self.orden:  
            bill_Appetizer=0
            bill_Beverage=0
            bill_mc=0
            if item["item"] == "Beverage":
                bill_Beverage = self.beverage.bill_Beverage(elemento= item["name"], cantidad= item["quantity"])
                amount_bill += bill_Beverage
            elif item["item"] == "Appetizer":
                bill_Appetizer = self.appetizer.bill_Appetizer(elemento= item["name"], cantidad= item["quantity"])
                amount_bill += bill_Appetizer
            elif item["item"] == "MainCourse":
                bill_mc = self.maincourse.bill_MainCourse( elemento= item["name"], cantidad= item["quantity"])
                amount_bill += bill_mc
        return f"el valor total a pagar es {amount_bill}"
    
beverage = Beverage(({
    "name" : "Sprite",
    "price" : 2.5
    },
			{
    "name" : "Coca-Cola",
    "price" : 3.0
    },
            {
    "name" : "Quatro",
    "price" : 2.5          
    }))
beverage.add_Menu()
appetizer = Appetizer(({
    "name" : "Alitas BBQ",
    "price" : 8.0
    },
			{
    "name" : "Alitas Miel",
    "price" : 7.5
    },
            {
    "name" : "Alitas Miel Mostaza",
    "price" : 8.2          
    },
            {
    "name" : "Alitas Ranch",
    "price" : 8.5          
    }))
appetizer.add_Menu()
maincourse = MainCourse(({
    "name" : "Pasta Carbonara",
    "price" : 8.0
    },
			{
    "name" : "Pasta Pesto",
    "price" : 7.5
    },
            {
    "name" : "Pasta Bechamel",
    "price" : 8.2          
    },
            {
    "name" : "Pasta Napolitana",
    "price" : 8.5          
    }))
maincourse.add_Menu()
order = Orderiter(({

    "item" : "MainCourse",
    "name" : "Pasta Pesto",
    "quantity" : 1
    },
			{
    "item" : "MainCourse",            
    "name" : "Pasta Carbonara",
    "quantity" : 1
    },
            {
    "item" : "Appetizer",
    "name" : "Alitas BBQ",
    "quantity" : 2          
    },
            {
    "item" : "Beverage",
    "name" : "Coca-Cola",
    "quantity" : 2          
    }), beverage, appetizer, maincourse)


print(order.calculate_bill())



