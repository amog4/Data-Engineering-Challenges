Data Flow
Inputs
Three data sources are read in from a public S3 bucket:

Constituent Data: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv
E-mail Data:  https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv
Boolean columns (including is_primary) in all of these datasets are 1/0 numeric values. 1 means True, 0 means False.
Subscription Data: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv
We only care about subscription statuses where chapter_id is 1.
If an email is not present in this table, it is assumed to still be subscribed where chapter_id is 1.
A dataset simulating CRM data is available in these public AWS S3 files:

Constituent Information: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv

Constituent Email Addresses: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv
Boolean columns (including is_primary) in all of these datasets are 1/0 numeric values. 1 means True, 0 means False.

Constituent Subscription Status: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv
We only care about subscription statuses where chapter_id is 1.
If an email is not present in this table, it is assumed to still be subscribed where chapter_id is 1.


Exercises


Column	    Type	    Description
email	    string	    Primary Email Address
code	    string	    Source code
is_unsub	boolean	    Is the primary email address unsubscribed?
create_dt	datetime	Person creation datetime
modified_dt	datetime	Person updated datetime

Use the output of #1 to produce an “acquisition_facts” file with the following schema that aggregates stats about when people in the dataset were acquired. Save it to the working directory.

Column	        Type	            Description
aquisition_date	datetime	        Calendar Date of Aquisition
aquisitions	    int	                count
