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

Pada bagian Persiapan Proyek pastikan menyampaikan instruksi yang lengkap dan sistematis agar proyek dapat dijalankan oleh orang lain tanpa hambatan. Silahkan lengkapi bagian Setup Environment dengan menuliskan instruksi berikut:

1. Membuat dan Mengaktifkan Virtual Environment (venv)

Gemini

2.5 Pro


PRO
Percakapan dengan Gemini

Tugas_2_Ja...ersity_fix
IPYNB

README (1)
MD
saya punya file kode python dalam file .ipynb ini, tolong buatkan Laporan dengan format seperti pada file README.md ini





Tampilkan alur berpikir
Tentu, berikut adalah laporan yang telah diisi berdasarkan file notebook Python Anda, dengan format yang sesuai dengan file README.md:

Proyek Akhir: Memprediksi Status Kelulusan Mahasiswa di Institusi Pendidikan
Business Understanding
Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

Permasalahan Bisnis
Permasalahan utama adalah untuk mengidentifikasi faktor-faktor penentu yang membedakan antara mahasiswa yang berhasil "Lulus" (Graduate) dan yang "Putus Studi" (Dropout). Institusi perlu membangun sebuah sistem prediktif untuk menandai mahasiswa yang berisiko dropout sedini mungkin, sehingga sumber daya pendukung akademik dan non-akademik dapat dialokasikan secara efektif.

Cakupan Proyek
Cakupan proyek ini meliputi:

Analisis Data Eksploratif (EDA): Untuk memahami data demografis, akademik, dan sosio-ekonomi mahasiswa serta hubungannya dengan status kelulusan.

Pemrosesan Data: Membersihkan data, melakukan feature selection, scaling pada fitur numerik, dan encoding pada fitur kategorikal.

Pengembangan Model: Membangun model klasifikasi machine learning untuk memprediksi status akhir mahasiswa (Lulus atau Dropout).

Evaluasi Model: Mengevaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan F1-score.

Identifikasi Fitur Penting: Menentukan fitur-fitur yang paling berpengaruh dalam memprediksi status mahasiswa.

Persiapan
Sumber Data:
Dataset diambil dari repositori GitHub dan dimuat ke dalam dataframe.

Python

# Clone repository dari github untuk mengakses dataset
!git clone https://github.com/Andishafira/Dicoding.git
# Baca dataset
import pandas as pd
df = pd.read_csv("/content/Dicoding/Belajar_Penerapan_Data_Science/Tugas_2_Menyelesaikan_Permasalahan_Institusi_Pendidikan/data.csv", sep=";")
Setup Environment:
Proyek ini menggunakan beberapa pustaka Python utama untuk analisis dan pemodelan. Ketergantungan utama tercantum dalam file requirements.txt yang dihasilkan oleh perintah berikut:

Python

!pip freeze > requirements.txt
Pustaka utama yang digunakan antara lain:

pandas

numpy

matplotlib & seaborn

scikit-learn (untuk preprocessing, model, dan evaluasi)

imblearn (untuk menangani data tidak seimbang)

joblib (untuk menyimpan model)

Business Dashboard
Proyek ini tidak mencakup pembuatan business dashboard interaktif. Namun, analisis data eksploratif (EDA) yang terdapat dalam notebook (seperti "Distribusi Variabel Target", "Distribusi Umur", "Hubungan Gender vs Status", dan "Mata Kuliah Lulus vs Status") berfungsi sebagai dasar untuk wawasan bisnis dan dapat dijadikan landasan untuk pembuatan dashboard di masa mendatang.

Menjalankan Sistem Machine Learning
Prototipe sistem machine learning ini dijalankan sebagai notebook Jupyter (Tugas_2_Jaya_University_fix.ipynb). Untuk menjalankan sistem dan mendapatkan prediksi:

Persiapan: Pastikan semua library dalam requirements.txt telah terinstal.

Menjalankan Notebook: Jalankan semua sel dalam notebook secara berurutan. Proses ini akan:

Mengunduh data.

Melakukan preprocessing data (scaling, encoding, oversampling).

Melatih model RandomForestClassifier menggunakan GridSearchCV untuk menemukan parameter terbaik.

Menyimpan model yang telah dilatih (rdf_model.joblib) serta objek scaler dan encoder yang relevan.

Prediksi: Model yang disimpan (rdf_model.joblib) dapat dimuat kembali untuk melakukan prediksi pada data baru, setelah data tersebut melalui proses scaling dan encoding yang sama menggunakan scaler/encoder yang juga telah disimpan.

Tidak ada tautan ke prototipe yang di-hosting; prototipe ini adalah kode yang ada di dalam file notebook.

Conclusion
Model machine learning (Random Forest Classifier) berhasil dikembangkan untuk memprediksi status kelulusan mahasiswa dengan akurasi 88.84% pada data uji.

Kinerja Model: Model menunjukkan kinerja yang baik, terutama dalam mengidentifikasi mahasiswa yang akan "Lulus" (Recall 0.93) dan cukup baik dalam mendeteksi mahasiswa yang berisiko "Dropout" (Recall 0.82).

Faktor Prediktif Utama: Analisis feature importance menunjukkan bahwa faktor akademik adalah prediktor terkuat. Fitur-fitur seperti:

Curricular_units_2nd_sem_approved (Jumlah mata kuliah lulus di semester 2)

Curricular_units_1st_sem_approved (Jumlah mata kuliah lulus di semester 1)

Curricular_units_2nd_sem_grade (Rata-rata nilai semester 2)

Curricular_units_1st_sem_grade (Rata-rata nilai semester 1)

Faktor finansial, seperti Tuition_fees_up_to_date (Status pembayaran UKT), juga terbukti menjadi prediktor penting.

Rekomendasi Action Items
Berdasarkan temuan tersebut, berikut adalah beberapa rekomendasi untuk institusi:

Implementasi Sistem Peringatan Dini: Institusi harus mengembangkan sistem untuk secara otomatis menandai mahasiswa yang menunjukkan kinerja akademik di bawah rata-rata pada semester 1 dan 2 (berdasarkan jumlah mata kuliah lulus dan nilai rata-rata). Mahasiswa ini harus segera mendapatkan bimbingan akademik intensif.

Intervensi Finansial Proaktif: Mengingat Tuition_fees_up_to_date adalah faktor penting, bagian administrasi keuangan harus proaktif menghubungi mahasiswa yang memiliki tunggakan (tetapi belum berstatus Debtor) untuk menawarkan skema pembayaran yang fleksibel atau bantuan keuangan, guna mencegah mereka dropout karena alasan finansial.

Fokus pada Keterlibatan Semester Awal: Keberhasilan di dua semester pertama sangat krusial. Institusi disarankan memperkuat program orientasi dan program mentoring antar-mahasiswa (senior-junior) untuk membantu mahasiswa baru beradaptasi dan berhasil secara akademik di tahun pertama mereka.


preprocessing
PY

app
PY

prediction
PY
update laporan tersebut karena saya menambahkan langkah tambahan yaitu deploy menggunakan streamlit dengan file seperti pada file yang saya unggah ini





Tampilkan alur berpikir
Tentu, saya telah memperbarui laporan Anda untuk menyertakan informasi mengenai deployment model menggunakan Streamlit, berdasarkan file app.py, preprocessing.py, dan prediction.py yang Anda unggah.

Berikut adalah laporan yang telah diperbarui:

Proyek Akhir: Memprediksi Status Kelulusan Mahasiswa di Institusi Pendidikan
Business Understanding
Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak hanya berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

Permasalahan Bisnis
Permasalahan utama adalah untuk mengidentifikasi faktor-faktor penentu yang membedakan antara mahasiswa yang berhasil "Lulus" (Graduate) dan yang "Putus Studi" (Dropout). Institusi perlu membangun sebuah sistem prediktif untuk menandai mahasiswa yang berisiko dropout sedini mungkin, sehingga sumber daya pendukung akademik dan non-akademik dapat dialokasikan secara efektif.

Cakupan Proyek
Cakupan proyek ini meliputi:

Analisis Data Eksploratif (EDA): Untuk memahami data demografis, akademik, dan sosio-ekonomi mahasiswa serta hubungannya dengan status kelulusan.

Pemrosesan Data: Membersihkan data, melakukan feature selection, scaling pada fitur numerik, dan encoding pada fitur kategorikal.

Pengembangan Model: Membangun model klasifikasi machine learning (Random Forest) untuk memprediksi status akhir mahasiswa (Lulus atau Dropout).

Evaluasi Model: Mengevaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan F1-score.

Deployment: Membuat prototipe aplikasi web interaktif menggunakan Streamlit untuk mempermudah penggunaan model prediksi.

Persiapan
Sumber Data:
Dataset diambil dari repositori GitHub dan dimuat ke dalam dataframe.

Python

# Clone repository dari github untuk mengakses dataset
!git clone https://github.com/Andishafira/Dicoding.git
# Baca dataset
import pandas as pd
df = pd.read_csv("/content/Dicoding/Belajar_Penerapan_Data_Science/Tugas_2_Menyelesaikan_Permasalahan_Institusi_Pendidikan/data.csv", sep=";")
Setup Environment:
Proyek ini menggunakan beberapa pustaka Python utama untuk analisis dan pemodelan. Ketergantungan utama tercantum dalam file requirements.txt yang dihasilkan oleh perintah berikut:

Python

!pip freeze > requirements.txt
Pustaka utama yang digunakan antara lain:

pandas

numpy

matplotlib & seaborn

scikit-learn

imblearn

joblib

streamlit (untuk deployment)

Business Dashboard
Proyek ini tidak mencakup pembuatan business dashboard interaktif. Namun, analisis data eksploratif (EDA) yang terdapat dalam notebook (seperti "Distribusi Variabel Target", "Distribusi Umur", "Hubungan Gender vs Status", dan "Mata Kuliah Lulus vs Status") berfungsi sebagai dasar untuk wawasan bisnis dan dapat dijadikan landasan untuk pembuatan dashboard di masa mendatang.

Menjalankan Sistem Machine Learning
Prototipe sistem machine learning ini telah di-deploy sebagai aplikasi web interaktif menggunakan Streamlit. Proses training model asli dilakukan dalam notebook Jupyter (Tugas_2_Jaya_University_fix.ipynb), yang kemudian menyimpan model terlatih dan scaler/encoder sebagai file .joblib.

Aplikasi Streamlit (app.py), dengan bantuan modul preprocessing.py dan prediction.py, kemudian memuat file-file ini untuk melakukan prediksi secara real-time berdasarkan input pengguna.

Cara Menjalankan Prototipe (Lokal):

Pastikan Anda memiliki file app.py, preprocessing.py, prediction.py, dan semua file .joblib (model dan encoders/scalers) dalam satu direktori.

Instal semua pustaka yang diperlukan (termasuk streamlit) dari file requirements.txt.

Buka terminal atau command prompt, navigasi ke direktori tersebut, dan jalankan perintah:

Bash

streamlit run app.py
Aplikasi akan otomatis terbuka di browser Anda. Pengguna dapat memasukkan 10 fitur yang diperlukan di sidebar untuk mendapatkan prediksi status mahasiswa (Lulus atau Dropout).

Conclusion
Model machine learning (Random Forest Classifier) berhasil dikembangkan untuk memprediksi status kelulusan mahasiswa dengan akurasi 88.84% pada data uji.

Kinerja Model: Model menunjukkan kinerja yang baik, terutama dalam mengidentifikasi mahasiswa yang akan "Lulus" (Recall 0.93) dan cukup baik dalam mendeteksi mahasiswa yang berisiko "Dropout" (Recall 0.82).

Faktor Prediktif Utama: Analisis feature importance menunjukkan bahwa faktor akademik adalah prediktor terkuat. Fitur-fitur seperti:

Curricular_units_2nd_sem_approved (Jumlah mata kuliah lulus di semester 2)

Curricular_units_1st_sem_approved (Jumlah mata kuliah lulus di semester 1)

Curricular_units_2nd_sem_grade (Rata-rata nilai semester 2)

Curricular_units_1st_sem_grade (Rata-rata nilai semester 1)

Faktor finansial, seperti Tuition_fees_up_to_date (Status pembayaran UKT), juga terbukti menjadi prediktor penting.

Rekomendasi Action Items
Berdasarkan temuan tersebut, berikut adalah beberapa rekomendasi untuk institusi:

Implementasi Sistem Peringatan Dini: Institusi harus menggunakan aplikasi prediktif (seperti prototipe Streamlit yang dibuat) untuk secara otomatis menandai mahasiswa yang menunjukkan kinerja akademik di bawah rata-rata pada semester 1 dan 2. Mahasiswa ini harus segera mendapatkan bimbingan akademik intensif.

Intervensi Finansial Proaktif: Mengingat Tuition_fees_up_to_date adalah faktor penting, bagian administrasi keuangan harus proaktif menghubungi mahasiswa yang memiliki tunggakan (tetapi belum berstatus Debtor) untuk menawarkan skema pembayaran yang fleksibel atau bantuan keuangan, guna mencegah mereka dropout karena alasan finansial.

Fokus pada Keterlibatan Semester Awal: Keberhasilan di dua semester pertama sangat krusial. Institusi disarankan memperkuat program orientasi dan program mentoring antar-mahasiswa (senior-junior) untuk membantu mahasiswa baru beradaptasi dan berhasil secara akademik di tahun pertama mereka.


buatkan penjelasan dashboard visualisasi tersebut, buat dengan analisis yang dalam dan lengkap. buat kesimpulannya juga





Tampilkan alur berpikir
Berikut adalah analisis mendalam dan lengkap dari visualisasi "Jaya University Dashboard" yang Anda berikan.

Analisis Dashboard Universitas Jaya
Dashboard ini menyajikan gambaran umum (snapshot) mengenai status akademik mahasiswa di Universitas Jaya, dengan fokus utama untuk memahami faktor-faktor yang berkaitan dengan kelulusan (Graduate) dan putus studi (Dropout).

Ringkasan KPI (Gambaran Umum)
Panel KPI di bagian atas memberikan konteks utama:

Total Mahasiswa: Terdapat 4.420 mahasiswa dalam dataset ini.

Status Utama: Dari total tersebut, 2.210 (50.0%) telah Lulus, 1.420 (32.1%) telah Putus Studi (Dropout), dan 794 (17.9%) masih Terdaftar (Enrolled).

Permasalahan Utama: Angka Dropout Rate sebesar 32.1% sangat signifikan dan menjadi masalah utama yang perlu diinvestigasi. Ini menunjukkan bahwa hampir sepertiga dari mahasiswa gagal menyelesaikan studi mereka.

Analisis Mendalam per Visualisasi
1. Distribusi Status Mahasiswa (Grafik Donat)
Grafik ini memvisualisasikan proporsi dari tiga status mahasiswa.

Lulus (50%): Setengah dari populasi mahasiswa dalam data ini berhasil lulus.

Dropout (32.1%): Ini adalah segmen terbesar kedua dan menyoroti besarnya masalah retensi mahasiswa.

Terdaftar (17.9%): Ini adalah kelompok minoritas, yang menunjukkan bahwa data ini sebagian besar berfokus pada hasil akhir (lulus atau dropout).

Analisis: Data ini tidak seimbang (imbalanced), di mana fokus analisis kemungkinan besar adalah untuk memahami perbedaan antara dua kelompok terbesar, yaitu Lulus dan Dropout.

2. Status vs Rata-Rata IPK Semester 1 & 2 (Grafik Batang)
Kedua grafik batang ini memberikan wawasan paling kuat tentang kapan mahasiswa mulai mengalami kesulitan.

IPK Semester 1:

Graduate: Memiliki rata-rata IPK Sem 1 tertinggi (sekitar 12.2).

Enrolled: Sedikit di bawahnya (sekitar 12.0).

Dropout: Memiliki rata-rata IPK Sem 1 yang jauh lebih rendah (sekitar 10.4).

IPK Semester 2:

Graduate: Rata-rata IPK Sem 2 meningkat menjadi sekitar 12.5.

Enrolled: Rata-rata IPK Sem 2 sedikit menurun menjadi sekitar 11.8.

Dropout: Rata-rata IPK Sem 2 turun drastis menjadi sekitar 9.8.

Analisis:

Kinerja Awal adalah Kunci: Terdapat korelasi positif yang sangat kuat antara kinerja akademik di semester pertama dan status kelulusan. Mahasiswa yang dropout sudah menunjukkan kinerja yang lebih rendah sejak awal.

Kesenjangan yang Melebar: Kesenjangan kinerja akademik semakin melebar di semester kedua. Mahasiswa yang akan lulus cenderung meningkatkan nilai mereka, sementara mahasiswa yang akan dropout nilainya semakin menurun. Ini menunjukkan bahwa semester 1 dan 2 adalah periode kritis untuk melakukan intervensi.

3. Perbandingan Status berdasarkan Gender (Grafik Batang Bertumpuk)
Grafik ini memecah status mahasiswa berdasarkan gender (Perempuan dan Laki-laki).

Distribusi Gender: Secara keseluruhan, jumlah mahasiswa Perempuan (sekitar 2.850) jauh lebih banyak daripada mahasiswa Laki-laki (sekitar 1.570). Proporsinya sekitar 65% Perempuan berbanding 35% Laki-laki.

Perbandingan Status:

Dropout: Jumlah absolut mahasiswa dropout hampir sama antara Perempuan (sekitar 700) dan Laki-laki (sekitar 720).

Graduate: Jumlah mahasiswa Perempuan yang lulus (sekitar 1.650) jauh lebih banyak daripada Laki-laki (sekitar 550).

Analisis:

Meskipun jumlah dropout secara absolut terlihat sama, tingkat dropout (dropout rate) untuk Laki-laki secara proporsional jauh lebih tinggi.

Dropout Rate Laki-laki (Perkiraan): 720 / 1.570 ≈ 45.8%

Dropout Rate Perempuan (Perkiraan): 700 / 2.850 ≈ 24.5%

Ini adalah temuan kritis: Mahasiswa laki-laki di universitas ini memiliki risiko dropout hampir dua kali lipat lebih tinggi daripada mahasiswa perempuan.

4. Status vs Beasiswa & Status Pembayaran (Grafik Batang Berkelompok)
Grafik ini menganalisis faktor finansial dan dukungan terhadap status mahasiswa.

Status Pembayaran (Tuition fees up to date):

Graduate: Mayoritas besar (sekitar 2.000 dari 2.210) memiliki status pembayaran yang lancar ("Yes").

Dropout: Sebaliknya, sebagian besar dropout tidak memiliki status pembayaran yang lancar. Terdapat sekitar 500 mahasiswa dropout yang status pembayarannya "No", dibandingkan dengan hanya sekitar 200 mahasiswa lulus.

Analisis: Terdapat korelasi negatif yang kuat antara status pembayaran yang tidak lancar dengan kelulusan. Ketidakmampuan membayar UKT adalah prediktor kuat untuk dropout.

Status Beasiswa (Scholarship Holder):

Dropout: Kelompok ini memiliki proporsi penerima beasiswa yang paling rendah (hanya sekitar 150 dari 1.420 mahasiswa, atau ≈ 10.5%).

Enrolled: Kelompok ini memiliki proporsi penerima beasiswa tertinggi (sekitar 350 dari 794, atau ≈ 44%).

Graduate: Proporsi penerima beasiswa di kelompok ini adalah sekitar 27% (600 dari 2.210).

Analisis: Menjadi penerima beasiswa tampaknya menjadi faktor pelindung yang kuat terhadap dropout. Tingkat dropout di kalangan penerima beasiswa sangat rendah.

Kesimpulan dan Rekomendasi
Kesimpulan Utama:

Masalah Utama: Universitas Jaya memiliki tingkat dropout yang mengkhawatirkan sebesar 32.1%.

Prediktor Terkuat: Kinerja akademik, khususnya nilai rata-rata (IPK) di Semester 1 dan 2, adalah indikator paling jelas untuk memprediksi hasil studi mahasiswa. Kesenjangan kinerja antara yang lulus dan dropout sudah terlihat sejak semester pertama dan semakin melebar di semester kedua.

Faktor Risiko Tinggi: Ada dua kelompok yang sangat rentan terhadap dropout:

Mahasiswa Laki-laki: Meskipun jumlahnya lebih sedikit, tingkat dropout mereka (sekitar 46%) hampir dua kali lipat lebih tinggi daripada mahasiswa perempuan (sekitar 24.5%).

Mahasiswa dengan Masalah Keuangan: Mahasiswa yang status pembayaran UKT-nya tidak lancar (Tuition fees up to date = "No") memiliki kemungkinan dropout yang sangat tinggi.

Faktor Pelindung: Menjadi penerima beasiswa secara signifikan mengurangi risiko dropout.

Rekomendasi Strategis (Action Items):

Implementasikan Sistem Peringatan Dini Akademik: Berdasarkan data IPK Semester 1 dan 2, pihak universitas harus secara proaktif mengidentifikasi mahasiswa yang nilainya mulai menurun dan mewajibkan mereka mengikuti program bimbingan akademik atau konseling.

Program Intervensi Finansial: Bagian keuangan harus memiliki sistem untuk memantau mahasiswa yang mulai menunggak pembayaran (bukan hanya yang sudah berstatus Debtor). Tawarkan skema cicilan yang fleksibel atau konseling keuangan untuk membantu mereka sebelum memutuskan dropout.

Buat Program Retensi Khusus Mahasiswa Laki-laki: Perlu ada penelitian lebih lanjut mengapa tingkat dropout mahasiswa laki-laki sangat tinggi. Institusi dapat mempertimbangkan program mentoring khusus, lokakarya, atau komunitas yang berfokus pada tantangan yang mungkin dihadapi oleh mahasiswa laki-laki di lingkungan kampus ini.

Perkuat Program Beasiswa: Data menunjukkan beasiswa sangat efektif dalam mencegah dropout. Mempertahankan atau bahkan memperluas program beasiswa dapat menjadi investasi yang baik untuk meningkatkan angka kelulusan.


Berdasarkan percakapan kita sebelumnya. Laporan yang sudah dibuat mendapatkan revisi. Revisinya seperti ini :

Pada bagian Persiapan Proyek pastikan kamu menyampaikan instruksi yang lengkap dan sistematis agar proyek dapat dijalankan oleh orang lain tanpa hambatan. Silahkan lengkapi bagian Setup Environment dengan menuliskan instruksi berikut:

Pada bagian Persiapan Proyek pastikan kamu menyampaikan instruksi yang lengkap dan sistematis agar proyek dapat dijalankan oleh orang lain tanpa hambatan. Silahkan lengkapi bagian Setup Environment dengan menuliskan instruksi berikut:

Membuat dan Mengaktifkan Virtual Environment (venv)

Instruksi tentang cara membuat dan mengaktifkan virtual environment perlu dijelaskan, agar lingkungan pengembangan tetap terisolasi dan stabil.

contoh:

dos-9667c8ac946a73d5878e2759956aa36220250510071144.png

Menginstal Dependensi dari requirements.txt

Kamu perlu menjelaskan cara menginstalnya menggunakan pip, sehingga seluruh pustaka yang dibutuhkan tersedia.

contoh

dos-6e9a24239cfbb6f6af9ecc304c98fa9e20250510071324.png

Dan lain-lain



Tolong bantu saya membuat perbaikannya





Tampilkan alur berpikir
Tentu, saya akan membantu Anda memperbaikinya.

Berikut adalah Laporan Proyek yang telah diperbarui dengan revisi pada bagian Persiapan Proyek dan Setup Environment sesuai instruksi Anda agar lebih lengkap dan sistematis.

Proyek Akhir: Memprediksi Status Kelulusan Mahasiswa di Institusi Pendidikan
Business Understanding
Institusi pendidikan (disebut sebagai Jaya University dalam nama file) menghadapi tantangan dalam mempertahankan mahasiswanya. Tingkat dropout yang tinggi tidak only berdampak pada finansial institusi tetapi juga pada reputasi akademisnya. Dengan memahami faktor-faktor kunci yang memengaruhi keberhasilan studi, institusi dapat secara proaktif mengidentifikasi mahasiswa yang berisiko dan memberikan intervensi yang tepat untuk mendukung mereka agar berhasil lulus.

Permasalahan Bisnis
Permasalahan utama adalah untuk mengidentifikasi faktor-faktor penentu yang membedakan antara mahasiswa yang berhasil "Lulus" (Graduate) dan yang "Putus Studi" (Dropout). Institusi perlu membangun sebuah sistem prediktif untuk menandai mahasiswa yang berisiko dropout sedini mungkin, sehingga sumber daya pendukung akademik dan non-akademik dapat dialokasikan secara efektif.

Cakupan Proyek
Cakupan proyek ini meliputi:

Analisis Data Eksploratif (EDA): Untuk memahami data demografis, akademik, dan sosio-ekonomi mahasiswa serta hubungannya dengan status kelulusan.

Pemrosesan Data: Membersihkan data, melakukan feature selection, scaling pada fitur numerik, dan encoding pada fitur kategorikal.

Pengembangan Model: Membangun model klasifikasi machine learning (Random Forest) untuk memprediksi status akhir mahasiswa (Lulus atau Dropout).

Evaluasi Model: Mengevaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan F1-score.

Deployment: Membuat prototipe aplikasi web interaktif menggunakan Streamlit untuk mempermudah penggunaan model prediksi.

Persiapan
Bagian ini menjelaskan langkah-langkah sistematis untuk menyiapkan dan menjalankan proyek ini di komputer lokal Anda tanpa hambatan.

Sumber Data:
Dataset utama (data.csv) dan semua script proyek ini berlokasi di dalam repositori GitHub.

Setup Environment:
Untuk memastikan proyek berjalan di lingkungan yang terisolasi, stabil, dan memiliki semua pustaka yang diperlukan, ikuti instruksi penyiapan berikut:

1. Klona (Clone) Repositori Proyek
Buka terminal atau Command Prompt, kemudian jalankan perintah berikut untuk menginduh semua file dari repository.
`git clone https://github.com/Andishafira/Dicoding.git`

Setelah selesai, masuk ke direktori repositori yang baru saja diunduh:

`cd Dicoding`

2. Membuat dan Mengaktifkan Virtual Environment (`venv`)

Sangat disarankan untuk membuat virtual environment agar dependensi proyek (pustaka) tidak bercampur dengan instalasi Python global.

  * Dari dalam direktori Dicoding, buat environment baru (misalnya, dengan nama `venv`):
    `python -m venv venv`

  * Selanjutnya, aktifkan environment tersebut
    * Di Windows ;
      `.\venv\Scripts\activate`
    * Di macOS/Linux:
      `source venv/bin/activate`
Setelah aktif, nama environment (`venv`) akan muncul di awal baris terminal.


3. Menginstal Dependensi dari `requirements.txt`

   
Setelah virtual environment aktif, instal semua pustaka yang diperlukan yang sudah terdaftar dalam file `requirements.txt` menggunakan pip:
`pip install -r requirements.txt`
Perintah ini akan secara otomatis mengunduh dan menginstal semua pustaka seperti streamlit, pandas, scikit-learn, dll., dengan versi yang tepat.

Setelah ketiga langkah ini selesai, lingkungan telah siap. Anda dapat melanjutkan untuk menjalankan proses training di notebook atau langsung menjalankan aplikasi Streamlit.


---

## Business Dashboard

Bussiness Dashboard dibuat menggunakan Google Looker Studio dan dapat diakses online menggunakan link : https://lookerstudio.google.com/reporting/3418ee20-b0bb-4347-9e83-2389bed4e706

![Dashboard](https://raw.githubusercontent.com/Andishafira/Dicoding/main/Belajar_Penerapan_Data_Science/Tugas_2_Menyelesaikan_Permasalahan_Institusi_Pendidikan/Dashboard/screencapture-lookerstudio-google-reporting-3418ee20-b0bb-4347-9e83-2389bed4e706-page-savYF-edit-2025-09-20-13_05_16.png)


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
