# labspy05

### Latihan 1
  - Buat Dictionary daftar kontak
  - Tampilkan kontak Ari
  - Tambah kontak baru dengan nama Riko, nomor 627654544
  - Ubah kontak Dina dengan nomor baru 6288999776
  - Tampilkan semua nama
  - Tampilkan semua nomor
  - Tampilkan daftar nama dan nomornya
  - hapus kontak Dina
 
  ### Program
   ![Screenshot (67)](https://user-images.githubusercontent.com/92736847/144781179-82e4cf6f-a119-4b12-9c70-fbed072cd48d.png)
    
   ![Screenshot (68)](https://user-images.githubusercontent.com/92736847/144781193-6c091d97-db7e-47a3-9481-1ca2a59a5633.png)
   
### Penjelasan
- Kontak Awal
```bash
a = {'Ari': 6281267888, 'Dina': 6287677776}
```

- Untuk menampilkan kontak Ari dapat menggunakan 
```bash
a['Ari']
```

- Kemudian untuk menambahkan kontak Riko dengan nomor 628765454 dapat menggunakan
```bash
a["Riko"] = "6287654544"'
```

- Sedangkan untuk mengubah kontak dapat menggunakan 
```bash
a['Dina'] = "6288999776"
```

- Untuk menampilkan semua nama dapat menggunakan 
```bash
print(a.keys())
```

- Sedangkan untuk menampilkan nomor dapat menggunakan 
```bash
print(a.values())
```

- Kemudian untuk menampilkan nama dan nomor dapat menggunakan 
```bash
print(a.items())
```


- Untuk menghapus kontak Dina dapat menggunakan 
```bash
del a["Dina"]
```

### Output
![Screenshot (69)](https://user-images.githubusercontent.com/92736847/144781599-9e6d4abe-9c18-4569-b3aa-583b134b4a46.png)

### Tugas Praktikum
-Buat program sederhana yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan
- Program dibuat dengan menggunakan *Dictionary*
- Tampilkan menu pilihan : (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data)
- Nilai akhir diambil dari perhitungan 3 komponen nilai (tugas 30%, uts 35%, uas 35%)
- Buatlah flowchart dan penjelasan programnya pada README.md
- Commit dan push repository ke github

### Program
![Screenshot (70)](https://user-images.githubusercontent.com/92736847/144782064-82d89d65-5a95-4558-9714-0e8ebe7bc659.png)
![Screenshot (71)](https://user-images.githubusercontent.com/92736847/144782077-30646ffb-a565-4a0a-ab74-4698f7fb4bbf.png)


### Penjelasan
- Buatlah dictionary yang akan diinput dengan data
```bash
data = {}
```

- Membuat perulangan dan keterangan untuk pilihan menu
```bash
while True:
    c = input("\n(L)ihat, (T)ambah, (U)bah), (H)apus, (C)ari, (K)eluar: ")
```

- Menambahkan data yang akan diinput kemudian masuk ke dalam dictionary
```bash
if c.lower() == 't':
        print("Tambah Data")
        nama = input("Nama\t\t: ")
        nim = int(input("NIM\t\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        akhir = tugas*30/100 + uts*35/100 + uas*35/100
        data[nama] = nim, uts, uas, tugas, akhir
```

- Jika ingin menampilkan data dapat menggunakan
```bash
elif c.lower() == 'l':
        if data.items():
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for z in data.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)
        else:
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)
```

- Mengubah data dapat menggunakan 
```bash
elif c.lower() == 'u':
        print("Ubah Data")
        nama = input("Masukkan Nama   : ")
        if nama in data.keys():
            nim = int(input("NIM\t\t: "))
            uts = int(input("Nilai UTS\t: "))
            uas = int(input("Nilai UAS\t: "))
            tugas = int(input("Nilai Tugas\t: "))
            akhir = tugas*30/100 + uts*35/100 + uas*35/100
            data[nama] = nim, uts, uas, tugas, akhir
        else:
            print("Nama {0} tidak ditemukan".format(nama))
```

- Menghapus data dapat menggunakan
```py
elif c.lower() == 'h':
        print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
```

- Mencari data dapat menggunakan
```bash
 elif c.lower() == 'c':
        print("Cari Data[case-sensitive]")
        nama = input("Masukkan Nama : ")
        if nama in data.keys():
            print("="*73)
            print("|                             Daftar Mahasiswa                          |")
            print("="*73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*73)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, uts, uas, tugas, akhir))
            print("="*73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
```

- Jika sudah selesai input pilih menu 'K' untuk memberhentikan program
```bash
elif c. lower() == 'k':
        break
```
### Output




