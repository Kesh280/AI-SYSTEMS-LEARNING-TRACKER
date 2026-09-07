#1

class store:

    

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def track(store):
        count = 0
        for i in store:
            count += 1
        print(count)


    @staticmethod
    def discount(price,discount):
        final_discount = ((price - discount)*100)/price
        print(final_discount)


pro1 = store("phone",20000)
pro2 = store("Laptop",40000)
pro3 = store("earphone",5000)


pro1.discount()
