sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]


def order(food_item):
    receipt = {}
    for item in food_item:
        if item['name'] in food_item:
            receipt[item['name']]['qty'] +=1 
        else:
            receipt[item['name']] = {
                'price': item['price'],
                'qty': 1
            }
    for sushi, value in receipt.items():
        price = value['price'] * value ['qty']
        print(sushi, value['qty'], [price])

    

order(sushi_orders)



