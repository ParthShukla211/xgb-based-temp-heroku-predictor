import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe = pickle.load(open('xgmodel.pkl','rb'))
st.title('XGBoost Based Temp Predictor')


LatDegree = st.number_input('LatDegree')
LongDegree = st.number_input('LongDegree')
MeasureDepth_m = st.number_input('MeasureDepth_m')
SurfTemp = st.number_input('SurfTemp')



# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict Clay'):
      input=pd.DataFrame({'LatDegree':[LatDegree],'LongDegree':[LongDegree],'MeasureDepth_m':[MeasureDepth_m],'SurfTemp':[SurfTemp]})
      result = pipe.predict(input)
      st.success('THE TEMPERATURE FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)
