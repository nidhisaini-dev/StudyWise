from security import hash_password, verify_password


class Student:
    def __init__(self, name, roll_number, password):
        self.name = name
        self.roll_number = roll_number
        self.password_hash = hash_password(password)

    def check_password(self, password):
        return verify_password(password, self.password_hash)