class Song:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, title):
        new_song = Song(title)
        if not self.head:
            self.head = new_song
            self.current = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
            new_song.prev = temp

    def remove_song(self, title):
        temp = self.head
        while temp:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                if self.current == temp:
                    self.current = temp.next or temp.prev

                print("Lagu dihapus")
                return
            temp = temp.next
        print("Lagu tidak ditemukan")

    def show_playlist(self):
        temp = self.head
        if not temp:
            print("Playlist kosong")
            return
        while temp:
            print(temp.title, end=" <-> ")
            temp = temp.next
        print("None")

    def play_current(self):
        if self.current:
            print("Sedang memutar:", self.current.title)
        else:
            print("Tidak ada lagu")

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            print("Sudah di lagu terakhir")

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_current()
        else:
            print("Sudah di lagu pertama")


# ===== MENU INTERAKTIF =====
playlist = Playlist()

while True:
    print("\n=== MENU PLAYLIST ===")
    print("1. Tambah Lagu")
    print("2. Hapus Lagu")
    print("3. Tampilkan Playlist")
    print("4. Putar Lagu Sekarang")
    print("5. Next Lagu")
    print("6. Lagu Sebelumnya")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        judul = input("Masukkan judul lagu: ")
        playlist.add_song(judul)

    elif pilih == "2":
        judul = input("Masukkan lagu yang ingin dihapus: ")
        playlist.remove_song(judul)

    elif pilih == "3":
        playlist.show_playlist()

    elif pilih == "4":
        playlist.play_current()

    elif pilih == "5":
        playlist.next_song()

    elif pilih == "6":
        playlist.prev_song()

    elif pilih == "0":
        print("Keluar dari program")
        break

    else:
        print("Pilihan tidak valid")
