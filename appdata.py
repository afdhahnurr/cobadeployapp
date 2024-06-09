import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

def main():
	st.subheader("Data-Data Kabupaten Bulungan")

	def file_selector(folder_path='./dataset'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Pilih file",filenames)
		return os.path.join(folder_path,selected_filename)

	filename = file_selector()

	# Read Data
	df = pd.read_csv(filename, sep = ';')
	# Show Dataset

	if st.checkbox("Tampilkan Data"):
		number = st.number_input("Jumlah Baris Untuk Ditampilkan",5,10)
		st.dataframe(df.head(number), hide_index=True)

	# Select Columns
	if st.checkbox("Pilih Kolom Untuk Ditampilkan"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Pilih Kolom",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df, hide_index=True)

	if st.button("Terima Kasih!"):
		st.balloons()

	st.sidebar.header("About App")
	st.sidebar.info("A Simple App for Exploring Kab. Bulungan's Data")

	st.sidebar.header("Data Source")
	st.sidebar.info("[BPS](https://bulungankab.bps.go.id/)")

	st.sidebar.header("Maintained by")
	st.sidebar.info("Bappeda & Litbang Kab. Bulungan")


if __name__ == '__main__':
	main()
