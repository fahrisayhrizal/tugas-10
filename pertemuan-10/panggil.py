import bangun_datar, bangun_ruang

print("====Luas Bangun Datar====")
print(f"Luas persegi = {bangun_datar.luas_persegi(5)}")
print(f"luas segitiga = {bangun_datar.luas_segitiga(5, 5)}")
print(f"luas lingkaran = {bangun_datar.luas_lingkaran(5)}")
print(f"luas ketupat= {bangun_datar.luas_ketupat(5, 5)}")
print(f"luas jajar genjang = {bangun_datar.luas_jajar_genjang(5, 5)}")

print("====Luas Bangun Ruang+====")
print(f"Luas Kubus = {bangun_ruang.luas_kubus(5)}")
print(f"Luas balok = {bangun_ruang.luas_balok(5, 5, 5)}")
print(f"Luas bola = {bangun_ruang.luas_bola(5)}")
print(f"Luas tabung = {bangun_ruang.luas_tabung(5, 5)}")
print(f"Luas kerucut = {bangun_ruang.luas_kerucut(5, 5)}")


