def sum(items):
    print('SUM')
    resul = 0
    for itm in items:
        resul += itm
    return resul


def r_sum(items):
    return items[0] + r_sum(items[1:]) if items else 0

print('HELLO')
print(__name__)