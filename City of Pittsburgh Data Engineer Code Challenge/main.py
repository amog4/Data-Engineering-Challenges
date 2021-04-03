import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#Tasks

"""Moving Rows With Null Values Into invalid_data
Converting Senate District Names to lower
taking a substring containing only year from birth date column
reording columns to place yr_born to the right of dateofbirth
converting yr_born datatype to integer
Finding Relationship Between Age, Party Affiliation, & Overall Ballot Requests """


application = pd.read_json('https://data.pa.gov/resource/mcba-yywm.json')


# mask nulls

mask = application.isnull().any(axis=1)

application['Invalid_data'] = mask

application = application[application['Invalid_data'] != True]


# Senate lower 

application['senate'] = application['senate'].str.lower()
application['senate'] = application['senate'].str.replace(' ','_')

print(f"Unique Senate {application['senate'].nunique()}")


# Year born


application['year_born'] = application['dateofbirth'].str[:4]

application['year_born'] = application['year_born'].astype(int)


# Find age


application['age'] = application['year_born'].apply(lambda x : 2021-x)

application['result'] = 1


age_party_count = application.groupby(['party','age'],axis = 0)['result'].sum().reset_index()


application['party'] = application['party'].apply(lambda x : 'Others' if x not in ['D','R'] else x)


# chart 1 

fig, ax = plt.subplots(figsize=(18,7))

colors = {"D":'blue',"R":'red',"Others":'purple'}
ax.scatter(x=application[application['party'] == 'D']['age'] , y=application[application['party'] == 'D']['result']  , c=application[application['party'] == 'D']['party'] .apply(lambda x : colors[x]))
ax.scatter(x=application[application['party'] == 'R']['age'] , y=application[application['party'] == 'R']['result']  , c=application[application['party'] == 'R']['party'] .apply(lambda x : colors[x]))
ax.scatter(x=application[application['party'] == 'Others']['age'] , y=application[application['party'] == 'Others']['result']  , c=application[application['party'] == 'Others']['party'] .apply(lambda x : colors[x]))
plt.legend(labels=['Democrats','Republicans','Third Party'])
plt.title('Ballot Requests as a Function of Age & Party', size=24)
plt.xlabel('Age', size=18)
plt.ylabel('Ballot Requests', size=18)


# Bin age

age_range = [0,29,39,49,59,69,79,89,100]

age_party_count['age_bins'] = pd.cut(age_party_count['age'],age_range)

age_p_bins= age_party_count.groupby(['age_bins','party'], as_index=False)['result'].sum()


dem_data =  age_p_bins.query('party == "D"')
rep_data = age_p_bins.query('party  == "R"')


# Chart 2
X = np.arange(dem_data['age_bins'].count())
fig, ax = plt.subplots()

ax.bar(X + 0.00, dem_data['result'], color=dem_data['party'].apply(lambda x: colors[x]), width = 0.25)
ax.bar(X + 0.25, rep_data['result'], color=rep_data['party'].apply(lambda x: colors[x]), width = 0.25)


# Ballot return time lag
application['ballotreturneddate'] = pd.to_datetime(application['ballotreturneddate'],format='%Y-%m-%d')
application['appissuedate'] = pd.to_datetime(application['appissuedate'],format='%Y-%m-%d')
application['date_diff'] = application['ballotreturneddate']  - application['appissuedate']

application['date_diff'] = int(application['date_diff'].astype(str).str.split(' ')[0][0])


# legislative_median_days

legislative_median_days = application[['legislative','date_diff']].groupby('legislative')['date_diff'].median().reset_index()


# Republican & Democratic Application Counts in Each County

dem_rep_data = application[application['party'].isin(["D","R"])]

# use unstack to reset index and fill na 

dem_rep_data = dem_rep_data.groupby(['countyname', 'party']).result.sum().unstack(fill_value = 0).stack().reset_index(name='result')