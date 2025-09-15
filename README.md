link PWS: https://msy-aulya-garudaeleven.pbp.cs.ui.ac.id

--Tugas 2--
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Membuat repositori garuda-eleven (nama dari football-shop), membuat dan menjalankan virtual environment.
 2. Proyek django dibuat dengan bantuan file requirements.txt yang berisi dependensi yang dibutuhkan. Dependensi ini diinstal dan proyek django bernama garuda_eleven dibuat.
 3. Membuat file .env dan .env.prod, menyesuaikan isinya dengan kredensial agar proyek dapat dideploy di PWS. Kemudian file settings.py dimodifikasi.
 4. Mengunggah ke repositori github dan membuat berkas .gitignore untuk menyaring berkas serta direktori yang harus diabaikan git.
 5. Membuat project di PWS dan push django project ke PWS. Pada langkah ini, URL deployment PWS ditambahkan pada allowed host pada file settings.py sehingga proyek bisa diakses melalui URL PWS.
 6. Membuat aplikasi main di dalam garuda-eleven. 'main' ditambahkan ke daftar installed_apps di file settings.py untuk mendaftarkan aplikasi main ke project django.
 7. Membuat direktori templates dalam aplikasi main, lalu membuat main.html yang akan menjadi tampilan pada PWS. Template pada file ini menyesuaikan ketentuan tugas, yaitu untuk menampilkan nama aplikasi, nama, dan kelas.
 8. Ketika membuat aplikasi main, ada file models.py. File ini diisi dengan class Product yang memiliki atribut name, price, description, thumbnail, category, is_featured, dan stock sesuai tipe masing-masing. Setelah melakukan perubahan, membuat dan menerapkan migrasi model agar perubahan tercatat di basis data.
 9. Menambahkan fungsi show_main pada file views.py dengan context nama aplikasi, nama, dan kelas untuk ditampilkan di web.
 10. File urls.py pada aplikasi main diisi dengan kode dan path yang bisa dieksekusi dan dipetakan ke views.py, pada tugas ini yaitu path('', show_main, name='show_main').
 11. Menambahkan path yang sama ke file urls.py pada direktori garuda-eleven, dengan import include dan langsung menambahkan pathnya dengan path('', include('main.urls')).
 12. Push kembali ke repository.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](https://github.com/slsbilaap/garuda-eleven/blob/master/Django.png?raw=true)
 Proses dimulai dengan adanya request HTTPS dari user. Request ini diterima oleh urls.py yang kemudian memetakan path ke views.py sebagai petunjuk path yang diinginkan. Selanjutnya views.py menjembatani models.py dan template html. File views.py mengembalikan template yang relevan berdasarkan permintaan, sesuai dengan data dari model. Model dalam file models.py terhubung ke database dan fungsinya adalah sebagai data yang ingin ditampilkan. Setelah proses ini, user mendapatkan tampilan yang diinginkan dengan data yang sesuai.

Jelaskan peran settings.py dalam proyek Django!
 Seperti peran setting pada perangkat lainnya, settings.py dalam proyek Django juga merupakan pusat konfigurasi. File ini menjaga keamanan proyek, seperti adanya kode mengenai secret key. Konfigurasi database dan juga daftar aplikasi juga berada dalam file ini. Dengan adanya hal tersebut, proyek dapat dijalankan dengan tampilan aplikasi sesuai data. Di dalam settings.py juga terdapat internasionalisasi yang mengatur bahasa dan zona waktu. Dapat disimpulkan bahwa settings.py mengatur berbagai aspek penting sehingga kode lain dapat terintegrasi dan proyek dapat berjalan dengan baik.

Bagaimana cara kerja migrasi database di Django?
 Database di Django perlu selalu menyesuaikan dengan model. Setelah adanya perubahan di file models.py, pembuatan migrasi dilakukan agar Django bisa membaca perubahan pada model. Migrasi ini berisi instruksi untuk mengubah database sehingga ketika diterapkan, Django mengubah atau menambahkan perubahan ke database. Dengan begitu, data yang ada selalu tersinkronisasi.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
 Django menggunakan bahasa Python yang cukup mudah dipahami dan digunakan. Selain itu, Django juga memiliki banyak fitur bawaan sehingga lebih mudah digunakan daripada framework lain. Pengguna Django juga banyak, sehingga dokumentasi lebih mudah ditemukan. Hal ini sangat membantu pembelajaran.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
 Asisten dosen sudah sangat membantu. Sayangnya saya awalnya tidak mengetahui bahwa ada discord bagi masing-masing asdos di kelas dan baru join di pertengahan waktu pengerjaan tutorial, di mana pada waktu tersebut saya sudah menyelesaikan tutorial.

--Tugas 3--
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 Platform biasanya melibatkan frontend, backend, hingga database. Agar semua bagian ini bisa terhubung dan bertukar informasi, maka data delivery dibutuhkan. Secara sederhana data delivery diperlukan agar request yang masuk bisa dikembalikan sesuai yang diinginkan karena data sudah terintegrasi. Data delivery ini memungkinkan user untuk mengakses objek dalam format XML atau JSON (pada tugas kali ini).

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 JSON lebih baik karena memiliki keunggulan di beberapa aspek penting dibandingkan XML. JSON juga lebih populer karena keunggulan ini. Sintaks JSON lebih padat dan mudah dibaca-tulis, dokumentasi skemanya juga sederhana dan lebih fleksibel dibandingkan XML. Selain itu, JSON memiliki ukuran file yang lebih kecil sehingga membutuhkan lebih sedikit memori dan transmisi data yang lebih cepat. Meskipun begitu, XML cocok untuk data yang kompleks dan memerlukan fitur yang lebih canggih dari JSON.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 Method is_valid() memiliki peran untuk mengecek informasi yang dimasukkan pada form dan mengonfirmasinya. Contohnya pada stok produk yang harus bernilai positif, is_valid() membuat user tidak bisa memasukkan stok negatif. Method ini memastikan data yang masuk sesuai aturan (dalam hal ini ditetapkan pada models.py).

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 csrf_token merupakan kode unik yang dihasilkan server setiap sesi user. Kode ini diperlukan sebagai lapisan keamanan untuk mencegah Cross-Site request Forgery (CSRF), yaitu penyerang mengirim request palsu dengan menyamar sebagai user. Penyerang bisa menyisipkan kode berbahaya yang berakibat pada pencurian data atau perubahan password. csrf_token dibuat untuk melindungi user dari kerugian ini seperti ketika user mengirim request, request tersebut dicocokkan dengan token unik pada sesi tersebut. Apabila tidak cocok, maka request ditolak sehingga pihak penyerang tidak dapat mengirim request palsu.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Membuat file base.html sebagai template dasar untuk web.
 2. Menambahkan template base.html ke settings.py sehingga template bisa dibaca.
 3. Membuat file forms.py pada main untuk menentukan informasi yang harus diisi ketika menambahkan produk baru.
 4. Menambahkan import form ke views.py dan membuat fungsi untuk menambah produk setelah mengisi form, serta menampilkan produk.
 5. Mengimport fungsi dari views.py ke urls.py dan menambahkan path yang sesuai agar bisa diakses.
 6. Memodifikasi template main.html untuk menambah tombol add product, kemudian template untuk menampilkan produk yang ada. Pada bagian bawah juga ditempatkan tombol untuk melihat detail produk.
 7. Membuat file create_product.html dan product_detail.html yang masing-masing berfungsi sebagai template tampilan web ketika menambahkan produk dan ketika membuka detail produk. Kedua template ini ditampilkan ketika menekan tombol Add Product atau View Details.
 8. Mengimport HttpResponse dan Serializer pada views.py agar user bisa mendapat respon berupa format XML dan JSON.
 9. Membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py yang menerima parameter request agar mengembalikannya dalam format XML atau JSON. Fungsi show by id menerima parameter id dan mengembalikan tampilan XML atau JSON berdasarkan id produk yang diminta. Semua fungsi memiliki variabel yang menyimpan hasil query dari Product dan mengembalikannya sesuai request.
 10. Import keempat fungsi yang dibuat ke urls.py, kemudian membuat path untuk masing-masing fungsi agar dapat diakses.
 11. Melakukan add, commit, dan push ke github dan pws.

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
 Mungkin lebih responsif saja, namun saya melihat bahwa asdos sudah banyak membantu pada waktu tutorial.

Screenshoot hasil akses URL pada Postman
![alt text](https://github.com/slsbilaap/garuda-eleven/blob/master/xml_json.jpg?raw=true)
