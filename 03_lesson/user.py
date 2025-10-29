class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_name_info(self):
        return f"Name: {self.first_name}, Last_name: {self.last_name}"
