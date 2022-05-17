import streamlit as st
import pyautogui
import pandas as pd
import numpy as np
from numpy import random
import time
import cv2
import LC
import PIL
from PIL import Image

#set title
st.title("Medi-Bot")

#import image
from PIL import Image
image= Image.open("robot.jpg")
st.image(image,width=150)

#subheader
st.markdown("# Hello!")
st.markdown("# My name is Medi-Bot.")
st.markdown("### I am here to assist you.")
id= None
n= None
df= pd.read_csv("user_data.csv")
st.markdown("## Do you have an existing Medi-ID? ")
x= st.selectbox("Select your response", ['< select >','Yes','No']) 
if x == 'No':
    st.markdown("### So shall we get started? (Yes/No)")
    start= st.text_input("Enter your response here:",value="")
    #df=pd.DataFrame()
    user=[]
    #getting user info
    if len(start)>0:
        if start.lower()[0] =='y':
            st.markdown("### To proceed, I would need some basic information about you.")
            st.markdown("### What is your name?")
            n= st.text_input("Please enter your First Name",value="")
            l= st.text_input("Please enter your Last Name",value="")
            user.append(n)
            user.append(l)
            if len(l)>0 :
                st.markdown("### How old are you?")
                a= st.number_input("Please enter your Age",value=0,step=1)
                user.append(a)
                if (1<a<100) :
                    st.markdown("### Are you a Male or a Female?")
                    g= st.selectbox("Please select your Gender", ['','Male', 'Female'])
                    user.append(g)
                    if len(g)<0 :
                        st.error("Please enter a valid response")
                    else:
                        if st.button("Submit") :
                            x=str(random.randint(1000)) 
                            id= n[0]+l[0]+x
                            user.append(id)
                            st.markdown("Your Unique Medi-ID is: ")
                            st.success(id)
                            st.info("## Please keep your Medi-ID with you for future.")
                            st.write("Please wait while your details are being processed...")
                            my_bar = st.progress(0)
                            for percent_complete in range(100):
                                time.sleep(0.01)
                                my_bar.progress(percent_complete + 1)
                            my_bar.empty()
                            
                            new_user={"First Name": n , "Last Name": l , "Age": a, "Gender": g , "Medi-ID": id}
                            df= df.append(new_user, ignore_index=True)
                            df=df[['First Name','Last Name','Age','Gender','Medi-ID']]
                            df.to_csv("user_data.csv")
                            #st.write(df)                           
elif x == '< select >':
    st.error("Please enter a Valid Response.")
else:
    st.markdown("### Please enter you Unique Medi-ID.")
    id= st.text_input("Enter here",value="")
    if id!= "":
        n=df[df['Medi-ID'] == id]['First Name'].values[0]
        a=df[df['Medi-ID'] == id]['Age'].values[0]
        g=df[df['Medi-ID'] == id]['Gender'].values[0]
                            
    else:
        st.error("Please enter a valid response.")
if (id != None) and (n != None) :
    st.markdown("### Hello "+n+" !")
    st.markdown("#### Please select the disease you want to daignose about.")
    d=st.selectbox("Please select here.",['< select >','Pnuemonia','Tuberculosis','Lung Cancer'])
    if d=='Lung Cancer':
        st.markdown("#### Please fill this small quesionnare to help us run the daignosis...")
        st.write("Please answer the following questions on a scale of 0-10.")
        A=st.slider("How much are you exposed to Air Pollution?",0,10)
        B=st.slider("How much Alcohol Consumer you are?",0,10)
        C=st.slider("Do you have any Dust Allergies?",0,10)
        D=st.slider("Are you exposed to any Occupational Hazards?",0,10)
        E=st.slider("Are you Exposed to any Genetic Risks of Lung Cancer?",0,10)
        F=st.slider("Do you suffer with any chronic lung disease?",0,10)
        G=st.slider("Do you follow a Balanced Diet?",0,10)
        H=st.slider("Are you a victim of Obesity?",0,10)
        I=st.slider("Are you a smoker?",0,10)
        J=st.slider("How much of a passive smoker are you?",0,10)
        K=st.slider("Do you suffer from chest pains?",0,10)
        L=st.slider("Do you cough up blood sometimes?",0,10)
        M=st.slider("Do you experience fatigue often?",0,10)
        N=st.slider("Are you experiencing sudden weight loss?",0,10)
        O=st.slider("Are you experiencing shortness of breath?",0,10)
        P=st.slider("Are you experiencing Wheezing?",0,10)
        Q=st.slider("Are you experiencing any difficulties in swallowing?",0,10)
        R=st.slider("Are you experiencing clubbing of your fingernails?",0,10)
        S=st.slider("Are you catching cold more frequently than usual?",0,10)
        T=st.slider("Are you experiencing dry coughs??",0,10)
        U=st.slider("Do you snore in your sleep",0,10)
        if g=='Male':
            V=1
        else:
            V=2
        lung=[]
        lung.append(a)
        lung.extend([V,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U])
        #df_lung=pd.DataFrame([lung],columns=['Age','Gender','Air Pollution','Alcohol use','Dust Allergy','OccuPational Hazards','Genetic Risk','chronic Lung Disease','Balanced Diet','Obesity','Smoking','Passive Smoker','Chest Pain','Coughing of Blood','Fatigue','Weight Loss','Shortness of Breath','Wheezing','Swallowing Difficulty','Clubbing of Finger Nails','Frequent Cold','Dry Cough','Snoring'])
        #st.write(df_lung)
        lc=st.button("Submit Response")
        if lc:
            lc_pred=LC.LC_predict([lung])
            #st.write(prediction)
            if lc_pred == 1:
                st.success(" ### According to my analysis, There are very LOW CHANCES of you having Lung Cancer.")
                f = open('Lung-Cancer_low_.txt','r')
                contents = f.read()
                bttn = st.download_button('What should be done next?',contents,file_name='Next Steps')
                if bttn:
                    st.markdown("### Thank you for choosing Medi-Bot...!!")
            elif lc_pred == 2:
                st.warning(" ### According to my analysis, There are SLIGHT CHANCES of you having Lung Cancer.")
                f = open('Lung-Cancer_medium_.txt','r')
                contents = f.read()
                bttn = st.download_button('What should be done next?',contents,file_name='Next Steps')
                if bttn:
                    st.markdown("### Thank you for choosing Medi-Bot...!!")
            else:
                st.error(" ### According to my analysis, There are very HIGH CHANCES of you having Lung Cancer.")
                f = open('Lung-Cancer_high_.txt','r')
                contents = f.read()
                bttn = st.download_button('What should be done next?',contents,file_name='Next Steps')
                if bttn:
                    st.markdown("### Thank you for choosing Medi-Bot...!!")
        #add pipeline for lung cancer prediction

    elif d=='Pnuemonia':
        st.markdown("## Please upload your X-ray image below.")
        image= st.file_uploader("Please upload JPEG/PNG image of your Xray here", type= ['jpg','jpeg','png'], accept_multiple_files=False)
        if image is not None:
            image = Image.open(image)
            x= np.array(image)
            tb=st.button("Submit Image")
            if tb:
                prediction = LC.pnm_predict(x)
                if prediction[0][0]==0:
                    st.success("### Normal")
                    f = open('No-Pnuemonia-Next-Steps.txt','r')
                    contents = f.read()
                    bttn = st.download_button('What should be done next?',contents,file_name='Next Steps')
                    if bttn:
                        st.markdown("### Thank you for choosing Medi-Bot...!!")
                else:
                    st.error("### Pnuemonia")
                    f = open('Pneumonia-Next-Steps.txt','r')
                    contents = f.read()
                    bttn = st.download_button('What should be done next?',contents,file_name='Next Steps')
                    if bttn:
                        st.markdown("### Thank you for choosing Medi-Bot...!!")  
        #add pipeline for Pnuemonia daignosis here

    elif d=='Tuberculosis':
        st.markdown("## Please upload your X-ray image below")
        image= st.file_uploader("Please upload JPEG/PNG image of your Xray here", type= ['jpg','jpeg','png'], accept_multiple_files=False)
        if image is not None:
            image = Image.open(image)
            x= np.array(image)
            tb=st.button("Submit Image")
            if tb:
                prediction = LC.tb_predict(x)
                if prediction[0][0]==0:
                    st.success("### Normal ")
                else:
                    st.error("### Tuberculosis")
                    f = open('TB-Next-Steps.txt','r')
                    contents = f.read()
                    bttn = st.download_button('What should be done next?',contents,file_name='Next Steps') 
                    if bttn:
                        st.markdown("### Thank you for choosing Medi-Bot...!!") 
        #add pipeline for TB daignosis here
    else:
        st.error("Please select a valid response.")

    

    if st.button("Reset"):
        pyautogui.hotkey("ctrl","F5")



