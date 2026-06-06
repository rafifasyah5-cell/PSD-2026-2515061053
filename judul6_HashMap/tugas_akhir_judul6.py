def jalankan_sistem_akademik():
    database_mahasiswa = {}

    while True:
        print("\n=== SISTEM DATA MAHASISWA ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Berdasarkan NPM")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            print("\n--- Tambah Data ---")
            npm = input("Masukkan NPM        : ")
            nama = input("Masukkan Nama       : ")
            jurusan = input("Masukkan Jurusan    : ")
            organisasi = input("Masukkan Organisasi : ")
            database_mahasiswa[npm] = {
                "nama": nama,
                "jurusan": jurusan,
                "organisasi": organisasi
            }
            print(f"Data mahasiswa {nama} berhasil disimpan!")

        elif pilihan == '2':
            print("\n--- Cari Data ---")
            npm_dicari = input("Masukkan NPM yang dicari: ")
            if npm_dicari in database_mahasiswa:
                data = database_mahasiswa[npm_dicari]
                print("\n[Data Ditemukan]")
                print(f"Nama       : {data['nama']}")
                print(f"Jurusan    : {data['jurusan']}")
                print(f"Organisasi : {data['organisasi']}")
            else:
                print("\n[Error] Mahasiswa dengan NPM tersebut tidak ditemukan.")

        elif pilihan == '3':
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    jalankan_sistem_akademik()