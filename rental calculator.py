# class LinkedListNode():
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#     def traverseList(self):
#         node=self
#         while node != None:
#             print(node.value)
#             node=node.next
# node1 = LinkedListNode('Mon')
# node2 = LinkedListNode('Tues')
# node3 = LinkedListNode('Wed')
# node1.next=node2
# node2.next=node3
# node1.traverseList()

class Calculator():

    def __init__(self):
        total = int(input("Total price of house: "))
        self.total = total

    def inititor(self):
        Calculator.cashflow(self)
        Calculator.roi(self)

    def income(self):
        rent = int(input("Price of rent per month: "))
        laundry = int(input("Estimated monthly laundry income: "))
        storage = int(input("Monthly storage income: "))
        misc = int(input("Miscellaneous monthly income: "))
        income_total =  rent + laundry + storage + misc
        return income_total

    def expense(self):
        print("If no expense, you can leave blank")
        tax = int(input("Monthly tax: "))
        insurance = int(input("Monthly insurance cost: "))
        utilities = int(input("Monthly utility cost: "))
        hoa = int(input("HOA fees: "))
        yard = int(input("Cost of landscaping and snow removal: "))
        vacancy = int(input("Savings for eventual vacancy: "))
        repairs = int(input("Monthly repair cost: "))
        capex = int(input("Capital expense savings: "))
        prop_mgmt = int(input("Cost for paying property manager: "))
        mortgage = int(input("Monthly mortgage: "))
        expense_total = tax + insurance + utilities + hoa + yard + vacancy + repairs + capex + prop_mgmt + mortgage
        print(f"Your total expenses are: {expense_total}")
        return expense_total
    
    def cashflow(self):
        cashflowed = self.income() - self.expense()
        self.cashflowed = cashflowed
        print(f"Your monthly profit: {cashflowed}")
        return cashflowed

    def roi(self):
        downpayment = int(input("Your downpayment: "))
        closing = int(input("Closing costs: "))
        rehab = int(input("Initial rehab cost: "))
        misc_roi = int(input("Misc setup expenses: "))
        total_investment = downpayment + closing + rehab + misc_roi
        annual_cash_flow = self.cashflowed * 12
        cash_return = (annual_cash_flow / total_investment) * 100
        print(f"Total investment: {total_investment} \nAnnual Cash Flow: {annual_cash_flow} \nTotal Cash Return: {cash_return}")

    # def nodemaker(self, other stuff)
    #make nodes for different properties, maybe compare home ROIs
    #Sort based on various criteria

    #blackjack, hangman

def execute():
    my_total = Calculator()
    my_total.inititor()

execute()

