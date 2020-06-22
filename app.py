import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title(" Datasets Explorer App")
    activities=["Eda","Plots"]

    choice=st.sidebar.selectbox("Select Activities",activities)

    if choice=="Eda":
        st.subheader("Exploratory Data Analysis")
        data=st.file_uploader("Upload your Dataset",type=["csv","txt"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
            cols=df.columns.to_list()

            if st.checkbox("Show Shape"):
                st.write(df.shape)
            if st.checkbox("Unique Values"):
      
                selected_columns=st.selectbox("Select Columns",cols)
                x=df[selected_columns].unique()
                st.write(x)
     
            if st.checkbox("Missing values"):
                st.write(df.isnull().any())
            if st.checkbox("Show all Columns"):

                st.write(cols)
            if st.checkbox("Get Numerical and non Numericals Columns"):
                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

                newdf = df.select_dtypes(include=numerics)
                p=newdf.columns
                main_list = np.setdiff1d(cols,p)
                st.write("Numerical columns",p)
                st.write("Non Numerical columns",main_list)
            if st.checkbox("Summary"):
                st.write(df.describe())
            if st.checkbox("Show partcular Columns"):

                selected_columns=st.multiselect("Select Columns",cols)
                df2=df[selected_columns]
                st.dataframe(df2)
            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:,-1].value_counts())
            if st.checkbox("Correlation Plot(Heatmap)"):
                st.write(sns.heatmap(df.corr(),annot=True))
                st.pyplot()











    if choice=="Plots":
        st.subheader("Data Visualization")
        data=st.file_uploader("Upload your Dataset",type=["csv","txt"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
            cols = df.columns.tolist()

            if st.checkbox("Show Value Counts"):
                col_n = st.multiselect("Select Columns To Plot",cols)
                for i in col_n:
                    st.write(df[i].value_counts().plot(kind='bar'))
                    st.pyplot()

            elif st.checkbox("Generate Plot"):
                cols = df.columns.tolist()
                plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
                col_name = st.multiselect("Select Columns To Plot",cols)
                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

                newdf = df.select_dtypes(include=numerics)
                p=newdf.columns
                main_list = np.setdiff1d(cols,p)
                non_num=list(set(main_list) & set(col_name))
                if non_num:
                    st.write("Could not create plot of ",non_num)
                col_name=list(set(col_name) & set(p))
  
                df2 = df[col_name]
                if st.button("Generate"):
                    st.success("Plots of {}".format(plot,col_name))

                if plot=='area':
                    st.area_chart(df2)
                if plot=='bar':
                    st.bar_chart(df2)
                if plot=='line':
                    st.line_chart(df2)
                elif plot:
                    cust_plot= df2.plot(kind=plot)
                    st.write(cust_plot)
                    st.pyplot()

if __name__=='__main__':
    main()