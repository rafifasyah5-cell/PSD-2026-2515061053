Program Mencari Halaman Buku

Program ini berfungsi sebagai asisten pencari cepat untuk menemukan data di dalam daftar yang sudah terurut, seperti mencari halaman buku. Tujuannya adalah memangkas waktu  agar tidak perlu mengecek ribuan data satu per satu.

Langkahnya sangat sederhana, pertama, program akan langsung melompat ke titik tengah dari seluruh halaman yang ada. Kedua, program membandingkan halaman tengah itu dengan target user jika terlalu kecil atau besar, ia langsung membuang separuh bagian buku yang tidak mungkin berisi target tersebut. Terakhir, langkah ini diulangi terus pada bagian yang tersisa sampai target ditemukan. Hasilnya, pencarian yang seharusnya memakan waktu lama bisa selesai hanya dalam hitungan detik.


<img width="773" height="351" alt="Screenshot 2026-05-05 155433" src="https://github.com/user-attachments/assets/ab6ba15d-7425-4f7e-b5e9-321039a75641" />

Bagian ini merupakan tahap persiapan dan validasi sebelum pencarian dimulai. Fungsi def dan print di awal bertujuan untuk membungkus kode dan menampilkan judul program. Penggunaan try berfungsi sebagai pengaman agar program tidak crash jika pengguna salah memasukkan input. Baris total dan target bertugas mengambil data angka dari pengguna, sementara if bertugas untuk memastikan halaman yang dicari memang ada di dalam rentang buku, jika tidak masuk akal, program akan langsung berhenti dengan perintah return. Terakhir, variabel awal, akhir, dan langkah disiapkan sebagai batas ruang lingkup pencarian dan penghitung jumlah percobaan yang akan dilakukan oleh algoritma.


<img width="594" height="216" alt="Screenshot 2026-05-05 155905" src="https://github.com/user-attachments/assets/62fbdeb2-0c02-46f0-9023-55ea49d0fb47" />

Bagian ini adalah inti dari proses pencarian di mana algoritma mulai bekerja membelah data secara berulang. Setelah memberikan notasi awal melalui perintah print, program memasuki while awal <= akhir yang berfungsi untuk terus mencari selama batas pencarian masih tersedia. Di dalam siklus tersebut, variabel langkah += 1 bertugas mencatat setiap kali percobaan dilakukan agar kita tahu seberapa efisien prosesnya. Kode yang paling krusial adalah tengah = (awal + akhir) // 2, di mana komputer menentukan titik tengah dari jangkauan halaman saat ini sebagai bahan tebakan. Terakhir, program mencetak halaman tengah yang sedang dibuka tersebut ke layar agar pengguna dapat melihat proses pemotongan halaman yang dilakukan oleh sistem.

<img width="1049" height="489" alt="Screenshot 2026-05-05 160119" src="https://github.com/user-attachments/assets/86275f1a-67ad-426f-925b-e3e9b3a843fd" />

Bagian ini adalah pengambil keputusan hasil pencarian. Jika halaman tengah sesuai target, program mencetak keberhasilan dan berhenti. Jika halaman terlalu kecil, batas awal dinaikkan, jika terlalu besar, batas akhir diturunkan untuk mempersempit area pencarian. Di akhir, terdapat except ValueError untuk menangani kesalahan input pengguna dan baris perintah paling bawah berfungsi untuk menjalankan seluruh simulasi tersebut.
