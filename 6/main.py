login='123'
parol='1234'

spaece_id=input("Spaece id kirirting")
password=input("Spacece parolini kiriting")

if login == spaece_id and parol == password:
    print("Siz kirdingiz!")
elif login != spaece_id:
    print("Spaece id xato!")
elif parol != password:
    print("Parol xato!") 
else:
     print("Space id va parol xato")