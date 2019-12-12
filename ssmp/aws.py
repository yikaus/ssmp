import boto3


def get_ssms():

    client = boto3.client('ssm')
    data = client.get_parameters_by_path(
            Path='/',
            Recursive=False,
        )
    print(data['Parameters'][0]['Name'],data['Parameters'][0]['Value'])
