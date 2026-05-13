
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    layout="wide"
)

# TITLE
st.title("Healthcare Operations & Patient Flow Analytics Dashboard")

# DASHBOARD DESCRIPTION
st.markdown(
    "Interactive healthcare analytics dashboard for monitoring patient flow, wait times, and operational performance."
)

# LOAD DATASET
df = pd.read_csv("cleaned_healthcare_data.csv")

# KPI CALCULATIONS
total_patients = len(df)

avg_wait_time = df['Patient Waittime'].mean()

avg_satisfaction = df['Patient Satisfaction Score'].mean()

total_admissions = df['Patient Admission Flag'].count()

# KPI SECTION
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", total_patients)

col2.metric("Average Wait Time", round(avg_wait_time, 2))

col3.metric("Avg Satisfaction", round(avg_satisfaction, 2))

col4.metric("Total Admissions", total_admissions)

# SIDEBAR
st.sidebar.title("Healthcare Filters")

st.sidebar.header("Filter Data")

# DEPARTMENT FILTER
department_filter = st.sidebar.selectbox(
    "Select Department",
    ['All'] + list(df['Department Referral'].unique())
)

# GENDER FILTER
gender_filter = st.sidebar.selectbox(
    "Select Gender",
    ['All'] + list(df['Patient Gender'].unique())
)

# MONTH FILTER
month_filter = st.sidebar.selectbox(
    "Select Month",
    ['All'] + list(df['Month'].unique())
)

# FILTER LOGIC
filtered_df = df.copy()

if department_filter != 'All':
    filtered_df = filtered_df[
        filtered_df['Department Referral'] == department_filter
    ]

if gender_filter != 'All':
    filtered_df = filtered_df[
        filtered_df['Patient Gender'] == gender_filter
    ]

if month_filter != 'All':
    filtered_df = filtered_df[
        filtered_df['Month'] == month_filter
    ]

# PATIENTS BY DEPARTMENT
dept_counts = filtered_df['Department Referral'].value_counts()

fig1, ax1 = plt.subplots()

dept_counts.plot(kind='bar', ax=ax1)

ax1.set_xlabel("Department")
ax1.set_ylabel("Number of Patients")
ax1.set_title("Patients by Department")

plt.xticks(rotation=45)

# AVERAGE WAIT TIME BY DEPARTMENT
wait_time = filtered_df.groupby(
    'Department Referral'
)['Patient Waittime'].mean()

fig2, ax2 = plt.subplots()

wait_time.plot(kind='bar', ax=ax2)

ax2.set_xlabel("Department")
ax2.set_ylabel("Average Wait Time")
ax2.set_title("Average Wait Time by Department")

plt.xticks(rotation=45)

# FIRST ROW OF CHARTS
col1, col2 = st.columns(2)

with col1:
    st.subheader("Patients by Department")
    st.pyplot(fig1)

with col2:
    st.subheader("Average Wait Time by Department")
    st.pyplot(fig2)

# SATISFACTION SCORE BY DEPARTMENT
satisfaction = filtered_df.groupby(
    'Department Referral'
)['Patient Satisfaction Score'].mean()

fig3, ax3 = plt.subplots()

satisfaction.plot(kind='bar', ax=ax3)

ax3.set_xlabel("Department")
ax3.set_ylabel("Average Satisfaction Score")
ax3.set_title("Average Satisfaction Score by Department")

plt.xticks(rotation=45)

# PEAK HOUR ANALYSIS
hourly_patients = filtered_df['Hour'].value_counts().sort_index()

fig4, ax4 = plt.subplots()

hourly_patients.plot(kind='line', marker='o', ax=ax4)

ax4.set_xlabel("Hour")
ax4.set_ylabel("Number of Patients")
ax4.set_title("Patient Admissions by Hour")

# SECOND ROW OF CHARTS
col3, col4 = st.columns(2)

with col3:
    st.subheader("Average Satisfaction Score by Department")
    st.pyplot(fig3)

with col4:
    st.subheader("Patient Admissions by Hour")
    st.pyplot(fig4)

# GENDER DISTRIBUTION
st.subheader("Patient Gender Distribution")

gender_counts = filtered_df['Patient Gender'].value_counts()

fig5, ax5 = plt.subplots()

gender_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax5
)

ax5.set_ylabel("")

ax5.set_title("Gender Distribution")

st.pyplot(fig5)

# BUSINESS INSIGHTS
st.subheader("Key Business Insights")

st.info(
    """
    • General Practice handled the highest patient volume.
    
    • Higher wait times negatively impacted patient satisfaction.
    
    • Peak admission activity occurred during busy operational hours.
    
    • Certain departments experienced operational bottlenecks.
    """
)

