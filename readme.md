[![author](https://img.shields.io/badge/author-feliperoll-purple.svg)](https://www.linkedin.com/in/felipe-roll/)

# :brazil: [Link para ReadMe em PT-BR](https://github.com/FelipeLRoll/prevencao-fraudes/edit/main/readmePortugues.md)
# Inspired by: [Fraud Detection](https://www.youtube.com/watch?v=r9aBF7dWX00)

# Project Overview: 
This project focuses on building a machine learning model to predict potential fraud in financial transactions. The dataset includes various features related to the loan and customer, such as age, gender, income, loan amount, repayment history, and others. The objective is to classify transactions as either potentially fraudulent or non-fraudulent, with the target column being "**Possivel_Fraude**".

This is a **classification problem**, and the steps taken in the project include data exploration, treatment, feature engineering, model training, evaluation, and tuning.

# Code and Resources used:
* **Jupyter Notebook, Git and Github** (version control)
* **Visual Studio Code** (project development environment)
* **Poetry** (project manager)
* **python = ">=3.12,<3.13"**
* **pandas = "^2.2.2"**
* **nbformat = "^5.10.4"**
* **plotly-express = "^0.4.1"**
* **scikit-learn = "^1.5.1"**
* **imbalanced-learn = "^0.12.3"**
* **numpy = ">=1.26.0,<2.0.0"**
* **openpyxl = "^3.1.5"**
* **streamlit = "^1.38.0"**
* **streamlit-dynamic-filters = "^0.1.9"**
* **langchain-google-genai = "^1.0.10"**
* **langchain-experimental = "^0.0.65"**
* **tabulate = "^0.9.0"**
&nbsp;
# Project Steps:
  * ## Exploratory Data Analysis
      Here we take a look at our dataset, to understand the structure and patterns. We detect some errors like the minimum value of "Idade"  being only 4 and some possible outliers in the "Valor_Renda" that will be looked at and treated in the next step.
  * ## Data Treatment
    This step focused on cleaning and preprocessing the data, we also optimized the columns to reduce the size of the dataset. This step had some of the following treatments:
    - Ordering some columns to give a sense of increased importance to the different types of values;
    - Removing duplicate lines;
    - Grouping values and creating intervals;
     
  * ## Visualization with *Plotly Express*
    Here many charts were made to better visualize our data and help us understand it better
    
  * ## Second Data Treatment
    Here we delete the columns that wont be part of our model and look for missing values.
    
  * ## Exploratory Data Analysis with Categorical Columns
    Here we take a closer look to Categorical Columns, creating histograms to visualize patterns and how they behave. We also observe that there is a tendency on our data when the column "Total_Pago" is greater than 60K, there is a high chance that it is not a fraud.
    
  * ## Exploratory Data Analysis with Numerical Columns
    The Objective here is to observe correlation between Numerical Columns, we find that "VL_Emprestimo" and "VL_Emprestimo_ComJuros" have a high positive correlation, and, "QT_Parcelas_Atraso" and "QT_Total_Parcelas_Pagas" have a high negative correlation, this will be fixed in the normalization of out data. We also took a look at outliers, median, max and min values using boxplots.
    
  * ## OneHotEncoding
    Here we split our data to use *Ordinal Encoding* for columns without a specific order, and *OneHotEncoding* for columns that have. This is crucial in order to train our model, this step transforms our data in numerical values to be used later.
    
  * ## Balacing the Target Column
    This step splits the data in the Target Column and the rest of the dataset, creating two datasets in order to balance out the Target Column using *SMOTE*, this help the machine learning model to not be biased towards one of the possible results.
    
  * ## Scaling the data with *RobustScaler*
    Here we test Padroniztion, Standardization and the *RobustScaler* in order to put our numerical values in the same scale and not create a bias for our model. After testing with all three methods, we chose to use *RobustScaler* because we decided to leave some outliers in our data. We also split the data in *train* and *test*
    
  * ## Model Creation, Hyperparameter Tunning, Training and Evaluation
    This step creates out Machine Learning Models that are going to be trained with our data, hyperparameters are also manualy assigned here. The three models used are *Random Forest Classifier*, *Support Vector Machine* and *K Neighbors Classifier*. We tested the **Accuracy**, **Best Hyperparameters**, **Training Time(in seconds)** and **Number of Total Trainings Made** for each of our models, having *K Neighbors Classifier* as the best model with an accuracy of 99.33%

    ## **Random Forest**

    ![randomforest.png](screenshots/randomforest.png "randomforest.png")

    ## **SVM**

    ![svm.png](screenshots/svm.png "svm.png")

    ## **KNN**

    ![knn.png](screenshots/knn.png "knn.png")

    ## **Results**

    ![resultado.png](screenshots/resultado.png "resultado.png")

 * ## Prediction
   The last step was to generate our model using **joblib** and then using the class *gerar_previsoes.py* to load a new dataset and make the predictions.  
    

# Dashboard [Fraud Detection](https://app.powerbi.com/reportEmbed?reportId=ba0459e9-5520-4b20-a76c-be442c03b13a&autoAuth=true&ctid=f310b526-e195-4805-a55e-67e28f2fefdb)

# Streamlit App (In Portuguese) [Fraud Detection](https://prevencao-fraudes.streamlit.app/)
  - **Home:** *Home Page of the WebApp*
  - **Dataframe:** *Here you can look at the dataframe and filter it*
  - **Graficos:** *Create some charts with the available filters and using plotly express*
  - **Dashboard:** *Visualize the Dashboard directly from the WebApp*
  - **Graficos Prontos:** *Charts used in the project, just select the one you want to see and interact with it*
  - **AI:** *Ask the AI about the Dataset*

# How to use
* Just acess [Fraud Detection](https://prevencao-fraudes.streamlit.app/) and try it!! OR
* Create a virtual enviroment using poetry
* Install the libraries by running ```poetry install```
* Run it with ```streamlit run app.py```

* ### To see the predictions in a new dataset, run the file ```gerar_modelo.py``` and ```gerar_previsoes.py```, you can also create your own dataset with the same columns and test it  
&nbsp;
# Developed by: 
  * [Felipe Roll - Linkedin](https://www.linkedin.com/in/felipe-roll)
  * [Felipe Roll - Github](https://github.com/FelipeLRoll)
  * [Felipe Roll - Gmail](felipelroll@gmail.com)



