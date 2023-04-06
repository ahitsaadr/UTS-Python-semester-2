#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

#Koneksi dari database
dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)
#menyiapkan objek kursor
cursorObject = dataBase.cursor()

#membuat database dengan nama "db_sales_V3922002"
cursorObject.execute("CREATE DATABASE db_sales_V3922002")


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'db_sales_V3922002'
)

cursorObject = dataBase.cursor()

#membuat tabel database sesuai dengan ketentuan yang ada
studentRecord = """CREATE TABLE data_barang (
                    id_barang VARCHAR(20) PRIMARY KEY,
                    nama_barang VARCHAR(20),
                    harga_barang INT,
                    stok_awal INT,
                    barang_masuk INT,
                    barang_keluar INT,
                    stok_akhir INT
                    )"""

cursorObject.execute(studentRecord)

#Disconect dari server
dataBase.close()


# In[1]:


import mysql.connector

#Koneksi ke database
dataBase = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'db_sales_V3922002'
)

cursorObject = dataBase.cursor()

#Fungsi untuk menambahkan data ke tabel
def insert_data( id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir ):
    sql = "INSERT INTO data_barang (id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)
    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")

#Fungsi untuk menampilkan data dari tabel
def show_data():
    query = "SELECT * FROM data_barang"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")

#Fungsi untuk mengupdate data di tabel
def update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir):
    sql = "UPDATE data_barang SET nama_barang = %s, harga_barang = %s, stok_awal = %s, barang_masuk = %s, barang_keluar = %s, stok_akhir = %s WHERE id_barang = %s"
    val = (nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir, id_barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

#Fungsi untuk menghapus data dari tabel
def delete_data(Id_Barang):
    sql = "DELETE FROM data_barang WHERE id_barang = %s"
    val = (id_barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")

#Fungsi untuk mencari data berdasarkan Id_Barang
def search_data(id_barang):
    sql = "SELECT * FROM data_barang WHERE id_barang = %s"
    val = (id_barang,)
    
    cursorObject.execute(sql, val)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil dicari")

#Script untuk pilihan menu
while True:
    print(" ")
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Keluar")
    print("-------------------")
    menu = input("Pilih menu> ") #input untuk pilihan menu yang akan dicari
    print(" ")

    #pilihan 1 "insert data"
    if menu == "1":
        id_barang = input("Masukkan id barang : ")
        nama_barang = input("Masukkan nama barang : ")
        harga_barang = int(input("Masukkan harga barang : "))
        stok_awal = int(input("Masukkan stok awal : "))
        barang_masuk = int(input("Masukkan barang masuk : "))
        barang_keluar = int(input("Masukkan barang keluar : "))
        
        #Rumus untuk mencari stok_akhir
        stok_akhir = stok_awal + barang_masuk - barang_keluar
        
        #mencetak Stok_Akhir dari rumus sebelumnya
        print("stok akhir : ", stok_akhir)
        
        insert_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)
    
    #pilihan 2 "show data"
    elif menu == "2":
        show_data()

    #pilihan 3 "update data"
    elif menu == "3":
        id_barang = input("Masukkan id barang yang akan diupdate : ")
        nama_barang = input("Masukkan nama barang baru : ")
        harga_barang = int(input("Masukkan harga barang baru : "))
        stok_awal = int(input("Masukkan stok awal baru : "))
        barang_masuk = int(input("Masukkan barang masuk baru : "))
        barang_keluar = int(input("Masukkan barang keluar baru : "))
        
        stok_akhir = stok_awal + barang_masuk - barang_keluar
        print("stok akhir setelah diupdate : ", stok_akhir)
        
        update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)

    #pilihan 4 "hapus data"
    elif menu == "4":
        id_barang = input("Masukkan id barang yang ingin dihapus : ")
        
        delete_data(id_barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        id_barang = input("Masukkan id barang yang ingin dicari : ")
        
        search_data(id_barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Terima kasih sudah menggunakan program kami, SEE U NEXT TIME ;)")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilihan anda tidak valid, Mohon coba lagi dan pilihlah dengan benar")


# In[ ]:




