class Address:
    def __init__(self, index, city, street, house, flat):
        self.ind = index
        self.city = city
        self.str = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return f"{self.ind}, {self.city}, {self.str}, {self.house}-{self.flat}"
