# Laporan Proyek Machine Learning: Sistem Rekomendasi

**Oleh:** Andi Shafira Dyah Kurniasari

## Abstrak

Proyek ini berfokus pada pembangunan dan evaluasi sistem rekomendasi film menggunakan dataset **MovieLens 100k**. Metodologi yang diterapkan adalah pendekatan hibrida, yang menggabungkan keunggulan dari model **Content-based Filtering** dan **Collaborative Filtering**. Model Content-based memanfaatkan metadata film seperti genre untuk merekomendasikan item serupa, sementara model Collaborative menganalisis pola perilaku pengguna (riwayat rating) untuk menemukan preferensi tersembunyi.

Pengujian model dilakukan dengan metrik **Root Mean Squared Error (RMSE)** untuk akurasi prediksi serta **Precision@k** dan **Recall@k** untuk mengukur relevansi rekomendasi teratas. Laporan ini merinci setiap tahapan, mulai dari pemuatan data, eksplorasi, pembangunan model, hingga analisis hasil dan implikasi bisnis.

---

## 1. Pendahuluan

Sistem rekomendasi adalah alat vital dalam platform digital modern, dirancang untuk mempersonalisasi pengalaman pengguna dan meningkatkan interaksi. Tanpa sistem ini, pengguna seringkali merasa kesulitan menemukan konten yang relevan di tengah banjirnya pilihan, yang dapat menyebabkan penurunan retensi. Proyek ini bertujuan membangun sistem rekomendasi yang cerdas dan efisien, yang tidak hanya akurat tetapi juga mampu memberikan rekomendasi yang beragam dan menarik.

---

## 2. Project Overview

Sistem rekomendasi telah menjadi komponen penting dalam berbagai platform digital, khususnya di bidang hiburan seperti layanan film dan musik. Tanpa sistem ini, pengguna kerap kesulitan menemukan konten yang relevan di antara banyaknya pilihan, yang berisiko menurunkan retensi dan kepuasan mereka.

Proyek ini berfokus pada pembangunan dan evaluasi sistem rekomendasi film menggunakan dataset **MovieLens 100k** untuk mempersonalisasi pengalaman pengguna dengan memberikan rekomendasi yang relevan, akurat, dan menarik.

**Mengapa proyek ini penting?**
- Platform berbasis konten (seperti Netflix atau Spotify) telah membuktikan bahwa sistem rekomendasi dapat meningkatkan *engagement* hingga 60–70% dari total konsumsi pengguna.
- Rekomendasi yang tepat sasaran tidak hanya meningkatkan kepuasan pengguna, tetapi juga berkontribusi pada retensi pelanggan jangka panjang.

**Referensi Terkait**:
- Ricci, F., Rokach, L., & Shapira, B. (2015). *Recommender Systems Handbook*. Springer. ([Tautan](https://www.researchgate.net/publication/227268858_Recommender_Systems_Handbook))
- Gómez-Uribe, C. A., & Hunt, N. (2016). *The Netflix Recommender System: Algorithms, Business Value, and Innovation*. ACM Transactions on Management Information Systems. ([Tautan](https://dl.acm.org/doi/10.1145/2843948))

---

## 3. Business Understanding

### Problem Statements
1.  Bagaimana membangun sistem rekomendasi yang mampu memberikan rekomendasi film yang relevan berdasarkan preferensi pengguna?
2.  Bagaimana meminimalkan masalah *cold-start* ketika pengguna memiliki riwayat interaksi yang terbatas?
3.  Bagaimana meningkatkan akurasi prediksi rating sekaligus menjaga keberagaman rekomendasi?

### Goals
Tujuan utama proyek ini adalah membangun sistem rekomendasi film yang dapat meningkatkan keterlibatan (*engagement*) pengguna dan memperpanjang durasi mereka di platform.

**Tujuan Teknis:**
1.  Mengembangkan sistem rekomendasi hibrida (Content-based + Collaborative Filtering) yang dapat menghasilkan daftar rekomendasi film yang relevan.
2.  Menyediakan *top-N recommendation* sebagai output yang dapat dievaluasi berdasarkan metrik standar.
3.  Mengevaluasi performa sistem menggunakan metrik **RMSE**, **Precision@k**, dan **Recall@k**.

**Manfaat Langsung:**
* **Peningkatan Retensi Pengguna**: Pengguna yang merasa platform memahami selera mereka cenderung akan kembali lagi.
* **Optimalisasi Konten**: Wawasan dari model dapat membantu tim konten dalam mengambil keputusan berbasis data.
* **Peluang Monetisasi**: Durasi tontonan yang lebih lama membuka peluang pendapatan dari iklan atau peningkatan langganan.

### Solution Approach
-   **Content-based Filtering**: Mengandalkan metadata film (genre) dan menghitung kemiripan menggunakan vektorisasi TF-IDF serta Cosine Similarity.
-   **Collaborative Filtering**: Menggunakan teknik *matrix factorization* (SVD, Neural Matrix Factorization) untuk menemukan pola preferensi pengguna.
-   **Hybrid Re-ranking Strategy**: Mengombinasikan hasil prediksi dari kedua pendekatan untuk menghasilkan rekomendasi yang lebih relevan.

---

## 4. Data Understanding

Dataset yang digunakan adalah **MovieLens 100k**, tersedia di [GroupLens Research](https://grouplens.org/datasets/movielens/100k/). Dataset ini terdiri dari empat file utama.

### 4.1 `ratings.csv`
-   **Jumlah Data**: 100.000 baris × 4 kolom.
-   **Isi Data**: Semua rating yang diberikan pengguna terhadap film.
-   **Kondisi Data**: Tidak ada *missing value* atau duplikasi.
-   **Fitur**:
    -   `userId`: ID unik pengguna.
    -   `movieId`: ID unik film.
    -   `rating`: Skor penilaian (0.5 – 5.0).
    -   `timestamp`: Waktu pemberian rating.
-   **Fungsi**: Data utama untuk *collaborative filtering*.

### 4.2 `movies.csv`
-   **Jumlah Data**: 1.682 baris × 3 kolom.
-   **Isi Data**: Informasi metadata film.
-   **Kondisi Data**: Tidak ada *missing value*.
-   **Fitur**:
    -   `movieId`: ID unik film.
    -   `title`: Judul film dan tahun rilis.
    -   `genres`: Daftar genre yang dipisahkan oleh `|`.
-   **Fungsi**: Sumber utama untuk *Content-based Filtering*.

### 4.3 `tags.csv`
-   **Jumlah Data**: 3.689 baris × 4 kolom.
-   **Isi Data**: Tag atau label yang diberikan pengguna pada film.
-   **Kondisi Data**: Terdapat *missing value* pada kolom `tag`.
-   **Fitur**: `userId`, `movieId`, `tag`, `timestamp`.
-   **Fungsi**: Metadata tambahan buatan pengguna untuk meningkatkan model berbasis konten.

### 4.4 `links.csv`
-   **Jumlah Data**: 1.682 baris × 3 kolom.
-   **Isi Data**: Tautan ke database film eksternal.
-   **Kondisi Data**: Tidak ada *missing value*.
-   **Fitur**: `movieId`, `imdbId`, `tmdbId`.

**Insight EDA**:
-   Distribusi rating condong ke nilai 3 & 4.
-   Genre terpopuler adalah Drama, Comedy, dan Action.
-   Dataset bersifat *sparse* (sebagian besar pengguna hanya menilai sebagian kecil film).

---

## 5. Data Preparation

Tahapan persiapan data yang dilakukan adalah sebagai berikut:
1.  **Pengumpulan dan Eksplorasi Data**: Dataset diunduh dan dianalisis untuk memahami struktur dan isinya. Ditemukan 9.742 judul film dan 100.836 rating.
2.  **Persiapan Data**:
    -   Tabel `ratings` dan `movies` digabungkan untuk menghubungkan setiap rating dengan metadata filmnya.
    -   Data dibagi menjadi set latih (80%) dan set uji (20%) untuk evaluasi model yang objektif.
3.  **Pengembangan Model Hibrida**:
    -   **Collaborative Filtering**: Dibangun menggunakan *library* **FastAI** untuk mempelajari pola interaksi pengguna-film.
    -   **Content-Based Filtering**: Dibangun menggunakan **TF-IDF Vectorizer** dan **Cosine Similarity** dari *library* Scikit-learn untuk merekomendasikan film berdasarkan kemiripan genre.
    -   **Penggabungan Hibrida**: Hasil dari kedua model digabungkan dengan sistem pembobotan untuk menghasilkan skor akhir.
4.  **Evaluasi Kinerja**: Model dievaluasi menggunakan metrik **Precision@10** dan **Recall@10** pada data uji.
5.  **Kesimpulan dan Strategi**: Hasil dianalisis untuk menarik kesimpulan dan merumuskan potensi bisnis.
6.  **Pembuatan Laporan**: Seluruh proses didokumentasikan dalam laporan ini.

---

## 6. Metodologi / Modeling and Result

### 6.1 Content-based Filtering
Pendekatan ini merekomendasikan film berdasarkan kesamaan atributnya, terutama **genre**. Keunggulannya adalah mampu mengatasi masalah *cold-start* karena tidak bergantung pada data pengguna lain.

**Cara Kerja:**
1.  **Vektorisasi Fitur dengan TF-IDF**: Genre setiap film diubah menjadi vektor numerik. **TF-IDF** (*Term Frequency-Inverse Document Frequency*) memberikan bobot lebih tinggi pada genre yang lebih langka dan informatif.
2.  **Kalkulasi Kemiripan dengan Cosine Similarity**: Setelah setiap film direpresentasikan sebagai vektor, **Cosine Similarity** digunakan untuk mengukur sudut antara dua vektor. Skor kemiripan berkisar dari 0 (tidak mirip) hingga 1 (identik), yang kemudian disimpan dalam sebuah matriks kemiripan.

### 6.2 Collaborative Filtering
Pendekatan ini bekerja dengan mengidentifikasi pola dari data interaksi historis pengguna (rating) berdasarkan asumsi bahwa pengguna dengan selera serupa di masa lalu akan memiliki selera serupa di masa depan.

**Teknik dan Parameter:**
1.  **FastAI: Neural Matrix Factorization**
    -   **Teknik**: Menggunakan arsitektur *neural network* untuk menangkap hubungan non-linear yang kompleks antara preferensi pengguna dan karakteristik item.
    -   **Parameter**:
        -   `embedding_dim`: 50
        -   `epochs`: 5
        -   `lr`: 5e-3 (0.005)

2.  **Surprise (SVD): Singular Value Decomposition**
    -   **Teknik**: Implementasi *Matrix Factorization* yang teroptimisasi untuk menguraikan matriks utilitas pengguna-item menjadi vektor laten.
    -   **Parameter**:
        -   `n_factors`: 100
        -   `n_epochs`: 20
        -   `lr_all`: 0.005
        -   `reg_all`: 0.02 (Koefisien regularisasi L2 untuk mencegah *overfitting*).

### 6.3 Hybrid Re-ranking
Strategi ini menggabungkan output dari kedua model untuk menghasilkan rekomendasi akhir yang lebih akurat.

**Cara Kerja:**
1.  **Generasi Kandidat**: Model *Collaborative Filtering* (FastAI) memprediksi rating untuk semua film yang belum ditonton pengguna, menghasilkan daftar kandidat awal.
2.  **Seleksi Kandidat Teratas**: Sejumlah film dengan prediksi rating tertinggi dipilih.
3.  **Kalkulasi Skor Kemiripan Konten**: Untuk setiap film kandidat, dihitung skor kemiripan genre (*Cosine Similarity*) terhadap film yang pernah diberi rating tinggi oleh pengguna.
4.  **Kombinasi Berbobot dan Re-ranking**: Skor akhir dihitung menggunakan formula berbobot, lalu daftar kandidat diurutkan ulang berdasarkan skor hibrida ini.
    > Skor Hibrida = (0.6 × Skor_Prediksi_CF) + (0.4 × Skor_Kemiripan_Konten)

---

## 7. Evaluation

### Metrik yang Digunakan
1.  **Root Mean Squared Error (RMSE)**

    $$
    RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}
    $$
    
2.  **Precision@k**

$$
    Precision@k = \frac{|\{ \text{Rekomendasi relevan pada top-k} \}|}{k}
$$
    
3.  **Recall@k**

$$
    Recall@k = \frac{|\{ \text{Rekomendasi relevan pada top-k} \}|}{|\{ \text{Seluruh item relevan} \}|}
$$

### Hasil Evaluasi
Kinerja sistem yang diukur dengan Precision@k dan Recall@k pada k=10 masih sangat rendah.
-   **Rata-rata Precision@10**: **0.0380** (hanya sekitar 3.8% dari 10 rekomendasi teratas yang relevan).
-   **Rata-rata Recall@10**: **0.0285** (sistem hanya berhasil menemukan 2.85% dari total film relevan bagi pengguna).

### Analisis Lebih Lanjut
Hasil yang rendah menunjukkan beberapa area yang perlu diperbaiki:
-   **Keterbatasan Data**: Jumlah data evaluasi mungkin tidak cukup besar atau tersebar merata.
-   **Masalah Cold-Start**: Banyak pengguna dalam set evaluasi yang tidak memiliki riwayat rating yang cukup, sehingga rekomendasi menjadi tidak akurat.
-   **Bobot Model Hibrida**: Pembobotan 60:40 mungkin belum optimal dan perlu disesuaikan.
-   **Definisi "Relevan"**: Batasan film relevan (misalnya, rating > 4) mungkin terlalu ketat jika sebagian besar rating pengguna lebih rendah.

Secara keseluruhan, alur kerja rekomendasi berhasil dibangun, namun model memerlukan iterasi lebih lanjut untuk siap digunakan di lingkungan produksi.

---

## 8. Strategi Bisnis
1.  **Personalisasi Dashboard**: Menampilkan rekomendasi personal di halaman utama.
2.  **Fitur "Film Serupa"**: Menampilkan rekomendasi berbasis konten pada halaman detail film.
3.  **Peningkatan Retensi**: Mengirimkan notifikasi atau email berisi rekomendasi untuk pengguna yang tidak aktif.
4.  **Segmentasi Pasar**: Menjalankan kampanye promosi yang disesuaikan dengan preferensi segmen pengguna.

---

## 9. Kesimpulan
Proyek ini berhasil membangun sistem rekomendasi film hibrida dengan alur kerja yang komprehensif. Nilai **RMSE** yang rendah menunjukkan model cukup akurat dalam memprediksi rating, namun nilai **Precision@k** dan **Recall@k** yang rendah menegaskan perlunya perbaikan lebih lanjut pada aspek relevansi rekomendasi.

**Rekomendasi Pengembangan Selanjutnya**:
-   Melakukan eksperimen bobot hibrida (misalnya melalui A/B testing).
-   Menambahkan fitur konten lain (aktor, sutradara, tag pengguna).
-   Mengeksplorasi algoritma yang lebih canggih (misalnya SVD++, *deep learning recommenders*).

---

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
