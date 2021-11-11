# Ahmed Rahman PSID: 1820239

class ItemToPurchase:
    def __init__(self,item_name='none',item_description='none',item_price=0,item_quantity=0):
        self.item_name=item_name
        self.item_price = item_price
        self.item_quantity =item_quantity
        self.item_description = item_description
    def print_item_cost(self):
        yikes = ('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,int(self.item_price),(int(self.item_price*self.item_quantity))))
        return yikes
    def print_item_description(self):
        yikes2 = '{}: {}'.format(self.item_name,self.item_description)
        print(yikes2)
        return yikes2




class ShoppingCart:
    def __init__(self,customer_name = 'none',current_date = 'January 1, 2016',cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items




    def add_item(self,):
        print('ADD ITEM TO CART\n')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name,item_description,item_price,item_quantity))




    def remove_item(self):
        print('REMOVE ITEM FROM CART\n')
        itemToRemove = str(input('Enter name of item to remove:\n'))
        for i in self.cart_items:
            if itemToRemove in self.cart_items:
                del self.cart_items[i]
            else:
                print('Item not found in cart. Nothing removed.')


    def modify_item(self):
        print('CHANGE ITEM QUANTITY\n')
        itemToModify = str(input('Enter the item name:\n'))
        breaker = True
        for i in self.cart_items:
            if i.item_name == itemToModify:
                NewQuan = int(input('Enter the new quantity:\n'))
                i.item_quantity = NewQuan
                breaker = False
        if breaker == True:
            print('Item not found in cart. Nothing modified.\n')



    def get_num_items_in_cart(self):
        totalItems = 0
        for i in self.cart_items:
            totalItems += i.item_quantity
        return totalItems

    def get_cost_of_cart(self):
        yikers = 0
        for i in self.cart_items:
            yikers += i.item_quantity * i.item_price
        return yikers

    def print_total(self):
        total = self.get_cost_of_cart()
        if (total == 0):
            print('SHOPPING CART IS EMPTY\n')
        else:
            print("{}'s Shopping Cart - {}\n".format(self.customer_name,self.current_date))
            print('Number of Items:',self.get_num_items_in_cart())
            for i in self.cart_items:
                print()





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
