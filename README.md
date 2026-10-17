# Pertemuan 07 Fungsi Python

**Nama:** Siti Auliyaatunnisaa  
**NIM:** 2225250085  
**Kelas:** 3A

## Tujuan

Mempelajari penggunaan fungsi, parameter, nilai balik (*return value*), dan ruang lingkup variabel (*scope*) untuk membuat program Python yang modular dan mudah dipahami.

## Cara Menjalankan

Jalankan program utama melalui terminal VS Code:

```bash
python praktik/utilitas_matematika.py
```

Untuk menjalankan latihan secara terpisah, gunakan perintah berikut:

```bash
python latihan/latihan_1_salam.py
python latihan/latihan_2_luas.py
python latihan/latihan_3_jumlah_n.py
python latihan/latihan_4_statistik.py
python latihan/latihan_5_scope.py
```

## Struktur Fungsi

1. `salam(nama, kelas)` menampilkan salam beserta nama dan kelas.
2. `luas_persegi_panjang(p, l)` menghitung dan mengembalikan luas persegi panjang.
3. `jumlah_n(n)` menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan.
4. `statistik(data)` mengembalikan nilai minimum, maksimum, dan rata-rata.
5. `demo(x)` memperlihatkan perbedaan variabel lokal dan global.
6. `luas_segitiga(a, t)` menghitung dan mengembalikan luas segitiga.
7. `faktorial(n)` menghitung faktorial menggunakan perulangan.
8. `tampilkan_menu()` menampilkan pilihan operasi matematika.
9. `baca_bilangan_bulat(pesan)` membaca dan memvalidasi bilangan bulat nonnegatif.
10. `main()` mengatur menu, input pengguna, pemanggilan fungsi, dan keluaran program.

## Hasil Pengujian

| Operasi | Input | Hasil yang Diharapkan | Status |
|---|---|---|---|
| Luas persegi panjang | p=8, l=5 | 40 | Sesuai jika lolos pengujian |
| Luas segitiga | a=10, t=6 | 30.0 | Sesuai jika lolos pengujian |
| Jumlah 1 sampai n | n=10 | 55 | Sesuai jika lolos pengujian |
| Faktorial | n=5 | 120 | Sesuai jika lolos pengujian |
| Faktorial | n=0 | 1 | Sesuai jika lolos pengujian |

## Refleksi

Setelah program dibagi menjadi beberapa fungsi, kode menjadi lebih terstruktur dan mudah dipahami. Setiap fungsi memiliki tanggung jawab yang jelas sehingga perhitungan dapat diuji secara terpisah dan digunakan kembali tanpa menuliskan rumus yang sama berulang kali.