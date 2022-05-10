import matplotlib.pyplot as plt
import random
import math
import numpy as np
import streamlit as st
st.write("Demo sineprime")
N=st.slider("frequency",1,20,1)
x=np.linspace(0,50,1000)
y=np.cos(x*N) + np.cos(x)
fig, ax=plt.subplots()
plt.plot(x, y)
st.pyplot(fig)


