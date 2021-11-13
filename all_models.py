class User:

    def __init__(self, name, fullname, password, email):
        self.name = name
        self.fullname = fullname
        self.password = password
        self.email = email

    @staticmethod
    def _validate_password(password):
        if len(password) < 4:
            print("password should be more than 4 chars")
            return None
        return True

    @classmethod
    def create(cls, name, fullname, password, email):
        cls._validate_password(password)
        return cls(name, fullname, password, email)

    def check_password(self, password):
        return self.password == password


class Customer(User):

    def __init__(self, name, fullname, password, email, wallet_amount):
        self.wallet_amount = wallet_amount
        super().__init__(name, fullname, password, email)


class Reseller(User):

    def __init(self, name, fullname, password, email, brand, logo):
        self.brand = brand
        self.logo = logo
        super().__init__(name, fullname, password, email)


class Product:
    product_list = list()

    def __init__(self, name, upc, price=0, description="", Reseller=None):
        self.name = name
        self.upc = upc
        self.price = price
        self.description = description
        self.Reseller = Reseller
        Product.product_list.append(self)

    def __str__(self):
        return f"upc: {self.upc} \t name: {self.name} \t Reseller: {self.Reseller.name}"

    def is_free(self):
        return self.price == 0

class Reseller(User):
    def __init__(self, name, fullname, password, email):
        super().__init__(name, fullname, password, email)

