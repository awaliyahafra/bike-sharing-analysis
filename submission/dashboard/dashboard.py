import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("main_data.csv")

# Konversi tanggal
df["dteday"] = pd.to_datetime(df["dteday"])

# Mapping label cuaca
weather_map = {
    1: "Clear",
    2: "Mist",
    3: "Light Rain/Snow",
    4: "Heavy Rain/Snow"
}

# Mapping label musim
season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

df["weather_label"] = df["weathersit"].map(weather_map)
df["season_label"] = df["season"].map(season_map)

# Header
st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis Penyewaan Sepeda Tahun 2011–2012")

# KPI
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Penyewaan", f"{df['cnt'].sum():,}")

with col2:
    st.metric("Rata-rata Harian", round(df['cnt'].mean()))

with col3:
    st.metric("Jumlah Hari", len(df))

# Visualisasi Cuaca
st.subheader("Rata-rata Penyewaan Berdasarkan Cuaca")

weather_analysis = (
    df.groupby("weather_label")["cnt"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(
    x=weather_analysis.index,
    y=weather_analysis.values,
    ax=ax
)

ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig)

# Visualisasi Musim
st.subheader("Rata-rata Penyewaan Berdasarkan Musim")

season_analysis = (
    df.groupby("season_label")["cnt"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(
    x=season_analysis.index,
    y=season_analysis.values,
    ax=ax
)

ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig)

# Tren Harian
st.subheader("Tren Penyewaan Sepeda Harian")

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["dteday"], df["cnt"])

ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig)