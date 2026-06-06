# Bike Sharing Data Analysis

## Deskripsi Proyek

Proyek ini merupakan analisis data Bike Sharing Dataset periode 2011–2012 untuk memahami faktor-faktor yang memengaruhi jumlah penyewaan sepeda.

## Pertanyaan Bisnis

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda harian selama tahun 2011–2012?

2. Pada musim apa jumlah penyewaan sepeda harian mencapai tingkat tertinggi dan terendah selama periode 2011–2012?

## Hasil Analisis

* Cuaca cerah menghasilkan rata-rata penyewaan sepeda tertinggi.
* Cuaca hujan atau salju ringan menghasilkan rata-rata penyewaan sepeda terendah.
* Musim Fall memiliki rata-rata penyewaan sepeda tertinggi.
* Musim Spring memiliki rata-rata penyewaan sepeda terendah.

## Struktur Direktori

submission/

├── dashboard/

│   ├── dashboard.py

│   └── main_data.csv

├── data/

│   ├── day.csv

│   └── hour.csv

├── notebook.ipynb

├── README.md

├── requirements.txt

└── url.txt

## Setup Environment

Install seluruh library yang dibutuhkan:

pip install -r requirements.txt

## Menjalankan Dashboard

Masuk ke folder dashboard:

cd dashboard

Jalankan Streamlit:

streamlit run dashboard.py
