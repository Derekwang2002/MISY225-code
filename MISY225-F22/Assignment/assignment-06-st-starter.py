# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# show the title
st.title('EDA for TITANIC dataset - by Wang Xing\'en')
st.header('Below is a datafraom')
# read csv and show the dataframe
ttnic_train = pd.read_csv('train.csv')
st.write(ttnic_train)

# create a figure with three subplots, size should be (15, 5)
st.header('Below is box plots for ticket price with different classes')
fig, ax = plt.subplots(1, 3, figsize=(15,5))

# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
i = 0

for class_name, class_df in ttnic_train.groupby('Pclass'):

    class_df.Fare.plot.box(ax=ax[i])
    ax[i].set_xlabel(f'Pclass = {class_name}')
    ax[i].set_ylabel('Fare')

    i += 1

st.pyplot(fig)



