from msilib.schema import Font
from tkinter import font
from sklearn.datasets import load_sample_image
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from yaml import load

@st.cache
def load_data():
    df=pd.read_csv('data.csv')
    return df

def salary():
    df=load_data()
    ops = ['Minimum Salary','Maximum Salary','Average Salary']
    sel_sal = st.selectbox("Select",ops)
    if sel_sal==ops[0]:
        fig = px.histogram(df, x='minimal_salary', marginal='box', 
                   color_discrete_sequence=['#330C73'])
        fig.update_layout(
            height=600, width=800, title_text='Minimal Salary',
            xaxis_title='salaries', yaxis_title="count", title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="black"        
        ))
        st.plotly_chart(fig)
    elif sel_sal==ops[1]:
        fig = px.histogram(df, x='maximal_salary', marginal='box', 
                   color_discrete_sequence=['#330C73'])
        fig.update_layout(
            height=600, width=800, title_text='Maximal Salary',
            xaxis_title='salaries', yaxis_title="count", title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="black" 
        ))
        st.plotly_chart(fig)
    elif sel_sal==ops[2]:
        fig = px.histogram(df, x='average_salary', marginal='box', 
                   color_discrete_sequence=['#330C73'])
        fig.update_layout(
            height=600, width=800, title_text='Average Salary',
            xaxis_title='salaries', yaxis_title="count", title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="black"
        ))
        st.plotly_chart(fig)

def job_open():
    df=load_data()
    ops = ['By Industry','By Sector','By Job Titles',]
    sel_sal = st.selectbox("Select",ops)
    if sel_sal==ops[0]:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['Industry'].value_counts().head(20).index,
            y=df['Industry'].value_counts().head(20).values,
            marker_color = '#330C73'))
        fig.update_layout(   
            height=600, width=800, title_text='Number of job openings by Industry',
            
            xaxis_title='job title', yaxis_title="count", title_x = 0.5,
            
            font=dict(
                    family="Courier New, monospace",
                    size=10,
                    color="black"     
        ))
        st.plotly_chart(fig)
    if sel_sal==ops[1]:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['Sector'].value_counts().head(20).index,
            y=df['Sector'].value_counts().head(20).values,
            marker_color = 'darkred'))
        fig.update_layout( 
            height=600, width=800, title_text='Number of job openings by Sector',
            xaxis_title='job title', yaxis_title="count", title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black" 
        ))
        st.plotly_chart(fig)
    if sel_sal==ops[2]:
        op = ['Without technologies','With technologies']
        sel = st.selectbox("Select",op)
        if sel==op[0]:
            fig = go.Figure()
            fig.add_trace(go.Bar(x=df['Job Title'].value_counts().head(20).index,
                y=df['Job Title'].value_counts().head(20).values,
                marker_color = 'darkgreen'))
            fig.update_layout(
                height=600, width=800, title_text='Number of job openings by Job Titles',
                xaxis_title='job title', yaxis_title="count", title_x = 0.5,
                font=dict(
                        family="Courier New, monospace",
                        size=14,
                        color="black"
            ))
            st.plotly_chart(fig)
        if sel==op[1]:
            df_copy = df[['Job Title','python', 'sql','excel','tableau', 'power bi']].copy()
            technology = df_copy.groupby('Job Title')[['python', 'sql','excel','tableau', 'power bi']].sum().sort_values(by='python', ascending=False).head(10)
            df_technology = pd.DataFrame(technology)
            df_technology.reset_index(inplace=True)
            df_technology['number_of_job_openings'] = df['Job Title'].value_counts()[:10].values
            fig = px.bar(df_technology, x='Job Title', y=['python', 'sql', 'excel', 'tableau',
                                             'power bi'],
            color_discrete_sequence=px.colors.qualitative.G10)
            fig.update_layout(
                height=600, width=800, title_text='Number of job openings by Job Title with technologies',
                xaxis_title='job title', yaxis_title="count",
                legend_title='technologies',
                font=dict(
                        family="Courier New, monospace",
                        size=14,
                        color="black"
            ))
            st.plotly_chart(fig)

def name_rating():
    df=load_data()
    ops = ['Minimum Salary','Maximum Salary','Average Salary','Companies with most Job offers']
    sel_sal = st.selectbox("Select",ops)
    if sel_sal==ops[0]:
        fig = px.scatter(df, y='Company Name', x='minimal_salary', color = 'Rating',
                 color_continuous_scale=px.colors.sequential.Bluered_r)
        fig.update_layout(
            height=600, width=800, title_text='Minimal salary and company names with rating scores',
            xaxis_title='salary', yaxis_title='Company Name', title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black"
                
        ))
        st.plotly_chart(fig)
    if sel_sal==ops[1]:
        fig = px.scatter(df, y='Company Name', x='maximal_salary', color = 'Rating',
                 color_continuous_scale=px.colors.sequential.Bluered_r)
        fig.update_layout(
            height=600, width=800, title_text='Maximal salary and company names with rating scores',
            xaxis_title='salary', yaxis_title='Company Name', title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black"
                
        ))
        st.plotly_chart(fig)
    if sel_sal==ops[2]:
        fig = px.scatter(df, y='Company Name', x='average_salary', color = 'Rating',
                 color_continuous_scale=px.colors.sequential.Bluered_r)
        fig.update_layout(  
            height=600, width=800, title_text='Average salary and company names with rating scores',
            xaxis_title='salary', yaxis_title='Company Name', title_x = 0.5,
            font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black" 
        ))
        st.plotly_chart(fig)
    if sel_sal==ops[3]:
        df_comp = df.groupby(['Company Name']).count()[['Job Title']]
        df_comp = df_comp.sort_values('Job Title', ascending=False)[:15]
        df_comp.plot(figsize = (18,8), kind = "bar")
        st.bar_chart(df_comp)

def revenue():
    df=load_data()
    ops = ['Bar','Pie']
    sel = st.selectbox("Select",ops)
    if sel == ops[0]:
        fig, ax = plt.subplots(facecolor='pink', figsize=(15,10))
        plt.title('Revenue')
        plt.xlabel('Amount')
        plt.ylabel('Count')
        df['Revenue'].value_counts().plot(kind='bar')
        plt.show()
        st.pyplot(fig)
    elif sel == ops[1]:
        fig, ax = plt.subplots(facecolor='pink', figsize=(15,10))
        plt.title('Revenue')
        df['Revenue'].value_counts().plot(kind='pie',
                                        autopct='%.1f',
                                        shadow=True)
        st.pyplot(fig)

def ownership():
    df=load_data()
    fig, ax = plt.subplots(facecolor='pink', figsize=(20,15))
    plt.title('Ownership')
    df['Type of ownership'].value_counts().plot(kind='barh')
    st.pyplot(fig)

def loc():
    df=load_data()
    loc_df=pd.read_csv('loc.csv')
    ops = ['By Location','By Industry','Ownership','Rating']
    sel = st.selectbox("Select",ops)
    if sel == ops[0]:
        fig = px.bar(loc_df, x='location', y='jobs', title='Data analytic job per location')
        st.plotly_chart(fig)
    if sel == ops[1]:
        industry = df.groupby("Industry").count()
        industry = industry["Job Title"]
        st.bar_chart(industry,height=500,width=500)
    if sel == ops[2]:
        ownership = df.groupby("Type of ownership").count()
        ownership = ownership["Job Title"]
        ownership.plot(figsize = (18,8), kind = "bar")
        st.bar_chart(ownership,height=500,width=500)
    if sel == ops[3]:
        rating = df.groupby("Rating").count()
        rating = rating["Job Title"]
        rating.plot(figsize = (18,8), kind = "bar")
        st.bar_chart(rating,height=500,width=500)


st.title('Job listing for Data Analytic Visualization')
st.header('This is a stramlit dashboard to analyze job listing for data analytic')

options = ['Salary','Job Opening','Company Name & Rating','Revenue','Ownership','Data Analyst job']
choice = st.sidebar.radio('Select any option',options)

if choice==options[0]:
    salary()
elif choice==options[1]:
    job_open()
elif choice==options[2]:
    name_rating()
elif choice==options[3]:
    revenue()
elif choice==options[4]:
    ownership()
elif choice==options[5]:
    loc()