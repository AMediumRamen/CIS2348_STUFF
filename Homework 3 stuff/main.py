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




    def add_item(self):
        print('ADD ITEM TO CART')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name,item_description,item_price,item_quantity))




    def remove_item(self):
        print('REMOVE ITEM FROM CART')
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
            print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
            print('Number of Items:',self.get_num_items_in_cart())
            print()
            for i in self.cart_items:
                print('{} {} @ ${} = ${}'.format(i.item_name,i.item_quantity,i.item_price,(i.item_quantity*i.item_price)))
            print('')
            print('Total: ${}'.format(total))


    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print('')
        print('Item Descriptions')
        for i in self.cart_items:
            print('{}:{}'.format(i.item_name,i.item_description))

    def output_shopping_cart(self):
        total = self.get_cost_of_cart()
        if (total == 0):
            print('SHOPPING CART IS EMPTY\n')
        else:
            print('OUTPUT SHOPPING CART')
            self.print_total()


    def output_descriptions(self):
        total = self.get_cost_of_cart()
        if (total == 0):
            print('SHOPPING CART IS EMPTY\n')
        else:
            print("OUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()

    def print_menu(self):

        userinput = ''
        while (userinput != 'q'):
            print("\nMENU\n"
                    "a - Add item to cart\n"
                    "r - Remove item from cart\n"
                    "c - Change item quantity\n"
                    "i - Output items' descriptions\n"
                    "o - Output shopping cart\n"
                    "q - Quit\n")
            userinput = input('Choose an option:\n')

            while (userinput != 'a' and userinput != 'r' and userinput != 'c' and userinput !='i' and userinput != 'o' and userinput != 'q'):
                userinput = input('Choose an option:\n')


            if userinput == 'a':
                self.add_item()
            if userinput == 'r':
                self.remove_item()
            if userinput == 'c':
                self.modify_item()
            if userinput == 'i':
                self.output_descriptions()
            if userinput == 'o':
                self.output_shopping_cart()



if __name__ == "__main__":
    customer_name = str(input("Enter customer's name:\n"))
    current_date = str(input("Enter today's date:\n"))
    print('')
    print('Customer name: {}'.format(customer_name))
    print("Today's date: {}".format(current_date))

    Cart = ShoppingCart(customer_name,current_date)

    Cart.print_menu()







