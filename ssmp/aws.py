import boto3
import pandas as pd

def get_data(path,recursive):
    client = boto3.client('ssm')
    paginator = client.get_paginator('get_parameters_by_path')
    page_iterator = paginator.paginate(
        Path=path,
        Recursive=recursive,
    )
    Firstpage=True
    for data in page_iterator:
        if Firstpage:
            df=pd.DataFrame.from_dict(data['Parameters'])
            Firstpage=False
        else:
            df=df.append(data['Parameters'])
    return df

def get_ssms(path,recursive):
    df = get_data(path,recursive)
    df['LastModifiedDate']=pd.to_datetime(df['LastModifiedDate']).dt.strftime("%y/%m/%d %H:%M")
    if df.empty == False:
        print(df[['Name','Type','Value','Version','LastModifiedDate']].to_string(index=False))

def search_ssms(path,key,recursive,value):

    df = get_data(path,recursive)
    df['LastModifiedDate']=pd.to_datetime(df['LastModifiedDate']).dt.strftime("%y/%m/%d %H:%M")
    if value:
        result=df.loc[df['Value'].str.contains(key)]
    else:
        result=df.loc[df['Name'].str.contains(key)]

    if result.empty:
        print("Not found")
    else:
        print(result[['Name','Type','Value','Version','LastModifiedDate']].to_string(index=False))
