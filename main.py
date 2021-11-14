from all_models import *

r1 = Reseller("narges", "moharrami", "123", "narges@gmail.com")

A1 = Address(123, "javid", "iran/tehran/enghelab")

c1 = Customer("negin", "moharrami", "456", "negin@gmail.com", "100", Address=A1)

p1 = Product("pencil", "25", 1000, Reseller=r1)

print(c1)

for pr in Product.product_list:
    print(pr)
