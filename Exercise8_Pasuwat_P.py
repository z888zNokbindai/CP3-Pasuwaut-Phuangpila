userid = input("ID : ")
userpass = input("Pass : ")
if userid == "custo" and userpass == "12123":
    print("Login Complete !!")
    print("------------------")
    print("Welcome to Nokbindai Shop")
    print("------------------")
    print("Please Choose Product")
    print("รหัสสินค้า   ชื่อสินค้า   ราคา")
    print("1       รถถัง    500THB")
    print("2      เรือดำน้ำ    800THB")
    print("3       ปืกกล    200THB")
    print("4      ระเบิดมือ   1000THB")
    print("5      นกบินได้   9999THB")
    print("-------------------")
    selectp = int(input("รหัสสินค้า   : "))
    selectv = int(input("จำนวนสินค้า  :"))
    if selectp == 1:
        prodname = "รถถัง"
        price = 500
        print("---------------")
        print("สินค้า" ,prodname ,"ราคา" ,price,"THB" ,"จำนวณที่ซื้อ ",selectv)
        print("รวมราคา" ,price*selectv )
        print("---------------")
        print("ขอบคุณที่ใช้บริการ Nokbindai Shop")
    if selectp == 2:
        prodname = "เรือดำน้ำ"
        price = 800
        print("---------------")
        print("สินค้า" ,prodname ,"ราคา" ,price,"THB" ,"จำนวณที่ซื้อ ",selectv)
        print("รวมราคา" ,price*selectv )
        print("---------------")
        print("ขอบคุณที่ใช้บริการ Nokbindai Shop")
    if selectp == 3:
        prodname = "ปืนกล"
        price = 200
        print("---------------")
        print("สินค้า" ,prodname ,"ราคา" ,price,"THB" ,"จำนวณที่ซื้อ ",selectv)
        print("รวมราคา" ,price*selectv )
        print("---------------")
        print("ขอบคุณที่ใช้บริการ Nokbindai Shop")
    if selectp == 4:
        prodname = "ระเบิดมือ"
        price = 1000
        print("---------------")
        print("สินค้า" ,prodname ,"ราคา" ,price,"THB" ,"จำนวณที่ซื้อ ",selectv)
        print("รวมราคา" ,price*selectv )
        print("---------------")
        print("ขอบคุณที่ใช้บริการ Nokbindai Shop")
    if selectp == 5:
        prodname = "นกบินได้"
        price = 9999
        print("---------------")
        print("สินค้า" ,prodname ,"ราคา" ,price,"THB" ,"จำนวณที่ซื้อ ",selectv)
        print("รวมราคา" ,price*selectv )
        print("---------------")
        print("ขอบคุณที่ใช้บริการ Nokbindai Shop")

else:
    print("ID or Password is Wrong !!!")
