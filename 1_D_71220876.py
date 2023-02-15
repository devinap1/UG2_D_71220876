print("=========== Makanan ===========")
print("1. telur bakar : Rp 7000")
print("2. lele terbang mas bhe : Rp 10000")
print("3. es coklat lempu : Rp 5000")
print("4. es doger langensari : Rp 13000")

print("=========== pesanan ===========")
telurbakar = int(input("telur bakar: "))
leleterbang = int(input("lele terbang : "))
escoklat = int(input("es coklat : "))
esdoger = int(input("es doger : "))


tmkn =telurbakar*7000
       
tmkn2 =leleterbang*10000
      
tminum =escoklat*5000

tminum2 =esdoger*13000

total=tmkn+tminum+tmkn2+tminum2

print("========== total =========")
print (telurbakar, "telur bakar = Rp ", tmkn)
print (leleterbang, "lele terbang = Rp ", tmkn2)
print (escoklat, "es coklat = Rp ", tminum)
print (esdoger, "es doger = Rp ", tminum2)
print("\njumlah total biaya yang harus dibayar: Rp",total)