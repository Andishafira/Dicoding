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

**Mengapa proyek ini penting?**\
- Platform berbasis konten (seperti Netflix, Disney+, atau Spotify untuk
musik) telah membuktikan bahwa sistem rekomendasi dapat meningkatkan
engagement hingga 60--70% dari konsumsi pengguna.\
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
    rekomendasi film yang relevan berdasarkan preferensi pengguna?\
2.  Bagaimana meminimalkan masalah *cold-start* ketika pengguna memiliki
    riwayat interaksi yang terbatas?\
3.  Bagaimana meningkatkan akurasi prediksi rating sekaligus menjaga
    keberagaman rekomendasi?

### Goals

Tujuan utama dari proyek ini adalah untuk membangun sebuah sistem rekomendasi film yang dapat meningkatkan keterlibatan (engagement) pengguna dan memperpanjang durasi mereka di platform. Saya ingin menyediakan rekomendasi yang sangat personal dan akurat, yang terasa seperti kurasi dari seorang ahli film. berikut adalah poin detail dari tujuan teknis project ini: 

1.  Mengembangkan sistem rekomendasi hibrida (Content-based +
    Collaborative Filtering) yang dapat menghasilkan daftar rekomendasi
    film yang relevan.\
2.  Menyediakan top-N recommendation sebagai output yang dapat
    dievaluasi berdasarkan metrik standar.\
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

-   **Cara kerja**: merekomendasikan film berdasarkan kesamaan genre.\
-   **Teknik**: TF-IDF Vectorizer pada `genres` → Cosine Similarity.\
-   **Parameter**: default TF-IDF, Cosine Similarity pairwise.

**Contoh Top-5 Rekomendasi (untuk film The Matrix)**:\
\| Rank \| Judul Film \| Genre \| Similarity \|
\|------\|-------------------------\|------------------\|------------\|
\| 1 \| The Matrix Reloaded \| Action\|Sci-Fi \| 0.89 \| \| 2 \| Dark
City \| Sci-Fi\|Thriller \| 0.85 \| \| 3 \| Terminator 2 \|
Action\|Sci-Fi \| 0.82 \| \| 4 \| Blade Runner \| Sci-Fi\|Drama \| 0.80
\| \| 5 \| Total Recall \| Action\|Sci-Fi \| 0.78 \|

### 6.2 Collaborative Filtering

-   **FastAI**: Neural Matrix Factorization.
    -   Parameter: embedding dim=50, epochs=5, lr=5e-3.\
-   **Surprise (SVD)**:
    -   Parameter: n_factors=100, n_epochs=20, lr_all=0.005,
        reg_all=0.02.

**Contoh Top-5 Rekomendasi (untuk userId=10, SVD)**:\
\| Rank \| Judul Film \| Predicted Rating \|
\|------\|-------------------------\|-----------------\| \| 1 \| Star
Wars: Episode IV \| 4.9 \| \| 2 \| Raiders of the Lost Ark \| 4.8 \| \|
3 \| The Empire Strikes Back \| 4.8 \| \| 4 \| Return of the Jedi \| 4.7
\| \| 5 \| Indiana Jones \| 4.7 \|

### 6.3 Hybrid Re-ranking

-   **Cara kerja**:
    1.  Prediksi rating dengan Collaborative Filtering.\
    2.  Ambil kandidat film dengan rating prediksi tertinggi.\
    3.  Hitung similarity konten terhadap film kesukaan pengguna.\
    4.  Gabungkan skor dengan bobot 0.6 (CF) dan 0.4 (Content-based).

**Contoh Top-5 Rekomendasi (untuk userId=10, Hybrid)**:\
\| Rank \| Judul Film \| Hybrid Score \|
\|------\|-------------------------\|--------------\| \| 1 \| Star Wars:
Episode IV \| 0.92 \| \| 2 \| Raiders of the Lost Ark \| 0.91 \| \| 3 \|
The Empire Strikes Back \| 0.89 \| \| 4 \| Return of the Jedi \| 0.88 \|
\| 5 \| Indiana Jones \| 0.87 \|

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

-   **RMSE (SVD)**: 0.94.\
-   **Precision@10 (Hybrid)**: 0.0380.\
-   **Recall@10 (Hybrid)**: 0.0285.

### Analisis Hasil

-   Model cukup akurat dalam prediksi rating (RMSE rendah).\
-   Precision & Recall rendah → indikasi masalah *cold-start*,
    keterbatasan data, bobot hibrida belum optimal.

------------------------------------------------------------------------

## 8. Strategi Bisnis

1.  **Personalisasi Dashboard**: rekomendasi personal di halaman utama.\
2.  **Fitur "Film Serupa"**: rekomendasi berbasis konten pada halaman
    detail film.\
3.  **Peningkatan Retensi**: notifikasi/email rekomendasi bagi pengguna
    tidak aktif.\
4.  **Segmentasi Pasar**: kampanye promosi sesuai preferensi pengguna.

------------------------------------------------------------------------

## 9. Kesimpulan

Proyek ini telah berhasil membangun sistem rekomendasi film hibrida
dengan alur kerja komprehensif. RMSE rendah menunjukkan model cukup
akurat dalam memprediksi rating, namun nilai Precision@k dan Recall@k
rendah menegaskan perlunya perbaikan.

**Rekomendasi pengembangan selanjutnya**:\
- Eksperimen bobot hibrida (A/B testing).\
- Tambahkan fitur konten lain (aktor, sutradara, tag).\
- Eksplorasi algoritma lanjutan (misalnya SVD++, deep learning
recommenders).

------------------------------------------------------------------------

## 10. Struktur Laporan

-   Abstrak\
-   Pendahuluan\
-   Project Overview\
-   Business Understanding\
-   Data Understanding\
-   Data Preparation\
-   Metodologi / Modeling and Result\
-   Evaluation\
-   Strategi Bisnis\
-   Kesimpulan
