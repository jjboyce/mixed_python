### Code to Merge Census Data by LA Areas ## 
import pandas as pd

census_df = pd.read_csv('copy_census_sexuality_tenancy_data.csv')

# Filter rows where Category is 'A'
filtered_df = census_df[census_df['Sexual_Code'].isin([2, 3, 4])]

merged_df = filtered_df.groupby('Lower tier local authorities Code', as_index=False).agg({
    'Lower tier local authorities': 'first',
    'Observation': 'sum'
})

# Save the merged DataFrame back to a new CSV file (optional)
merged_df.to_csv('shortened_data.csv', index=False)

