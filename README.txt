Tugas Kriptografi
Proyek ini merupakan implementasi dari algoritma kriptografi Vigenère, Playfair, dan Hill Cipher. Program ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi pesan baik dari input langsung maupun dari file teks.

Folder proyek terdiri dari empat file:
- main.py: File utama yang mengelola tampilan antarmuka dan interaksi pengguna.
- vigenere.py: Implementasi algoritma Vigenère.
- playfair.py: Implementasi algoritma Playfair.
- hill.py: Implementasi algoritma Hill Cipher.
- index.html: Untuk tampilan pada website

Cara Penggunaan
1. Persyaratan:
   - Python 3.x
   - Library numpy (untuk operasi matriks)
   Install library numpy dengan perintah:
   pip install nump

2. Menjalankan Program:
   - Jalankan file main.py untuk memulai aplikasi.
   - Pilih jenis cipher (Vigenère, Playfair, Hill) dan pilih tindakan (enkripsi atau dekripsi).
   - Masukkan pesan dan kunci sesuai yang diminta.

3. Format Kunci:
   - Kunci harus memiliki panjang minimal 12 karakter untuk algoritma Playfair dan Vigenere
   - Untuk Hill cipher, 9 karakter pertama HARUS menggunakan KRIPTOUNNAIK untuk key nya, sisanya bisa random

4. Input:
   - Pesan dapat diinput langsung melalui keyboard atau diambil dari file teks dengan format .txt.
  
Penjelasan Algoritma
1. Vigenere Cipher
Vigenere Cipher adalah teknik enkripsi dasar yang memanfaatkan kunci untuk menggeser huruf-huruf dalam pesan. Setiap huruf diubah berdasarkan posisi huruf dalam kunci.

2. Playfair Cipher
Playfair Cipher merupakan metode kriptografi yang memakai matriks 5x5 dari huruf-huruf. Proses enkripsi dilakukan dengan memadukan huruf-huruf dalam pasangan, yang hasilnya bergantung pada posisi masing-masing huruf dalam matriks.

3. Hill Cipher
Hill Cipher melibatkan penggunaan matriks untuk mengamankan pesan. Kunci disusun dalam bentuk matriks 3x3, sedangkan pesan diubah menjadi vektor, kemudian diproses melalui operasi matriks menggunakan kunci tersebut.
