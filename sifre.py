import random

print (""" hello world""")
#alfabeler
#ingilizce alfabe
alfabeeng = ["a","b","c","d","e","f","g","h","ı","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#türkçe alfabe
alfabetr  = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
#rakamlar
rakamlar   = ["0","1","3","4","5","6","7","8","9"]
#semboller
semboller  = [";",":"",",".","!","'","^","+","%","&","/","(",")","=","?","_","-","*",">","£","#","$","{","}"]
#kodlar

#izinler

while True:
    izin1 = input("Şifrenizde.Türkçe harf kullanılsın mı?(evet,hayır):")
    izin1 = izin1.lower()
    if izin1 == "evet":
        print("Şifrenizde.Türkçe harfler kullanılacaktır!")
        break
    elif izin1 == "hayır":
        print("Şifrenizde.Türkçe harfler kullanılmayacaktır!")
        break
    elif izin1 == 'q':
        quit()
    elif izin1 == 'Q':
        quit()
    else:
        print("Yanlış bir işlem yaptınız.Çıkmak için 'q'ye basınız.")



while True:
    izin2 = input("Şifrenizde rakamlar kullanılsın mı?(evet,hayır):")
    izin2 = izin2.lower()
    if izin2 == "evet":
        print("Şifrenizde rakamlar kullanılacaktır!")
        break
    elif izin2 == "hayır":
        print("Şifrenizde rakamlar kullanılmayacaktır!")
        break
    elif izin2 == 'q':
        quit()
    elif izin2 == 'Q':
        quit()
    else:
        print("Yanlış bir işlem yaptınız...")

while True:
    izin3 = input("Şifrenizde semboller kullanılsın mı?(evet,hayır):")
    izin3 = izin3.lower()
    if izin3 == "evet":
        print("Şifrenizde semboller kullanılacaktır!")
        break
    elif izin3 == "hayır":
        print("Şifrenizde semboller kullanılmayacaktır!")
        break
    elif izin3 == 'q':
        quit()
    elif izin3 == 'Q':
        quit()
    else:
        print("Yanlış bir işlem yaptınız...")

while True:
    uzunluk = input("Şifreniz kaç basamaklı olsun:")
    try:
        uzunluk = int(uzunluk)
        print(f"Şifreniz {uzunluk} basamaktan oluşacak")
        break

    except ValueError:
        print("Yanlış bir işlem yaptınız. Lütfen tam sayı giriniz örnek = (8,5,6,2,4).")
        continue

#işlem

sifre = list()
for i in range(uzunluk):
    if izin1 == 'evet' and izin2 == 'evet' and izin3 == 'evet':
        sifrelist = rakamlar + alfabetr + semboller
        sifre = random.choice(sifrelist)
        print(sifre,end='')
    elif  izin1 == 'evet' and izin2 == 'evet' and izin3 == 'hayır':
        sifrelist = alfabetr + rakamlar
        sifre = random.choice(sifrelist)
        print(sifre,end='')
    elif izin1 == 'hayır' and izin2 == 'evet' and izin3 == 'evet':
        sifrelist = alfabeeng + rakamlar + semboller
        sifre =random.choice(sifrelist)
        print(sifre,end='')
    elif izin1 == 'evet' and izin2 == 'hayır' and izin3 == 'evet':
        sifrelist = alfabetr + semboller
        sifre = random.choice(sifrelist)
        print(sifre,end='')
    elif izin1 == 'hayır' and izin2 == 'hayır' and izin3 == 'hayır':
        sifre = random.choice(alfabeeng)
        print(sifre,end='')
    elif izin1 == 'hayır' and izin2 == 'evet'  and izin3 == 'hayır':
        sifrelist = alfabeeng + rakamlar
        sifre = random.choice(sifrelist)
        print(sifre,end='')
    elif izin1 == 'hayır' and izin2 == 'hayır' and izin3 == 'evet':
        sifrelist = alfabeeng + rakamlar
        sifre = random.choice(sifrelist)
        print(sifre,end='')
    elif izin1 == 'evet' and izin2 == 'hayır' and izin3 == 'hayır':
        sifre = random.choice(alfabetr)
        print(sifre,end='')
    else:
        print("Bir şeyler yanlış çıktı...")
print("")
