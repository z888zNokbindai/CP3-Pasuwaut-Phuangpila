def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Error")
        return False
def showMenu():
    print("------Nokbindai Shop------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userselect = int(input("select menu : "))
    if userselect == 1:
        inputttp = int(input("ttp : "))
        print(vatcalc(inputttp))
    elif userselect == 2:
        print(pricecalc())
def vatcalc(tprice):
    vat = 7
    result = tprice + (tprice * vat / 100)
    return result
def pricecalc():
    price1 = int(input("price 1 : "))
    price2 = int(input("price 2 : "))
    result = vatcalc(price1 + price2)
    return result

login()
