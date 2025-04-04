# Last updated: 4/4/2025, 6:10:20 PM
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Join prices and units_sold tables based on product_id
    merged_data = prices.merge(units_sold, on='product_id')
    
    # Filter the merged data to only include purchase_date within the price period
    filtered_data = merged_data[
        (merged_data['purchase_date'] >= merged_data['start_date']) &
        (merged_data['purchase_date'] <= merged_data['end_date'])
    ]
    
    # Calculate revenue for each sale
    filtered_data['revenue'] = filtered_data['price'] * filtered_data['units']
    
    # Group by product_id and calculate the average selling price
    result = filtered_data.groupby('product_id')['revenue'].sum() / filtered_data.groupby('product_id')['units'].sum()
    
    # Round the result to two decimal places
    result = result.round(2).reset_index()
    result.columns = ['product_id', 'average_price']

    # Find all unique product_id
    prices = pd.DataFrame(columns=['product_id'], data=prices['product_id'].unique())

    # Left merge on prices and retain products with zero sales units.
    result = prices.merge(result[['product_id', 'average_price']], on='product_id', how='left').fillna(0)
    
    return result

