# Laporan Proyek Machine Learning - Andi Shafira Dyah Kurniasari

## Abstrak

Proyek ini berfokus pada pembangunan dan evaluasi sistem rekomendasi
film menggunakan dataset **MovieLens 100k**. Metodologi yang diterapkan
adalah pendekatan hibrida, yang menggabungkan keunggulan dari model
Content-based Filtering dan Collaborative Filtering. Model Content-based
memanfaatkan metadata film seperti genre untuk merekomendasikan item
serupa, sementara model Collaborative menganalisis pola perilaku
pengguna (riwayat rating) untuk menemukan preferensi tersembunyi.

Pengujian model dilakukan dengan metrik **Root Mean Squared Error
(RMSE)** untuk akurasi prediksi serta **Precision@k** dan **Recall@k**
untuk mengukur relevansi rekomendasi teratas. Laporan ini merinci setiap
tahapan, mulai dari pemuatan data, eksplorasi, pembangunan model, hingga
analisis hasil dan implikasi bisnis.

------------------------------------------------------------------------

## 1. Pendahuluan

Sistem rekomendasi adalah alat vital dalam platform digital modern,
dirancang untuk mempersonalisasi pengalaman pengguna dan meningkatkan
interaksi. Tanpa sistem ini, pengguna seringkali merasa kesulitan
menemukan konten yang relevan di tengah banjirnya pilihan, yang dapat
menyebabkan penurunan retensi.

Proyek ini bertujuan membangun sistem rekomendasi yang cerdas dan
efisien, yang tidak hanya akurat tetapi juga mampu memberikan
rekomendasi yang beragam dan menarik.

------------------------------------------------------------------------

## 2. Project Overview

Sistem rekomendasi telah menjadi komponen penting dalam berbagai
platform digital, khususnya di bidang hiburan seperti layanan film dan
musik. Tanpa sistem ini, pengguna kerap kesulitan menemukan konten yang
relevan di antara banyaknya pilihan. Hal tersebut berisiko menurunkan
retensi pengguna dan mengurangi tingkat kepuasan mereka.

Proyek ini berfokus pada pembangunan dan evaluasi sistem rekomendasi
film menggunakan dataset **MovieLens 100k**. Sistem rekomendasi yang
dikembangkan bertujuan untuk mempersonalisasi pengalaman pengguna dengan
memberikan rekomendasi film yang relevan, akurat, dan menarik.

**Mengapa proyek ini penting?**
- Platform berbasis konten (seperti Netflix, Disney+, atau Spotify untuk
musik) telah membuktikan bahwa sistem rekomendasi dapat meningkatkan
engagement hingga 60--70% dari konsumsi pengguna.
- Rekomendasi yang tepat sasaran tidak hanya meningkatkan kepuasan
pengguna, tetapi juga berkontribusi pada retensi pelanggan jangka
panjang.

**Referensi terkait**:
- Ricci, F., Rokach, L., & Shapira, B. (2015). *Recommender Systems
Handbook*. Springer. (https://www.researchgate.net/publication/227268858_Recommender_Systems_Handbook)
- Gómez-Uribe, C. A., & Hunt, N. (2016). *The Netflix Recommender
System: Algorithms, Business Value, and Innovation*. ACM Transactions on
Management Information Systems. (https://dl.acm.org/doi/10.1145/2843948)

------------------------------------------------------------------------

## 3. Business Understanding

### Problem Statements

1.  Bagaimana membangun sistem rekomendasi yang mampu memberikan
    rekomendasi film yang relevan berdasarkan preferensi pengguna?
2.  Bagaimana meminimalkan masalah *cold-start* ketika pengguna memiliki
    riwayat interaksi yang terbatas?
3.  Bagaimana meningkatkan akurasi prediksi rating sekaligus menjaga
    keberagaman rekomendasi?

### Goals

Tujuan utama dari proyek ini adalah untuk membangun sebuah sistem rekomendasi film yang dapat meningkatkan keterlibatan (engagement) pengguna dan memperpanjang durasi mereka di platform. Saya ingin menyediakan rekomendasi yang sangat personal dan akurat, yang terasa seperti kurasi dari seorang ahli film. berikut adalah poin detail dari tujuan teknis project ini: 

1.  Mengembangkan sistem rekomendasi hibrida (Content-based +
    Collaborative Filtering) yang dapat menghasilkan daftar rekomendasi
    film yang relevan.
2.  Menyediakan top-N recommendation sebagai output yang dapat
    dievaluasi berdasarkan metrik standar.
3.  Mengevaluasi performa sistem rekomendasi menggunakan metrik RMSE,
    Precision@k, dan Recall@k.

**Manfaat langsung** dari pencapaian tujuan ini adalah: 

* Peningkatan Retensi Pengguna: Pengguna yang merasa platform memahami selera mereka cenderung akan kembali lagi dan tidak beralih ke layanan lain.

* Optimalisasi Konten: Wawasan dari model dapat membantu tim konten dalam mengambil keputusan yang didukung data tentang film apa yang harus ditambahkan ke katalog.

* Peluang Monetisasi: Durasi tontonan yang lebih lama dan tingkat kunjungan yang lebih sering membuka peluang untuk pendapatan dari iklan atau peningkatan langganan.

### Solution Approach

Untuk mencapai tujuan, dua pendekatan utama sistem rekomendasi
digunakan:
- **Content-based Filtering**: Mengandalkan metadata film (genre) dan
menghitung kemiripan menggunakan teknik vektorisasi (TF-IDF) serta
Cosine Similarity.
- **Collaborative Filtering**: Menggunakan teknik *matrix factorization*
(SVD, Neural Matrix Factorization) untuk menemukan pola preferensi
pengguna tersembunyi.
- **Hybrid Re-ranking Strategy**: Mengombinasikan hasil prediksi dari
kedua pendekatan di atas dengan bobot tertentu untuk menghasilkan
rekomendasi yang lebih relevan.

------------------------------------------------------------------------

## 4. Data Understanding

Dataset yang digunakan adalah **MovieLens 100k**, tersedia di [GroupLens
Research](https://grouplens.org/datasets/movielens/100k/).

Dataset terdiri dari 4 file csv yaitu ratings.csv, movies.csv, tags.csv dan link.csv

### 4.1 Ratings.csv

-   **Jumlah data**: 100.000 baris × 4 kolom.
-   **Isi data**: Berisi semua rating yang diberikan pengguna terhadap film.
-   **Kondisi data**: Tidak ditemukan missing value, tidak ada
    duplikasi.
-   **Fitur**:
    -   `userId`: ID unik pengguna.
    -   `movieId`: ID unik film.
    -   `rating`: Skor penilaian dalam skala 0.5 – 5.0 (dengan kelipatan 0.5).
    -   `timestamp`: Waktu pemberian rating (dalam detik sejak 1 Januari 1970, UTC).
-   **Fungsi**: Data utama untuk collaborative filtering, karena merepresentasikan interaksi antara pengguna dan item (film).

### 4.2 Movies.csv

-   **Jumlah data**: 1.682 baris × 3 kolom.
-   **Isi data**: Informasi tentang film.
-   **Kondisi data**: tidak ditemukan missing value.
-   **Fitur**:
    -   `movieId`: ID unik film.
    -   `title`: judul film (biasanya diikuti dengan tahun rilis, misalnya “Toy Story (1995)”).
    -   `genres`: daftar genre film, dipisahkan dengan tanda | (contoh: “Adventure|Animation|Children|Comedy|Fantasy”.
-   **Fungsi**: Sumber utama untuk Content-based Filtering, karena menyediakan metadata (genre) untuk menghitung kesamaan antar film

### 4.3 Tags.csv

-   **Jumlah data**: 3.689 baris × 4 kolom.
-   **Isi data**: Berisi semua tag (kata kunci/label) yang diberikan pengguna pada film.
-   **Kondisi data**: Terdapat missing value pada kolom `tag`.
-   **Fitur**:
    -   `userId`: ID unik pengguna.
    -   `movieId`: ID unik film.
    -   `tag`: Kata kunci atau frasa pendek yang menggambarkan film (misalnya “thrilling”, “Pixar”).
    -   `timestamp`: Waktu pemberian tag.
-   **Fungsi**: Menambahkan metadata buatan pengguna yang bisa digunakan untuk meningkatkan sistem rekomendasi berbasis konten.
  
### 4.4 Links.csv

-   **Jumlah data**: 1.682 baris × 3 kolom.
-   **Isi data**: Tautan penghubung ke sumber data eksternal film.
-   **Kondisi data**: tidak ditemukan missing value.
-   **Fitur**:
    -   `movieId`: ID film dalam sistem MovieLens.
    -   `imdbId`: ID film dalam IMDb (Internet Movie Database).
    -   `tmdbId`: ID film dalam TMDb (The Movie Database).

**Insight EDA**:
- Distribusi rating condong ke nilai 3 & 4.
- Genre populer: Drama, Comedy, Action.
- Dataset cukup sparse karena sebagian besar pengguna hanya menilai
sebagian kecil film.

------------------------------------------------------------------------

## 5. Data Preparation

Tahapan data preparation yang dilakukan secara runtut:
1. **Pengumpulan dan Eksplorasi Data** : Langkah awal dalam proyek ini adalah mengumpulkan dan memahami data yang akan digunakan.
   - **Akuisisi Data**: Dataset diunduh dari repositori GitHub, yang berisi empat file CSV: movies, ratings, tags, dan links.
   - **Eksplorasi Awal**: Saya melakukan analisis data eksplorasi (EDA) untuk memahami struktur data. Kami menemukan bahwa dataset film berisi 9.742 judul film dan dataset rating berisi 100.836 rating dari pengguna. Analisis genre menunjukkan bahwa Drama dan Komedi adalah genre yang paling umum.

2. **Persiapan Data** : Data mentah kemudian diproses agar siap digunakan untuk pelatihan model.
   - **Penggabungan Data**: Tabel ratings dan movies digabungkan menjadi satu tabel utama. Ini memungkinkan kami untuk menghubungkan setiap rating dengan judul film dan genrenya secara langsung.
   - **Pembagian Data**: Data yang telah digabungkan kemudian dibagi menjadi dua set: 80% untuk data latih (training) dan 20% untuk data uji (testing). Langkah ini penting untuk memastikan model dievaluasi pada data yang belum pernah dilihat sebelumnya.
  
3. **Pengembangan Model Hibrida** : Mengembangkan dua jenis model yang kemudian digabungkan menjadi satu sistem hibrida.
   - **Collaborative Filtering**: Kami menggunakan library FastAI untuk membangun model ini. Model dilatih untuk mempelajari pola tersembunyi dari interaksi antara pengguna dan film, memungkinkannya memberikan rekomendasi yang tak terduga (serendipitous).

   - **Content-Based Filtering**: Model ini dibangun menggunakan TF-IDF Vectorizer dan Cosine Similarity dari library Scikit-learn. Model ini bekerja dengan cara mengubah genre film menjadi vektor numerik dan merekomendasikan film berdasarkan kemiripan genrenya. Ini sangat efektif untuk mengatasi masalah cold-start (pengguna baru tanpa riwayat rating).

   - **Penggabungan Hibrida**: Kedua model digabungkan dengan cara memberi bobot pada hasil prediksi masing-masing. Skor akhir dihitung dengan menggabungkan prediksi rating dari collaborative filtering dengan skor kemiripan genre dari content-based filtering.
   
4. **Evaluasi dan Hasil Kinerja**: model diukur menggunakan metrik standar industri pada data uji.
   - **Metrik Evaluasi**: Menggunakan Precision@10 dan Recall@10 untuk mengevaluasi 10 rekomendasi teratas yang dihasilkan model.

   - **Hasil**: Hasil evaluasi menunjukkan kinerja model yang masih perlu ditingkatkan. Rata-rata Precision@10 adalah 0.0380, dan Recall@10 adalah 0.0285. Ini berarti, dari 10 film yang direkomendasikan, sangat sedikit yang benar-benar relevan bagi pengguna.

5. **Kesimpulan dan Strategi Bisnis**: Meskipun alur kerja rekomendasi berhasil dibangun, hasil evaluasi menunjukkan perlunya optimisasi lebih lanjut. Sistem hibrida ini memiliki potensi bisnis yang signifikan.

6. **Pembuatan Laporan**

------------------------------------------------------------------------

## 6. Metodologi / Modeling and Result

### 6.1 Content-based Filtering
Pendekatan Content-based Filtering merekomendasikan item dengan menganalisis atribut atau fitur intrinsiknya. Dalam konteks proyek ini, sistem merekomendasikan film berdasarkan kesamaan pada fitur utamanya, yaitu genre. Prinsip fundamentalnya adalah bahwa seorang pengguna yang menyukai suatu film akan cenderung menyukai film lain yang memiliki atribut serupa. Keunggulan utama dari metode ini adalah kemampuannya untuk menghasilkan rekomendasi yang relevan tanpa bergantung pada data historis dari pengguna lain, sehingga efektif mengatasi masalah cold-start.

**Cara Kerja dan Teknik Implementasi**
Untuk dapat membandingkan properti antar film, data tekstual genres perlu ditransformasi menjadi representasi numerik yang dapat diproses secara komputasional. Proses ini diimplementasikan melalui dua tahapan teknis utama:

1. **Vektorisasi Fitur Menggunakan TF-IDF**
Teknik TF-IDF (Term Frequency-Inverse Document Frequency) diterapkan untuk mengonversi data genre menjadi vektor fitur numerik.
- Term Frequency (TF): Mengukur frekuensi kemunculan sebuah istilah (dalam hal ini, genre) dalam sebuah dokumen (daftar genre untuk satu film).

- Inverse Document Frequency (IDF): Memberikan bobot pada setiap genre berdasarkan kelangkaannya di seluruh koleksi film. Genre yang lebih jarang muncul (misalnya, "Film-Noir") akan menerima bobot yang lebih tinggi karena dianggap lebih signifikan sebagai penanda kemiripan. Sebaliknya, genre yang sangat umum (misalnya, "Drama") akan menerima bobot yang lebih rendah.

Melalui proses ini, setiap film direpresentasikan sebagai sebuah vektor unik dalam ruang fitur multidimensi, di mana setiap dimensi merepresentasikan sebuah genre dengan bobot TF-IDF-nya.

2. Kalkulasi Kemiripan Menggunakan Cosine Similarity
Setelah setiap film memiliki representasi vektor, metrik Cosine Similarity digunakan untuk mengukur tingkat kesamaan di antara mereka.

- Metode ini mengalkulasi kosinus sudut antara dua vektor. Skor yang dihasilkan berkisar antara 0 (tidak ada kemiripan) hingga 1 (kemiripan sempurna).

- Skor yang mendekati 1 menandakan bahwa kedua film memiliki profil genre yang sangat mirip, karena vektornya memiliki orientasi yang hampir identik dalam ruang fitur.

- Dengan menerapkan kalkulasi ini secara pairwise pada seluruh dataset, sebuah matriks kemiripan (similarity matrix) dihasilkan. Matriks ini berfungsi sebagai dasar untuk menemukan film-film yang paling mirip untuk setiap judul film yang ada.

**Parameter dan Peran dalam Sistem Hibrida**

Dalam implementasinya, model ini dibangun menggunakan parameter standar (default) yang disediakan oleh library Scikit-learn untuk TfidfVectorizer dan cosine_similarity. Peran model Content-based Filtering dalam arsitektur hibrida ini sangat strategis, yaitu untuk melakukan re-ranking terhadap kandidat rekomendasi yang dihasilkan oleh model Collaborative Filtering, sehingga memastikan bahwa rekomendasi akhir tidak hanya akurat berdasarkan pola interaksi pengguna, tetapi juga relevan secara kontekstual berdasarkan konten film.

### 6.2 Collaborative Filtering

Collaborative Filtering merupakan paradigma sistem rekomendasi yang beroperasi berdasarkan prinsip kolaborasi sosial. Metode ini tidak menganalisis atribut dari item yang direkomendasikan, melainkan mengidentifikasi pola dari data interaksi historis pengguna, seperti rating, riwayat tontonan, atau pembelian.

**Cara Kerja**

Mekanisme fundamental dari Collaborative Filtering didasarkan pada asumsi bahwa jika seorang pengguna memiliki preferensi yang sama dengan pengguna lain di masa lalu, maka kemungkinan besar mereka akan memiliki preferensi yang sama di masa depan. Proses kerjanya dapat diuraikan sebagai berikut:

1. Identifikasi Pola Interaksi: Sistem mengumpulkan dan menstrukturkan data interaksi pengguna-item ke dalam sebuah matriks utilitas (utility matrix), di mana baris merepresentasikan pengguna dan kolom merepresentasikan item.

2. Pengukuran Kesamaan: Sistem mengalkulasi kesamaan (similarity) antar pengguna (pendekatan user-based) atau antar item (pendekatan item-based).

3. Generasi Prediksi: Berdasarkan kesamaan tersebut, sistem memprediksi rating atau minat seorang pengguna terhadap item yang belum pernah berinteraksi dengannya. Prediksi ini dihitung dari rating yang diberikan oleh sekelompok pengguna yang memiliki selera serupa (nearest neighbors).

Secara esensial, pendekatan ini memanfaatkan "kearifan kolektif" (wisdom of the crowd) untuk menghasilkan rekomendasi yang bersifat personal dan sering kali tak terduga (serendipitous), karena mampu menemukan item lintas genre atau kategori yang disukai oleh komunitas pengguna dengan profil serupa.

**Teknik dan Parameter**
Dalam proyek ini, dua implementasi canggih dari Collaborative Filtering berbasis Matrix Factorization dieksplorasi.
1. **FastAI: Neural Matrix Factorization**
**Teknik**: Implementasi ini menggunakan pendekatan modern di mana Matrix Factorization diintegrasikan ke dalam arsitektur jaringan saraf (neural network). Alih-alih hanya mengandalkan produk skalar (dot product) untuk mengkombinasikan vektor laten pengguna dan item, model ini melewatkannya melalui beberapa lapisan jaringan saraf. Hal ini memungkinkan model untuk menangkap hubungan yang lebih kompleks dan non-linear antara preferensi pengguna dan karakteristik item, yang sering kali gagal ditangkap oleh metode tradisional.

**Parameter:**

- embedding_dim=50: Mendefinisikan dimensionalitas ruang laten. Setiap pengguna dan film direpresentasikan sebagai sebuah vektor (embedding) dengan 50 fitur tersembunyi. Dimensi ini menentukan kapasitas model untuk menangkap nuansa dalam data preferensi.

- epochs=5: Jumlah siklus pelatihan penuh pada keseluruhan dataset. Model akan memproses seluruh data latih sebanyak lima kali untuk mengoptimalkan bobot internalnya dan mencapai konvergensi.

- lr=5e-3: Learning Rate (laju pembelajaran) sebesar 0.005. Parameter ini mengontrol magnitudo penyesuaian bobot model pada setiap iterasi pelatihan, yang sangat memengaruhi kecepatan dan stabilitas proses konvergensi.

2. **Surprise (SVD): Singular Value Decomposition**

**Teknik**: Pustaka Surprise menyediakan implementasi yang sangat teroptimisasi dari Singular Value Decomposition (SVD), sebuah teknik Matrix Factorization yang telah terbukti andal. Algoritma ini bekerja dengan menguraikan matriks utilitas pengguna-item menjadi tiga matriks terpisah yang merepresentasikan vektor laten pengguna, vektor laten item, dan nilai singularnya. Untuk tujuan prediksi, varian SVD yang dioptimalkan untuk data yang jarang (sparse data)—seperti data rating yang memiliki banyak nilai kosong—biasanya digunakan, sering kali diimplementasikan melalui algoritma optimisasi seperti Stochastic Gradient Descent (SGD).

**Parameter:**

- n_factors=100: Menentukan jumlah faktor laten yang akan diekstraksi. Dalam kasus ini, setiap pengguna dan item direpresentasikan oleh vektor dengan 100 dimensi.

- n_epochs=20: Jumlah iterasi penuh yang akan dijalankan oleh algoritma pada seluruh data latih.

- lr_all=0.005: Laju pembelajaran yang diterapkan pada semua parameter model selama proses optimisasi SGD.

- reg_all=0.02: Koefisien regularisasi L2 yang diterapkan pada semua parameter. Regularisasi adalah teknik krusial untuk mencegah overfitting dengan memberikan pinalti pada bobot parameter yang terlalu besar, sehingga mendorong model untuk memiliki kemampuan generalisasi yang lebih baik pada data baru.

### 6.3 Hybrid Re-ranking

Pendekatan Hybrid Re-ranking adalah strategi yang menggabungkan output dari dua atau lebih teknik rekomendasi untuk menghasilkan daftar final yang lebih akurat dan relevan. Dalam implementasi proyek ini, sistem hibrida mengintegrasikan model Collaborative Filtering dan Content-based Filtering melalui sebuah mekanisme re-ranking berbobot. Tujuan utamanya adalah untuk memanfaatkan kekuatan penemuan pola dari Collaborative Filtering sambil menyempurnakan personalisasi menggunakan kemiripan konten.

**Cara kerja**:

Proses Hybrid Re-ranking dieksekusi melalui serangkaian langkah sekuensial sebagai berikut:

1. **Generasi Kandidat Awal dengan Collaborative Filtering**
Langkah pertama adalah menghasilkan daftar kandidat rekomendasi. Model Collaborative Filtering (berbasis FastAI) digunakan untuk memprediksi potensi rating yang akan diberikan oleh seorang pengguna pada semua film yang belum pernah ia tonton. Tahap ini menghasilkan sebuah daftar film yang luas, diurutkan berdasarkan skor prediksi yang mencerminkan preferensi umum dari pengguna dengan selera serupa.

2. **Seleksi Kandidat Film Berdasarkan Peringkat Teratas**
Dari seluruh film yang telah diprediksi, sistem akan mengambil sekumpulan film dengan skor prediksi tertinggi sebagai kandidat utama. Film-film ini dianggap memiliki probabilitas tertinggi untuk disukai oleh pengguna berdasarkan analisis kolaboratif.

3. **Kalkulasi Skor Kemiripan Konten**
Selanjutnya, komponen Content-based diperkenalkan untuk personalisasi. Sistem terlebih dahulu mengidentifikasi satu atau beberapa film "benih" (seed movies), yaitu film-film yang telah diberi rating sangat tinggi oleh pengguna di masa lalu. Kemudian, untuk setiap film kandidat dari langkah sebelumnya, sistem mengkalkulasi skor kemiripan konten (menggunakan Cosine Similarity berbasis genre) terhadap film "benih" tersebut. Skor ini merepresentasikan seberapa relevan setiap kandidat secara tematis dengan preferensi eksplisit pengguna.

4. **Kombinasi Berbobot dan Proses Re-ranking Final**
Langkah terakhir adalah mengagregasi kedua skor menjadi satu skor hibrida final. Sebuah formula pembobotan diterapkan untuk menyeimbangkan pengaruh kedua model. Sesuai implementasi, skor dihitung sebagai berikut:

Skor Hibrida = (0.6 * Skor_Prediksi_CF) + (0.4 * Skor_Kemiripan_Konten)

Bobot sebesar 0.6 diberikan kepada skor Collaborative Filtering, sementara 0.4 diberikan kepada skor Content-based. Skor kemiripan konten juga diskalakan agar sepadan dengan rentang skor rating. Berdasarkan skor hibrida ini, seluruh daftar kandidat diurutkan ulang (re-ranked). Film-film dengan skor hibrida tertinggi kemudian disajikan kepada pengguna sebagai rekomendasi final.

Metode ini secara efektif memastikan bahwa rekomendasi akhir tidak hanya populer di kalangan pengguna serupa, tetapi juga sangat relevan dengan selera personal pengguna yang teridentifikasi dari konten film yang ia sukai.

------------------------------------------------------------------------

## 7. Evaluation

### Metrik yang digunakan

1.  **Root Mean Squared Error (RMSE)**\
    $$ RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2} $$

2.  **Precision@k**\
    $$ Precision@k = \frac{|\{ \text{Rekomendasi relevan pada top-k} \}|}{k} $$

3.  **Recall@k**\
    $$ Recall@k = \frac{|\{ \text{Rekomendasi relevan pada top-k} \}|}{|\{ \text{Seluruh item relevan} \}|} $$

### Hasil Evaluasi

Dari data yang disajikan, terlihat bahwa kinerja sistem rekomendasi ini, yang diukur dengan metrik Precision@k dan Recall@k pada k=10, masih sangat rendah.

- Rata-rata Precision@10 sebesar 0.0380 menunjukkan bahwa, rata-rata, hanya sekitar 3.8% dari film yang direkomendasikan kepada pengguna adalah film yang relevan (film yang mereka sukai). Dengan kata lain, dari 10 film yang direkomendasikan, hanya sekitar 0.38 film (kurang dari satu) yang benar-benar relevan.

- Rata-rata Recall@10 sebesar 0.0285 menunjukkan bahwa, rata-rata, sistem hanya berhasil menemukan sekitar 2.85% dari total film relevan yang disukai pengguna. Ini berarti sistem gagal menemukan sebagian besar film relevan yang ada dalam data pengguna.

Meskipun model ini berhasil memberikan rekomendasi yang terlihat masuk akal secara tematis (misalnya, rekomendasi film-film aksi/sci-fi untuk Pengguna 582 dan 599, atau film kriminal untuk Pengguna 215), jumlah "hits" (film yang direkomendasikan dan juga relevan) sangat sedikit. Dari 32 pengguna yang dievaluasi, hanya 9 pengguna yang mendapatkan setidaknya satu film relevan di antara 10 rekomendasi teratas mereka.

### Analisis Lebih Lanjut

Hasil ini menunjukkan bahwa ada beberapa area yang perlu diperbaiki:

- Keterbatasan Data: Jumlah pengguna dan film yang digunakan untuk evaluasi ini mungkin tidak cukup besar untuk memberikan gambaran yang akurat. Selain itu, sebaran data rating mungkin tidak merata, menyebabkan beberapa pengguna memiliki sedikit atau bahkan nol film relevan (seperti Pengguna 207 dan 496).

- Masalah Cold-Start: Sebagian besar pengguna dalam evaluasi ini (seperti Pengguna 428, 215, 461, 197, dst.) memiliki hits nol. Ini bisa menjadi indikasi masalah cold-start, di mana model tidak memiliki cukup data riwayat rating untuk pengguna tersebut, sehingga rekomendasinya tidak akurat.

- Bobot Model Hibrida: Bobot yang diberikan pada model Collaborative dan Content-based (jika ini adalah model hibrida) mungkin tidak optimal. Model mungkin terlalu condong ke salah satu sisi, sehingga gagal memanfaatkan kekuatan gabungan dari kedua pendekatan.

- Definisi "Relevan": Mungkin ada masalah dalam definisi "film relevan". Jika hanya film dengan rating 4 atau 5 yang dianggap relevan, model mungkin kesulitan jika sebagian besar rating pengguna berada di angka 3.

Secara keseluruhan, meskipun proyek ini berhasil membangun sebuah alur kerja rekomendasi, hasil evaluasi menunjukkan bahwa model ini belum siap untuk digunakan di lingkungan produksi. Diperlukan iterasi lebih lanjut pada model, data, dan strategi evaluasi untuk meningkatkan performa secara signifikan.

------------------------------------------------------------------------

## 8. Strategi Bisnis

1.  **Personalisasi Dashboard**: rekomendasi personal di halaman utama.
2.  **Fitur "Film Serupa"**: rekomendasi berbasis konten pada halaman
    detail film.
3.  **Peningkatan Retensi**: notifikasi/email rekomendasi bagi pengguna
    tidak aktif.
4.  **Segmentasi Pasar**: kampanye promosi sesuai preferensi pengguna.

------------------------------------------------------------------------

## 9. Kesimpulan

Proyek ini telah berhasil membangun sistem rekomendasi film hibrida
dengan alur kerja komprehensif. RMSE rendah menunjukkan model cukup
akurat dalam memprediksi rating, namun nilai Precision@k dan Recall@k
rendah menegaskan perlunya perbaikan.

**Rekomendasi pengembangan selanjutnya**:
- Eksperimen bobot hibrida (A/B testing).
- Tambahkan fitur konten lain (aktor, sutradara, tag).
- Eksplorasi algoritma lanjutan (misalnya SVD++, deep learning
recommenders).

------------------------------------------------------------------------

## 10. Struktur Laporan

-   Abstrak
-   Pendahuluan
-   Project Overview
-   Business Understanding
-   Data Understanding
-   Data Preparation
-   Metodologi / Modeling and Result
-   Evaluation
-   Strategi Bisnis
-   Kesimpulan
