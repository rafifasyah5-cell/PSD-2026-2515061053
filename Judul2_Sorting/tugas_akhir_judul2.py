def selection_sort_buku(daftar_buku, urutan="asc"):
    n = len(daftar_buku)
    for i in range(n):
        target_indeks = i
        for j in range(i + 1, n):
            if urutan == "asc":
                if daftar_buku[j]['tinggi'] < daftar_buku[target_indeks]['tinggi']:
                    target_indeks = j
            else:
                if daftar_buku[j]['tinggi'] > daftar_buku[target_indeks]['tinggi']:
                    target_indeks = j
        
        daftar_buku[i], daftar_buku[target_indeks] = daftar_buku[target_indeks], daftar_buku[i]

def main():
    rak_buku = []
    print("=== Program Rak Buku ===")
    
    try:
        n_input = input("Berapa buku yang mau disusun? ")
        n = int(n_input)
        
        for i in range(n):
            judul = input("Judul buku ke-" + str(i+1) + ": ")
            tinggi_input = input("Tinggi buku " + judul + " (cm): ")
            tinggi = int(tinggi_input)
            rak_buku.append({"judul": judul, "tinggi": tinggi})

        print("\nPilih metode pengurutan:")
        print("1. Ascending (Kecil ke Besar)")
        print("2. Descending (Besar ke Kecil)")
        pilihan = input("Masukkan pilihan (1/2): ")

        mode = "asc" if pilihan == "1" else "desc"
        label = "Kecil ke Besar" if mode == "asc" else "Besar ke Kecil"

        selection_sort_buku(rak_buku, mode)

        print("\n--- Hasil Urutan (" + label + ") ---")
        for b in rak_buku:
            print("[" + str(b['tinggi']) + " cm] " + b['judul'])

    except ValueError:
        print("Terjadi kesalahan: Pastikan memasukkan angka untuk jumlah dan tinggi buku.")

if __name__ == "__main__":
    main()