### normalising data ###
import pandas as pd

normalise_df = pd.read_csv('copy_aggregate_data_lgbt_by_area.csv')

column_to_score = 'Observation'

normalise_df['Score'] = (normalise_df[column_to_score] - normalise_df[column_to_score].min()) / (normalise_df[column_to_score].max() - normalise_df[column_to_score].min())

normalise_df['Score'] = normalise_df['Score'].round(2)

normalise_df.to_csv('scored_file.csv', index=False)