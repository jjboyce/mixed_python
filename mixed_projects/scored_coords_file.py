## create scored coords file ###

## change data to co-ordinates and score ###
import os
import csv
import pandas as pd

scored_df = pd.read_csv('scored_file.csv')
coords_df = pd.read_csv('coords_file.csv')

columns_to_complete = ['authorities', 'coords', 'Score']

complete_file = pd.merge(scored_df, coords_df, on='authorities', how='inner')

complete_file.to_csv('scored_coords_file.csv', index=False)


