class Gateway:
    def __init__(self, name):
        self.name = name


class Payment:
    gateways = (Gateway("G1"), Gateway("G2"))

    def __init__(self, purchase):
        self.purchase = purchase

    def gate_way(self):
        return self.gateways[0] if self.purchase.total_price() < 15000 else self.gateways[1]

    @property
    def pay(self):
        gateway = self.gate_way()
        print(f"payment is being paid through {gateway.name}")
