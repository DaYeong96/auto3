
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import matplotlib
#import cv2
#import seaborn as sns
import plotly.express as px
#from skimage import io
from keras.models import load_model
from tensorflow.python import tf2

def welcome():
    st.title('이 앱은 용해탱크의 이상상황을 예측하는 앱입니다.')
    
    st.subheader('모바일에서는 상단의 ">"를 클릭해 데이터 입력 방식을 변경해주세요.') 
    
    st.image('용해탱크.png',use_column_width=True)   



#################################

def INSP_def():
    st.title('용해탱크 이상탐지 예측 서비스')
    st.title(' ')
    st.subheader('(1) 생산품의 수분함유량 10개 입력해주세요.')
    st.subheader('시간의 흐름을 판단하기 위해 10개의 값이 필요합니다.')

    
    INSP1 = st.slider('1 생산품의 수분함유량을 입력하세요', 0, 5)    #변수별로 10개씩 
    #st.write('1 생산품의 수분함유량:', INSP1)
    INSP2 = st.slider('2 생산품의 수분함유량을 입력하세요', 0, 5)    
    #st.write('2 생산품의 수분함유량:', INSP2)
    INSP3 = st.slider('3 생산품의 수분함유량을 입력하세요3', 0, 5)    
    #st.write('3 생산품의 수분함유량:', INSP3)
    INSP4 = st.slider('4 생산품의 수분함유량을 입력하세요', 0, 5)   
    #st.write('4 생산품의 수분함유량:', INSP4)
    INSP5 = st.slider('5 생산품의 수분함유량을 입력하세요', 0, 5)    
    #st.write('5 생산품의 수분함유량:', INSP5)
    INSP6 = st.slider('6 생산품의 수분함유량을 입력하세요', 0, 5)    
    #st.write('6 생산품의 수분함유량:', INSP6)
    INSP7 = st.slider('7 생산품의 수분함유량을 입력하세요', 0, 5)     
    #st.write('7 생산품의 수분함유량:', INSP7)
    INSP8 = st.slider('8 생산품의 수분함유량을 입력하세요', 0, 5)     
    #st.write('8 생산품의 수분함유량:', INSP8)
    INSP9 = st.slider('9 생산품의 수분함유량을 입력하세요', 0, 5)     
    #st.write('9 생산품의 수분함유량:', INSP9)
    INSP10 = st.slider('10 생산품의 수분함유량을 입력하세요', 0, 5)   
    #st.write('10 생산품의 수분함유량:', INSP10)


    INSP = pd.DataFrame({'INSP':[INSP1,INSP2,INSP3,INSP4,INSP5,INSP6,INSP7,INSP8,INSP9,INSP10]})

   
    st.subheader(' ')
    st.subheader('생산품의 수분함유량 Line Chart')
    st.line_chart(INSP)
    
    return INSP


############################################################

def MELT_TEMP_def():
    st.title('용해탱크 이상탐지 예측 서비스')
    st.title(' ')
    st.subheader('(2) 용해 온도 10개 입력해주세요.')
    st.subheader('시간의 흐름을 판단하기 위해 10개의 값이 필요합니다.')


    MELT_TEMP1 = st.slider('1 용해 온도를 입력하세요', 300, 900)  
    #st.write('1 용해 온도:', MELT_TEMP1)
    MELT_TEMP2 = st.slider('2 용해 온도를 입력하세요', 300, 900)  
    #st.write('2 용해 온도:', MELT_TEMP2)
    MELT_TEMP3 = st.slider('3 용해 온도를 입력하세요', 300, 900)  
    #st.write('3 용해 온도:', MELT_TEMP3)
    MELT_TEMP4 = st.slider('4 용해 온도를 입력하세요', 300, 900)  
    #st.write('4 용해 온도:', MELT_TEMP4)
    MELT_TEMP5 = st.slider('5 용해 온도를 입력하세요', 300, 900)  
    #st.write('5 용해 온도:', MELT_TEMP5)
    MELT_TEMP6 = st.slider('6 용해 온도를 입력하세요', 300, 900)  
    #st.write('6 용해 온도:', MELT_TEMP6)
    MELT_TEMP7 = st.slider('7 용해 온도를 입력하세요', 300, 900)  
    #st.write('7 용해 온도:', MELT_TEMP7)
    MELT_TEMP8 = st.slider('8 용해 온도를 입력하세요', 300, 900)  
    #st.write('8 용해 온도:', MELT_TEMP8)
    MELT_TEMP9 = st.slider('9 용해 온도를 입력하세요', 300, 900)  
    #st.write('9 용해 온도:', MELT_TEMP9)
    MELT_TEMP10 = st.slider('10 용해 온도를 입력하세요', 300, 900)  
    #st.write('10 용해 온도:', MELT_TEMP10)


    MELT_TEMP = pd.DataFrame({'MELT_TEMP' : [MELT_TEMP1, MELT_TEMP2, MELT_TEMP3, MELT_TEMP4, MELT_TEMP5, 
                                             MELT_TEMP6, MELT_TEMP7, MELT_TEMP8, MELT_TEMP9, MELT_TEMP10]})
    
    st.subheader(' ')
    st.subheader('용해 온도 Line Chart')
    st.line_chart(MELT_TEMP)
    
    return MELT_TEMP


############################################################


def MOTORSPEED_def():
    st.title('용해탱크 이상탐지 예측 서비스')
    st.title(' ')
    st.subheader('(3) 용해 교반속도 10개 입력해주세요.')
    st.subheader('시간의 흐름을 판단하기 위해 10개의 값이 필요합니다.')


    MOTORSPEED1 = st.slider('1 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('1 용해 교반속도:', MOTORSPEED1)
    MOTORSPEED2 = st.slider('2 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('2 용해 교반속도:', MOTORSPEED2)
    MOTORSPEED3 = st.slider('3 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('3 용해 교반속도:', MOTORSPEED3)
    MOTORSPEED4 = st.slider('4 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('4 용해 교반속도:', MOTORSPEED4)
    MOTORSPEED5 = st.slider('5 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('5 용해 교반속도:', MOTORSPEED5)
    MOTORSPEED6 = st.slider('6 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('6 용해 교반속도:', MOTORSPEED6)
    MOTORSPEED7 = st.slider('7 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('7 용해 교반속도:', MOTORSPEED7)
    MOTORSPEED8 = st.slider('8 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('8 용해 교반속도:', MOTORSPEED8)
    MOTORSPEED9 = st.slider('9 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('9 용해 교반속도:', MOTORSPEED9)
    MOTORSPEED10 = st.slider('10 용해 교반속도를 입력하세요', 0, 2000)   
    #st.write('10 용해 교반속도:', MOTORSPEED10)

    
    MOTORSPEED = pd.DataFrame({'MOTORSPEED' : [MOTORSPEED1, MOTORSPEED2, MOTORSPEED3, MOTORSPEED4, MOTORSPEED5,
                                               MOTORSPEED6, MOTORSPEED7, MOTORSPEED8, MOTORSPEED9, MOTORSPEED10]})
    
    st.subheader(' ')
    st.subheader('용해 교반속도 Line Chart')
    st.line_chart(MOTORSPEED)
    
    return MOTORSPEED
    
    
#########################################################################    
    
    
def auto_def(INSP, MELT_TEMP, MOTORSPEED):
    
#     INSP=INSP_def()
#     MELT_TEMP=MELT_TEMP_def()
#     MOTORSPEED=MOTORSPEED_def()
    
    new_x_df = pd.concat([INSP,MELT_TEMP,MOTORSPEED] ,axis=1)
    
    scaler_call = joblib.load("rscaler.pkl")   #정규화
    model_call = load_model('lstm_ae최종75_w(10)(128-32-b(64)).h5')

    new_x_df_scale = scaler_call.transform(new_x_df) #정규화 
    new_x_df_scale = new_x_df_scale.reshape(1,10,3)  #3차원 


    result = model_call.predict(new_x_df_scale)  #예측 
    
    def flatten(X):
        flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
        for i in range(X.shape[0]):
            flattened_X[i] = X[i, (X.shape[1]-1), :]
        return(flattened_X)
    
    
    mse = np.mean(np.power(flatten(new_x_df_scale) - flatten(result), 2), axis=1)
    error_df = pd.DataFrame({'Reconstruction_error':mse})
    threshold_fixed = 0.45472266911544296
    pred_y = [1 if e > threshold_fixed else 0 for e in error_df['Reconstruction_error'].values]   #75

    st.title(' ')
    st.subheader('(4) 용해탱크의 이상탐지 결과는 다음과 같습니다.')

    
    
    if INSP.sum().values == 0 or MELT_TEMP.sum().values == 0 or MOTORSPEED.sum().values == 0:
        st.info("분석 중입니다.")
    else:
        if pred_y==1:
            st.error("비정상으로 예측됩니다.")
        else:
            st.success("정상으로 예측됩니다.")


##############################################################################
 

selected_box = st.sidebar.selectbox('다음중 선택해주세요',
                                    ('설명서','1. 생산품의 수분함유량 입력', '2. 용해 온도 입력', '3. 용해 교반속도 입력', '결과'))
    
if selected_box == '설명서':
    welcome()
    st.sidebar.write("모바일에서는 상단의 X를 눌러 원래화면으로 가세요")
    
if selected_box == '1. 생산품의 수분함유량 입력':
    INSP_def()
    st.sidebar.write("모바일에서는 상단의 X를 눌러 원래화면으로 가세요")
    
if selected_box == '2. 용해 온도 입력':
    MELT_TEMP_def()
    st.sidebar.write("모바일에서는 상단의 X를 눌러 원래화면으로 가세요")
    
if selected_box == '3. 용해 교반속도 입력':
    MOTORSPEED_def()
    st.sidebar.write("모바일에서는 상단의 X를 눌러 원래화면으로 가세요")
    
if selected_box == '결과':
    auto_def(INSP, MELT_TEMP, MOTORSPEED)
    st.sidebar.write("모바일에서는 상단의 X를 눌러 원래화면으로 가세요")
      
