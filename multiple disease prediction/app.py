# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:03:44 2023

@author: devku
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/devku/Desktop/multiple disease prediction/saved model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/devku/Desktop/multiple disease prediction/saved model/heart_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/devku/Desktop/multiple disease prediction/saved model/parkinson_model.sav', 'rb'))




#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Predition',
                           'Parkinsons Prediction'],
                          
                          icons = ['activity', 'heart', 'person'],
                          
                          default_index = 0)
    
    
#Diabetes Prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction Using ML')
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin in Level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of person')
        
        
    #code for prediction
    diab_dignosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==0):
            diab_dignosis = 'The person is diabetic'
        else:
            diab_dignosis = 'The person is not diabetic'
            
    st.success(diab_dignosis)
            
            

    
if(selected == 'Heart Disease Predition'):
    
    #page title
    st.title('Heart Disease Predition Using ML')
    
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of person')
        
    with col2:
        sex = st.text_input('sex ')
        
    with col3:
        cp = st.text_input('Chest pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum cholestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dl')
        
    with col1:
        restecg	= st.text_input('Resting Electrocardiographic result')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('major vessels colored by flourosopy')
        
    with col1:
         thal = st.text_input('thal: 0=normal; 1 = fixed defect; 2 = reversable defect')

    #code for prediction
    heart_dignosis = ''

    #creating a button for prediction
    if st.button('Heart Diease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs,	restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if (heart_prediction[0] == 0):
            heart_dignosis = 'The Person does not have a Heart Disease'
        else:
            heart_dignosis = 'The Person has Heart Disease'
        
    st.success(heart_dignosis)

         
if(selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction Using ML')
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col2:
        jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP = st.text_input('MDVP:RAP')
        
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col2:
        DDP = st.text_input('Jitter:DDP	')
        
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('MDVP:NHR')
        
    with col1:
         HNR = st.text_input('MDVP:HNR')
         
    with col2:
         RPDE = st.text_input('RPDE')
         
    with col3:
         DFA  = st.text_input('DFA')
         
    with col1:
         spread1 = st.text_input('spread1')
         
    with col2:
         spread2 = st.text_input('spread2')
         
    with col3:
         D2 = st.text_input('D2')
         
    with col1:
         PPE = st.text_input('PPE')

          
        
    #code for prediction
    parkinsons_dignosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, APQ, DDA, NHR, HNR, RPDE,  DFA, spread1, spread2,  D2, PPE]])
        
        if (parkinsons_prediction[0]==0):
            parkinsons_dignosis = 'The Person does not have Parkinsons Disease'
        else:
            parkinsons_dignosis = 'The Person has Parkinsons Disease'
            
    st.success(parkinsons_dignosis)

