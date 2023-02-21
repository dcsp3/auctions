import random
import string

class Id():
    def __init__(self):
        self.id = ""

    def generate(self):
        for i in range(5):
            self.id+=random.choice(string.ascii_lowercase)
        return self.id

