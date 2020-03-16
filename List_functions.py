from hmac import new

stocks = ['Sterlite', 'Avenew Supermarkets', 'ONGC', 'Himadri', 'PnG', ]
print(stocks[-3])
new_stocks = sorted(stocks)
print(f'New Stocks List sorted : {new_stocks}')
print(f'Original Stocks Unchanged : {stocks}')
stocks.sort()
print(f'Stocks in-place sorting : {stocks}')

for stock in stocks:
    if "ONGC" in stocks:
        print("ONGC" in new_stocks)

for index, stock in enumerate(new_stocks, start=1):
    print(f'Index = {index} & Value = {stock}')

list_as_string = ', '.join(new_stocks)
print(list_as_string)

make_list_from_string = list_as_string.split(', ')
print(make_list_from_string)

# List ids

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a
print(f' a == b : {a == b}')
print(f' a is b : {a is b}')
print(f' a is c : {a is c}')
print(f' id of a : {id(a)}')
print(f' id of c : {id(c)}')
print(f' id of b : {id(b)}')
