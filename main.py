from all_models import *

r1 = Reseller("narges", "moharrami", "123", "narges@gmail.com")

c1 = Customer("negin","moharrami", "456","negin@gmail.com","100")

p1 = Product("pencil", "25", 1000, Reseller=r1)

for pr in Product.product_list:
    print(pr)