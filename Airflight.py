# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:08:20 2022

@author: User
"""

import streamlit as st
import pandas as pd

airdata = pd.read_csv('AirPassengers.csv')
#st.table(airdata)
airdata['Year'] = pd.to_datetime(airdata['Month']).dt.year
def main():
        st.title('Air Pessenger Data')
        

        #year = st.text_input('Select Year to filter out')
        #airdata['Mon'] = pd.datetime(airdata('Month').dt.year)
        year = st.selectbox('Year',airdata.Year.unique()) 
    
        button = st.button('Show Result')
    
        if button:
           subset = airdata[airdata['Year'] == year]
           st.table(subset)
    
if __name__=='__main__':
     main()   