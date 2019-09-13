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
    # No. of females is significantly higher than males

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

def clean_data(df):
    # Now we'll drop the columns that are not required
    df.drop(columns=['PatientId', 'ScheduledDay', 'AppointmentDay', 'Handcap'], inplace=True)

    # Rename columns for convenience
    df.rename(columns={'AppointmentID': 'appointment_id', 'Age': 'age', 'Gender': 'gender',
    'Neighbourhood': 'neighbourhood', 'Scholarship': 'scholarship', 'Hipertension': 'hypertension',
    'Diabetes': 'diabetes', 'Alcoholism': 'alcoholism', 'SMS_received': 'sms_received',
    'No-show': 'no_show'}, inplace=True)

    return df

def explore_gender(df):

    # First, let's look at how gender relates to no-shows


    plt.pie(df['gender'].value_counts(), labels=['F', 'M'], autopct='%1.1f%%')
    plt.title('DISTRIBUTION OF APPOINTMENTS BY GENDER')
    plt.show()

    # No. of females is significantly higher than females

    """Above are the total counts of both genders. We create two DataFrames below, one where the
     patients didn't show up and one where they did show up"""

    df_no_show = df.query('no_show == "Yes"')
    df_show = df.query('no_show == "No"')

    # Let's store the counts of both genders in Pandas Series

    total_count_genders = df['gender'].value_counts()
    total_count_genders

    # Now, let's see gender counts for df_no_show and df_show

    no_show_gender_counts = df_no_show['gender'].value_counts()
    no_show_gender_counts

    show_gender_counts = df_show['gender'].value_counts()
    show_gender_counts

    # To make a uniform comparison between the genders, let's calculate the proportions of gender counts for shows and no-shows

    no_show_gender_proportions = no_show_gender_counts/total_count_genders
    no_show_gender_proportions

    show_gender_proportions = show_gender_counts/total_count_genders
    show_gender_proportions

    # We observe that the proportions of genders showing up and not showing up are almost similar

    # Let's plot our findings

    sns.set_style('darkgrid')
    ind = np.arange(len(show_gender_proportions))
    width = 0.35

    male_bar = plt.bar(ind, [show_gender_proportions['M'], no_show_gender_proportions['M']], width,
    color='r', alpha=0.7, label='Male')
    female_bar = plt.bar(ind+width, [show_gender_proportions['F'], no_show_gender_proportions['F']], width,
    color='b', alpha=0.7, label='Female')
    plt.title('APPOINTMENT FULFILMENT BY GENDER')
    plt.xlabel('WHETHER PATIENT SHOWED UP OR NOT')
    plt.ylabel('PROPORTION OF PEOPLE')
    locations = ind+width/2
    labels = ['Showed Up', 'No-showed']
    plt.xticks(locations, labels)
    plt.legend();
    plt.show()
    print(plt)

    # Thus, we can clearly see that about 80% of the people of both genders showed-up for their appointments
    # whereas about 20% didn't

def explore_neighbourhoods(df):

    df_no_show = df.query('no_show == "Yes"')
    df_show = df.query('no_show == "No"')

    # Now, let's see which are the neighbourhoods with the most no-shows

    no_show_neighbourhoods_patient_count = df_no_show['neighbourhood'].value_counts()
    no_show_neighbourhoods_patient_count

    # We observe that there are 80 neighbourhoods in our DataFrame.

    # Let's try and get the proportion of no-shows relative to the original neighbourhood counts

    patients_by_neighbourhood = df['neighbourhood'].value_counts()
    neighbourhood_proportions = no_show_neighbourhoods_patient_count/patients_by_neighbourhood

    # Let's try to get the top 5 neighbourhoods with the most no-show proportions

    neighbourhood_proportions.sort_values(ascending=False, inplace=True)

    top_no_show_neighbourhoods = neighbourhood_proportions.head(5)
    top_no_show_neighbourhoods

    # Let's plot these

    width = 0.35
    plt.bar(1, top_no_show_neighbourhoods[0], width, color='r', alpha=0.7, label=top_no_show_neighbourhoods.index[0].title())
    plt.bar(2, top_no_show_neighbourhoods[1], width, color='y', alpha=0.7, label=top_no_show_neighbourhoods.index[1].title())
    plt.bar(3, top_no_show_neighbourhoods[2], width, color='g', alpha=0.7, label=top_no_show_neighbourhoods.index[2].title())
    plt.bar(4, top_no_show_neighbourhoods[3], width, color='b', alpha=0.7, label=top_no_show_neighbourhoods.index[3].title())
    plt.bar(5, top_no_show_neighbourhoods[4], width, color='magenta', alpha=0.7, label=top_no_show_neighbourhoods.index[4].title())
    plt.title('NEIGHBOURHOODS WITH HIGHEST PROPORTIONS OF NO_SHOWS')
    plt.xlabel('NEIGHBOURHOODS')
    plt.ylabel('PROPORTIONS OF NO-SHOWS')
    plt.legend();
    plt.show()

def explore_age_groups(df):
    # Let's try and see no-shows by age groups

    df['age'].describe()

    df[df['age'] == df['age'].min()]

    # We see that the minimum age in the database is -1, which is ambiguous. Hence, we'll remove that row from the database

    df.drop(99832, inplace=True)

    df['age'].describe()

    """Now, let's use Pandas' cut function to distribute ages into groups. We'll create groups using the
    values obtained from describe(), i.e., the 5 number summary"""

    bin_edges = [0, 18.00, 37.00, 55.00, 115.00]
    bin_names = ['Children', 'Young Adults', 'Middle-Aged', 'Seniors']

    # We now create a new column for age-group in the DataFrame

    df['age_group'] = pd.cut(df['age'], bin_edges, labels=bin_names)

    # Let's check our DataFrame

    df.head()

    # Let us group the DataFrame by these age-groups and try to see no-shows according to age-groups

    no_show_counts_by_age_group = df.groupby(['age_group', 'no_show'])['appointment_id'].count()
    no_show_counts_by_age_group

    total_appointments_by_age_groups = df.groupby('age_group')['appointment_id'].count()
    total_appointments_by_age_groups
    plt.pie(total_appointments_by_age_groups, labels=bin_names, autopct='%1.1f%%')
    plt.title('DISTRIBUTION OF APPOINTMENTS BY AGE GROUPS')
    plt.show()
    # Looks like appointments are evenly distributed among the age groups

    # Let's try to get the proportions of no-shows for all age-groups

    children_proportions = no_show_counts_by_age_group['Children']/total_appointments_by_age_groups['Children']
    children_proportions

    adult_proportions = no_show_counts_by_age_group['Young Adults']/total_appointments_by_age_groups['Young Adults']
    adult_proportions

    middle_proportions = no_show_counts_by_age_group['Middle-Aged']/total_appointments_by_age_groups['Middle-Aged']
    middle_proportions

    senior_proportions = no_show_counts_by_age_group['Seniors']/total_appointments_by_age_groups['Seniors']
    senior_proportions

    # Now, let us plot these values

    ind = np.arange(len(children_proportions))
    width=0.2
    child_bars = plt.bar(ind, children_proportions, width, color='c', alpha=0.7, label='Children')
    adult_bars = plt.bar(ind+width, adult_proportions, width, color='g', alpha=0.7, label='Young Adults')
    middle_bars = plt.bar(ind+width*2, middle_proportions, width, color='m', alpha=0.7, label='Middle-Aged')
    senior_bars = plt.bar(ind+width*3, senior_proportions, width, color='y', alpha=0.7, label='Seniors')
    plt.ylabel('PROPORTIONS')
    plt.xlabel('APPOINTMENT FUlFILLMENT')
    plt.title('PROPORTIONS OF APPOINTMENT FULFILMENTS BY AGE GROUPS')
    locations = ind+ 1.5*width
    labels = ['Showed-Up', 'No-Shows']
    plt.xticks(locations, labels)
    plt.legend();
    plt.show()

if __name__ == '__main__':
    df = load_data('noshowappointments-kagglev2-may-2016.csv')
    assess_data(df)
    clean_data(df)
    explore_gender(df)
    explore_neighbourhoods(df)
    explore_age_groups(df)
