import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

value = st.slider("三角函式",min_value=0,max_value=5)
t = np.arange(0.,5,0.05)
y1 = np.sin(np.random.randn() * value * np.pi * t)
y2 = np.cos(np.random.randn()* value * np.pi * t)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)