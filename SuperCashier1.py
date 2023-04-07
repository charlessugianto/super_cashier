import pandas as pds
import numpy as npy
from tabulate import tabulate

class Transaction:
    # Membuat dict belanja
    dict_toko = {"Item": [], "Quantity": [], "Price": []}
    data = pds.DataFrame(dict_toko)

    def _init_(self):
        """Fungsi inisialisasi untuk class Transaction"""
        self.nama_toko = "Toko Andi"
        
    def add_item(self, nama_item: str, jumlah_item: int, harga_item: float or int):
        """Fungsi menambahkan nama_item, jumlah_item, harga_item ke dalam dictionary
            nama_item (str): nama item
            jumlah_item (int): jumlah item
            harga_item (float atau int): harga per item """

        # Cek tipe data nama_item
        if type(nama_item) != str:
            print("Masukkan tipe data 'nama_item' dengan ketentuan string")
        
        # Cek tipe data jumlah_item
        elif type(jumlah_item) != int:
            print("Masukkan tipe data 'jumlah_item' dengan ketentuan integer dan harus lebih besar dari 0")
        
        # Cek jumlah_item tidak boleh kurang dari nol
        elif jumlah_item < 0:
            print("Masukkan jumlah item lebih besar dari 0")
        
        # Cek tipe data harga_item
        elif type(harga_item) != float and type(harga_item) != int:
            print("Masukkan tipe data 'harga_item' dengan ketentuan float atau integer")
        
        else:
            # Menyimpan tipe data nama_item, jumlah_item, dan harga_item
            self.data.loc[len(self.data)] = [nama_item, jumlah_item, harga_item,]
            print("Item yang berhasil masuk dalam keranjang")
            print(f"Nama item     : {nama_item}")
            print(f"Jumlah           : {jumlah_item}")
            print(f"Harga per item: Rp. {harga_item}")

            
    def update_item_name(self, nama_item: str, update_nama_item: str):
        """Fungsi memperbaharui nama_item ke dalam dictionary
            nama_item (str): nama item lama
            update_nama_item (str): nama item baru"""
        
        # List seluruh item_name
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek nama_item pada list_nama_item 
            if nama_item not in list_nama_item:
                print("nama_item belum ada dalam list")
            
            else:
                # Cek tipe data nama_item 
                if type(nama_item) != str:
                    print("nama_item belum mengikuti ketentuan string")
                # Cek tipe data update_nama_item
                
                elif type(update_nama_item) != str:
                    print("update_nama_item belum mengikuti ketentuan string")
                
                else:
                    # Menyimpan tipe data nama_item baru
                    self.data.loc[self.data.Item == nama_item, "Item"] = update_nama_item
                    print(f"Anda telah berhasil mengganti item {nama_item} menjadi {update_nama_item}")

        except ValueError:
            print(f"Item {nama_item} tidak ada dalam riwayat belanja Anda")

            
    def update_item_quantity(self, nama_item: str, update_jumlah_item: int):
        """Fungsi memperbaharui jumlah_item ke dalam dictionary
            nama_item (str): nama item lama
            update_jumlah_item (int): jumlah item baru"""

        # List seluruh item_name
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek nama_item pada list_nama_item
            if nama_item not in list_nama_item:
                print("nama_item belum ada dalam list")
            
            else:
                # Cek tipe data nama_item 
                if type(nama_item) != str:
                    print("nama_item belum mengikuti ketentuan string")
                
                # Cek tipe data update_jumlah_item
                elif type(update_jumlah_item) != int:
                    print("update_jumlah_item belum mengikuti ketentuan integer")
                
                else:
                    # Menyimpan tipe data update_jumlah_item baru
                    self.data.loc[self.data.Item == nama_item, "Quantity"] = update_jumlah_item
                    print(f"Anda telah berhasil mengganti jumlah item {nama_item} menjadi {update_jumlah_item}")

        except ValueError:
            print(f"Item {nama_item} tidak ada dalam riwayat belanja Anda")

            
    def update_item_price(self, nama_item: str, update_harga: float or int):
        """Fungsi memperbaharui harga_item ke dalam dictionary
            nama_item (str): nama item lama
            update_harga (float atau int): harga baru"""
        
        # List seluruh item_name
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek nama_item pada list_nama_item
            if nama_item not in list_nama_item:
                print("nama_item belum ada dalam list")

            else:
                # Cek tipe data nama_item 
                if type(nama_item) != str:
                    print("nama_item belum mengikuti ketentuan string")

                # Cek tipe data nama_item  update_harga
                elif type(update_harga) != float and type(update_harga) != int:
                    print("update_harga belum mengikuti ketentuan integer atau float")

                else:
                    # Menyimpan tipe data update_harga baru
                    self.data.loc[self.data.Item == nama_item, "Price"] = update_harga
                    print(f"Anda telah berhasil mengganti harga item {nama_item} menjadi {update_harga}")

        except ValueError:
            print(f"Item {nama_item} tidak ada dalam riwayat belanja Anda")

            
    def delete_item(self, nama_item: str):
        """Fungsi menghapus item dari dictionary
            nama_item (str): nama_item yang ingin dihapus oleh user"""

        # List seluruh item_name
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek nama_item pada list_nama_item
            if nama_item not in list_nama_item:
                print("nama_item belum ada dalam list")

            else:
                # Cek tipe data nama_item 
                if type(nama_item) != str:
                    print("nama_item belum mengikuti ketentuan string")
                else:
                    # Tampilkan data yang telah dihapus
                    print(f"Anda telah berhasil menghapus item {nama_item} dari transaksi sebelumnya")

                    # Group by nama_item
                    data = self.data.drop(self.data.index[self.data.Item == nama_item],inplace=True,)

                    # Tampilkan table
                    table = tabulate(data, headers="keys", tablefmt="github")

                    return print(table)

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")
            

    def reset_transaction(self):
        """Fungsi menghapus semua item yang ada dalam dictionary"""

        # Tampilkan tabel kosong
        print("Semua item berhasil di delete!")

        # Drop index in attribute class data
        self.data.drop(self.data.index, inplace=True)

        # Create and show table
        table = tabulate(self.data, headers="keys", tablefmt="github")

        return print(table)
    

    def check_order(self):
        """Fungsi mengecek kembali item yang telah diinputkan"""

        # Memanggil data belanjaan
        output_data = self.data.copy()

        # Membuat kolom baru
        output_data["Total_Price"] = (output_data.Quantity * output_data.Price)
        
        # Tampilkan tabel
        table = tabulate(output_data, headers = "keys", tablefmt = "github")

        return print(table)
    

    def total_price(self):
        """Fungsi menghitung total transaksi belanjaan, beserta dengan diskon"""
        
        # Memanggil data belanjaan
        output_data = self.data.copy()
        
        # Membuat kolom baru
        output_data["Total_Price"] = (output_data.Quantity * output_data.Price)
        
        # Membuat variabel total pembayaran
        total = npy.sum(output_data.Total_Price)

        # Diskon 0 persen, jika total belanjaan dibawah sama dengan 200 ribu rupiah
        if total >= 0 and total <= 200_000:
            return print(f"Total pembayaran sebesar Rp.{int(total)}")

        # Diskon 5 persen, jika total belanjaan diatas 200 ribu dan dibawah sama dengan 300 ribu
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 5% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        # Diskon 8 persen, jika total belanjaan diatas 300 ribu dan dibawah sama dengan 500 ribu
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 8% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        # Diskon 10 persen, jika total belanjaan diatas 500 ribu
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 10% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        else:
            return "Total Belanja tidak boleh kurang dari nol"