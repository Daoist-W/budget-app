from math import ceil, floor

class Category:

    # constructor
    def __init__(self, category, budget):
        self.currentBalance = budget
        self.ledger = [{"amount" : budget, "description" : "initial deposit"}]
        self.category = category
    
    # methods
    def withdraw (self, amount, description=""):
        if amount > self.currentBalance:
            return False
        self.currentBalance -= amount
        self.ledger.append({"amount": - amount, "description": description})
        return True
    
    def deposit (self, amount, description=""):
        self.currentBalance += amount
        self.ledger.append({"amount": amount, "description": description})
        return True
    
    def get_balance (self):
        return self.currentBalance

    def transfer (self, amount, category):
        # balance check
        if self.currentBalance <= 0:
            return False
        self.withdraw(amount, f"Transfer to {category.category}")
        category.deposit(amount, f"Transfer from {self.category}")
        return True

    def get_ledger(self):
        return tuple(self.ledger)

    def print_budget(self):
        # formatting title
        title = []
        title_length = len(self.category)
        left_stars = ceil((30 - title_length) / 2)
        right_stars = floor((30 - title_length) / 2)
        for num in range(left_stars):   
            title.append("*")
        title.append(self.category)
        for num in range(right_stars):   
            title.append("*")
        
        # converting into a string from list
        title = "".join(title)
        
        # formatting items
        items_list = []

        # loop that populates items_list with string formatted items 
        for item in range(len(self.ledger)):
            list_row = []
            desc_length = len(self.ledger[item]["description"])
            amount_len = len(str(self.ledger[item]["amount"]))
            for num in range(23):
                if num < desc_length:
                    list_row.append(self.ledger[item]["description"][num])
                else:
                    list_row.append(" ")
            for num in range(24, 31):
                if num <= 30 - amount_len:
                    list_row.append(" ")
            list_row.append(str(self.ledger[item]["amount"]))

            # store inside items_list
            items_list.append("".join(list_row) + "\n")
        
        # converting into a string from list
        items_list = "".join(items_list)

        # calculating total
        totals_row = self.currentBalance

        # append all to file
        file = open(f"outputs/{self.category}.txt", "w")
        lines = [title + "\n", items_list, f"Total: {totals_row}"]
        for item in lines:
            file.write(item)
        file.close

        # returning everything for terminal display
        return (
            title,
            items_list,
            f"Total: {totals_row}"
        )



            

            


            
        

