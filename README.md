# Laporan Tugas Uas Komputer Grafik - Mohamad Ilman Huda

## Biodata
Nama : Mohamad Ilman huda \
Kelas : 06TPLE007 \
Mata Kuliah : Komputer Grafik 

## Project Overview

Proyek ini merupakan tugas UAS Komputer Grafik yang bertujuan untuk membuat aplikasi web menggunakan Python Flask yang memungkinkan pengguna untuk memotong (crop) gambar dengan posisi dan ukuran sesuai dengan pilihan mereka. Aplikasi ini akan memberikan pengguna antarmuka yang intuitif untuk memilih area yang ingin mereka potong dari gambar dan menyimpannya sebagai gambar terpisah.


## Business Understanding

### Problem Statements

Bagaimana cara memotong sebuah gambar menggunakan web aplikasi yang mana gambar tersebut bisa disesuaikan posisi dan ukuran nya ?

### Goals

membuat website aplikasi untuk memotong sebuah gambar dengan posisi yang kita inginkan dan ukuran yang kita inginkan menggunakan python flask.

## Data Understanding

Variabel-variabel pada icrop_flask adalah sebagai berikut :

- top left : mengambil gambar bagian atas kiri
- top right : mengambil gambar bagian atas kanan
- top center : mengambil gambar bagian atas tengah
- center : mengambil gambar pada posisi tengah
- center left : mengambil gambar pada posisi tengah kiri
- center right : mengambil gambar pada posisi tengah kanan
- bottom center : mengambil gambar pada posisi bawah tengah
- bottom right : mengambil gambar pada posisi bawah kanan
- bottom left : mengambil gambar pada posisi bawah kiri
- size : ukuran dari gambar yang akan di potong
- img/image : variable dari sebuah gambar

## Feature
<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)&nbsp;&nbsp;
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.2.x/)&nbsp;&nbsp;
Bootstrap
Jquery
SweeatAlert

</div>

# Result

Pertama-tama jalankan file python flask nya terlebih dahulu atau bisa akses ke halaman web yang sudah saya deploy ke sini : https://siapaajah256.pythonanywhere.com/

![Halaman Utama](<https://github.com/hudilman/icrop_flask/blob/main/img_md/home.JPG>)

Setelah tertampil halaman utama bisa klik choose file untuk memilih file yang akan diupload, perlu diperhatikan bahwa saya sudah set hanya menerima file jpg,png dan jpeg baik disisi frontend ataupun disisi backend, jadi kalian tidak akan bisa memasukan file selain format yang saya izinkan.
upload file bersifat required yang artinya jika kalian klik simpan tidak akan ada action apapun.

Setelah berhasil mengupload gambar , maka akan tampil halaman seperti berikut :

![success upload](<https://github.com/hudilman/icrop_flask/blob/main/img_md/success%20upload%20gambar.JPG>)

tampilan succcess tersebut saya menggunakan sweeatalert dari js hanya untuk menampilkan pesan berhasil atau gagal.

kemudian pada tahap ini masukan ukuran dan posisi yang kita inginkan untuk memotong gambar yang sudah kita upload sebelumnya.
perlu diingat bahwa kedua input tersebut bersifat required yang artinya tidak boleh kosong dan jika kosong tidak akan bisa melakukan submit.

![Halaman potong gambar](<https://github.com/hudilman/icrop_flask/blob/main/img_md/atur%20gambar%20untuk%20di%20potong.JPG>)

berikut dibawah ini adalah halaman terakhir ketika kita berhasil memotong gambar.

![Output](<https://github.com/hudilman/icrop_flask/blob/main/img_md/output%20potong%20gambar.JPG>)

pastikan bahwa ukuran yang kita masukan tidak melebihi dari ukuran gambar asli agar tidak terjadi error seperti berikut.

![input ukuran terlalu besar](<https://github.com/hudilman/icrop_flask/blob/main/img_md/ukuran%20yang%20di%20input%20terlalu%20besar.JPG>)


# Kesimpulan

Berdasarkan hasil diatas saya berhasil memenuhi harapan untuk membuat aplikasi memotong gambar dengan ukuran dan posisi yang harus diinput sesuai keinginan dari user, dan saya juga sudah membuat validasi pada setiap input yang dimasukan.
aplikasi yang saya buat 100% sudah memenuhi kebutuhan dari tugas uas komputer grafik, adapun aplikasi yang sudah saya deploy bisa di akses di url : https://siapaajah256.pythonanywhere.com/
