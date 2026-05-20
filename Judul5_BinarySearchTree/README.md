https://youtu.be/JEODRmmfmU4


Program ini adalah simulasi sistem katalog perpustakaan yang menggunakan struktur data Binary Search Tree (BST) untuk menyusun buku berdasarkan nomor ISBN. Aturan kerjanya sangat sederhana yaitu setiap buku yang baru masuk akan dibandingkan dengan buku yang sudah ada, lalu diletakkan di cabang sebelah kiri jika ISBN-nya lebih kecil, atau di cabang sebelah kanan jika ISBN-nya lebih besar.

Dengan membagi jalur ke kiri dan kanan seperti ini, program dapat menemukan buku jauh lebih cepat karena ia langsung mengabaikan separuh dari total data pada setiap langkah pencarian. Selain mempercepat proses pelacakan, struktur pembagian ini juga membuat sistem secara otomatis mengurutkan semua koleksi buku dari ISBN terkecil hingga terbesar tanpa perlu menggunakan rumus pengurutan tambahan.



<img width="392" height="155" alt="Screenshot 2026-05-20 150545" src="https://github.com/user-attachments/assets/2ba1ddb8-bd06-4a49-900c-488389f3247f" />

Fungsi ini bertindak sebagai cetakan pabrik untuk membuat objek buku baru. Ketika dipanggil, ia akan menerima data berupa nomor ISBN dan judul, lalu menyimpannya secara permanen ke dalam blok memori. Selain menyimpan data, fungsi ini juga menyiapkan dua ruang kosong bernama left dan right.

![Uploading Screenshot 2026-05-20 150730.png…]()

Fungsi ini bertugas sebagai langkah persiapan awal persis saat sistem perpustakaan pertama kali dihidupkan. Tugas utamanya sangat sederhana, yaitu menetapkan nilai root atau akar menjadi kosong.

<img width="724" height="165" alt="Screenshot 2026-05-20 150824" src="https://github.com/user-attachments/assets/cf6ad61e-3fdd-409c-be8c-3226a7c11450" />

Fungsi ini akan mengecek kondisi awal perpustakaan terlebih dahulu. Apabila sistem melihat status root masih kosong, buku yang baru masuk tersebut akan langsung diletakkan di puncak dan diangkat menjadi buku pertama atau akar pohon. Namun, jika posisi puncak sudah terisi oleh buku lain, fungsi ini akan meminta bantuan mesin internal sistem untuk mencarikan posisi rak yang kosong dan sesuai.

![Uploading Screenshot 2026-05-20 150959.png…]()

Fungsi ini bekerja secara diam-diam di belakang layar dengan membandingkan ISBN buku baru terhadap buku yang sedang dievaluasi. Apabila ISBN baru nilainya lebih kecil, ia akan langsung menelusuri jalur sebelah kiri, dan jika lebih besar ia akan pergi ke jalur kanan. Proses penelusuran ini dilakukan terus-menerus dengan memanggil dirinya sendiri berulang kali sampai ia akhirnya menemukan ruang yang benar-benar kosong untuk meletakkan buku tersebut.

<img width="825" height="176" alt="Screenshot 2026-05-20 151035" src="https://github.com/user-attachments/assets/66e5263a-ad08-44c5-a9fb-0b534860e4ee" />

Pengguna cukup memasukkan nomor ISBN yang dicari, lalu fungsi ini akan menyuruh mesin pelacak internal untuk mulai menelusuri tumpukan buku dimulai dari bagian akar.

<img width="569" height="178" alt="Screenshot 2026-05-20 151204" src="https://github.com/user-attachments/assets/680034c0-8601-47fd-b7f2-79d2a1b7cde7" />

Ini adalah algoritma yang bergerak sangat cepat menelusuri cabang-cabang pohon. Ia memiliki rem pengaman agar tidak berputar-putar mencari tanpa henti. Ia akan langsung berhenti bekerja apabila jalurnya sudah mentok yang berarti bukunya tidak ada, atau saat buku dengan ISBN yang dicari sudah tepat berada di depannya.

<img width="610" height="111" alt="Screenshot 2026-05-20 151244" src="https://github.com/user-attachments/assets/2a79df90-ab20-45b9-bf04-bd1323d02f7d" />

Fungsi ini ibarat sebuah tombol yang ketika ditekan akan merapikan tampilan layar, mencetak garis pembatas, dan menuliskan judul daftar.

<img width="612" height="456" alt="Screenshot 2026-05-20 151335" src="https://github.com/user-attachments/assets/08a7c8dc-5ef0-4428-9b1e-e8045bf35107" />

fungsi _inorder yang bekerja dengan pola pergerakan yang sangat kaku. Ia diprogram untuk selalu menelusuri jalur paling kiri terlebih dahulu sampai ujung yang paling dalam, lalu mencetak data buku di sana, barulah ia mundur sedikit untuk memeriksa dan mencetak jalur kanannya. Pola pergerakan seperti ini secara matematis menjamin bahwa daftar buku yang keluar di layar akan selalu tercetak dengan urutan yang sempurna, berbaris rapi dari nomor ISBN yang paling kecil hingga yang paling besar tanpa memerlukan proses pengurutan tambahan.
