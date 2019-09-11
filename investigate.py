#In this project, I'm investigating a dataset that contains 100,000 records of medical appointments in Brazil.

#Importing the packages required for analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the csv file into a Pandas DataFrame

df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
