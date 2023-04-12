import SuperCashier1 as s

# Test Case 1: Menambahkan dua item baru
user = s.Transaction()
print("Test Case 1")
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
print("Berikut adalah transaksi belanja Anda :")
user.check_order()
user.total_price()

# Test Case 2: Menghapus salah satu item
user.delete_item("Pasta Gigi")
print("Berikut adalah transaksi belanja Anda :")
user.check_order()
user.total_price()


# Test Case 3: Menghapus semua item
user.reset_transaction()


# Test Case 4: Menghitung total belanja
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
user.add_item("Mainan Mobil", 1, 200_000)
print("\n")
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Tabel Pemesanan :")
user.check_order()
user.total_price()


# Test Case 5: Memperbaharui Item, Quantity, dan Harga
print("Tabel Pemesanan Sebelum Update:")
user.check_order()
user.total_price()
print("\n")
# Update Item pasta gigi
user.update_item_name("Pasta Gigi", "Sabun Mandi")
# Update Quantity ayam goreng
user.update_item_quantity("Ayam Goreng", 3)
# Update Harga mie instan
user.update_item_price("Mie Instan", 3_500)
print("\n")
print("Tabel Pemesanan Setelah Update:")
user.check_order()
user.total_price()


# Test Case 6: Kesalahan Input
user.add_item("Gula", -25, 10_000)


# Test Case 7: Kesalahan Input
user.add_item("Gula", "Lima", 10_000)