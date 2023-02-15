#Devina

pelanggan = []

member = []

while True:
    print("Selamat Datang!")
    print("1.Menambah")
    print("2.Menampilkan")
    print("3.Keluar")
    
    choice = int(input("Silahkan masukkan pilihan: "))
    
    if choice == 1:
        mskplg = input("Masukkan Nama Pelanggan: ")
        pelanggan.append(mskplg)
        mskmbr = input("Masukkan Jenis Member: ")
        member.append(mskmbr)
        print ("Data Sudah Berhasil Ditambahkan!\n\n")
        
    elif choice == 2:
        print("----------------------")
        print("Pelanggan\tMember")
        print(pelanggan[0],"\t\t",member[0])
        print()
        
    else:
        exit()
else:
    print("sistem berhenti")