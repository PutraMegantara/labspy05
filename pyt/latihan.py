a = {'Ari': 6281267888, 'Dina': 6287677776}
print("# Kontak Awal")
print("="*30)
print("     Nama    |  Nomor Telpon  |")
print("="*30)
print("     Ari     |  6281267888", "\n     Dina    |  6287677776")
print("="*30)

# Menampilkan kontak Ari
print("\n# Menampilkan Kontak Ari")
print("="*30)
print("     Nama    |  Nomor Telpon  |")
print("="*30)
print("     Ari     |  ", a['Ari'])
print("="*30)

# Menambah kontak
print("\n# Menambahkan Kontak Riko")
a["Riko"] = "6287654544"
print("="*30)
print("     Nama    |  Nomor Telpon  |")
print("="*30)
print("     Ari     |  ", a['Ari'])
print("     Dina    |  ", a['Dina'])
print("     Riko    |  ", a['Riko'])
print("="*30)

# Mengubah kontak Dina
print("\n# Mengubah Kontak Dina")
a['Dina'] = "6288999776"
print("="*30)
print("     Nama    |  Nomor Telpon  |")
print("="*30)
print("     Ari     |  ", a['Ari'])
print("     Dina    |  ", a['Dina'])
print("     Riko    |  ", a['Riko'])
print("="*30)

# Menampilakn semua nama
print("\n# Menampilkan Semua Nama")
print(a.keys())

# Menampilkan semua nomor
print("\n# Menampilkan Semua Nomor")
print(a.values())

# Menampilkan daftar nama dan nomornya
print("\n# Menampilkan Daftar Nama dan Nomornya")
print(a.items())

# Hapus kontak Dina

print("\n# Menghapus Kontak Dina")
del a["Dina"]
print("="*30)
print("     Nama    |  Nomor Telpon  |")
print("="*30)
print("     Ari     |  ", a['Ari'])
print("     Riko    |  ", a['Riko'])
print("="*30)
