print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri anda.")
nama = input("Masukkan nama anda: ")
tahun_lahir = input("Masukkan tahun lahir anda: ")
umur = 2024 - int(tahun_lahir)

print(
    f"Selamat datang {nama} dalam program python, per 2024 umur anda adalah {umur} tahun. \n"
)
print("Terima kasih telah menggunakan program python!")

for i in "Eunoia Kayra":
    if i == " ":
        continue
    print(f"Looping nama anak cantik: {i}")

print("Cek tinggi badan. \n")
tinggi_badan = int(input("Masukkan tinggi badan anda: "))

if tinggi_badan >= 160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Tinggi badan anda tidak mencukupi")

counter = int(input("Masukkan tahun sekarang: "))
while counter > 1996:
    print(counter)
    counter -= 1
else:
    print("You arrived to the year that i born!")

angka = [1, 2, 3, 4, 5]
# pangkat = []
# for n in angka:
#     pangkat.append(n**2)
pangkat = [n**2 for n in angka]

print(pangkat)

evenNumber = [i for i in range(0, 501) if i % 2 == 0]
print(evenNumber)
