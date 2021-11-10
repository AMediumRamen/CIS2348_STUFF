# Ahmed Rahman PSID: 1820239
class ItemToPurchase:
    def __init__(self,item_name='none',item_price=0,item_quantity=0):
        self.item_name=item_name
        self.item_price = item_price
        self.item_quantity =item_quantity
    def print_item_cost(self):
        yikes = ('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,int(self.item_price),(int(self.item_price*self.item_quantity))))
        return yikes
if __name__ == "__main__":
    print('Item 1')
    Item1 = ItemToPurchase()
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))

    Item1.item_name = name
    Item1.item_price = price
    Item1.item_quantity = quantity
    item1cost = price*quantity
    print('')
    print('Item 2')
    Item2 =ItemToPurchase()
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))

    Item2.item_name = name
    Item2.item_price = price
    Item2.item_quantity = quantity
    item2cost = price*quantity
    print('')
    print('TOTAL COST')
    print(Item1.print_item_cost())
    print(Item2.print_item_cost())
    print('')
    print('Total: ${}'.format(int(item1cost+item2cost)))



