import pandas as pd
import os

PATH= '/Users/Sarah/Downloads/'
filename = 'College_Graduation_or_More.xlsx'
year = 2017
new_filename = 'city_wide_coll_grad_2017.csv'
comm_or_city = 'City'

def read_data(path, filename):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(path, filename))
    elif filename.endswith('.xls') or filename.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(path, filename))
    else:
        print('unexpected file type in read_data')
    return df

def parse_chi_health_atlas_df(df, date_range, geog):
   df = df[df['Year'] == date_range]
   if isinstance(date_range, int):
       df = df[df['Geography'] == geog]
   return df

df = read_data(PATH, filename)
df = parse_chi_health_atlas_df(df, year, comm_or_city)


df['Crude_Rate_Standardized'] = df['Crude_Rate'].apply(lambda x: 
                            ((x - df['Crude_Rate'].mean())/df['Crude_Rate'].std()))
#df['Crude_Rate_Standardized'].head(20)
#df['perc_nonwhite'] = 100 - df['Percent']
#df['perc_nonwhite'][i]+df['Percent'][i]

df.to_csv(os.path.join(PATH, new_filename))