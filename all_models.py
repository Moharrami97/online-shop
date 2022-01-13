from notification import EmailNotification, SmsNotification
from decorator import notify_observed
from payment import Payment

COUNTRY_LIST = ["iran", "turkey"]
VAT = {"iran": 9, "turkey": 15}


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


class Address:
    def __init__(self, geo_location, name, country):
        self.geo_location = geo_location
        self.name = name
        self.country = country


class Customer(User):

    def __init__(self, name, fullname, password, email, wallet_amount, Address):
        self.wallet_amount = wallet_amount
        self.Address = Address
        super().__init__(name, fullname, password, email)

    def __str__(self):
        return f"name: {self.name} \t geo_location: {self.Address.geo_location}"


class Reseller(User):

    def __init(self, name, fullname, password, email, brand, logo):
        self.brand = brand
        self.logo = logo
        super().__init__(name, fullname, password, email)


class Product:
    def __init__(self, name, upc, price=0, description="", Reseller=None):
        self.name = name
        self.upc = upc
        self.price = price
        self.description = description
        self.Reseller = Reseller

    def __str__(self):
        return f"upc: {self.upc} \t name: {self.name} \t Reseller: {self.Reseller.name}"

    def is_free(self):
        return self.price == 0


def checkout_permission(func):
    def wrapper(obj, user):
        if obj.user == user:
            return func(obj)
        return f"you are not allow checkout"

    return wrapper


class Purchase:
    observers = [EmailNotification, SmsNotification]

    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.product_list = []
        self.product = self.product_list
        self.payment = Payment(self)

    def add_product(self, products_list):
        if not isinstance(products_list, list):
            products_list = [products_list]
        self.product_list.extend(products_list)

    def total_price(self):
        s = 0
        for product in self.product_list:
            s += product.price
        return s

    @checkout_permission
    @notify_observed(message="purchase paid")
    def checkout(self):
        return "checkout done"

    def checkout_type_pay(self):
        self.payment.pay


def calculate_vat(func):
    def wrapper(pur):
        vat = VAT[pur.address.country]
        total_price = pur.total_price()
        return total_price + total_price * vat / 100

    return wrapper


def show_total_price(p):
    return p.total_price()


@calculate_vat
def show_vat_pluse_price(p):
    return p.total_price()
