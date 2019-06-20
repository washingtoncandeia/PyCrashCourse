##---------------------
# Cap5 - Instruções If
# toppings.py, p.135
##---------------------

available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested in requested_toppings:
        if requested in available_toppings:
            print('Adding ' + requested + '.')
        else:
            print('Sorry, we do not have ' + requested + '.')
    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')