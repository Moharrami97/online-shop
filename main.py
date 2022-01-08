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

purchase_iran = Purchase(c1, c1.Address)
purchase_turkey = Purchase(c2, c2.Address)

purchase_iran.add_product([p1, p3])
purchase_turkey.add_product([p1, p3])

print(show_total_price(purchase_turkey))
print(show_vat_pluse_price(purchase_turkey))

print(show_total_price(purchase_iran))
print(show_vat_pluse_price(purchase_iran))

print(purchase_iran.checkout(c1))
print(purchase_iran.checkout(c2))