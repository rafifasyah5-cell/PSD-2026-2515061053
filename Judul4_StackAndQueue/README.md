Program ini adalah sistem pemesanan tiket kereta api sederhana yang menggunakan konsep queue array atau antrian FIFO (First In First Out). Program ini memungkinkan pengguna untuk menambahkan pemesanan tiket, memproses antrian pemesanan paling depan, dan melihat daftar antrian yang sedang menunggu. Data penumpang disimpan dalam list berupa nama dan tujuan perjalanan. Program berjalan menggunakan menu interaktif sehingga pengguna bisa memilih fitur yang diinginkan sampai memilih keluar dari program.

<img width="593" height="358" alt="Screenshot 2026-05-12 094708" src="https://github.com/user-attachments/assets/ca44c0e9-5a35-41b0-8f6b-ab19ab5870dc" />

Fungsi ini digunakan untuk menambahkan data pemesanan tiket ke dalam antrian. Pengguna diminta memasukkan nama penumpang dan tujuannya, kemudian data disimpan ke dalam dictionary dan dimasukkan ke queue menggunakan append().


<img width="487" height="241" alt="Screenshot 2026-05-12 094715" src="https://github.com/user-attachments/assets/f7cedf75-3069-4755-bfe6-248207182093" />

Fungsi ini digunakan untuk memproses antrian pemesanan paling depan. Program akan mengecek apakah queue kosong atau tidak. Jika ada data, maka data paling depan akan diambil menggunakan pop(0) lalu ditampilkan nama dan tujuan penumpangnya.

<img width="711" height="771" alt="Screenshot 2026-05-12 094734" src="https://github.com/user-attachments/assets/9c2b4129-f99b-4b63-ace4-622b3cd356e4" />

Bagian ini digunakan untuk menjalankan program utama sekaligus menampilkan seluruh isi antrian. tampilkan_antrian() berfungsi menampilkan daftar pemesanan yang ada di queue secara berurutan. while True membuat program terus berjalan dan menampilkan menu berulang kali sampai pengguna memilih keluar. Sedangkan if else digunakan untuk membaca pilihan menu pengguna dan menentukan fungsi mana yang akan dijalankan, seperti menambah pemesanan, memproses antrian, menampilkan antrian, atau keluar dari program.

<img width="423" height="711" alt="Screenshot 2026-05-12 095109" src="https://github.com/user-attachments/assets/508923a5-c425-4bad-a332-a36b6116ce73" />

Output ini menunjukkan bahwa user diminta untuk menginput data penumang  yang akan masuk ke dalam antrian atau Queue untuk diproses

<img width="419" height="244" alt="Screenshot 2026-05-12 095125" src="https://github.com/user-attachments/assets/8fd77c7f-fb47-4bb4-83b2-80cd8aa2d579" />

Output ini menunjukkan bahwa penumpang yang pertama mengantri akan menjadi penumpang pertama yang diproses 

<img width="406" height="241" alt="Screenshot 2026-05-12 095137" src="https://github.com/user-attachments/assets/08e0962a-f613-4d7b-9b1c-78b018019299" />

Output ini menunjukkan list semua penumpang yang masih masuk ke daftar antrian / Queue 
