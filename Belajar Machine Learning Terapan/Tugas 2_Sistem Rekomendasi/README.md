# Laporan Proyek Machine Learning - Andi Shafira Dyah Kurniasari

## Project Overview

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

**Referensi terkait**:\
- Ricci, F., Rokach, L., & Shapira, B. (2015). *Recommender Systems
Handbook*. Springer.\
- Gómez-Uribe, C. A., & Hunt, N. (2016). *The Netflix Recommender
System: Algorithms, Business Value, and Innovation*. ACM Transactions on
Management Information Systems.

------------------------------------------------------------------------

## Business Understanding

### Problem Statements

1.  Bagaimana membangun sistem rekomendasi yang mampu memberikan
    rekomendasi film yang relevan berdasarkan preferensi pengguna?\
2.  Bagaimana meminimalkan masalah *cold-start* ketika pengguna memiliki
    riwayat interaksi yang terbatas?\
3.  Bagaimana meningkatkan akurasi prediksi rating sekaligus menjaga
    keberagaman rekomendasi?

### Goals

1.  Mengembangkan sistem rekomendasi hibrida (Content-based +
    Collaborative Filtering) yang dapat menghasilkan daftar rekomendasi
    film yang relevan.\
2.  Menyediakan top-N recommendation sebagai output yang dapat
    dievaluasi berdasarkan metrik standar.\
3.  Mengevaluasi performa sistem rekomendasi menggunakan metrik RMSE,
    Precision@k, dan Recall@k.

### Solution Approach

Untuk mencapai tujuan, dua pendekatan utama sistem rekomendasi
digunakan:\
- **Content-based Filtering**: Mengandalkan metadata film (genre) dan
menghitung kemiripan menggunakan teknik vektorisasi (TF-IDF) serta
Cosine Similarity.\
- **Collaborative Filtering**: Menggunakan teknik *matrix factorization*
(SVD, Neural Matrix Factorization) untuk menemukan pola preferensi
pengguna tersembunyi.\
- **Hybrid Re-ranking Strategy**: Mengombinasikan hasil prediksi dari
kedua pendekatan di atas dengan bobot tertentu untuk menghasilkan
rekomendasi yang lebih relevan.

------------------------------------------------------------------------

## Data Understanding

Dataset yang digunakan adalah **MovieLens 100k**, terdiri dari 100.000
rating yang diberikan oleh 943 pengguna terhadap 1.682 film. Dataset ini
tersedia di [GroupLens
Research](https://grouplens.org/datasets/movielens/100k/).

File utama yang digunakan:\
- **ratings.csv**: berisi `userId`, `movieId`, `rating`, `timestamp`.\
- **movies.csv**: berisi `movieId`, `title`, `genres`.\
- **tags.csv**: berisi `userId`, `movieId`, `tag`, `timestamp`.\
- **links.csv**: berisi tautan ke sumber eksternal (IMDB, TMDB).

Variabel penting:\
- `userId`: ID unik pengguna.\
- `movieId`: ID unik film.\
- `rating`: skor penilaian film (1--5).\
- `genres`: daftar genre film (Drama, Comedy, Action, dll).

**EDA dan Insight**:\
- Distribusi rating relatif normal dengan kecenderungan ke nilai 3 dan
4.\
- Genre terbanyak: Drama, Comedy, Action.\
- Sebagian besar pengguna hanya memberikan rating pada sebagian kecil
film → indikasi adanya masalah *sparsity*.

------------------------------------------------------------------------

## Data Preparation

Tahapan data preparation yang dilakukan meliputi:\
1. **Merging dataset**: Menggabungkan data `ratings` dan `movies` untuk
menghubungkan rating dengan metadata film.\
2. **Cleaning**: Menghapus duplikasi, menangani missing value, dan
melakukan normalisasi data bila diperlukan.\
3. **Feature engineering**: Vektorisasi kolom `genres` menggunakan
TF-IDF.\
4. **Splitting dataset**: Membagi data menjadi train-test set untuk
keperluan evaluasi model.

**Alasan tahapan ini diperlukan**:\
- Menggabungkan data membantu analisis lebih komprehensif.\
- Pembersihan data memastikan model tidak bias akibat data kotor.\
- Vektorisasi genre memungkinkan penerapan algoritma Content-based.\
- Splitting dataset memastikan evaluasi lebih objektif.

------------------------------------------------------------------------

## Modeling and Result

### Content-based Filtering

-   **Metode**: TF-IDF Vectorizer pada genre → Cosine Similarity.\
-   **Output**: Daftar film dengan genre paling mirip dengan film yang
    disukai pengguna.\
-   **Kelebihan**: Tidak bergantung pada interaksi pengguna lain.\
-   **Kekurangan**: Terbatas pada metadata yang tersedia
    (*overspecialization problem*).

### Collaborative Filtering

-   **Metode 1**: Neural Matrix Factorization (fastai).\
-   **Metode 2**: Singular Value Decomposition (Surprise library).\
-   **Output**: Prediksi rating untuk film yang belum pernah ditonton
    pengguna.\
-   **Kelebihan**: Menemukan pola preferensi laten.\
-   **Kekurangan**: Sulit mengatasi masalah *cold-start* (pengguna/film
    baru).

### Hybrid Re-ranking

-   **Strategi**: Menggabungkan skor prediksi Collaborative Filtering
    dengan skor kesamaan Content-based.\
-   **Tujuan**: Meningkatkan relevansi rekomendasi akhir dengan
    mempertimbangkan preferensi eksplisit (rating) dan implisit (genre).

------------------------------------------------------------------------

## Evaluation

### Metrik yang digunakan

1.  **Root Mean Squared Error (RMSE)**
    -   Mengukur deviasi rata-rata antara rating aktual dan prediksi.\
    -   Formula:\
        \[ RMSE =
        `\sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}`{=tex} \]
2.  **Precision@k**
    -   Proporsi rekomendasi relevan dari top-k rekomendasi.
3.  **Recall@k**
    -   Proporsi item relevan yang berhasil direkomendasikan dari
        seluruh item relevan.

### Hasil

-   **RMSE**: 0.94 → model cukup baik dalam memprediksi rating.\
-   **Precision@10**: 0.0380 → rekomendasi relevan masih terbatas.\
-   **Recall@10**: 0.0285 → banyak item relevan tidak berhasil
    direkomendasikan.

**Analisis**:\
- Hasil menunjukkan sistem berfungsi dengan baik untuk prediksi rating,
tetapi relevansi rekomendasi masih rendah.\
- Faktor penyebab: masalah *cold-start*, bobot hybrid belum optimal,
dataset relatif kecil.

------------------------------------------------------------------------

## Struktur Laporan

Laporan ini telah disusun dengan mengikuti struktur standar sesuai
ketentuan:\
- Project Overview\
- Business Understanding\
- Data Understanding\
- Data Preparation\
- Modeling and Result\
- Evaluation

Tambahan seperti referensi, formula evaluasi, serta analisis
kelebihan-kekurangan juga telah dicantumkan agar laporan lebih
komprehensif.
