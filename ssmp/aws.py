import boto3
import pandas as pd


def get_ssms(path):

    client = boto3.client('ssm')
    data = client.get_parameters_by_path(
            Path=path,
            Recursive=False,
        )
    df=pd.DataFrame.from_dict(data['Parameters'])
    df['LastModifiedDate']=pd.to_datetime(df['LastModifiedDate']).dt.strftime("%y/%m/%d %H:%M")
    if df.empty == False:
        print(df[['Name','Type','Value','Version','LastModifiedDate']].to_string(index=False))

def search_ssms(path,key,recursive):

    client = boto3.client('ssm')
    data = client.get_parameters_by_path(
            Path=path,
            Recursive=recursive,
        )
    df=pd.DataFrame.from_dict(data['Parameters'])
    df['LastModifiedDate']=pd.to_datetime(df['LastModifiedDate']).dt.strftime("%y/%m/%d %H:%M")
    result=df.loc[df['Name'].str.contains(key)]
    if result.empty == False:
        print(result[['Name','Type','Value','Version','LastModifiedDate']].to_string(index=False))
    else:
        print("Not found")
