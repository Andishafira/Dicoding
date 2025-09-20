# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

### Latar Belakang Bisnis

Institusi pendidikan Jaya Jaya University menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

---

### Permasalahan Bisnis

Permasalahan utama adalah untuk mengidentifikasi faktor-faktor penentu yang membedakan antara mahasiswa yang berhasil "Lulus" (Graduate) dan yang "Putus Studi" (Dropout). Institusi perlu membangun sebuah sistem prediktif untuk menandai mahasiswa yang berisiko dropout sedini mungkin, sehingga sumber daya pendukung akademik dan non-akademik dapat dialokasikan secara efektif.

---

### Cakupan Proyek

Cakupan proyek ini meliputi:

1. **Analisis Data Eksploratif (EDA)**: Untuk memahami data demografis, akademik, dan sosio-ekonomi mahasiswa serta hubungannya dengan status kelulusan.
2. **Pemrosesan Data**: Membersihkan data, melakukan feature selection, scaling pada fitur numerik, dan encoding pada fitur kategorikal.
   
3. **Pengembangan Model**: Membangun model klasifikasi machine learning (Random Forest) untuk memprediksi status akhir mahasiswa (Lulus atau Dropout).
4. **Pengembangan Model**: Membangun model klasifikasi machine learning (Random Forest) untuk memprediksi status akhir mahasiswa (Lulus atau Dropout).
5. **Evaluasi Model**: Mengevaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan F1-score.
6. **Deployment** : Membuat prototipe aplikasi web interaktif menggunakan Streamlit untuk mempermudah penggunaan model prediksi
7. **Visualisasi Dashboard**: Menyajikan temuan-temuan kunci dan KPI dalam sebuah dashboard bisnis.

---

### Persiapan

**Sumber Data :**
Dataset diambil dari repositori GitHub dan dimuat ke dalam dataframe dengan sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

**Setup Environment :**

Untuk memastikan proyek berjalan di lingkungan yang terisolasi, stabil, dan memiliki semua pustaka yang diperlukan, ikuti instruksi penyiapan berikut:

1. Klona (Clone) Repositori Proyek
Buka terminal atau Command Prompt, kemudian jalankan perintah berikut untuk menginduh semua file dari repository.

```git clone https://github.com/Andishafira/Dicoding.git```

Setelah selesai, masuk ke direktori repositori yang baru saja diunduh:

```cd Dicoding```

2. Membuat dan Mengaktifkan Virtual Environment (`venv`)

Sangat disarankan untuk membuat virtual environment agar dependensi proyek (pustaka) tidak bercampur dengan instalasi Python global.

  * Dari dalam direktori Dicoding, buat environment baru (misalnya, dengan nama `venv`):

    ```python -m venv venv```

  * Selanjutnya, aktifkan environment tersebut
    * Di Windows ;

       ```.\venv\Scripts\activate```
      
    * Di macOS/Linux:
      
      ```source venv/bin/activate```
      
Setelah aktif, nama environment (`venv`) akan muncul di awal baris terminal.


3. Menginstal Dependensi dari `requirements.txt`

   
Setelah virtual environment aktif, instal semua pustaka yang diperlukan yang sudah terdaftar dalam file `requirements.txt` menggunakan pip:

```pip install -r requirements.txt```

Perintah ini akan secara otomatis mengunduh dan menginstal semua pustaka seperti streamlit, pandas, scikit-learn, dll., dengan versi yang tepat.

Setelah ketiga langkah ini selesai, lingkungan telah siap. Anda dapat melanjutkan untuk menjalankan proses training di notebook atau langsung menjalankan aplikasi Streamlit.


---

## Business Dashboard

Bussiness Dashboard dibuat menggunakan Google Looker Studio dan dapat diakses online menggunakan link : https://lookerstudio.google.com/reporting/3418ee20-b0bb-4347-9e83-2389bed4e706

![Dashboard](https://raw.githubusercontent.com/Andishafira/Dicoding/main/Belajar_Penerapan_Data_Science/Tugas_2_Menyelesaikan_Permasalahan_Institusi_Pendidikan/Dashboard/Andisha-Dashboard.png)


Dashboard ini menyajikan gambaran umum (snapshot) mengenai status akademik mahasiswa di Universitas Jaya, dengan fokus utama untuk memahami faktor-faktor yang berkaitan dengan kelulusan (Graduate) dan putus studi (Dropout). Dashboard ini dibuat menggunakan dataset yang telah didecoding sehingga lebih mudah dibaca dan dimengerti. 

1. **Statistik Utama**

Panel di bagian atas memberikan informasi informasi penting yaitu:

  * Total Mahasiswa: Terdapat 4.420 mahasiswa dalam dataset ini.

  * Status Utama: Dari total tersebut, 2.210 (50.0%) telah Lulus, 1.420 (32.1%) telah Putus Studi (Dropout), dan 794 (17.9%) masih Terdaftar (Enrolled).

  * Permasalahan Utama: Angka Dropout Rate sebesar 32.1% sangat signifikan dan menjadi masalah utama yang perlu diinvestigasi. Ini menunjukkan bahwa hampir sepertiga dari mahasiswa gagal menyelesaikan studi mereka.

**Temuan** : dari total populasi mahasiswa, hampir setengah berhasil lulus, sepertiga mengalami dropout, dan sisanya masih berstatus aktif/enrolled

2. **Distribusi Status Mahasiswa (pie chart)**

Grafik ini memvisualisasikan proporsi dari tiga status mahasiswa.

  * Lulus (49,9%): Setengah dari populasi mahasiswa dalam data ini berhasil lulus.

  * Dropout (32.1%): Cukup tinggi, lebih dari 3 mahasiswa dari 10 berhenti di tengah jalan.

  * Terdaftar (17.9%): Ini adalah kelompok minoritas, mahasiswa yang masih aktif menjalani studi.

**Temuan**: Tingginya dropout rate (32%) menunjukkan adanya masalah signifikan pada keberlangsungan studi mahasiswa.

3. **Distribusi Dropout Berdasarkan Jurusan**
Jurusan dengan dropout terbanyak:

   - Management (Evening)
   - Management (Reguler)
   - Nursing
   - Journalism and Communication

**Temuan**:

Jurusan manajemen (baik reguler maupun kelas malam) dan keperawatan memiliki jumlah dropout tinggi. Hal ini bisa terkait faktor beban akademik, biaya, atau kurangnya dukungan belajar. Jurusan-jurusan dengan orientasi praktik tinggi (Nursing, Tourism, Journalism) juga rentan dropout.

4. **Distribusi Lulusan Berdasarkan Jurusan**

   Jurusan dengan lulusan terbanyak:
   
   - Nursing (hampir 600 lulusan)
   - Social Service
   - Journalism and Communication
   - Veterinary Nursing
   - Management

**Temuan**:

Meski memiliki dropout tinggi, Nursing tetap menghasilkan jumlah lulusan terbanyak, menunjukkan daya tarik jurusan ini kuat meskipun tingkat kesulitan juga tinggi.

5. **Faktor yang Mempengaruhi Dropout**

Variabel paling berpengaruh:

   - Curricular Units Semester 2

   - Curricular Units Semester 1

   - Tuition Fees Up to Date

   - Age at Enrollment

   - Application Mode

**Temuan**:

  * Nilai akademik (semester 1 & 2) merupakan indikator paling besar terhadap dropout → mahasiswa dengan nilai rendah berisiko tinggi keluar.

  * Masalah keuangan (tuition fees) juga krusial → mahasiswa dengan keterlambatan pembayaran lebih rentan dropout.

  * Faktor demografis (usia saat masuk, jalur pendaftaran) berperan, meski lebih kecil.

6. **Rata-Rata Nilai Akademik Berdasarkan Status**

**Temuan**:

  * Lulusan memiliki nilai jauh lebih tinggi dibanding yang dropout.

  * Mahasiswa yang dropout mengalami penurunan nilai signifikan dari semester 1 ke semester 2 → mengindikasikan kesulitan akademik yang makin berat.

  * Mahasiswa yang masih aktif (enrolled) berada di tengah-tengah, masih punya peluang lulus jika performa akademik meningkat.

**Kesimpulan Analisis Keseluruhan Laporan Dashboard Visualisasi**

1. Dropout Rate Tinggi (32%) → hampir 1 dari 3 mahasiswa tidak menyelesaikan studi, ini angka yang cukup kritis untuk kualitas pendidikan.
2. Faktor Akademik adalah Penentu Utama → nilai semester 1 & 2 menjadi indikator dropout terbesar, mahasiswa yang gagal adaptasi sejak awal kuliah sangat berisiko keluar.
3. Masalah Finansial Memperburuk Risiko Dropout → keterlambatan pembayaran biaya kuliah turut memengaruhi keberlangsungan studi.
4. Jurusan dengan Tingkat Dropout Tinggi → terutama Manajemen dan Keperawatan, perlu intervensi khusus seperti bimbingan akademik, konseling, atau dukungan finansial.
5. Nilai Mahasiswa Dropout Sangat Rendah → menunjukkan pola gagal adaptasi akademik, mungkin karena metode pengajaran, beban studi terlalu berat, atau kurangnya support sistem.

---
## Menjalankan Sistem Machine Learning

Prototipe sistem machine learning ini telah di-deploy sebagai aplikasi web interaktif menggunakan Streamlit. Proses training model asli dilakukan dalam notebook Jupyter (`Tugas_2_Jaya_University_fix.ipynb`), yang kemudian menyimpan model terlatih dan scaler/encoder sebagai file `.joblib`.

Aplikasi Streamlit (`app.py`), dengan bantuan modul `preprocessing.py` dan `prediction.py`, kemudian memuat file-file ini untuk melakukan prediksi secara real-time berdasarkan input pengguna.

**Cara Menjalankan Prototipe (Lokal):**

1. Pastikan memiliki file ` app.py `, ` preprocessing.py `, ` prediction.py `, dan semua file ` .joblib ` (model dan encoders/scalers) dalam satu direktori.

2. Instal semua pustaka yang diperlukan (termasuk streamlit) dari file ` requirements.txt. `

3. Buka terminal atau command prompt, navigasi ke direktori tersebut, dan jalankan perintah:

` streamlit run app.py `

4. Aplikasi akan otomatis terbuka di browser Anda. Pengguna dapat memasukkan 10 fitur yang diperlukan di sidebar untuk mendapatkan prediksi status mahasiswa (Lulus atau Dropout).

**Cara Menjalankan Prototipe (Online):**

Akses link berikut : https://dicoding-student-performance-andi-shafira.streamlit.app/

---

## Conclusion

Model machine learning (Random Forest Classifier) berhasil dikembangkan untuk memprediksi status kelulusan mahasiswa dengan akurasi 88.84% pada data uji.

* Kinerja Model: Model menunjukkan kinerja yang baik, terutama dalam mengidentifikasi mahasiswa yang akan "Lulus" (Recall 0.93) dan cukup baik dalam mendeteksi mahasiswa yang berisiko "Dropout" (Recall 0.82).

* Faktor Prediktif Utama: Analisis feature importance menunjukkan bahwa faktor akademik adalah prediktor terkuat. Fitur-fitur seperti:

   - `Curricular_units_2nd_sem_approved` (Jumlah mata kuliah lulus di semester 2)
   - `Curricular_units_1st_sem_approved` (Jumlah mata kuliah lulus di semester 1)
   - `Curricular_units_2nd_sem_grade` (Rata-rata nilai semester 2)
   - `Curricular_units_1st_sem_grade` (Rata-rata nilai semester 1)

* Faktor finansial, seperti Tuition_fees_up_to_date (Status pembayaran UKT), juga terbukti menjadi prediktor penting.

---

### Rekomendasi Action Items

Berdasarkan temuan tersebut, berikut adalah beberapa rekomendasi untuk institusi:

- Implementasi Sistem Peringatan Dini: Institusi harus menggunakan aplikasi prediktif (seperti prototipe Streamlit yang dibuat) untuk secara otomatis menandai mahasiswa yang menunjukkan kinerja akademik di bawah rata-rata pada semester 1 dan 2. Mahasiswa ini harus segera mendapatkan bimbingan akademik intensif.
- Intervensi Finansial Proaktif: Mengingat Tuition_fees_up_to_date adalah faktor penting, bagian administrasi keuangan harus proaktif menghubungi mahasiswa yang memiliki tunggakan (tetapi belum berstatus Debtor) untuk menawarkan skema pembayaran yang fleksibel atau bantuan keuangan, guna mencegah mereka dropout karena alasan finansial.
- Fokus pada Keterlibatan Semester Awal: Keberhasilan di dua semester pertama sangat krusial. Institusi disarankan memperkuat program orientasi dan program mentoring antar-mahasiswa (senior-junior) untuk membantu mahasiswa baru beradaptasi dan berhasil secara akademik di tahun pertama mereka.
