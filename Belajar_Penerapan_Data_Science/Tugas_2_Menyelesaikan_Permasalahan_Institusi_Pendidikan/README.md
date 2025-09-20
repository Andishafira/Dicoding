# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

### Latar Belakang Bisnis

Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

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
Kebutuhan requirements untuk menjalankan program IPYNB tersedia dalam file requirements_ipynb.txt. Kemudian, untuk melakukan deployment, kebutuhan requirements tersedia dalam file requirements.txt.

---

## Business Dashboard

Bussiness Dashboard dibuat menggunakan Google Looker Studio dan dapat diakses online menggunakan link : https://lookerstudio.google.com/reporting/3418ee20-b0bb-4347-9e83-2389bed4e706

Dashboard ini menyajikan gambaran umum (snapshot) mengenai status akademik mahasiswa di Universitas Jaya, dengan fokus utama untuk memahami faktor-faktor yang berkaitan dengan kelulusan (Graduate) dan putus studi (Dropout). Dashboard ini dibuat menggunakan dataset yang telah didecoding sehingga lebih mudah dibaca dan dimengerti. 

**Ringkasan KPI (Gambaran Umum)**
Panel KPI di bagian atas memberikan konteks utama:

  * Total Mahasiswa: Terdapat 4.420 mahasiswa dalam dataset ini.

  * Status Utama: Dari total tersebut, 2.210 (50.0%) telah Lulus, 1.420 (32.1%) telah Putus Studi (Dropout), dan 794 (17.9%) masih Terdaftar (Enrolled).

  * Permasalahan Utama: Angka Dropout Rate sebesar 32.1% sangat signifikan dan menjadi masalah utama yang perlu diinvestigasi. Ini menunjukkan bahwa hampir sepertiga dari mahasiswa gagal menyelesaikan studi mereka.

Artinya, dari total populasi mahasiswa, hampir setengah berhasil lulus, sepertiga mengalami dropout, dan sisanya masih berstatus aktif/enrolled

Analisis visual utama dari dashboard meliputi:
1. **Distribusi Status Mahasiswa (pie chart)**

Grafik ini memvisualisasikan proporsi dari tiga status mahasiswa.

  * Lulus (49,9%): Setengah dari populasi mahasiswa dalam data ini berhasil lulus.

  * Dropout (32.1%): Cukup tinggi, lebih dari 3 mahasiswa dari 10 berhenti di tengah jalan.

  * Terdaftar (17.9%): Ini adalah kelompok minoritas, mahasiswa yang masih aktif menjalani studi.

Insight: Tingginya dropout rate (32%) menunjukkan adanya masalah signifikan pada keberlangsungan studi mahasiswa.

2. **Distribusi Dropout Berdasarkan Jurusan**
Jurusan dengan dropout terbanyak:

  1.  Management (Evening)
  2.  Management (Reguler)
  3.  Nursing
  4.  Journalism and Communication

Insight:
Jurusan manajemen (baik reguler maupun kelas malam) dan keperawatan memiliki jumlah dropout tinggi. Hal ini bisa terkait faktor beban akademik, biaya, atau kurangnya dukungan belajar. Jurusan-jurusan dengan orientasi praktik tinggi (Nursing, Tourism, Journalism) juga rentan dropout.

3. **Distribusi Lulusan Berdasarkan Jurusan**

   Jurusan dengan lulusan terbanyak:
    1. Nursing (hampir 600 lulusan)
    2. Social Service
    3. Journalism and Communication
    4. Veterinary Nursing
    5. Management
Insight:
Meski memiliki dropout tinggi, Nursing tetap menghasilkan jumlah lulusan terbanyak, menunjukkan daya tarik jurusan ini kuat meskipun tingkat kesulitan juga tinggi.

4. **Faktor yang Mempengaruhi Dropout**

Variabel paling berpengaruh:
  * Curricular Units Semester 2

  * Curricular Units Semester 1

  * Tuition Fees Up to Date

  * Age at Enrollment

  * Application Mode

**Insight:**

  * Nilai akademik (semester 1 & 2) merupakan indikator paling besar terhadap dropout → mahasiswa dengan nilai rendah berisiko tinggi keluar.

  * Masalah keuangan (tuition fees) juga krusial → mahasiswa dengan keterlambatan pembayaran lebih rentan dropout.

  * Faktor demografis (usia saat masuk, jalur pendaftaran) berperan, meski lebih kecil.

5. **Rata-Rata Nilai Akademik Berdasarkan Status**

**Insight:**

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

## Conclusion

Model machine learning (Random Forest Classifier) berhasil dikembangkan untuk memprediksi status kelulusan mahasiswa dengan akurasi 88.84% pada data uji.

* Kinerja Model: Model menunjukkan kinerja yang baik, terutama dalam mengidentifikasi mahasiswa yang akan "Lulus" (Recall 0.93) dan cukup baik dalam mendeteksi mahasiswa yang berisiko "Dropout" (Recall 0.82).

* Faktor Prediktif Utama: Analisis feature importance menunjukkan bahwa faktor akademik adalah prediktor terkuat. Fitur-fitur seperti:

  1. 'Curricular_units_2nd_sem_approved' (Jumlah mata kuliah lulus di semester 2)
  2. 'Curricular_units_1st_sem_approved' (Jumlah mata kuliah lulus di semester 1)
  3. 'Curricular_units_2nd_sem_grade' (Rata-rata nilai semester 2)
  4. 'Curricular_units_1st_sem_grade' (Rata-rata nilai semester 1)

* Faktor finansial, seperti Tuition_fees_up_to_date (Status pembayaran UKT), juga terbukti menjadi prediktor penting.

---

### Rekomendasi Action Items

Berdasarkan temuan tersebut, berikut adalah beberapa rekomendasi untuk institusi:

- Implementasi Sistem Peringatan Dini: Institusi harus menggunakan aplikasi prediktif (seperti prototipe Streamlit yang dibuat) untuk secara otomatis menandai mahasiswa yang menunjukkan kinerja akademik di bawah rata-rata pada semester 1 dan 2. Mahasiswa ini harus segera mendapatkan bimbingan akademik intensif.
- Intervensi Finansial Proaktif: Mengingat Tuition_fees_up_to_date adalah faktor penting, bagian administrasi keuangan harus proaktif menghubungi mahasiswa yang memiliki tunggakan (tetapi belum berstatus Debtor) untuk menawarkan skema pembayaran yang fleksibel atau bantuan keuangan, guna mencegah mereka dropout karena alasan finansial.
- Fokus pada Keterlibatan Semester Awal: Keberhasilan di dua semester pertama sangat krusial. Institusi disarankan memperkuat program orientasi dan program mentoring antar-mahasiswa (senior-junior) untuk membantu mahasiswa baru beradaptasi dan berhasil secara akademik di tahun pertama mereka.
