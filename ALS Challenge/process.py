import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os,sys
import boto3
from datetime import datetime




# Read the files
constituent_information = pd.read_csv('data/cons.csv')
subscribers  = pd.read_csv('data/cons_email_chapter_subscription.csv',sep=',')
email = pd.read_csv('data/cons_email.csv',sep=',')


#  Add filters

email_primary = email.query('is_primary	 == 1')
subscribers_chapter = subscribers.query('chapter_id == 1')

# Get source

get_source = email_primary[['email','create_dt','modified_dt','cons_email_id','cons_id']].join(
    constituent_information[['cons_id','source']].set_index('cons_id'))

# Create people csv

people = get_source[['email','create_dt','modified_dt','cons_email_id','source']].merge(subscribers[['cons_email_id','isunsub']] ,
            how ='left',left_on = 'cons_email_id', right_on ='cons_email_id' )

# Small Transformtions
people['isunsub'] = people['isunsub'].apply(lambda x: True if x == 1.0 else False)
people['create_dt'] = people['create_dt'].apply(lambda d : d.split(',')[1])
people['modified_dt'] = people['modified_dt'].apply(lambda d :  d.split(',')[1])

#save the file
people[['email','source','create_dt','modified_dt','isunsub']].to_csv('data/people.csv',index=False)

#Get Aquisitions

people_df = pd.read_csv('data/people.csv',usecols= ['create_dt'])
people_df['aquisition_date'] = people_df['create_dt'].apply(lambda d : datetime.strptime(d.strip().split(' ')[0],'%Y-%m-%d'))

#Save agg
people_df = people_df.groupby('aquisition_date').count().reset_index().rename(columns = {'create_dt':'aquisitions'})
people_df.to_csv('data/aquisitions.csv',index=False)

