# ML_Price_Prediction

### Summary
Price Prediction Model is a model that is useful for predicting vehicle prices based on the vehicle features that are input, where if the user enters the vehicle data, the model will provide output in the form of price recommendations that are suitable for users to use in renting their vehicles.

This repository mainly has 2 files:
1. **tf_car_price_prediction.ipynb** which is used to predict price recommendations for cars based on 6 inputs, namely mileage, brand, model, category, year, and gear_box_type
2. **tf_motorbike_price_prediction.ipynb** which is used to predict price recommendations for motorbikes based on 5 inputs namely mileage, brand, model, year and cc

### How do I create a model?
1. Load dataset from repository ML_Price_prediction/characteristic.csv using pandas
2. Exploring the data by looking at all the information
3. Perform cleaning and preprocessing processes such as dropping columns, changing data types, slicing, removing missing values, cleaning outliers, performing data transformations, and performing normalization

### Data Preparation for Modeling
1. Features in the data will be separated into 2 variables, namely the predictor variable (X) and the output variable (y)
2. The data that has been processed will be divided and randomized using the help of the sklearn.model_selection.train_test_split library into 2 parts, namely training data and testing data

### Modeling Process
1. Define the model, the model architecture used is DNN which consists of 5 layers with 1633 input features for cars and 207 features for motorcycles with 1 output using the "relu" activation function and regularization assistance to overcome overfitting.
2. Define "callbacks", the model architecture uses LearningRateScheduler callbacks which are set to change the learning rate from 1e-5 with a multiple of 10 every 20x iterations up to 100 iterations to find out the best learning rate that can be achieved by the model.
- Callbacks for Cars


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/75710522-184f-483d-a0d1-bc2dc92366d0)
- Callbacks for Motor


![image](https://github.com/Rentaku/ML_Price_Prediction/assets/132776192/ba146538-7ceb-4ef7-94e6-0d6d6f4b2790)


4. Define compile, model architecture using optimizers adam, with 'mean_absolute_error' as a loss function, and using the RSquared metric to measure how good the quality of the model is to the data.
5. The model will be run for 100x iterations to try to achieve the best performance that can be obtained from the architecture created.

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
1  Loss            58429.3      
2  R-Squared       0.776639 
3  Val_Loss        78986.9      
4  Val_RS-Squared  0.574143 


- Motor
1  Loss            19678.1      
2  R-Squared       0.649843 
3  Val_Loss        27285.8      
4  Val_RS-Squared  0.66169  
