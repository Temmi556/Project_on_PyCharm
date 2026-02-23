class Chain:
    def __init__(self,number_of_items):
        self.number_of_items = number_of_items
    def __str__(self):
        return "Chain with " + str(self.number_of_items) + " items"
    def __len__(self):
        return self.number_of_items

chain_1 = Chain(5)
print(chain_1)
print(len(chain_1))