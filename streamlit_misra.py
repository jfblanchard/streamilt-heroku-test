# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:43:32 2022

@author: Jon

Another streamlit tutorial

"""

import streamlit as st

# create 4 containers
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Streamlit running on Heroku (hopefully)')
    st.text('In this project, I will do some things first and then some other things')
    
with dataset:
    st.header('A container for the dataset')
    st.text('Things like shape, features, nulls, dtypes, stats')
    
with features:
    st.header('Feature engineering will go here')
    
with model_training:
    st.header('Start training a model')
    st.text('You can choose the hyperparameters here and see how they affect things.')

