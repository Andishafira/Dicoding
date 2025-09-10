# Laporan Proyek Machine Learning - Prediksi Pembatalan Reservasi Hotel

## Domain Proyek

Industri perhotelan merupakan salah satu pilar utama sektor pariwisata yang sangat kompetitif dan sensitif terhadap dinamika pasar. Salah satu tantangan operasional dan finansial terbesar yang dihadapi oleh hotel adalah pembatalan reservasi. Pembatalan, terutama yang terjadi mendekati tanggal kedatangan, secara langsung berdampak pada hilangnya pendapatan (*revenue loss*) karena kamar yang telah dipesan menjadi kosong dan sulit untuk dijual kembali dalam waktu singkat.

Menurut sebuah studi, tingkat pembatalan reservasi hotel bisa mencapai 20% secara global, dan angka ini dapat meningkat hingga 40% pada beberapa segmen pasar, terutama pemesanan online [1]. Fenomena ini memaksa hotel untuk menerapkan strategi manajemen pendapatan yang kompleks, seperti *overbooking* (menjual lebih banyak kamar daripada yang tersedia). Namun, strategi *overbooking* sendiri memiliki risiko tinggi; jika prediksi pembatalan tidak akurat, hotel dapat menghadapi situasi kekurangan kamar yang berakibat pada kekecewaan pelanggan, biaya kompensasi, dan kerusakan reputasi jangka panjang.

Oleh karena itu, kemampuan untuk memprediksi kemungkinan seorang pelanggan membatalkan reservasi menjadi sangat krusial. Dengan model prediksi yang akurat, manajer hotel dapat membuat keputusan yang lebih cerdas dan berbasis data untuk mengoptimalkan tingkat hunian, menyesuaikan kebijakan pemesanan, dan pada akhirnya memaksimalkan pendapatan. Proyek ini bertujuan untuk membangun model *machine learning* yang mampu mengklasifikasikan status pemesanan hotel (dibatalkan atau tidak) berdasarkan data historis reservasi.

**Referensi:**

[1] Rahmawati et al. (2024), "Develompent of Machine Learning Model to Predict Hotel Room Reservation Cancellations," *Jurnal Teknologi Informasi dan Terapan*, Vol. 11 No. 2 (2024): December. Tersedia: [https://publikasi.polije.ac.id/jtit/article/view/5440](https://publikasi.polije.ac.id/jtit/article/view/5440).

[2] Prasetya et al. (2024), "Stacking Machine Learning Model for Predict Hotel Booking Cancellations," *Jurnal Matematika, Statistika dan Komputasi*, Vol. 20 No. 3 (2024): May 2024. Tersedia: [https://journal.unhas.ac.id/index.php/jmsk/article/view/32619](https://journal.unhas.ac.id/index.php/jmsk/article/view/32619).

---

## Business Understanding

Proses bisnis utama yang menjadi fokus adalah manajemen reservasi dan pendapatan hotel. Setiap reservasi yang masuk memiliki probabilitas untuk dibatalkan. Kemampuan untuk mengestimasi probabilitas ini sebelum tanggal kedatangan adalah aset strategis yang sangat berharga.

### Problem Statements

Berdasarkan latar belakang tersebut, masalah utama yang perlu dipecahkan adalah:
- **Ketidakpastian Pendapatan:** Hotel kesulitan dalam memprediksi pendapatan secara akurat akibat tingginya variabilitas dalam tingkat pembatalan reservasi.
- **Inefisiensi Operasional:** Ketidakmampuan memprediksi pembatalan menyebabkan kesulitan dalam manajemen inventaris kamar, alokasi staf, dan perencanaan sumber daya lainnya.
- **Kurangnya Segmentasi Risiko:** Hotel belum memiliki alat yang efektif untuk mengidentifikasi segmen pelanggan atau tipe pemesanan yang memiliki risiko pembatalan tertinggi, sehingga tidak dapat menerapkan strategi mitigasi yang tertarget.

### Goals

Tujuan dari proyek ini adalah untuk menjawab pernyataan masalah yang telah diuraikan:
- **Mengembangkan Model Prediktif:** Membangun sebuah model klasifikasi *machine learning* yang mampu memprediksi secara akurat apakah sebuah reservasi akan dibatalkan atau tidak.
- **Mengidentifikasi Faktor Kunci:** Menganalisasi dan memahami faktor-faktor utama yang paling berpengaruh terhadap keputusan pembatalan oleh pelanggan.
- **Menyediakan Solusi Terukur:** Menghasilkan model dengan metrik evaluasi yang jelas (seperti Akurasi dan F1-Score) yang dapat dijadikan dasar untuk pengambilan keputusan bisnis.

### Solution Statements

Untuk mencapai tujuan tersebut, beberapa pendekatan solusi akan dieksplorasi dan dibandingkan:
1.  **Pemodelan dengan Algoritma Klasik:** Mengembangkan dan mengevaluasi performa tiga model *machine learning* yang umum digunakan untuk masalah klasifikasi pada data tabular: Regresi Logistik, Random Forest, dan XGBoost. Model dengan performa terbaik akan diidentifikasi sebagai *baseline* yang kuat.
2.  **Peningkatan Performa dengan Hyperparameter Tuning:** Melakukan optimasi pada model terbaik dari pendekatan pertama (Random Forest) menggunakan `GridSearchCV` untuk menemukan kombinasi *hyperparameter* yang optimal, dengan tujuan meningkatkan akurasi dan F1-Score.
3.  **Pemodelan dengan Jaringan Saraf Tiruan (Deep Learning):** Membangun model *deep learning* dengan arsitektur *sequential* sebagai pembanding untuk melihat apakah pendekatan non-linear yang lebih kompleks dapat memberikan performa yang lebih unggul dibandingkan model-model klasik pada dataset ini.

---

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah "Hotel Reservations Classification Dataset" yang bersumber dari platform Kaggle. Dataset ini berisi data reservasi hotel riwayat yang mencakup berbagai atribut pemesanan.

Tautan Dataset: [Kaggle: Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset)

Dataset ini terdiri dari 36.275 baris data (reservasi) dan 19 kolom (fitur). Tidak terdapat nilai yang hilang (*missing values*) pada dataset ini, yang menunjukkan kualitas data awal yang sangat baik.

### Variabel-variabel pada Dataset

Berikut adalah penjelasan untuk setiap variabel (fitur) dalam dataset:
- **Booking_ID**: ID unik untuk setiap reservasi.
- **no_of_adults**: Jumlah tamu dewasa.
- **no_of_children**: Jumlah tamu anak-anak.
- **no_of_weekend_nights**: Jumlah malam akhir pekan (Sabtu atau Minggu) yang dipesan.
- **no_of_week_nights**: Jumlah malam hari kerja (Senin hingga Jumat) yang dipesan.
- **type_of_meal_plan**: Jenis paket makanan yang dipesan.
- **required_car_parking_space**: Indikator (0 atau 1) apakah pelanggan membutuhkan tempat parkir.
- **room_type_reserved**: Tipe kamar yang dipesan.
- **lead_time**: Jarak hari antara tanggal pemesanan dengan tanggal kedatangan.
- **arrival_year**: Tahun kedatangan.
- **arrival_month**: Bulan kedatangan.
- **arrival_date**: Tanggal kedatangan.
- **market_segment_type**: Segmen pasar dari mana reservasi berasal (misalnya, Online, Offline).
- **repeated_guest**: Indikator (0 atau 1) apakah pelanggan tersebut adalah tamu yang pernah menginap sebelumnya.
- **no_of_previous_cancellations**: Jumlah pembatalan sebelumnya oleh pelanggan yang sama.
- **no_of_previous_bookings_not_canceled**: Jumlah pemesanan yang tidak dibatalkan sebelumnya oleh pelanggan yang sama.
- **avg_price_per_room**: Harga rata-rata per kamar per malam.
- **no_of_special_requests**: Jumlah permintaan khusus yang dibuat oleh pelanggan.
- **booking_status**: Variabel target. Bernilai 'Canceled' jika dibatalkan, dan 'Not_Canceled' jika tidak.

### Exploratory Data Analysis (EDA)
![Visualisasi Data](https://raw.githubusercontent.com/Andishafira/Dicoding/main/Belajar%20Machine%20Learning%20Terapan/Tugas%201/Visualisasi%20Data.png)

Analisis data eksploratif dilakukan untuk mendapatkan wawasan awal dari data. Berdasarkan visualisasi yang telah dilakukan:

- **Distribusi Fitur Numerik**: `lead_time` dan `avg_price_per_room` menunjukkan distribusi yang condong ke kanan (*right-skewed*). Ini berarti sebagian besar pemesanan dilakukan dalam rentang waktu yang tidak terlalu jauh dari tanggal kedatangan dengan harga yang moderat.
- **Korelasi dengan Pembatalan**:
    - **Segmen Pasar**: Plot menunjukkan bahwa segmen pasar "Online" memiliki proporsi pembatalan yang jauh lebih tinggi dibandingkan dengan segmen "Offline". Ini logis, karena kemudahan proses pembatalan pada platform online.
    - **Tipe Kamar**: Tipe kamar yang berbeda menunjukkan tingkat pembatalan yang bervariasi, menandakan bahwa fitur ini relevan untuk prediksi.

---

## Data Preparation

Tahapan persiapan data dilakukan untuk memastikan data siap digunakan oleh model *machine learning*. Prosesnya adalah sebagai berikut:

1.  **Penghapusan Fitur Tidak Relevan**: Fitur `Booking_ID` dihapus karena merupakan pengenal unik dan tidak memiliki nilai prediktif.
2.  **Penanganan Nilai Janggal**: Ditemukan bahwa beberapa data pada kolom `avg_price_per_room` memiliki nilai 0. Karena harga kamar 0 sangat tidak umum, nilai ini dianggap sebagai anomali. Nilai-nilai ini diganti dengan nilai median dari kolom tersebut. Median dipilih karena lebih robust terhadap *outlier* dibandingkan rata-rata, terutama pada data dengan distribusi yang condong.
3.  **Encoding Variabel Target**: Variabel target `booking_status` diubah menjadi format numerik biner menggunakan `LabelEncoder`. Nilai 'Not_Canceled' diubah menjadi 1 dan 'Canceled' menjadi 0.
4.  **Pemisahan Fitur**: Fitur-fitur dibagi menjadi dua kelompok: numerik dan kategorikal. Ini diperlukan untuk menerapkan teknik *scaling* dan *encoding* yang berbeda pada masing-masing kelompok.
5.  **Pembuatan Pipeline Preprocessing**: Untuk memastikan konsistensi dan menghindari kebocoran data (*data leakage*), `ColumnTransformer` dan `Pipeline` dari Scikit-learn digunakan.
    - **Fitur Numerik**: `RobustScaler` diterapkan pada fitur-fitur numerik. Scaler ini dipilih karena ketahanannya terhadap *outlier*, yang sesuai dengan karakteristik data seperti `lead_time`.
    - **Fitur Kategorikal**: `OneHotEncoder` diterapkan pada fitur-fitur kategorikal (`type_of_meal_plan`, `room_type_reserved`, `market_segment_type`). Teknik ini mengubah setiap kategori menjadi kolom biner baru, menghindari asumsi urutan antar kategori yang bisa menyesatkan model.
6.  **Pembagian Dataset**: Dataset dibagi menjadi data latih (*training set*) dan data uji (*testing set*) dengan proporsi 70:30. Parameter `stratify=y` digunakan untuk memastikan proporsi kelas target (dibatalkan vs. tidak dibatalkan) tetap sama pada kedua set, yang sangat penting untuk melatih model yang seimbang.

---

## Modeling

Tahapan pemodelan mengikuti pendekatan yang telah diuraikan dalam *solution statements*. Seluruh proses pemodelan digabungkan dengan pipeline pra-pemrosesan untuk memastikan alur kerja yang rapi dan dapat direproduksi.

### 1. Perbandingan Model Machine Learning Klasik

Tiga algoritma dievaluasi untuk mendapatkan performa dasar:

- **Regresi Logistik**:
    - **Kelebihan**: Model ini sederhana, cepat dilatih, dan hasilnya sangat mudah diinterpretasikan. Baik sebagai *baseline* yang kuat.
    - **Kekurangan**: Cenderung memiliki performa yang kurang baik pada masalah yang kompleks karena asumsi hubungan linear antara fitur dan target.
    - **Parameter**: `max_iter` diatur ke 1000 untuk memastikan konvergensi.

- **Random Forest Classifier**:
    - **Kelebihan**: Merupakan model *ensemble* yang kuat, mampu menangkap hubungan non-linear yang kompleks, dan secara inheren tahan terhadap *overfitting* dibandingkan pohon keputusan tunggal.
    - **Kekurangan**: Kurang dapat diinterpretasikan dibandingkan Regresi Logistik dan bisa lebih lambat untuk dilatih.
    - **Parameter**: Menggunakan parameter *default* dari Scikit-learn sebagai titik awal.

- **XGBoost Classifier**:
    - **Kelebihan**: Algoritma *gradient boosting* yang sangat efisien dan kuat, seringkali memberikan performa terbaik pada data tabular.
    - **Kekurangan**: Lebih kompleks untuk di-tuning dan sensitif terhadap *hyperparameter*.
    - **Parameter**: `use_label_encoder=False` dan `eval_metric='logloss'` digunakan sesuai dengan praktik terbaik versi terbaru.

### 2. Peningkatan Model dengan Hyperparameter Tuning

Berdasarkan hasil awal, **Random Forest** menunjukkan F1-Score tertinggi. Oleh karena itu, model ini dipilih untuk dioptimasi lebih lanjut.
- **Proses**: `GridSearchCV` digunakan untuk mencari kombinasi *hyperparameter* terbaik secara sistematis.
- **Parameter yang Diuji**:
    - `n_estimators`: [100, 200] (Jumlah pohon dalam forest)
    - `max_depth`: [10, 20, None] (Kedalaman maksimum setiap pohon)
    - `min_samples_split`: [2, 5] (Jumlah sampel minimum untuk membagi sebuah node)
- **Hasil**: Parameter terbaik yang ditemukan adalah `{'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 200}`.

### 3. Model Deep Learning

Sebagai pembanding, sebuah model Jaringan Saraf Tiruan (ANN) juga dibangun.
- **Arsitektur**: Model *sequential* dengan tiga *hidden layer* (masing-masing 256 neuron dengan aktivasi ReLU) dan lapisan *dropout* (rate 0.3) setelah setiap *hidden layer* untuk regularisasi. Lapisan *output* menggunakan aktivasi Sigmoid untuk masalah klasifikasi biner.
- **Proses Pelatihan**: Model dikompilasi dengan *optimizer* 'Adam' dan *loss function* 'binary_crossentropy'. *Callbacks* `EarlyStopping` (dengan *patience* 15 pada `val_loss`) dan `ReduceLROnPlateau` digunakan untuk menghentikan pelatihan jika tidak ada kemajuan dan menyesuaikan *learning rate* secara dinamis.

---

## Evaluation

Metrik evaluasi yang digunakan harus sesuai dengan konteks masalah. Dalam kasus ini, tujuan bisnisnya adalah meminimalkan kerugian akibat pembatalan, sehingga penting untuk menyeimbangkan antara presisi dan recall.

### Metrik Evaluasi

* **Akurasi**: Proporsi prediksi yang benar dari total prediksi.  

  $$
  \text{Akurasi} = \frac{TP + TN}{TP + TN + FP + FN}
  $$

* **F1-Score**: Rata-rata harmonik dari presisi dan recall.  
  Metrik ini sangat baik digunakan ketika terdapat ketidakseimbangan kelas atau ketika biaya *false positive* dan *false negative* perlu diseimbangkan.  

$$
F1 = 2 \times \frac{\mathrm{Presisi} \times \mathrm{Recall}}{\mathrm{Presisi} + \mathrm{Recall}}
$$

  * **Presisi**: Dari semua yang diprediksi 'Tidak Batal', berapa persen yang benar-benar tidak batal.

  $$
  \mathrm{Presisi} = \frac{TP}{TP + FP}
  $$
  
  * **Recall**: Dari semua yang seharusnya 'Tidak Batal', berapa persen yang berhasil diprediksi dengan benar.  

  $$
  \mathrm{Recall} = \frac{TP}{TP + FN}
  $$

Dalam konteks ini, **F1-Score** dianggap sebagai metrik utama karena memberikan gambaran yang lebih seimbang tentang performa model dalam mengidentifikasi kedua kelas.

### Hasil Evaluasi

Berikut adalah ringkasan performa dari semua model yang telah diuji pada *test set*:

| Model | Accuracy | F1 Score |
| :--- | :---: | :---: |
| **Random Forest (Default)** | **0.9037** | **0.9299** |
| Optimized Random Forest | 0.9011 | 0.9281 |
| XGBoost | 0.8971 | 0.9248 |
| Deep Learning | 0.8798 | 0.9100 |
| Logistic Regression | 0.8081 | 0.8624 |

**Analisis Hasil**:
- **Model Terbaik**: **Random Forest** dengan parameter *default* memberikan performa tertinggi, baik dari segi Akurasi (90.4%) maupun F1-Score (0.930).
- **Performa Ensemble vs. Linear**: Model berbasis *ensemble* (Random Forest, XGBoost) secara signifikan mengungguli model linear (Regresi Logistik). Hal ini mengindikasikan bahwa hubungan antara fitur dan probabilitas pembatalan bersifat non-linear dan kompleks.
- **Hasil Optimasi**: Menariknya, model Random Forest yang telah dioptimasi dengan `GridSearchCV` memiliki performa yang sedikit lebih rendah daripada model dengan parameter *default*. Ini bisa berarti bahwa parameter *default* dari Scikit-learn sudah sangat cocok untuk dataset ini, atau rentang pencarian pada `GridSearchCV` perlu diperluas. Namun, perbedaan yang sangat kecil ini (kurang dari 0.2%) pada dasarnya dapat diabaikan, yang menunjukkan model sudah cukup stabil.
- **Perbandingan dengan Deep Learning**: Model *deep learning* menunjukkan performa yang kuat (F1-Score 0.91), namun masih sedikit di bawah model *ensemble tree*. Ini adalah fenomena yang cukup umum pada data tabular terstruktur di mana model seperti Random Forest dan XGBoost seringkali menjadi pilihan yang sangat kompetitif atau bahkan lebih unggul.

**Kesimpulan Akhir**:
Berdasarkan metrik F1-Score, **Random Forest Classifier (dengan parameter default)** adalah model terbaik untuk tugas prediksi pembatalan reservasi hotel pada dataset ini. Model ini mampu memberikan keseimbangan yang sangat baik antara presisi dan recall, menjadikannya alat yang andal untuk mendukung pengambilan keputusan manajemen pendapatan hotel.
