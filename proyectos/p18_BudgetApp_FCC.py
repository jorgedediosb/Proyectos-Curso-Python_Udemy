# Proyecto 'Budget App' perteneciente al curso 'Scientific Computing with Python' de FCC

class Category:
    '''
    La clase 'Category' crea instancias de objetos basados en diferentes categorías de presupuesto,
    como comida, ropa y entretenimiento.
    Cuando se imprime el presupuesto, muestra:
    - Una línea de título donde el nombre de la categoría está centrado en una línea de caracteres *.
    - Una lista de los elementos del presupuesto. Cada línea muestra la descripción y el monto.
    - Una línea que muestra el total de la categoría.
    '''
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            items += f"{description} {amount:>{30 - len(description) - 1}}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_percentages = [(c.get_balance() / sum(cat.get_balance() for cat in categories)) * 100 for c in categories]
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in spent_percentages:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    max_len = max(len(c.category) for c in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    return chart.rstrip()

# EJEMPLO DE USO:
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more")
clothing.deposit(350, "initial deposit")
food.transfer(50, clothing)
entertainment.deposit(200, "initial deposit")
entertainment.withdraw(25.39, "gasoline")

print(food)
print(clothing)
print(entertainment)
print('------------------------------')
print(create_spend_chart([food, clothing, entertainment]))
