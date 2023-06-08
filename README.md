# ML_Price_Prediction

### Summary
Price Prediction Model adalah sebuah model yang berguna untuk memprediksi harga kendaraan berdasarkan fitur kendaraan yang diinput, dimana apabila pengguna memasukan data kendaraannya maka model akan memberikan output berupa rekomendasi harga yang cocok untuk pengguna gunakan dalam menyewakan kendaraannya.

Repository ini utamanya memiliki 2 file:
1. **tf_car_price_prediction.ipynb** yang digunakan untuk memprediksi rekomendasi harga untuk mobil berdasarkan 6 input yaitu mileage, brand, model, category, tahun, dan gear_box_type
2. **tf_motobike_price_prediction.ipynb** yang digunakan untuk memprediksi rekomendasi harga untuk motor berdasarkan 5 input yaitu mileage, brand, model, tahun, dan cc

## 1. tf_car_price_prediction.ipynb
### Bagaimana cara membuat model?
1. Load dataset dari repository ML_Price_prediction/characteristic.csv using pandas
2. Melakukan eksplorasi terhadap data dengan melihat segala informasinya
3. Melakukan proses cleaning dan preprocessing seperti drop kolom, mengubah tipe data, slicing, menghapus missing value, membersihkan outlier, melakukan transformasi data, dan melakukan normalisasi

### Data Preparation for Modelling
1. Fitur pada data akan dipisah kedalam 2 variabel yaitu variabel predictor (X) dan variabel output (y)
2. Data yang sudah di proses akan dibagi dan diacak menggunakan bantuan library sklearn.model_selection.train_test_split menjadi 2 bagian yaitu data training dan data testing

### Modelling Process
1. Define the model, arsitektur model yang digunakan adalah DNN yang terdiri dari 5 layer dengan input sebanyak 1633 fitur untuk mobil dan 207 fitur untuk motor dengan output sebanyak 1 menggunakan activation function "relu" dan bantuan regularization untuk mengatasi overfitting.
2. Define "callbacks", arsitektur model menggunakan callbacks LearningRateScheduler yang diatur untuk mengubah learning rate dari 1e-5 dengan kelipatan 10 setiap 20x kali iterasi hingga 100 iterasi untuk mengetahui learning rate yang terbaik yang bisa dicapai oleh model.
- Mobil

- Motor

4. Define compile, arsitektur model menggunakan optimizers adam, dengan 'mean_absolute_error' sebagai loss function, dan menggunakan metric RSquared untuk mengukur seberapa baik kualitas model terhadap data.
5. Model akan dijalankan sebanyak 100x iterasi untuk berusaha mencapai performa terbaik yang bisa diperoleh dari arsitektur yang dibuat.

### Evaluation
