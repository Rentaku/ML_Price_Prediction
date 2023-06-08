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
- Callbacks for Mobil


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/75710522-184f-483d-a0d1-bc2dc92366d0)
- Callbacks for Motor


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/ba146538-7ceb-4ef7-94e6-0d6d6f4b2790)


4. Define compile, arsitektur model menggunakan optimizers adam, dengan 'mean_absolute_error' sebagai loss function, dan menggunakan metric RSquared untuk mengukur seberapa baik kualitas model terhadap data.
5. Model akan dijalankan sebanyak 100x iterasi untuk berusaha mencapai performa terbaik yang bisa diperoleh dari arsitektur yang dibuat.

### Evaluation
1. Plot the loss of the model in the epoch. The plot is for the loss of both the train set and the test set. After plotting, check the graph. Does the loss continue to decrease or unstable and if it continues to decrese, the the model is good-fit.
- Mobil


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/143af30c-332a-439b-8313-0b332ecb36fd)


- Motor


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/d14d3f00-47b5-4e77-bde7-c5bb09040c41)


2. Plot the RSquared of the model in the epoch. As the opposite of loss, the the plot is for RSquared of both the train set and the test set should increase in each epoch. After plotting, check the graph. Does the RSquared continue to increase or unstable and if it continues to increase, the the model is good-fit.

-Mobil


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/a347169e-7935-4c23-9975-6d7a2416257f)


- Motor


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/b0b40e79-2a6f-475b-92e2-0520acb4be30)


3. Result of loss and RSquared
- Mobil
0  Loss            58429.3      
1  R-Squared       0.776639 
2  Val_Loss        78986.9      
3  Val_RS-Squared  0.574143 


- Motor
0  Loss            19678.1      
1  R-Squared       0.649843 
2  Val_Loss        27285.8      
3  Val_RS-Squared  0.66169  
