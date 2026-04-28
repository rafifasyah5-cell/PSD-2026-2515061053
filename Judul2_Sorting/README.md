PROGRAM SORTING RAK BUKU DENGAN SELECTION SORT 
Program ini bekerja dengan cara meminta input data buku lalu mensorting daftar tersebut berkali-kali untuk mencari buku yang paling pendek atau paling tinggi sesuai pilihan user. Setelah menemukan buku yang dicari, program akan menukar posisinya ke urutan yang benar satu per satu hingga seluruh rak tersusun rapi. Hasil akhirnya adalah daftar buku yang sudah terurut yang ditampilkan kembali di layar melalui proses seleksi dan penukaran posisi yang konsisten.


<img width="1097" height="364" alt="Screenshot 2026-04-28 100034" src="https://github.com/user-attachments/assets/7f637522-4720-4f79-ad9d-39293591df29" />

Bagian ini berfungsi untuk menyeleksi dan menukar posisi buku. Program akan memindai seluruh daftar untuk mencari buku yang ukurannya paling tepat (paling pendek atau paling tinggi). Setelah ketemu, posisi buku tersebut langsung ditukar ke urutan yang benar. Proses ini diulang terus-menerus sampai seluruh rak tersusun rapi.

<img width="703" height="338" alt="Screenshot 2026-04-28 100128" src="https://github.com/user-attachments/assets/19a1953e-5bea-4961-80c9-7e2629b38411" />
Bagian ini merupakan tahap pengumpulan data untuk mencatat informasi buku. Program akan meminta jumlah buku yang diinginkan, lalu melalui perulangan, user diminta memasukkan judul dan tinggi tiap buku. Seluruh informasi tersebut disimpan ke dalam daftar utama agar siap diurutkan pada tahap berikutnya.

<img width="653" height="339" alt="Screenshot 2026-04-28 100143" src="https://github.com/user-attachments/assets/6d27d91e-2c44-4d4c-8345-3b0ac9cc5fc2" />
Bagian ini adalah tahap penentuan mode dan penyajian hasil akhir. Program meminta user memilih arah pengurutan, lalu secara otomatis menentukan apakah proses akan berjalan secara menaik atau menurun berdasarkan pilihan tersebut. Setelah fungsi pengurutan selesai bekerja, program melakukan perulangan untuk mencetak daftar buku yang telah rapi ke layar sehingga kamu bisa melihat urutan judul dan tinggi buku sesuai hasil seleksi yang dilakukan.

<img width="936" height="159" alt="Screenshot 2026-04-28 101631" src="https://github.com/user-attachments/assets/bd4e1def-3c3f-4470-a554-03d98ce68f1d" />
Bagian terakhir ini berfungsi sebagai pengaman dan pemicu program. Baris except ValueError akan menangkap kesalahan jika kamu memasukkan teks saat program meminta angka, sehingga program tidak langsung berhenti error melainkan memberikan pesan peringatan yang jelas. Sementara itu, baris paling bawah memastikan bahwa seluruh fungsi utama dijalankan secara otomatis hanya ketika file tersebut dibuka langsung, sehingga program bisa berjalan dari awal sampai selesai dengan teratur.  
