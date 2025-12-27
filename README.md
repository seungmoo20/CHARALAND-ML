# 🏠 CHARALAND ML
### Prediksi Harga Rumah Jabodetabek Berbasis Machine Learning

CHARALAND merupakan proyek Machine Learning berbasis website yang bertujuan
untuk memperkirakan harga rumah di wilayah Jabodetabek menggunakan data historis
properti tahun 2022.

Proyek ini dikembangkan sebagai bagian dari pembelajaran dan eksplorasi
penerapan Artificial Intelligence pada data properti residensial.


## 📌 Tujuan Proyek
1. Mengembangkan model Machine Learning untuk memprediksi harga rumah.
2. Membangun website interaktif berbasis Flask sebagai antarmuka pengguna.
3. Mengintegrasikan model ML ke dalam sistem web secara end-to-end.


## 🧠 Algoritma yang Digunakan
- **XGBoost Regressor**
- Alasan pemilihan:
  - Performa tinggi pada data tabular
  - Mampu menangani hubungan non-linear
  - Stabil terhadap data kompleks


## 📊 Dataset
Dataset yang digunakan merupakan dataset harga rumah Jabodetabek tahun 2022
yang diperoleh dari Kaggle:

🔗 https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek

Jumlah data: **3.553 baris**

### Fitur utama yang digunakan:
- Luas bangunan (m²)
- Luas tanah (m²)
- Jumlah kamar tidur & kamar mandi
- Lokasi (kota & distrik)
- Garasi & carport
- Sertifikat
- Furnishing
- Kondisi properti
- Tipe properti
- Daya listrik
- Koordinat geografis (latitude & longitude)



## ⚙️ Alur Pengembangan
1. Exploratory Data Analysis (EDA)
2. Seleksi fitur & preprocessing
3. Pembuatan pipeline Machine Learning
4. Training & evaluasi model
5. Penyimpanan model menggunakan Joblib
6. Integrasi model ke aplikasi web Flask

Notebook pengembangan tersedia pada folder `notebooks/`.



## 📈 Performa Model
- **R² Score** ≈ 0.85
- **MAE** ≈ ± 600–700 juta Rupiah

Hasil prediksi bersifat estimasi dan mencerminkan kondisi pasar tahun 2022.


## 🌐 Website
Website dibangun menggunakan:
- Flask (Backend)
- HTML, CSS, JavaScript (Frontend)

Pengguna dapat memasukkan karakteristik rumah dan memperoleh estimasi harga
secara otomatis melalui model Machine Learning.


## 🚀 Cara Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
python app.py
