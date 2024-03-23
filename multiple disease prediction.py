# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:24:57 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu






diabetes_model = pickle.load(open("C:/Users/HP/Desktop/Multiple Disease Prediction website/Saved Models/diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("C:/Users/HP\Desktop/Multiple Disease Prediction website/Saved Models/heart_disease_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction'],
                            icons =['activity','heart'],
                           default_index = 0)

if(selected == 'Diabetes Prediction'):



    st.title('Diabetes Prediction Using ML')

  
    
    
    col1,col2 = st.columns(2)
   
    with col1:
      Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
      Glucose = st.text_input('Glucose Level') 
      
    with col1:  
      BloodPressure = st.text_input('Blood Pressure Level')
      
    with col2:  
      SkinThickness = st.text_input('Skin Thickness Level')  
      
    with col1:  
      Insulin = st.text_input('Insulin Level') 
      
    with col2:
      BMI = st.text_input('BMI Value')    
      
    with col1:   
      DiabetesPedigreeFunction = st.text_input('Degree Pedigree Function Value')    
    
    with col2:
      Age = st.text_input('Age')  
      
    
  
    
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Glucose]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is diabetic'
            
        else:
            diab_diagnosis = 'The person is non diabetic'
        
    st.success(diab_diagnosis)    
    
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Preduction Using Ml') 
    

    
    col1,col2 = st.columns(2)
   
    with col1:
      Age = st.text_input('Age')
    
    with col2:
      Sex = st.text_input('Sex') 
      
    with col1:  
      cp = st.text_input('Chest Pain Type')
      
    with col2:  
      trestbps = st.text_input('Resting Blood Pressure')  
      
    with col1:  
      chol = st.text_input('Cholestrol') 
      
    with col2:
     fbs = st.text_input('Fasting Blood Sugar')    
      
    with col1:   
      restecg = st.text_input('Resting Electrocardiac Value')    
    
    with col2:
      thalach = st.text_input('Maximum heart Rate Recieved ') 
      
    with col1:
       exang = st.text_input('Exercise Induces angina ')   
       
    with col2:
        oldpeak = st.text_input('Old peak ')   
        
    with col1:
        slope = st.text_input('Slope ')    
        
    with col2:
       ca = st.text_input('Number of major vessel ')     
       
    with col1:
       thal = st.text_input('Thal ')    
       
  
     
    
    heart_diagnosis=''
    
    if st.button('Heart Disease Test Result'):
        if Age == '' or Sex == '' or cp == '' or trestbps == '' or chol == '' or fbs == '' or restecg == '' or thalach == '' or exang == '' or oldpeak == '' or slope == '' or ca == '' or thal == '':
          st.error("Please fill in all the input fields.")
        else:
          Age = float(Age)
          Sex = int(Sex)
          cp = float(cp)
          trestbps = float(trestbps)
          chol = float(chol)
          fbs = int(fbs)
          restecg = float(restecg)
          thalach = float(thalach)
          exang = int(exang)
          oldpeak = float(oldpeak)
          slope = float(slope)
          ca = float(ca)
          thal = float(thal)
           
            
        heart_prediction = heart_disease_model.predict([[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis = 'The person has heart disease'
            
        else:
            heart_diagnosis = 'The person do not have heart disease'
        
    st.success(heart_diagnosis)    
    