https://youtu.be/liSQsA6kO7M

Program ini bekerja dengan konsep doubly linked list, di mana setiap lagu disimpan sebagai node yang saling terhubung ke lagu berikutnya dan sebelumnya. Playlist memiliki penunjuk utama (head) untuk lagu pertama dan current untuk lagu yang sedang diputar. Saat user memilih menu, program akan menjalankan fungsi sesuai input. Menambah lagu akan menyambungkan node baru di akhir playlist. Menghapus lagu akan memutus dan menyambung ulang node di sekitarnya tanpa menggeser data lain. Fitur next dan previous memindahkan posisi current ke lagu setelah atau sebelumnya, sehingga bisa navigasi maju-mundur seperti playlist pada aplikasi musik.
Output yang ditampilkan menyesuaikan aksi user, seperti daftar lagu, lagu yang sedang diputar, atau notifikasi jika sudah di lagu terakhir atau pertama. Program terus berjalan dalam loop sampai user memilih keluar.

<img width="382" height="158" alt="Screenshot 2026-04-21 185929" src="https://github.com/user-attachments/assets/9241d7e8-a1fa-4a0e-b212-331f5deef8dc" />
Fungsi ini itu berguna untuk menyimpan judul lagu dan sebagai pointer sebagai next dan prev


<img width="296" height="113" alt="Screenshot 2026-04-21 190138" src="https://github.com/user-attachments/assets/c9104a49-4f71-44d8-bda8-9270c1f0bd6a" />
fungsi ini menginisialisasi playlist dengan head sebagai penunjuk lagu pertama dan current sebagai lagu yang sedang diputar, yang awalnya masih kosong


<img width="366" height="292" alt="Screenshot 2026-04-21 190401" src="https://github.com/user-attachments/assets/fa36285e-f3d2-4734-96f1-67eeed310ed7" />
fungsi ini menambahkan lagu ke playlist. Jika masih kosong, lagu langsung jadi head dan current. Jika tidak, lagu ditambahkan di akhir dan disambungkan dengan node sebelumnya


<img width="573" height="475" alt="Screenshot 2026-04-21 190452" src="https://github.com/user-attachments/assets/ccb69a19-909b-484e-9e90-bc13a672c3aa" />
fungsi ini menghapus lagu berdasarkan judul. Jika ditemukan, sambungan antar node diperbaiki. Jika lagu yang dihapus sedang diputar, maka current dipindahkan ke lagu terdekat


<img width="398" height="239" alt="Screenshot 2026-04-21 190526" src="https://github.com/user-attachments/assets/c988b396-183c-4786-9a4d-7bbf767165f7" />
fungsi ini menampilkan semua lagu dari awal sampai akhir dengan mengikuti pointer next


<img width="541" height="154" alt="Screenshot 2026-04-21 190557" src="https://github.com/user-attachments/assets/b8375134-696c-4f2e-953b-5bfbcba0a649" />
fungsi ini menampilkan lagu yang sedang diputar jika ada


<img width="440" height="180" alt="Screenshot 2026-04-21 190634" src="https://github.com/user-attachments/assets/434a1511-e42d-4329-ba6b-323b07e5dbe3" />
fungsi ini memindahkan ke lagu berikutnya jika tersedia, jika tidak akan muncul pesan bahwa sudah di akhir


<img width="447" height="196" alt="Screenshot 2026-04-21 190704" src="https://github.com/user-attachments/assets/aece3e83-3d6f-4a77-a2c6-c2e54753ccdd" />
ungsi ini memindahkan ke lagu sebelumnya jika ada, jika tidak akan muncul pesan bahwa sudah di awal


<img width="435" height="661" alt="Screenshot 2026-04-21 190800" src="https://github.com/user-attachments/assets/76b16be4-1732-4d44-b876-36e2d2d6d9cf" />
berfungsi sebagai menu interaktif yang terus berjalan dan memanggil fungsi sesuai pilihan user sampai program dihentikan
