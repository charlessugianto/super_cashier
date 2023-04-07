# Latar Belakang
Membuat sistem kasir self service, sehingga pelanggan toko dapat memasukkan item yang dibeli, 
jumlah item, dan harga untuk memperbaiki proses bisnis di toko Andi, dimana Andi adalah seorang
pemiliki supermarket besar di salah satu kota di Indonesia.

# Requirements/Objektif
- Membuat ID transaksi customer
- Memasukkan nama item, jumlah item, dan harga barang ke dalam fungsi add_item kasir
- Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya
  - Membuat dan menggunakkan fungsi update_item_name
  - Membuat dan menggunakkan fungsi update_item_qty
  - Membuat dan menggunakkan fungsi update_item_price
- Jika batal membeli item belanjaan, maka membuat dan menggunakkan fungsi delete_item
- Membuat suatu perintah untuk mereset ulang data transaksi dengan fungsi reset_transaction
- Membuat suatu perintah untuk memeriksa kembali data transaksi dengan fungsi check_order
- Menghitung total pembayaran dan diskon sesuai dengan fungsi total_price dengan ketentuan
  - Jika total belanja Andi diatas Rp 200.000 maka akan mendapatkan diskon 5%
  - Jika total belanja Andi diatas Rp 300.000 maka akan mendapatkan diskon 8%
  - Jika total belanja Andi diatas Rp 500.000 maka akan mendapatkan diskon 10%

# Penjelasan Flowchart
<img width="545" alt="Flowchart Super Cashier" src="https://user-images.githubusercontent.com/129651972/230600782-751fe667-125e-46f1-bfbd-d27a01f71144.png">

# Penjelasan Function
  - Class Transaction, akan menjadi kelas yang berisi beberapa fungsi untuk sistem kasir dan akan menampung input data dari pelanggan
  <img width="503" alt="Screenshot 2023-04-07 at 21 29 43" src="https://user-images.githubusercontent.com/129651972/230625941-67e21332-099a-44c7-a006-b5ad5d80805c.png">

  -  Atribute, memiliki informmasi nama toko Andi
  <img width="503" alt="Screenshot 2023-04-07 at 21 29 36" src="https://user-images.githubusercontent.com/129651972/230625957-d132070c-6af9-4b22-993a-100b773a84a8.png">

  -  Add_Item, memiliki fungsi untuk menampung tipe data nama_item berupa string, jumlah_item berupa integer dan lebih besar dari 0, dan harga_item berupa integer atau float. Tidak hanya untuk menambahkan item ke dalam riwayat transaksi, tetapi juga untuk memeriksa tipe data, apakah telah sesuai dengan yang diinputkan. Jika tidak sesuai, maka akan keluar pesan error, dan pelanggan diminta untuk melakukan input kembali dengan tipe data yang benar.
  <img width="883" alt="Screenshot 2023-04-07 at 21 30 53" src="https://user-images.githubusercontent.com/129651972/230626140-6a6e1546-14d1-412d-b725-fe9ff975e86b.png">

-  Update_Item_Name, memiliki fungsi untuk memperbaharui tipe data nama_item berupa string, jumlah_item berupa integer, dan harga_item berupa integer atau float. Tidak hanya untuk memperbaharui item ke dalam riwayat transaksi yang telah dibuat sebelumnya, tetapi juga untuk memeriksa tipe data, apakah telah sesuai dengan yang diinputkan. Jika tidak sesuai, maka akan keluar pesan error, dan pelanggan diminta untuk melakukan input kembali dengan tipe data yang benar. 
<img width="861" alt="Screenshot 2023-04-07 at 21 37 29" src="https://user-images.githubusercontent.com/129651972/230627056-336dfd83-4ede-4b06-9e1f-977f694c9a2e.png">

-  Update_Item_Quantity
