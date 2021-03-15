import numpy as np
import pandas as pd 

#Set to see max rows display should be 500 rows and all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.options.display.float_format = '{:.2f}'.format

Loan_df=pd.read_csv("C:\\Users\\gunak\\Desktop\\tableau\\loan.csv",encoding='utf-8')

#checking Nulls
print(Loan_df.isnull().sum())

#dropping 100% Na columns
Loan_df.dropna(how='all', axis=1,inplace=True)

#Dropping columns That has same values and insignificant  for analysis i.e.Desc,Emp_title,application_type,member_id
Loan_df.drop(['acc_now_delinq','chargeoff_within_12_mths','delinq_amnt','tax_liens','pymnt_plan','url',
'collections_12_mths_ex_med','policy_code','application_type','initial_list_status','desc','emp_title','title','member_id'],axis=1,inplace=True)

#Filling Na values with blanks to maintain uniform in Datatypes
Loan_df.fillna('',inplace=True)

#Converting Dti into Percentage as per Data Dictionary data Defination

#Loan_df['dti'].map(lambda n: '{:,.2%}'.format(n))

#print(Loan_df.head())
#print(Loan_df.shape)

# Remove suffix 'xx', months in zip code,Term column
Loan_df['zip_code'] = Loan_df[['zip_code']].applymap(lambda x:str(x).rstrip('xx'))
Loan_df['term'] = Loan_df[['term']].applymap(lambda x:str(x).rstrip('months'))
#converting into str datatype of term to int
Loan_df['term'] = Loan_df['term'].astype('int64')


#Adding new column for pub_rec_bankruptcies_Y/N to make it values as NO if its Zero
Loan_df['pub_rec_bankruptcies_Y/N']=Loan_df[['pub_rec_bankruptcies']].applymap(lambda x : 'NO' if x == 0 else 'YES')

#Adding Issued Year from issue_d column
Year=pd.to_datetime(Loan_df['issue_d'], format='%b-%y')
Loan_df['issue_d_year']=Year.dt.year

#Anlaysing Loan Amount whether its Small/Avg/High as per statistical categorial method as first, Avg  and Higest Quartiles

F_Q,A_Q,H_Q=(Loan_df['funded_amnt_inv']).quantile(.25),(Loan_df['funded_amnt_inv']).quantile(.50),(Loan_df['funded_amnt_inv']).quantile(.75)
print(F_Q,A_Q,H_Q)

#Adding new col as Derived col for intrepreting funded_amnt_inv by above F_Q,A_Q,H_Q values to find outliers

Loan_df['typeOfloan']= ['High(>14400)' if i>14400 else 'Avg(>5000 & <=8975)' if i>5000 and i<=8975 else 'Above Avg(>8733 & <=14000)' if i>8975 and i<14400 else 'Low(<=5000)'  for i in Loan_df['funded_amnt_inv']]

#Adding Loan(G/B) if Loan_status that are "Current", "Issued" and "Fully Paid" can be called “Good Loans” else "Bad Loans"
Loan_df['Loan(G/B)']= ['Bad' if i == 'Charged Off' else 'Good' for i in Loan_df['loan_status'] ]

#converting Loan_Status to number column for further analysis
Loan_df.loan_status[Loan_df.loan_status == 'Fully Paid' or Loan_df.loan_status == 'Current'] = 0
Loan_df.loan_status[Loan_df.loan_status == 'Charged Off'] = 1

print ('Cleaning is our dataset Lending (Loan) Club dataset is completed!')


#Saving cleaned data to folder for tableau visualisations
Loan_df.to_csv('C:\\Users\\gunak\Desktop\\tableau\\Cleaned_Loan.csv')



