menu = [
    {
        'type': 'Appetizers',
        'food':[
            'Wings',
            'Cookies',
            'Spring Rolls'
        ]
    },

    {
        'type': 'Entrees',
        'food': [
            'Salmon',
            'Steak',
            'Meat Tornado',
            'A Literal Garden'
        ]
    }
    ,
    {
        'type':'Desserts',
        'food':[
            'Ice Cream',
            'Cake',
            'Pie'
        ]
    }
    ,
    {
        'type': 'Drinks',
        'food': [
            'Coffee',
            'Tea',
            'Unicorn Tears'
        ]
    }
]

order_list = []
def Ordering(order):
    order_list.append(order)
    order_count = order_list.count(order)
    for i in range(len(menu)):
        if order in menu[i]['food']:
            print(f"**{order_count} order of {order} have been added to your meal **")

if __name__ == "__main__":
    welcome_message = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    '''

    print(welcome_message)
    for i in range(len(menu)):
        print(menu[i]['type'])
        print('----------')
        for x in menu[i]['food']:
            print(x)
        print('')

print('''
***********************************
** What would you like to order? **
***********************************''')

order = input()

while(order != 'quit'):
    Ordering(order)
    order = input()

