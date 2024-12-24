"""Javohir Sadullayev 24-214 - group"""

contactList = [{'name': 'Javohir', 'phone': '+998949421706', 'email': 'javohirsadullayev836@gmail.com', 'address': 'Jizzax'},{'name': 'Javlon', 'phone': '+998949421706', 'email': 'javohirsadullayev836@gmail.com', 'address': 'Jizzax'}, {'name': 'Temur', 'phone': '+998949321243', 'email': 'Zarafshon', 'address': 'Samarqand'}]
# contactList = []
contactDict = {}
numbers = "1234567890"
letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ'abcdefghijklmnopqrstuvxyz"
# name show
def nameShow():
    for contact in contactList:
        print()
        print(contact["name"])
        print()
      
# number show
def numberShow():
      for contact in contactList:
        print()
        print(contact["phone"])
        print()
# new contact add
def newContact():
    
    name = input("Ism kiriting: ")
    while True:
        check = False
        for i in contactList:
            for nameletter in name:
                if nameletter not in letters:
                    check = True
        if check:
            print("Belgilar kiritmang: ")
            name = input("Ism kiriting: ")
            continue
        for i in contactList:
            if i["name"] == name:
                check = True
        if check:
            print("Bu ism bor")
            name = input("Ism kiriting: ")
            continue
        elif name.strip() == "":
            print("Bo'sh qiymat kiritmang: ")
            name = input("Ism kiriting: ")
            continue
        elif not name.isalpha():
            print("Faqat harf kiriting: ")
            name = input("Ism kiriting: ")
        else:
            break
           
    phone = input("Raqam kiriting: ")
     
    while True:
        check = False
        for i in contactList:
            for num in numbers:
                if not phone.isdigit() == False:
                    check = True
        if check:
            print("Faqat raqam kiriting: ")
            phone = input("Raqam kiriting: ")
            continue
        elif  not phone.startswith("+998"):
            print("+998 kiritilishi kerak")
            phone = input("+998 va raqam kiriting: ")
            continue
        
        check = False
        for i in contactList:
                if i["phone"] == phone:
                    check = True
        if check:
            print("Bu raqam bor")
            phone = input("Raqam kiriting: ")
            continue
        elif len(phone) < 13:
            print("Uzunligi 13 ta bo'lishi kerak")
            phone = input("Raqam kiriting: ")
        # if " " in phone and "" in phone:
        elif phone.strip() == "":
            print("Bo'sh qiymat kiritmang: ")
            phone = input("Raqam kiriting: ")
            continue
        elif not phone[1:].isdigit():
            print("Raqam kiriting: ")
            phone = input("Raqam kiriting: ")
            continue
        else:
            break
    
    email = input("Email kiriting: ")
    
    while True:
        if  not email.endswith("@gmail.com") and not email.endswith("@gmail.ru"):
            print("@ va gmail va . kiritilishi kerak")
            email = input("Email kiriting: ")
            continue
        elif email.strip() == "":
            print("Bo'sh qiymat kiritmang: ")
            email = input("Email kiriting: ")
            continue
        elif len(email) < 12:
            print("Uzunligi kamida 12 bo'lishi kerak")
            email= input("Email kiriting: ")
        else:
            break
    
    address = input("Manzil kiriting: ")
    while True:
        if address.strip() == "":
            print("Bo'sh qiymat kiritmang: ")
            address = input("Manzil kiriting: ")
            continue
        else:
            break
        
    contactDict = {"name": name, "phone": phone, "email": email, "address": address}
    contactList.append(contactDict)
    
    print()
    print(30 * "*")
    print("💾Yangi kontakt qo'shildi.💾")
    print(30 * "*")
    print()

# contact change
def changeContact():
    if contactList == []:
        print()
        print(30 * "*")
        print("🕳List bo'sh🕳")
        print(30 * "*")
        print()  
        return     
    choose = input("1.Ism bo'yicha o'zgartirish\n2.Raqam bo'yicha o'zgartirish\n")
    
    if choose == "1":    
        nameShow()
        changeName = input("Ism kiriting: ")
        
        for contact in contactList:
            if contact["name"] == changeName:           
                NewName = input("Yangi ism kiriting: ")
                
                while True:
                    check = False
                    for i in contactList:
                        for nameletter in NewName:
                            if nameletter not in letters:
                                check = True
                    if check:
                        print("Belgilar kiritmang: ")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    for i in contactList:
                        if i["name"] == NewName:
                            check = True
                    if check:
                        print("Bu ism bor")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    elif NewName.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    elif not NewName.isalpha():
                        print("Faqat harf kiriting: ")
                        NewName = input("Ism kiriting: ")
                    else:
                        break
                    
                NewwPhone = input("Yangi tel raqam kiriting: ")
                
                while True:
                    check = False
                    for i in contactList:
                        for num in numbers:
                            if NewwPhone.isdigit() == True:
                                check = True
                    if check:
                        print("Faqat raqam kiriting: ")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif  not NewwPhone.startswith("+998"):
                        print("+998 kiritilishi kerak")
                        NewwPhone = input("+998 va raqam kiriting: ")
                        continue
                    
                    check = False
                    for i in contactList:
                            if i["phone"] == NewwPhone:
                                check = True
                    if check:
                        print("Bu raqam bor")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif len(NewwPhone) < 13:
                        print("Uzunligi 13 ta bo'lishi kerak")
                        NewwPhone = input("Raqam kiriting: ")
                    elif NewwPhone.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif not phone[1:].isdigit():
                        print("Raqam kiriting: ")
                        phone = input("Raqam kiriting: ")
                        continue
                    else:
                        break
                    
                    
                NewEmail = input("Yangi email kiriting: ")
                
                while True:
                    if  not NewEmail.endswith("@gmail.com") and not NewEmail.endswith("@gmail.ru"):
                        print("@ va gmail va . kiritilishi kerak")
                        NewEmail = input("Email kiriting: ")
                        continue
                    elif NewEmail.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewEmail = input("Email kiriting: ")
                        continue
                    elif len(NewEmail) < 12:
                        print("Uzunligi kamida 12 bo'lishi kerak")
                        NewEmail= input("Email kiriting: ")
                    else:
                        break
                
                NewAddress = input("Yangi manzil kiriting: ")
                
                while True:
                    if NewAddress.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewAddress = input("Manzil kiriting: ")
                        continue
                    else:
                        break
        
                
                
                contact["name"] = NewName
                contact["phone"] = NewwPhone
                contact["email"] = NewEmail
                contact["address"] = NewAddress
                            
                print()
                print(30 * "*")    
                print("♻️Yangilandi♻️")
                print(30 * "*")
                print()
                break
            
        else:
            print()
            print(30 * "*")
            print("❌Ism topilmadi❌")
            print(30 * "*")
            print()
            changeContact()
            
    elif choose == "2":
        numberShow()
        
        changeTellNumber = input("Tel raqam kiriting: ")
        
        for contact in contactList:
            if contact["phone"] == changeTellNumber:           
                NewName = input("Yangi ism kiriting: ")
                
                while True:
                    check = False
                    for i in contactList:
                        for nameletter in NewName:
                            if nameletter not in letters:
                                check = True
                    if check:
                        print("Belgilar kiritmang: ")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    for i in contactList:
                        if i["name"] == NewName:
                            check = True
                    if check:
                        print("Bu ism bor")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    elif NewName.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewName = input("Yangi ism kiriting: ")
                        continue
                    elif not NewName.isalpha():
                        print("Faqat harf kiriting: ")
                        NewName = input("Ism kiriting: ")
                    else:
                        break
                    
                NewwPhone = input("Yangi tel raqam kiriting: ")
                
                while True:
                    check = False
                    for i in contactList:
                        for num in numbers:
                            if NewwPhone.isdigit() == True:
                                check = True
                    if check:
                        print("Faqat raqam kiriting: ")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif  not NewwPhone.startswith("+998"):
                        print("+998 kiritilishi kerak")
                        NewwPhone = input("+998 va raqam kiriting: ")
                        continue
                    
                    check = False
                    for i in contactList:
                            if i["phone"] == NewwPhone:
                                check = True
                    if check:
                        print("Bu raqam bor")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif len(NewwPhone) < 13:
                        print("Uzunligi 13 ta bo'lishi kerak")
                        NewwPhone = input("Raqam kiriting: ")

                    elif NewwPhone.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewwPhone = input("Raqam kiriting: ")
                        continue
                    elif not phone[1:].isdigit():
                        print("Raqam kiriting: ")
                        phone = input("Raqam kiriting: ")
                        continue
                    else:
                        break
                    
                    
                NewEmail = input("Yangi email kiriting: ")
                
                while True:
                    if  not NewEmail.endswith("@gmail.com") and not NewEmail.endswith("@gmail.ru"):
                        print("@ va gmail va . kiritilishi kerak")
                        NewEmail = input("Email kiriting: ")
                        continue
                    elif NewEmail.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewEmail = input("Email kiriting: ")
                        continue
                    elif len(NewEmail) < 12:
                        print("Uzunligi kamida 12 bo'lishi kerak")
                        NewEmail= input("Email kiriting: ")
                    else:
                        break
                
                NewAddress = input("Yangi manzil kiriting: ")
                
                while True:
                    if NewAddress.strip() == "":
                        print("Bo'sh qiymat kiritmang: ")
                        NewAddress = input("Manzil kiriting: ")
                        continue
                    else:
                        break
                          
                contact["name"] = NewName
                contact["phone"] = NewwPhone
                contact["email"] = NewEmail
                contact["address"] = NewAddress
                            
                print()
                print(30 * "*")    
                print("♻️Yangilandi♻️")
                print(30 * "*")
                print()
                break
        else:
            print()
            print(30 * "*")
            print("❌Tel raqam topilmadi❌")
            print(30 * "*")
            print()
            changeContact()
    else:
        print()
        print(30 * "*")
        print("1 yoki 2 kiriting...")
        print(30 * "*")
        print()
        changeContact()
        
    if contactList == []:
            print()
            print(30 * "*")
            print("🕳List bo'sh🕳")
            print(30 * "*")
            print()
          
# contact delete
def deleteContact():
    if contactList == []:
        print()
        print(30 * "*")
        print("🕳List bo'sh🕳")
        print(30 * "*")
        print()  
        return 
    
    choose = input("1. Ism bo'yicha o'chirish\n2. Raqam bo'yicha o'chirish\n")
    
    if choose == "1":
        nameShow()
        changeName = input("O'chirmoqchi bo'lgan ismni kiriting: ")
        for contact in contactList:
            if contact["name"] in changeName:
                contactList.remove(contact)
                print(30 * "*")
                print("🗑 Kontakt o'chirildi 🗑")
                print(30 * "*")
                return
        else:
            print(30 * "*")
            print("❌ Ism topilmadi ❌")
            print(30 * "*")
            deleteContact()
        
    elif choose == "2":
        numberShow()
        changeTellNumber = input("O'chirmoqchi bo'lgan raqamni kiriting: ")
        for contact in contactList:
            if contact["phone"] in changeTellNumber:
                contactList.remove(contact)
                print(30 * "*")
                print("🗑 Kontakt o'chirildi 🗑")
                print(30 * "*")
                return 
        else:
            print(30 * "*")
            print("❌ Tel raqam topilmadi ❌")
            print(30 * "*")
            deleteContact()
        
    else:
        print(30 * "*")
        print("1 yoki 2 kiriting...")
        print(30 * "*")


# contact search
def searchContact():
    if contactList == []:
        print()
        print(30 * "*")
        print("🕳List bo'sh🕳")
        print(30 * "*")
        print()  
        return 
    choose = input("1.Ism bo'yicha qidirish\n2.Raqam bo'yicha qidirish\n")
    
    if choose == "1":
        nameShow()
        searchName = input("Qidirmoqchi bo'lgan ismni kiriting: ")
        check = False
        for contact in contactList:
            if searchName.lower() in contact["name"].lower():
                print()
                print(30 * "*")
                print(f"Ism: {contact['name']}")
                print(f"Telefon raqam: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Manzil: {contact['address']}")
                print(30 * "*")
                print()
                check = True
                
        if not check:
            print()
            print(30 * "*")
            print("❌Ism topilmadi❌")
            print(30 * "*")
            print()
    elif choose == "2":
        numberShow()
        searchNumber = input("Qidirmoqchi bo'lgan tel raqamni kiriting: ")
        check = False
        for contact in contactList:
            if searchNumber in contact["phone"]:
                print()
                print(30 * "*")
                print(f"Ism: {contact['name']}")
                print(f"Telefon raqam: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Manzil: {contact['address']}")
                print(30 * "*")
                print()
                check = True
                
        if not check == True:
            print()
            print(30 * "*")
            print("❌Tel raqam topilmadi❌")
            print(30 * "*")
            print()
    else:
        print()
        print(30 * "*")
        print("1 yoki 2 kiriting...")
        print(30 * "*")
        print()
        
                    
# contact show all
def showAllContact():
    if contactList == []:
        print()
        print(30 * "*")
        print("Kontakt hali bo'sh")
        print(30 * "*")
        print()
    else:
        print()
        print(30 * "*")
        for contact in contactList:
            print()
            print(f"Ism: {contact["name"]}")
            print(f"Telefon raqam: {contact["phone"]}")
            print(f"Email: {contact["email"]}")
            print(f"Manzil: {contact["address"]}")
            print()
        print(30 * "*")
        print()
    
# main
while True:
    print("📘 Contact Book 📘")
    
    print("1. ➕ Yangi kontakt qo'shish ➕")
    print("2. ♻️ Kontaktni yangilash ♻️")
    print("3. 🗑 Kontaktni o'chirish 🗑")
    print("4. 🔎 Kontaktni qidirish 🔎")
    print("5. 📤 Barcha kontaktlarni ko'rsatish 📤")
    print("6. ➡️ Chiqish ➡️")
    
    choice = input("Son kiriting: ")
   
    if choice == "1":
        newContact()
    elif choice == "2":
        changeContact()
    elif choice == "3":
        deleteContact()
    elif choice == "4":
        searchContact()
    elif choice == "5":
        showAllContact()
    elif choice == "6":
        print()
        print(30 * "*")
        print("Kuningiz yaxshi o'tsin")
        print(30 * "*")
        print()
        break