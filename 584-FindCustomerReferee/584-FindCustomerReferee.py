# Last updated: 4/4/2025, 5:45:37 PM
df = visits_no_trans.groupby('customer_id', as_index=False)['visit_id'].count()

return df.rename(columns={'visit_id': 'count_no_trans'})