#In this project, I'm investigating a dataset that contains 100,000 records of medical appointments in Brazil.

#Importing the packages required for analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the csv file into a Pandas DataFrame
def load_data(str):
    df = pd.read_csv(str)
    return df

#Assessing the data
def assess_data(df):

    df.head()
    df.info()

    # We have 110527 rows and 14 columns.

    # We see that there are no null values in the dataset and hence we don't need to handle any missing data

    """We see that No-show is our independent variable. We can investigate how the gender of a person relates to him/her
    showing up for an appointment. In addition to gender, we can similarly investigate how the age,
    neighbourhood, and various conditions like diabetes can indicate a person fulfilling his/her appointment."""

    # We can also explore whether a person receiving a government scholarship has anything to do with no-shows

    # We can see if no-shows by persons receiving SMSes are lower than those who didn't get any messages

    # The PatientId is quite ambiguous and irrelevant for our investigation and hence can be dropped.

    # ScheduledDay and AppointmentDay are not needed for the present investigation and hence can be dropped.

    # Check for duplicate rows

    sum(df.duplicated())

    # So, there are no duplicate rows in our dataset

    df['Gender'].value_counts()
    # Two gender types: F and M

    df['Neighbourhood'].value_counts()

    # 81 neighbourhoods

    df['Scholarship'].value_counts()

    # Two Categories: 0(No) or 1(Yes)

    df['No-show'].value_counts()
    # Two categories : "No" or "Yes"

    df['SMS_received'].value_counts()
    # Two categories: 0(No) or 1(Yes)

    df['Handcap'].value_counts()
    # The Handcap column is ambiguous as we don't have details about the categories. Hence, we'll drop it

    df['Alcoholism'].value_counts()
    # Two categories: 0(No) or 1(Yes)

    df['Diabetes'].value_counts()
    # Two categories: 0(No) or 1(Yes)

    df['Hipertension'].value_counts()
    # Two categories: 0(No) or 1(Yes)


def main():
    df = load_data('noshowappointments-kagglev2-may-2016.csv')
    assess_data(df)
