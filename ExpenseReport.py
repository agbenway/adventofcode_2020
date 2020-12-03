import requests

entries = response.content.decode('utf-8').splitlines()

for i in entries:
    for j in entries:
        if i != j and int(i) + int(j) == 2020:
            product = int(i) * int(j)
            print('expense for ' + i + ' & ' + j + ' = ' + str(product))
            break

for i in entries:
    for j in entries:
        if i != j:
            for h in entries:
                if h != j and int(i) + int(j) + int(h) == 2020:
                    product = int(i) * int(j) * int(h)
                    print('expense for ' + i + ' & ' + j + ' & ' + h + ' = ' + str(product))
                    break
