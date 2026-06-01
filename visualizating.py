import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#data from 1992-2022 i.e lupus mortality ,US epidemiological data
data ={
    'Disease': ['Lupus (SLE)', 'Lupus (SLE)', 'Endometriosis'],
    'Gender': ['Female', 'Male', 'Female'],
    'High_Risk_Age_Onset': ['15-44', '15-44', '15-49'],
    'Recorded_Deaths_US_1999_2022': [44569, 7861, 0], 
    'Estimated_Living_US': [1350000, 150000, 6500000] 
}
df=pd.DataFrame(data)
lupus_mask = df['Disease'] == 'Lupus (SLE)'
total_lupus_deaths = df.loc[lupus_mask, 'Recorded_Deaths_US_1999_2022'].sum()
df['Percent_of_Lupus_Deaths'] = np.where( 
    lupus_mask,
    np.round((df['Recorded_Deaths_US_1999_2022'] / total_lupus_deaths) * 100, 1),   #mortality calculation
    np.nan
)

print(df.to_string(index=False))