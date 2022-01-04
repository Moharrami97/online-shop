from all_models import *

r1 = Reseller("narges", "moharrami", "123", "narges@gmail.com")

A1 = Address(123, "javid", "iran")

A2 = Address(456, "bahar", "turkey")

c1 = Customer("negin", "moharrami", "456", "negin@gmail.com", "100", Address=A1)

c2 = Customer("maryam", "moradi", "456", "maryam@gmail.com", "100", Address=A2)

p1 = Product("Rugs1", "25", 10000, Reseller=r1)
p2 = Product("Mobile", "26", 5000, Reseller=r1)
p3 = Product("Rugs2", "27", 9000, Reseller=r1)
product_list = [p1, p2, p3]

purchase1 = Purchase(c1, c1.Address)

purchase2 = Purchase(c2, c2.Address)

print(purchase2.total_price())
purchase1.add_product(p2)
purchase2.add_product([p1, p3])
print(purchase2.total_price())

for pr in product_list:
    print(pr)
