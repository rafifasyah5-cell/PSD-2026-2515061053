queue = []

def tambah_pemesanan():
    nama = input("Masukkan nama penumpang: ")
    tujuan = input("Masukkan tujuan: ")
    
    data = {
        "nama": nama,
        "tujuan": tujuan
    }
    
    queue.append(data)
    print("Pemesanan berhasil ditambahkan!\n")

def proses_pemesanan():
    if len(queue) == 0:
        print("Antrian pemesanan kosong!\n")
    else:
        data = queue.pop(0)
        print("Pemesanan diproses")
        print("Nama    :", data["nama"])
        print("Tujuan  :", data["tujuan"])
        print()

def tampilkan_antrian():
    if len(queue) == 0:
        print("Tidak ada antrian pemesanan.\n")
    else:
        print("=== Antrian Pemesanan Tiket ===")
        nomor = 1
        for data in queue:
            print(f"{nomor}. {data['nama']} - {data['tujuan']}")
            nomor += 1
        print()

while True:
    print("=== SISTEM PEMESANAN TIKET KERETA API ===")
    print("1. Tambah Pemesanan")
    print("2. Proses Pemesanan")
    print("3. Tampilkan Antrian")
    print("4. Keluar")
    
    pilih = input("Pilih menu: ")
    print()

    if pilih == "1":
        tambah_pemesanan()
    elif pilih == "2":
        proses_pemesanan()
    elif pilih == "3":
        tampilkan_antrian()
    elif pilih == "4":
        print("Program selesai.")
        break
    else:
        print("Menu tidak tersedia!\n")