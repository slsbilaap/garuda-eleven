link PWS: https://msy-aulya-garudaeleven.pbp.cs.ui.ac.id

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Membuat repositori garuda-eleven (nama dari football-shop) dan membuat serta menjalankan virtual environment.
 2. Proyek django dibuat dengan bantuan file requirements.txt yang berisi dependensi yang dibutuhkan. Dependensi ini diinstal dan proyek django bernama garuda_eleven dibuat dengan perintah "django-admin startproject football_news ."
 3. Membuat file .env dan .env.prod, menyesuaikan isinya dengan kredensial agar proyek dapat dideploy di PWS.
 4. Memodifikasi settings.py seperti menambahkan allowed host agar dapat diakses local host dan memodifikasi bagian database agar sesuai dengan kredensial.
 5. 


Membuat sebuah proyek Django baru. >>
 Membuat aplikasi dengan nama main pada proyek tersebut.
 Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
 Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
thumbnail sebagai gambar item dengan tipe URLField.
category sebagai kategori item dengan tipe CharField.
is_featured sebagai status unggulan item dengan tipe BooleanField.
 Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
 Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
 Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.



Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


Jelaskan peran settings.py dalam proyek Django!


Bagaimana cara kerja migrasi database di Django?


Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?


Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Asisten dosen sudah sangat membantu. Sayangnya saya awalnya tidak mengetahui bahwa ada discord untuk masing-masing asdos di kelas dan baru join di pertengahan waktu pengerjaan tutorial, di mana pada waktu tersebut saya sudah menyelesaikan tutorial.
