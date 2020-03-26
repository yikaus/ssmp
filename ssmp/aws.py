import boto3
import pandas as pd
import functools

MAX_COLWIDTH=100

def left_justified(df,quiet):
    formatters = {}
    for li in list(df.columns):
        if li in ('Version',):
            form = "{{!s:<8}}".format()
        else:
            max = min(df[li].str.len().max(),MAX_COLWIDTH-1)
            form = "{{:<{}s}}".format(max)
        formatters[li] = functools.partial(str.format, form)
    return df.to_string(formatters=formatters, index=False, header=(not quiet))

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
            if df.empty:
                return df
            else:
                Firstpage=False
        else:
            df=df.append(data['Parameters'])
    df['LastModifiedDate']=pd.to_datetime(df['LastModifiedDate']).dt.strftime("%y/%m/%d %H:%M")
    pd.options.display.max_colwidth=MAX_COLWIDTH
    pd.options.display.colheader_justify='left'
    return df

def get_ssms(path,recursive,all,quiet):
    df = get_data(path,recursive)
    if df.empty == False:
        if all:
            print(left_justified(df[['Name','Type','Value','Version','LastModifiedDate']],quiet))
        else:
            print(left_justified(df[['Name','Value']],quiet))

def search_ssms(path,key,recursive,value,all,quiet):

    df = get_data(path,recursive)
    if df.empty == False:
        if value:
            result=df.loc[df['Value'].str.contains(key)]
        else:
            result=df.loc[df['Name'].str.contains(key)]

        if result.empty:
            print("Not found")
        else:
            if all:
                print(left_justified(result[['Name','Type','Value','Version','LastModifiedDate']],quiet))
            else:
                print(left_justified(result[['Name','Value']],quiet))
    else:
        print("No parameters found")
