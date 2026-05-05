def simulasi_cari_halaman():
    print("=== SIMULASI PENCARIAN HALAMAN BUKU (BINARY SEARCH) ===")
    
    try:
        total = int(input("Masukkan total halaman buku: "))
        target = int(input(f"Mau cari halaman berapa? (1-{total}): "))

        if target > total or target < 1:
            print(f"Maaf, halaman {target} tidak ada di buku ini!")
            return

        awal = 1
        akhir = total
        langkah = 0
        
        print(f"\nMemulai pencarian halaman {target}...")
        print("-" * 50)

        while awal <= akhir:
            langkah += 1
            tengah = (awal + akhir) // 2
            
            print(f"Langkah {langkah}: Membuka halaman {tengah}")

            if tengah == target:
                print("-" * 50)
                print(f"HASIL: Halaman {target} DITEMUKAN!")
                print(f"Total percobaan buka buku: {langkah} kali.")
                return
            
            if tengah < target:
                print(f"   [Terlalu kecil] -> Lihat ke arah kanan (halaman {tengah + 1} ke atas)")
                awal = tengah + 1
            else:
                print(f"   [Terlalu besar] -> Lihat ke arah kiri (halaman {awal} sampai {tengah - 1})")
                akhir = tengah - 1

    except ValueError:
        print("Error: Harap masukkan angka bulat (integer) yang valid!")

simulasi_cari_halaman()