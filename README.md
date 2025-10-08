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


--Tugas 4--
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
 Django AuthenticationForm merupakan form bawaan django yang digunakan untuk proses autentikasi pada saat user login. Form ini menyediakan field username dan password secara otomatis, tanpa harus dibuat kodenya. Kelebihannya yaitu lebih sederhana digunakan karena sudah terintegrasi dengan sistem autentikasi Django, sudah menyediakan validasi bawaan seperti salah password sehingga tidak perlu dibuat manual, dan aman karena menggunakan hash password bawaan Django. Namun form ini memiliki kekurangan yaitu bersifat sangat umum sementara terkadang kustomisasi diperlukan, dan UI yang sangat sederhana sehingga perlu diubah agar tampilannya lebih menarik. 

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
 Autentikasi pada Django merupakan proses verifikasi identitas user, sementara otorisasi merupakan proses menentukan ruang lingkup yang boleh dilakukan user setelah login. Contohnya sekarang user A sedang login sehingga terjadi proses autentikasi yang mengecek username dan password, kemudian otorisasi dari user A hanya membolehkan pengaksesan halaman-halaman tertentu. Pada Django, ada django.contrib.auth yang menangani autentikasi. Sementara untuk otorisasi, Django menggunakan permissions dan group seperti @login_required(login_url='/login') pada tugas dimana akses terhadap tampilan produk hanya dapat dilihat jika user sudah berhasil login.

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
 Session merepresentasikan seri dari HTTP request dan response di antara web browser dan server yang spesifik. Perbedaannya, data cookie disimpan pada sisi klien dan data session disimpan di sisi server. Karena itu, session lebih aman (data sensitif tidak disimpan di klien). Session juga bisa menyimpan data besar, namun data ini bisa membebani server karena butuh penyimpanan. Session juga hilang saat user timeout atau clear session. Sebaliknya, cookies tidak membebani server dan dapat digunakan untuk keperluan "remember me" atau preferensi user. Namun kekurangannya, cookies memiliki kapasitas terbatas (hanya 4KB) dan dapat dimanipulasi oleh user sehingga kurang aman jika tidak dienkripsi.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
 Penggunaan cookies tidak aman secara default dan memiliki risiko potensial. Risiko yang dapat terjadi misalnya penyadapan lewat HTTP. Django menghadapi hal ini melalui penyediaan beberapa setting keamanan cookie, seperti CSRF_COOKIE_TOKEN sebagai token unik untuk verifikasi request, CSRF_COOKIE_HTTPONLY sebagai opsi yang dapat diset sehingga membuat CSRF tidak dapat diakses lewat JavaScript, dan berbagai fungsi lainnya.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Melakukan import UserCreationForm, message, AuthenticationForm, login, dan logout pada views.py.
 2. Menambahkan fungsi register pada views.py untuk menghasilkan formulir registrasi yang otomatis menghasilkan akun user ketika disubmit.
 3. Membuat berkas register.html sebagai tampilan form ketika register.
 4. Menambahkan fungsi login_user ke views.py untuk mengidentifikasi pengguna yang login
 5. Membuat berkas login.html untuk memberi tampilan login ketika web dibuka.
 6. Menambahkan fungsi logout_user pada views.py untuk melakukan logout. Agar dapat logout, tombol Logout ditambahkan pada tampilan main.
 7. Mengimport register, login_user, logout_user ke urls.py dan menambahkan path agar semuanya dapat diakses user.
 8. Mengimport login_required pada views.py dan menambahkan kode @login_required(login_url='/login') di atas fungsi show_main dan show_product sehingga halaman utama nantinya hanya dapat diakses oleh pengguna yang sudah login.
 9. Menambahkan import datetime, reverse, dan HttpResponseRedirect pada views.py dan mengubah beberapa kode: menambahkan kode untuk menyimpan cookie bernama last_login pada fungsi login_user, menambahkan akses cookie dengan request.COOKIES.get('last_login', 'Never') pada context di fungsi show_main, dan mengubah kode logout_user untuk menghapus cookie last_login setelah logout.
 10. Memodifikasi main.html agar menampilkan sesi terakhir login user.
 11. Mengimport user ke models.py sebagai langkah awal dalam menghubungkan models dan user, kemudian menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
 12. Membuat migrasi dan menjalankannya.
 13. Mengubah create_product pada views.py sehingga pengguna yang sedang login terhubung dengan objek yang dibuatnya.
 14. Memodifikasi show_main sehingga dapat melakukan filtering terhadap pembuat produk.
 15. Membuat tombol filter "My" dan "All" pada main.html.
 16. Menambahkan tampilan nama pembuat produk di product_detail.html.
 17. Membuat dua akun pengguna dengan masing-masing 3 dummy data.

--Tugas 5--

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
 1. Inline styles: menyatakan style yang langsung digunakan pada elemen HTML, penggunaannya dengan style="color= #94CEFF". Inline style dianggap kuat karena bisa meng-override perintah lain (kecuali jika memakai !important) dan paling dekat dengan elemen.
 2. ID selector: menggunakan id elemen yang unik per halaman untuk menjalankan selector sehingga lebih dianggap penting daripada class yang bisa dipakai berulang.
 3. Classes selector: selector yang dapat dipakai berkali-kali, contohnya .lead { font-size: 10px; }
 4. Element selector: memungkinkan pengubahan properti untuk semua elemen yang memiliki tag HTML yang sama dengan langsung menunjuk tag HTML tersebut. Dianggap paling lemah karena terlalu umum, bisa berefek pada semua elemen dengan tag HTML yang sama.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
 Responsive design memungkinkan user untuk mendapatkan tampilan web yang menyesuaikan dengan berbagai ukuran layar yang sedang digunakan user tersebut. Konsep ini sangat penting karena user biasanya tidak hanya mengakses web dari pc atau laptop, namun juga dari smartphone masing-masing. Tanpa responsive design, tampilan web yang misalnya hanya dirancang untuk akses pc tidak dapat diakses dengan baik pada smartphone sehingga user experience tidak akan baik. Contoh aplikasi yang sudah menerapkan responsive design yaitu netflix, karena tampilannya pada desktop dan smartphone maupun tablet berbeda, namun tetap memiliki fungsi yang sama. Tampilan aplikasi yang belum menerapkan responsive design akan sama dari berbagai device. Contohnya halaman login SIAK yang terlihat normal ketika diakses dari desktop, namun sangat kecil jika diakses dari hp.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
 Margin merupakan jarak dari suatu elemen dengan elemen lain, border merupakan bingkai yang membungkus elemen-elemen pada web, dan padding merupakan jarak antara konten dan bordernya. Contoh pengimplementasiannya yaitu (misalkan pada file css)
 -box {
    margin: 3px; (jarak antar elemen 3px)
    border: 2px solid #56769C; (garis bingkai dengan tebal 2px dan warna biru)
    padding: 15px; (jarak isi konten ke border)
 }

Jelaskan konsep flex box dan grid layout beserta kegunaannya!
 Flex box digunakan untuk menyusun elemen berukuran satu dimensi, untuk mengaturnya dalam baris atau kolom dengan fleksibel. Contoh flex box yaitu pada navigation bar. Sedikit berbeda dengan ini, grid layout dirancang untuk dua dimensi dan dapat membuat layout yang lebih kompleks, dengan baris dan kolom. Contoh penggunaannya pada galeri foto dimana foto disusun berdasarkan baris dan kolom.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 1. Menambahkan tailwind ke aplikasi football shop, dengan memodifikasi file base.html
 2. Menambahkan fungsi edit_product pada views.py, kemudian membuat file edit_product.html sebagai tampilan ketika mengedit produk. Setelah file selesai, mengimport fungsi edit_product ke urls.py dan menambahkan pathnya.
 3. Menambahkan fungsi delete_product pada views.py, mengimport ke urls.py, dan menambahkan pathnya agar bisa menghapus produk.
 4. Mencoba menambahkan tombol edit dan delete pada main.html dan mengecek apakah program sudah berjalan dengan benar.
 5. Membuat tampilan navigation bar (navbar.html) yang disesuaikan dengan warna yang diinginkan.
 6. Mengonfigurasi static pada aplikasi, seperti menambahkan whitenoise middleware pada settings.py.
 7. Membuat global.css untuk membuat kelas custom, mengikuti tutorial namun dengan warna yang disesuaikan.
 8. Menambahkan global.css ke base.html agar dapat digunakan dalam template Django.
 9. Mengedit tampilan navigation bar agar sesuai dengan yang diinginkan.
 10. Mengedit tampilan login seperti mengubah warna.
 11. Mengedit tampilan register dan menyesuaikan palet warnanya dengan login.
 12. Membuat file card_products.html dan mengeditnya agar dapat menampilkan produk yang dijual dan menyesuaikan tampilannya agar memuat lebih banyak produk dalam satu layar.
 13. Menambahkan no-product.pny sebagai image tampilan jika produk masih kosong.
 14. Memasukkan card_news.html dan no-product.png ke main-html dan mengubah warna tampilan pada main.
 15. Mengedit halaman detail, create, dan edit product agar sesuai dengan palet warna.
 16. Push ke git dan pws.

 -- Tugas 6 --

Apa perbedaan antara synchronous request dan asynchronous request?
 Pada asynchronous request, kita dapat memperbarui sebagian elemen data pada halaman tanpa harus me-reload halaman secara keseluruhan. Pada request ini, proses dijalankan secara paralel sehingga UI lebih interaktif dan tidak lambat. Berbeda dengan synchronous request yang menjalankan proses secara berurutan sehingga UI bisa jadi kurang responsif jika servernya lambat.

Bagaimana AJAX bekerja di Django (alur request–response)?
 Ketika ada sebuah request, JavaScript membuat XMLHttpRequest object yang kemudian mengirimkan request ke server. Server kemudian memproses request dan mengembalikan response ke halaman web. Response ini kemudian dibaca oleh JavaScript dan JavaScript melakukan aksi berikutnya sesuai dengan langkah yang dibuat. AJAX di sini memadukan web dan JavaScript dan HTML DOM. AJAX-lah yang mengirim data dengan menggunakan XML, JSON, ataupun text. AJAX membuat halaman web bisa memperbarui data secara asinkronus.

Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
 AJAX memungkinkan akses yang lebih cepat dan responsif karena tidak perlu mereload seluruh halaman (hanya bagian tertentu saja). AJAX juga memungkinkan user berinteraksi secara realtime sehingga UXnya lebih baik dan hal ini membuat interaktivitas antara server dan user tinggi sehingga cocok untuk fitur-fitur dinamis seperti notifikasi atau live. Karena alasan yang sama juga, AJAX lebih efisien karena dapat mengurangi beban server dengan data yang dikirim lebih kecil.

Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
 Agar menjamin keamanan, dapat digunakan CSRF token. Selain itu, input pada server juga bisa divalidasi sehingga tidak ada input yang membahayakan. Agar data sensitif tidak bisa diakses pihak luar, bisa juga dengan menggunakan HTTPS dan membatasi response.

Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
 Dengan AJAX, navigasi pengguna lebih cepat karena tidak perlu reload manual. Hal ini juga memungkinkan user untuk mendapatkan feedback dengan cepat dan interaksi yang lebih natural dengan server.