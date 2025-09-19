# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang Bisnis

PT Jaya Jaya Maju, sebuah perusahaan multinasional yang beroperasi sejak tahun 2000, telah mencapai skala operasional yang impresif dengan lebih dari 1.000 karyawan tersebar di berbagai wilayah. Walaupun telah berkembang pesat, perusahaan menghadapi sebuah tantangan operasional kritis: tingkat attrition (pengunduran diri) karyawan yang sangat tinggi. Analisis data (merujuk pada 1.058 sampel karyawan yang valid dari dataset) mengungkap bahwa attrition rate aktual perusahaan telah mencapai 16,92%. Angka ini tidak hanya melebihi ambang batas wajar industri (sekitar 10%), tetapi juga menandakan adanya permasalahan sistemik dalam manajemen sumber daya manusia yang memerlukan investigasi mendalam.

Tingkat turnover yang kronis ini menimbulkan dampak negatif berlapis yang signifikan bagi perusahaan. Pertama, terjadi eskalasi biaya rekrutmen dan pelatihan; setiap karyawan yang keluar harus digantikan, memicu siklus biaya yang berkelanjutan untuk iklan lowongan, proses seleksi, onboarding, dan pelatihan hingga karyawan baru mencapai produktivitas penuh. Kedua, terjadi disrupsi operasional dan penurunan produktivitas tim. Lebih dari sekadar kehilangan tenaga kerja, perusahaan kehilangan intellectual capital dan pengalaman institusional. Analisis data mengonfirmasi bahwa risiko attrition tertinggi terkonsentrasi pada karyawan yang lebih muda dan memiliki masa kerja singkat (terutama 0-2 tahun, seperti yang ditunjukkan oleh visualisasi YearsAtCompany), yang berarti investasi onboarding perusahaan seringkali gagal memberikan laba atas investasi (ROI). Ketiga, terdapat indikasi kuat penurunan kepuasan dan engagement karyawan. Fitur-fitur dalam dataset seperti JobSatisfaction, WorkLifeBalance, dan EnvironmentSatisfaction adalah metrik vital. Data menunjukkan bahwa faktor-faktor seperti OverTime (lembur) memiliki korelasi yang sangat kuat dengan attrition, mengisyaratkan bahwa kelelahan (burnout) dan ketidakpuasan terhadap keseimbangan kerja-hidup kemungkinan besar berperan sebagai katalisator utama yang mendorong karyawan untuk mencari peluang di tempat lain.

Menghadapi situasi ini, Manajemen HR di Jaya Jaya Maju menyadari urgensi untuk beralih dari strategi reaktif (hanya mengganti karyawan yang hilang) menjadi pendekatan proaktif yang berbasis data. Terdapat kebutuhan mendesak untuk tidak hanya memahami faktor-faktor fundamental penyebab attrition, tetapi juga untuk mengembangkan sebuah model prediktif yang andal. Tujuan utamanya adalah untuk mengidentifikasi karyawan berisiko tinggi secara dini, sehingga memungkinkan perusahaan menyusun strategi intervensi yang tepat sasaran, meningkatkan retensi talenta kunci, dan pada akhirnya mengurangi attrition rate ke tingkat yang lebih sehat dan berkelanjutan secara finansial.

### Permasalahan Bisnis

Permasalahan bisnis fundamental yang dihadapi PT Jaya Jaya Maju adalah ketidakmampuan perusahaan untuk menanggulangi attrition rate yang telah mencapai 16,92% (berdasarkan analisis terhadap 1.058 karyawan yang valid), yang berakar pada kesenjangan informasi kritis. Secara spesifik, perusahaan belum dapat membedakan antara faktor-faktor yang memiliki dampak signifikan secara statistik dan yang hanya bersifat anekdotal. Terdapat ketidakpastian strategis mengenai seberapa besar pengaruh sebenarnya dari metrik finansial (seperti MonthlyIncome), faktor demografis (seperti Age dan MaritalStatus), dan indikator perilaku kerja (seperti OverTime yang berlebihan dan DistanceFromHome) terhadap probabilitas seorang karyawan untuk mengundurkan diri. Tanpa pemahaman mendalam mengenai pola-pola ini, setiap strategi retensi yang diterapkan berisiko salah sasaran dan tidak efisien secara biaya. Permasalahan ini diperburuk oleh ketiadaan alat bantu analitis yang memadai; manajemen HR saat ini tidak memiliki business dashboard terpusat untuk memantau indikator-indikator kunci attrition ini secara berkala. Ketiadaan infrastruktur pemantauan ini memaksa proses pengambilan keputusan menjadi reaktif—berfokus pada penggantian karyawan setelah mereka keluar—alih-alih proaktif, yang seharusnya memungkinkan intervensi dini sebelum turnover terjadi. Oleh karena itu, proyek ini esensial untuk menjembatani kesenjangan analitis tersebut dengan mengidentifikasi faktor penyebab secara presisi dan menyediakan alat untuk pemantauan berkelanjutan.

### Cakupan Proyek

1. **Pembersihan dan Persiapan Data**: Memuat dataset mentah (employee_data.csv), menangani nilai yang hilang (ditemukan 412 nilai NaN pada kolom target 'Attrition' yang kemudian dihilangkan), dan menghapus fitur-fitur konstan yang tidak memberikan nilai prediktif (seperti 'EmployeeCount', 'Over18', dll.).
2. **Analisis Data Eksploratif (EDA)**: Melakukan analisis statistik dan visualisasi untuk mengidentifikasi pola terkait attrition. Ini termasuk analisis bivariat antara fitur (seperti MonthlyIncome, Age, OverTime, MaritalStatus) dan target Attrition.
3. **Pengujian Statistik**: Menjalankan uji Chi-Square untuk memvalidasi secara statistik hubungan antara fitur kategorikal dan attrition.
4. **Pengembangan Model**: Membangun model machine learning menggunakan XGBClassifier untuk memprediksi probabilitas attrition.
5. **Optimasi Model**: Menangani tantangan dataset yang sangat tidak seimbang (hanya 16,9% kelas positif) dengan menggunakan teknik hyperparameter tuning melalui RandomizedSearchCV, yang dioptimalkan secara spesifik untuk F1-Score guna menyeimbangkan Precision dan Recall.
6. **Visualisasi Dashboard**: Menyajikan temuan-temuan kunci dan KPI dalam sebuah dashboard bisnis.

### Persiapan

Sumber data: 

Setup environment:

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from scipy.stats import chi2_contingency
```

## Business Dashboard

Dashboard visualisasi (Laporan_Tanpa_Judul.pdf) merangkum temuan-temuan utama yang dihadapi bisnis. Dashboard ini menggunakan dataset yang telah dibersihkan yang terdiri dari 1.058 karyawan, di mana 179 di antaranya telah mengundurkan diri, menghasilkan Attrition Rate sebesar 16,92%.

Analisis visual utama dari dashboard meliputi:
1. Persebaran Attrition berdasarkan Departemen: Jumlah absolut karyawan yang keluar tertinggi berasal dari departemen Research & Development, diikuti oleh departemen Sales.
2. Persebaran Attrition berdasarkan Posisi (JobRole): Peran pekerjaan dengan jumlah attrition tertinggi secara absolut adalah Sales Executive, Research Scientist, dan Laboratory Technician. Analisis lebih dalam di notebook juga mengonfirmasi bahwa secara proporsional, Sales Representative memiliki risiko keluar tertinggi.
3. Risiko vs. Pendapatan (MonthlyIncome): Dashboard menyajikan grafik sebar (scatter plot) yang secara jelas memvisualisasikan korelasi negatif antara pendapatan dan risiko attrition. Karyawan dengan probabilitas risiko tinggi (ditandai oranye) terkonsentrasi secara signifikan pada rentang pendapatan bulanan yang lebih rendah. Temuan ini didukung penuh oleh analisis boxplot dalam notebook, yang menunjukkan bahwa median gaji karyawan yang keluar (1) jauh lebih rendah daripada mereka yang bertahan (0).

## Conclusion

Proyek ini berhasil mengidentifikasi faktor-faktor pendorong utama attrition karyawan di PT Jaya Jaya Jaya dan membangun model prediktif XGBoost yang telah dioptimalkan. Tantangan utama dataset adalah ketidakseimbangan kelas yang parah (16,92% kelas positif), yang ditangani dengan mengoptimalkan model secara spesifik untuk F1-Score selama proses RandomizedSearchCV. Model final yang telah di-tuning mencapai kinerja yang solid untuk dataset yang tidak seimbang, dengan hasil pada data uji sebagai berikut:

* F1-Score (Kelas 1): 0.53
* Recall (Kelas 1): 0.44 (Model ini berhasil mengidentifikasi 44% dari semua karyawan yang sebenarnya akan keluar).
* Precision (Kelas 1): 0.67 (Dari semua karyawan yang diprediksi model akan keluar, 67% di antaranya adalah prediksi yang benar).

Temuan terpenting dari analisis ini adalah faktor-faktor prediktor utama yang memengaruhi keputusan seorang karyawan untuk keluar, yang diekstraksi dari model XGBoost final. Faktor-faktor tersebut diurutkan berdasarkan tingkat kepentingannya:
1. MonthlyIncome (Pendapatan Bulanan)
2. OverTime_Yes (Bekerja Lembur)
3. Age (Usia)
4. TotalWorkingYears (Total Tahun Bekerja)
5. DistanceFromHome (Jarak dari Rumah)


### Rekomendasi Action Items (Optional)

Berdasarkan temuan berbasis data di atas, berikut adalah rekomendasi tindakan yang dapat ditindaklanjuti untuk mengurangi attrition:

- Prioritaskan Tinjauan Kompensasi: Mengingat MonthlyIncome adalah prediktor #1, lakukan tinjauan struktur gaji yang kompetitif, terutama untuk karyawan di level awal dan dalam peran berisiko tinggi (seperti Sales Representative) yang berada di kuartil pendapatan bawah.
- Investigasi Budaya Lembur: OverTime adalah prediktor #2. Manajemen harus menyelidiki penyebab utama tingginya permintaan lembur. Ini adalah indikator kuat dari kelelahan (burnout) dan harus segera ditangani, baik melalui alokasi sumber daya yang lebih baik, perbaikan proses, atau kompensasi lembur yang lebih adil.
- Fokus pada Retensi Karyawan Muda/Baru: Prediktor #3 (Age) dan #4 (TotalWorkingYears), serta temuan EDA pada YearsAtCompany, menunjukkan bahwa karyawan yang lebih muda dan yang baru bergabung (0-2 tahun) adalah yang paling rentan. Kembangkan program retensi yang ditargetkan untuk demografi ini, seperti program mentoring yang kuat, jalur karier yang jelas, dan peningkatan engagement selama proses onboarding.
- Terapkan Model Prediktif: Gunakan model XGBoost yang telah dibangun ini untuk secara proaktif menandai karyawan aktif yang memiliki profil risiko tinggi. Tim HR dapat menggunakan daftar ini untuk melakukan intervensi pencegahan, seperti "stay interview" (wawancara retensi), untuk memahami dan mengatasi kekhawatiran spesifik mereka sebelum mereka memutuskan untuk mengundurkan diri.
