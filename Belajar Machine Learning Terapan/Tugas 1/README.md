\# Laporan Proyek Machine Learning - Prediksi Pembatalan Reservasi Hotel



\## Domain Proyek



Industri perhotelan merupakan salah satu pilar utama sektor pariwisata yang sangat kompetitif dan sensitif terhadap dinamika pasar. Salah satu tantangan operasional dan finansial terbesar yang dihadapi oleh hotel adalah pembatalan reservasi. Pembatalan, terutama yang terjadi mendekati tanggal kedatangan, secara langsung berdampak pada hilangnya pendapatan (\*revenue loss\*) karena kamar yang telah dipesan menjadi kosong dan sulit untuk dijual kembali dalam waktu singkat.



Menurut sebuah studi, tingkat pembatalan reservasi hotel bisa mencapai 20% secara global, dan angka ini dapat meningkat hingga 40% pada beberapa segmen pasar, terutama pemesanan online \[1]. Fenomena ini memaksa hotel untuk menerapkan strategi manajemen pendapatan yang kompleks, seperti \*overbooking\* (menjual lebih banyak kamar daripada yang tersedia). Namun, strategi \*overbooking\* sendiri memiliki risiko tinggi; jika prediksi pembatalan tidak akurat, hotel dapat menghadapi situasi kekurangan kamar yang berakibat pada kekecewaan pelanggan, biaya kompensasi, dan kerusakan reputasi jangka panjang.



Oleh karena itu, kemampuan untuk memprediksi kemungkinan seorang pelanggan membatalkan reservasi menjadi sangat krusial. Dengan model prediksi yang akurat, manajer hotel dapat membuat keputusan yang lebih cerdas dan berbasis data untuk mengoptimalkan tingkat hunian, menyesuaikan kebijakan pemesanan, dan pada akhirnya memaksimalkan pendapatan. Proyek ini bertujuan untuk membangun model \*machine learning\* yang mampu mengklasifikasikan status pemesanan hotel (dibatalkan atau tidak) berdasarkan data historis reservasi.



\*\*Referensi:\*\*

\[1] K. Kraja, "Factors affecting cancelation of hotel reservation," \*Academic Journal of Interdisciplinary Studies\*, vol. 9, no. 1, p. 16, 2020. \[Online]. Tersedia: \[https://www.richtmann.org/journal/index.php/ajis/article/view/11130](https://www.richtmann.org/journal/index.php/ajis/article/view/11130).



\## Business Understanding



Proses bisnis utama yang menjadi fokus adalah manajemen reservasi dan pendapatan hotel. Setiap reservasi yang masuk memiliki probabilitas untuk dibatalkan. Kemampuan untuk mengestimasi probabilitas ini sebelum tanggal kedatangan adalah aset strategis yang sangat berharga.



\### Problem Statements



Berdasarkan latar belakang tersebut, masalah utama yang perlu dipecahkan adalah:

\- \*\*Ketidakpastian Pendapatan:\*\* Hotel kesulitan dalam memprediksi pendapatan secara akurat akibat tingginya variabilitas dalam tingkat pembatalan reservasi.

\- \*\*Inefisiensi Operasional:\*\* Ketidakmampuan memprediksi pembatalan menyebabkan kesulitan dalam manajemen inventaris kamar, alokasi staf, dan perencanaan sumber daya lainnya.

\- \*\*Kurangnya Segmentasi Risiko:\*\* Hotel belum memiliki alat yang efektif untuk mengidentifikasi segmen pelanggan atau tipe pemesanan yang memiliki risiko pembatalan tertinggi, sehingga tidak dapat menerapkan strategi mitigasi yang tertarget.



\### Goals



Tujuan dari proyek ini adalah untuk menjawab pernyataan masalah yang telah diuraikan:

\- \*\*Mengembangkan Model Prediktif:\*\* Membangun sebuah model klasifikasi \*machine learning\* yang mampu memprediksi secara akurat apakah sebuah reservasi akan dibatalkan atau tidak.

\- \*\*Mengidentifikasi Faktor Kunci:\*\* Menganalisis dan memahami faktor-faktor utama yang paling berpengaruh terhadap keputusan pembatalan oleh pelanggan.

\- \*\*Menyediakan Solusi Terukur:\*\* Menghasilkan model dengan metrik evaluasi yang jelas (seperti Akurasi dan F1-Score) yang dapat dijadikan dasar untuk pengambilan keputusan bisnis.



\### Solution Statements



Untuk mencapai tujuan tersebut, beberapa pendekatan solusi akan dieksplorasi dan dibandingkan:

1\.  \*\*Pemodelan dengan Algoritma Klasik:\*\* Mengembangkan dan mengevaluasi performa tiga model \*machine learning\* yang umum digunakan untuk masalah klasifikasi pada data tabular: Regresi Logistik, Random Forest, dan XGBoost. Model dengan performa terbaik akan diidentifikasi sebagai \*baseline\* yang kuat.

2\.  \*\*Peningkatan Performa dengan Hyperparameter Tuning:\*\* Melakukan optimasi pada model terbaik dari pendekatan pertama (Random Forest) menggunakan `GridSearchCV` untuk menemukan kombinasi \*hyperparameter\* yang optimal, dengan tujuan meningkatkan akurasi dan F1-Score.

3\.  \*\*Pemodelan dengan Jaringan Saraf Tiruan (Deep Learning):\*\* Membangun model \*deep learning\* dengan arsitektur \*sequential\* sebagai pembanding untuk melihat apakah pendekatan non-linear yang lebih kompleks dapat memberikan performa yang lebih unggul dibandingkan model-model klasik pada dataset ini.



\## Data Understanding



Dataset yang digunakan dalam proyek ini adalah "Hotel Reservations Classification Dataset" yang bersumber dari platform Kaggle. Dataset ini berisi data reservasi hotel riwayat yang mencakup berbagai atribut pemesanan.



Tautan Dataset: \[Kaggle: Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset)



Dataset ini terdiri dari 36.275 baris data (reservasi) dan 19 kolom (fitur). Tidak terdapat nilai yang hilang (\*missing values\*) pada dataset ini, yang menunjukkan kualitas data awal yang sangat baik.



\### Variabel-variabel pada Dataset



Berikut adalah penjelasan untuk setiap variabel (fitur) dalam dataset:

\- \*\*Booking\_ID\*\*: ID unik untuk setiap reservasi.

\- \*\*no\_of\_adults\*\*: Jumlah tamu dewasa.

\- \*\*no\_of\_children\*\*: Jumlah tamu anak-anak.

\- \*\*no\_of\_weekend\_nights\*\*: Jumlah malam akhir pekan (Sabtu atau Minggu) yang dipesan.

\- \*\*no\_of\_week\_nights\*\*: Jumlah malam hari kerja (Senin hingga Jumat) yang dipesan.

\- \*\*type\_of\_meal\_plan\*\*: Jenis paket makanan yang dipesan.

\- \*\*required\_car\_parking\_space\*\*: Indikator (0 atau 1) apakah pelanggan membutuhkan tempat parkir.

\- \*\*room\_type\_reserved\*\*: Tipe kamar yang dipesan.

\- \*\*lead\_time\*\*: Jarak hari antara tanggal pemesanan dengan tanggal kedatangan.

\- \*\*arrival\_year\*\*: Tahun kedatangan.

\- \*\*arrival\_month\*\*: Bulan kedatangan.

\- \*\*arrival\_date\*\*: Tanggal kedatangan.

\- \*\*market\_segment\_type\*\*: Segmen pasar dari mana reservasi berasal (misalnya, Online, Offline).

\- \*\*repeated\_guest\*\*: Indikator (0 atau 1) apakah pelanggan tersebut adalah tamu yang pernah menginap sebelumnya.

\- \*\*no\_of\_previous\_cancellations\*\*: Jumlah pembatalan sebelumnya oleh pelanggan yang sama.

\- \*\*no\_of\_previous\_bookings\_not\_canceled\*\*: Jumlah pemesanan yang tidak dibatalkan sebelumnya oleh pelanggan yang sama.

\- \*\*avg\_price\_per\_room\*\*: Harga rata-rata per kamar per malam.

\- \*\*no\_of\_special\_requests\*\*: Jumlah permintaan khusus yang dibuat oleh pelanggan.

\- \*\*booking\_status\*\*: Variabel target. Bernilai 'Canceled' jika dibatalkan, dan 'Not\_Canceled' jika tidak.



\### Exploratory Data Analysis (EDA)



Analisis data eksploratif dilakukan untuk mendapatkan wawasan awal dari data. Berdasarkan visualisasi yang telah dilakukan:



\- \*\*Distribusi Fitur Numerik\*\*: `lead\_time` dan `avg\_price\_per\_room` menunjukkan distribusi yang condong ke kanan (\*right-skewed\*). Ini berarti sebagian besar pemesanan dilakukan dalam rentang waktu yang tidak terlalu jauh dari tanggal kedatangan dengan harga yang moderat.

\- \*\*Korelasi dengan Pembatalan\*\*:

&nbsp; - \*\*Segmen Pasar\*\*: Plot menunjukkan bahwa segmen pasar "Online" memiliki proporsi pembatalan yang jauh lebih tinggi dibandingkan dengan segmen "Offline". Ini logis, karena kemudahan proses pembatalan pada platform online.

&nbsp; - \*\*Tipe Kamar\*\*: Tipe kamar yang berbeda menunjukkan tingkat pembatalan yang bervariasi, menandakan bahwa fitur ini relevan untuk prediksi.



\## Data Preparation



Tahapan persiapan data dilakukan untuk memastikan data siap digunakan oleh model \*machine learning\*. Prosesnya adalah sebagai berikut:



1\.  \*\*Penghapusan Fitur Tidak Relevan\*\*: Fitur `Booking\_ID` dihapus karena merupakan pengenal unik dan tidak memiliki nilai prediktif.



2\.  \*\*Penanganan Nilai Janggal\*\*: Ditemukan bahwa beberapa data pada kolom `avg\_price\_per\_room` memiliki nilai 0. Karena harga kamar 0 sangat tidak umum, nilai ini dianggap sebagai anomali. Nilai-nilai ini diganti dengan nilai median dari kolom tersebut. Median dipilih karena lebih robust terhadap \*outlier\* dibandingkan rata-rata, terutama pada data dengan distribusi yang condong.



3\.  \*\*Encoding Variabel Target\*\*: Variabel target `booking\_status` diubah menjadi format numerik biner menggunakan `LabelEncoder`. Nilai 'Not\_Canceled' diubah menjadi 1 dan 'Canceled' menjadi 0.



4\.  \*\*Pemisahan Fitur\*\*: Fitur-fitur dibagi menjadi dua kelompok: numerik dan kategorikal. Ini diperlukan untuk menerapkan teknik \*scaling\* dan \*encoding\* yang berbeda pada masing-masing kelompok.



5\.  \*\*Pembuatan Pipeline Preprocessing\*\*: Untuk memastikan konsistensi dan menghindari kebocoran data (\*data leakage\*), `ColumnTransformer` dan `Pipeline` dari Scikit-learn digunakan.

&nbsp;   - \*\*Fitur Numerik\*\*: `RobustScaler` diterapkan pada fitur-fitur numerik. Scaler ini dipilih karena ketahanannya terhadap \*outlier\*, yang sesuai dengan karakteristik data seperti `lead\_time`.

&nbsp;   - \*\*Fitur Kategorikal\*\*: `OneHotEncoder` diterapkan pada fitur-fitur kategorikal (`type\_of\_meal\_plan`, `room\_type\_reserved`, `market\_segment\_type`). Teknik ini mengubah setiap kategori menjadi kolom biner baru, menghindari asumsi urutan antar kategori yang bisa menyesatkan model.



6\.  \*\*Pembagian Dataset\*\*: Dataset dibagi menjadi data latih (\*training set\*) dan data uji (\*testing set\*) dengan proporsi 70:30. Parameter `stratify=y` digunakan untuk memastikan proporsi kelas target (dibatalkan vs. tidak dibatalkan) tetap sama pada kedua set, yang sangat penting untuk melatih model yang seimbang.



\## Modeling



Tahapan pemodelan mengikuti pendekatan yang telah diuraikan dalam \*solution statements\*. Seluruh proses pemodelan digabungkan dengan pipeline pra-pemrosesan untuk memastikan alur kerja yang rapi dan dapat direproduksi.



\### 1. Perbandingan Model Machine Learning Klasik



Tiga algoritma dievaluasi untuk mendapatkan performa dasar:



\- \*\*Regresi Logistik\*\*:

&nbsp; - \*\*Kelebihan\*\*: Model ini sederhana, cepat dilatih, dan hasilnya sangat mudah diinterpretasikan. Baik sebagai \*baseline\* yang kuat.

&nbsp; - \*\*Kekurangan\*\*: Cenderung memiliki performa yang kurang baik pada masalah yang kompleks karena asumsi hubungan linear antara fitur dan target.

&nbsp; - \*\*Parameter\*\*: `max\_iter` diatur ke 1000 untuk memastikan konvergensi.



\- \*\*Random Forest Classifier\*\*:

&nbsp; - \*\*Kelebihan\*\*: Merupakan model \*ensemble\* yang kuat, mampu menangkap hubungan non-linear yang kompleks, dan secara inheren tahan terhadap \*overfitting\* dibandingkan pohon keputusan tunggal.

&nbsp; - \*\*Kekurangan\*\*: Kurang dapat diinterpretasikan dibandingkan Regresi Logistik dan bisa lebih lambat untuk dilatih.

&nbsp; - \*\*Parameter\*\*: Menggunakan parameter \*default\* dari Scikit-learn sebagai titik awal.



\- \*\*XGBoost Classifier\*\*:

&nbsp; - \*\*Kelebihan\*\*: Algoritma \*gradient boosting\* yang sangat efisien dan kuat, seringkali memberikan performa terbaik pada data tabular.

&nbsp; - \*\*Kekurangan\*\*: Lebih kompleks untuk di-tuning dan sensitif terhadap \*hyperparameter\*.

&nbsp; - \*\*Parameter\*\*: `use\_label\_encoder=False` dan `eval\_metric='logloss'` digunakan sesuai dengan praktik terbaik versi terbaru.



\### 2. Peningkatan Model dengan Hyperparameter Tuning



Berdasarkan hasil awal, \*\*Random Forest\*\* menunjukkan F1-Score tertinggi. Oleh karena itu, model ini dipilih untuk dioptimasi lebih lanjut.

\- \*\*Proses\*\*: `GridSearchCV` digunakan untuk mencari kombinasi \*hyperparameter\* terbaik secara sistematis.

\- \*\*Parameter yang Diuji\*\*:

&nbsp; - `n\_estimators`: \[100, 200] (Jumlah pohon dalam forest)

&nbsp; - `max\_depth`: \[10, 20, None] (Kedalaman maksimum setiap pohon)

&nbsp; - `min\_samples\_split`: \[2, 5] (Jumlah sampel minimum untuk membagi sebuah node)

\- \*\*Hasil\*\*: Parameter terbaik yang ditemukan adalah `{'max\_depth': 20, 'min\_samples\_split': 2, 'n\_estimators': 200}`.



\### 3. Model Deep Learning



Sebagai pembanding, sebuah model Jaringan Saraf Tiruan (ANN) juga dibangun.

\- \*\*Arsitektur\*\*: Model \*sequential\* dengan tiga \*hidden layer\* (masing-masing 256 neuron dengan aktivasi ReLU) dan lapisan \*dropout\* (rate 0.3) setelah setiap \*hidden layer\* untuk regularisasi. Lapisan \*output\* menggunakan aktivasi Sigmoid untuk masalah klasifikasi biner.

\- \*\*Proses Pelatihan\*\*: Model dikompilasi dengan \*optimizer\* 'Adam' dan \*loss function\* 'binary\_crossentropy'. \*Callbacks\* `EarlyStopping` (dengan \*patience\* 15 pada `val\_loss`) dan `ReduceLROnPlateau` digunakan untuk menghentikan pelatihan jika tidak ada kemajuan dan menyesuaikan \*learning rate\* secara dinamis.



\## Evaluation



Metrik evaluasi yang digunakan harus sesuai dengan konteks masalah. Dalam kasus ini, tujuan bisnisnya adalah meminimalkan kerugian akibat pembatalan, sehingga penting untuk menyeimbangkan antara presisi dan recall.



\### Metrik Evaluasi



\- \*\*Akurasi\*\*: Proporsi prediksi yang benar dari total prediksi.

&nbsp; $$

&nbsp; \\text{Akurasi} = \\frac{\\text{TP} + \\text{TN}}{\\text{TP} + \\text{TN} + \\text{FP} + \\text{FN}}

&nbsp; $$

\- \*\*F1-Score\*\*: Rata-rata harmonik dari presisi dan recall. Metrik ini sangat baik digunakan ketika terdapat ketidakseimbangan kelas atau ketika biaya \*false positive\* dan \*false negative\* perlu diseimbangkan.

&nbsp; $$

&nbsp; \\text{F1-Score} = 2 \\times \\frac{\\text{Presisi} \\times \\text{Recall}}{\\text{Presisi} + \\text{Recall}}

&nbsp; $$

&nbsp; - \*\*Presisi\*\*: Dari semua yang diprediksi 'Tidak Batal', berapa persen yang benar-benar tidak batal.

&nbsp; - \*\*Recall\*\*: Dari semua yang seharusnya 'Tidak Batal', berapa persen yang berhasil diprediksi dengan benar.



Dalam konteks ini, \*\*F1-Score\*\* dianggap sebagai metrik utama karena memberikan gambaran yang lebih seimbang tentang performa model dalam mengidentifikasi kedua kelas.



\### Hasil Evaluasi



Berikut adalah ringkasan performa dari semua model yang telah diuji pada \*test set\*:



| Model | Accuracy | F1 Score |

| :--- | :---: | :---: |

| \*\*Random Forest (Default)\*\* | \*\*0.9037\*\* | \*\*0.9299\*\* |

| Optimized Random Forest | 0.9011 | 0.9281 |

| XGBoost | 0.8971 | 0.9248 |

| Deep Learning | 0.8798 | 0.9100 |

| Logistic Regression | 0.8081 | 0.8624 |



\*\*Analisis Hasil\*\*:

\- \*\*Model Terbaik\*\*: \*\*Random Forest\*\* dengan parameter \*default\* memberikan performa tertinggi, baik dari segi Akurasi (90.4%) maupun F1-Score (0.930).

\- \*\*Performa Ensemble vs. Linear\*\*: Model berbasis \*ensemble\* (Random Forest, XGBoost) secara signifikan mengungguli model linear (Regresi Logistik). Hal ini mengindikasikan bahwa hubungan antara fitur dan probabilitas pembatalan bersifat non-linear dan kompleks.

\- \*\*Hasil Optimasi\*\*: Menariknya, model Random Forest yang telah dioptimasi dengan `GridSearchCV` memiliki performa yang sedikit lebih rendah daripada model dengan parameter \*default\*. Ini bisa berarti bahwa parameter \*default\* dari Scikit-learn sudah sangat cocok untuk dataset ini, atau rentang pencarian pada `GridSearchCV` perlu diperluas. Namun, perbedaan yang sangat kecil ini (kurang dari 0.2%) pada dasarnya dapat diabaikan, yang menunjukkan model sudah cukup stabil.

\- \*\*Perbandingan dengan Deep Learning\*\*: Model \*deep learning\* menunjukkan performa yang kuat (F1-Score 0.91), namun masih sedikit di bawah model \*ensemble tree\*. Ini adalah fenomena yang cukup umum pada data tabular terstruktur di mana model seperti Random Forest dan XGBoost seringkali menjadi pilihan yang sangat kompetitif atau bahkan lebih unggul.



\*\*Kesimpulan Akhir\*\*:

Berdasarkan metrik F1-Score, \*\*Random Forest Classifier (dengan parameter default)\*\* adalah model terbaik untuk tugas prediksi pembatalan reservasi hotel pada dataset ini. Model ini mampu memberikan keseimbangan yang sangat baik antara presisi dan recall, menjadikannya alat yang andal untuk mendukung pengambilan keputusan manajemen pendapatan hotel.

