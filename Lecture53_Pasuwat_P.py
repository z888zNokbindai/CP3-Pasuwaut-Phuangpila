def calvat(price):
    result = price + price * 7 / 100
    return result
tpriceInput = int(input("price : "))
print(calvat(tpriceInput))
