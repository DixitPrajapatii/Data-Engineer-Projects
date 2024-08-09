import pandas as pd
import os
import boto3
from io import StringIO

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file
csv_file_path = os.path.join(current_dir, 'tweets.csv')

def Tweets_ETL():
    # Read the CSV file using the constructed path
    row_data = pd.read_csv(csv_file_path)
    
    # filling the column values Nan with NA
    dataframe = row_data.fillna('NA')
    
    #making title in proper case
    dataframe.columns = dataframe.columns.str.title()
    
    # Adding two column rank on likes and rank on shares
    dataframe['Rank_On_Number_Of_Likes'] = dataframe['Number_Of_Likes'].rank(ascending=False, method='min')
    dataframe['Rank_On_Number_Of_Shares'] = dataframe['Number_Of_Shares'].rank(ascending=False, method='min')
    
    # Convert the dataframe to a CSV buffer
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)

    # Upload the CSV buffer to S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket='airflowpro24', Key='Updated_tweets.csv', Body=csv_buffer.getvalue())

    return 'ETL process completed and file uploaded to S3'

# Uncomment the following line if you want to test the function manually
# Tweets_ETL()

