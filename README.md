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
