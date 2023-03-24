import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

teams=[
 'Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Kings XI Punjab',
 'Kings XI Punjab',
 'Delhi Capitals'
]

e_cities=['Mumbai',
  'Kolkata',
 'Delhi',
 'Bangalore',
 'Chennai',
 'Chandigarh',
 'Jaipur',
 'Hyderabad',
 'Abu Dhabi',
 'Durban',
 'Pune',
 'Ahmedabad',
 'Centurion',
 'Dharamsala',
 'Port Elizabeth',
 'Visakhapatnam',
 'Ranchi',
 'Indore']

st.title('IPL 2023 Score Prediction')
col1,col2=st.columns(2)

with col1:
    batting_team=st.selectbox('Select batting team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select bowling team',sorted(teams))

city=st.selectbox('Select city',sorted(e_cities))

col3,col4,col5=st.columns(3)

with col3:
 current_score= st.number_input('Current Score')


with col4:
 overs_completed=st.number_input('Overs completed(over>5)')

with col5:
 wickets=st.slider('Wickets_out',0,10)

last_five_over=st.number_input('Runs Scoed in last 5 Overs')

if st.button('Predict Score'):
  balls_left=120-(overs_completed*6)
  wickets_left=10- wickets
  crr=current_score/overs_completed

  input_data_f=pd.DataFrame(
  {'batting_team':[batting_team],'bowling_team': [bowling_team],'city': city, 'current_score' : [current_score],
   'balls_left': [balls_left],'wickets_left': [wickets],'crr': [crr], 'last_five_over': [last_five_over]

  }
 )
  result=pipe.predict(input_data_f)
  st.text("Predicted Score  "+ str(int(result[0])))


