listm = []
plist = []
def showBill():
    total = 0
    print("Nokbin Shop")
    for i in range(len(listm)):
        print(listm[i],plist[i])
        total += plist[i]
    print("total : ",total)
while True:
    mName = input("Please Input Name : ")
    if (mName.lower() == "exit"):
        break
    else:
        mPrice = int(input("Please Input Price : "))
        listm.append(mName)
        plist.append(mPrice)
showBill()





