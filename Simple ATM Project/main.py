
# Script By Kevien OJ
# IG : Kevien.OJ
# copyright 2021 

from os import name
import random
import datetime as dt

print(10*"=","Welcome To Kevien Bank","="*10)
fist = ["Kevien","Andy","Jojo","Lena","Layla"]
last = ["Lee Hyung","Herman","Hutson","Reymont","Matshuda"]
pilihan = f"\n Pilih Opsi\n 1.1 Cek saldo anda\n 1.2 Mengambil Uang\n 1.3 Menyetor Uang\n"        
option = f"\n Choise Option\n 2.1 Ceck your Wallet\n 2.2 Wihdraw\n 2.3 Deposit\n"
atm = ["Panin","BNI","Mandiri","BCA"]
today = dt.date.today()

# Language and Option 

# Indonesia Lang

fist_name = random.choice(fist)
last_name = random.choice(last)
atm_name = random.choice(atm)

id_user = f'{random.randint(100,999)}-2203-{random.randint(100,999)}'
print(f" Name : {fist_name} {last_name}\n Card : {id_user}\n Date : {today}\n Bank {atm_name}\n")


lang = str(input("Please Choise Your Language :\n 1.Indonesia \n 2.English\n Your Choise : "))
if lang=="1":
        print(pilihan)

        
        # User Choise

        option_user = str(input("Pilihan kamu :"))

        if option_user=="1.1":
                resault = 500 
                print(f"Jumlah Tabungan Kamu: ${resault}")
        
        elif option_user=="1.2":
              print("\nUang kamu berjumlah $500,Kamu mau mengambil berapa?\n")
              print("\n$50\n$150\n$350\n$500\n$1000\ncustom\n")

              withdraw = str(input("Masukan Jumlah yang ingin anda ambil : "))

              if withdraw== "$50":
                        hasil = 500 - 50
                        print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil}")
                
              
              elif withdraw=="$150":
                        hasil = 500 - 150 
                        print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil}")
                        

              elif withdraw=="$350":
                        hasil = 500 - 350    
                        print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil} ")
              elif withdraw=="$500":
                        hasil = 500 - 500
                        print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil} ")
              elif withdraw=="$1000":
                        hasil = 500 - 1000
                      
                        if hasil < 0:
                            print("Maaf saldo anda kurang")
                        else:
                            print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil}")

              elif withdraw== "custom":
                        dana = int(input("Masukan Nominal Penarikan : "))
                        hasil = 500 - dana

                        if hasil < 0:
                                    print("Maaf saldo anda kurang")
                        else:
                                    print(f"Penarikan Berhasil, Saldo anda tersisa ${hasil}")
                                      
              else:
                      print("Error,Try Again!")

        elif option_user=="1.3":
                setor = int(input("Masukan angka tabungan :"))
                hasil = 500 + setor
                print(f"Saldo kamu bertambah menjadi : ${hasil}") 
                
                
        else:
              print("Coba Lagi :( ")

              print("Terimakasih telah memakai jasa kami :) ")


# English Lang

elif lang== "2":
        print(option)

# User Choise
        option_user_English = str(input("Your Option :"))

        if option_user_English=="2.1":
                resault2 = 500 
                print(f"Your Balance: ${resault2}")
      
        elif option_user_English=="2.2":
              print("\nYour money is $500,how much do you want to take?\n")
              print("\n$50\n$150\n$350\n$500\n$1000\ncustom\n")

              withdraw2 = str(input("Please enter the amount you want to withdraw : "))

              if withdraw2== "$50":
                        hasil2 = 500 - 50
                        print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")
                
              
              elif withdraw2=="$150":
                        hasil2 = 500 - 150 
                        print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")
                        

              elif withdraw2=="$350":
                        hasil2 = 500 - 350    
                        print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")
              elif withdraw2=="$500":
                        hasil2 = 500 - 500
                        print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")
              elif withdraw2=="$1000":
                        hasil2 = 500 - 1000
                      
                        if hasil2 < 0:
                            print("Sorry Your Balance is Not Enough")
                        else:
                            print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")

              elif withdraw2== "custom":
                        dana2 = int(input("Please Enter The Nominal : "))
                        hasil2 = 500 - dana2

                        if hasil2 < 0:
                                    print("Sorry Your Balance is Not Enough")
                        else:
                                    print(f"Withdraw Successful, Your Remaining Balance ${hasil2}")

                                      
              else:
                      print("Error,Try Again!")

        elif option_user_English=="2.3":
                    setor = int(input("Enter Saving Amount :"))
                    hasil2 = 500 + setor
                    print(f"Your Balance Increases to : ${hasil2}") 
                
                
        else:
              print("Error,Try Again! :( ")


else:
        print("Language Not Available,Please Try Again!")

               
print("\nThank You For Using Our Service :) ")   
