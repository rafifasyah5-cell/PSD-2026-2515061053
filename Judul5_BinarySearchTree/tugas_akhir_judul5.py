class BukuNode:
    def __init__(self, isbn, judul):
        self.isbn = isbn        
        self.judul = judul      
        self.left = None        
        self.right = None       
        
class PerpustakaanBST:
    def __init__(self):
        self.root = None       

    def tambah_buku(self, isbn, judul):
        if self.root is None:
            self.root = BukuNode(isbn, judul)
            print(f"[{isbn}] '{judul}' berhasil ditambahkan sebagai Root.")
        else:
            self._insert_rekursif(self.root, isbn, judul)

    def _insert_rekursif(self, node, isbn, judul):
        if isbn < node.isbn:
            if node.left is None:
                node.left = BukuNode(isbn, judul)
                print(f"[{isbn}] '{judul}' ditambahkan di kiri {node.isbn}.")
            else:
                self._insert_rekursif(node.left, isbn, judul)
        elif isbn > node.isbn:
            if node.right is None:
                node.right = BukuNode(isbn, judul)
                print(f"[{isbn}] '{judul}' ditambahkan di kanan {node.isbn}.")
            else:
                self._insert_rekursif(node.right, isbn, judul)
        else:
            print(f"Buku dengan ISBN {isbn} sudah ada di sistem.")

    def cari_buku(self, isbn):
        hasil = self._cari_rekursif(self.root, isbn)
        if hasil:
            print(f"\n[HASIL PENCARIAN] ISBN {isbn} ditemukan: '{hasil.judul}'")
        else:
            print(f"\n[HASIL PENCARIAN] Buku dengan ISBN {isbn} tidak ditemukan.")

    def _cari_rekursif(self, node, isbn):
        if node is None or node.isbn == isbn:
            return node
        if isbn < node.isbn:
            return self._cari_rekursif(node.left, isbn)
        return self._cari_rekursif(node.right, isbn)

    def tampilkan_semua_urut(self):
        print("\n--- DAFTAR BUKU PERPUSTAKAAN (URUT ISBN) ---")
        self._inorder(self.root)
        print("--------------------------------------------")

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(f"ISBN: {node.isbn} | Judul: {node.judul}")
            self._inorder(node.right)

perpus = PerpustakaanBST()
perpus.tambah_buku(500, "Algoritma dan Struktur Data")
perpus.tambah_buku(300, "Pemrograman Python Dasar")
perpus.tambah_buku(700, "Kecerdasan Buatan")
perpus.tambah_buku(200, "Matematika Diskrit")
perpus.tambah_buku(400, "Rekayasa Perangkat Lunak")
perpus.tambah_buku(600, "Sistem Operasi")
perpus.tambah_buku(800, "Jaringan Komputer")
perpus.tampilkan_semua_urut()
perpus.cari_buku(400) 
perpus.cari_buku(999) 