from namara_python import Client

client = Client(
    api_key='5cd2d5e2f3d1c3968bf8025451b8f1ecb738c041ceb44c3c2061e61ec7188cac',  
    auth_url='https://account.namara.io',
    api_url='https://app.dataxch.ai/#/organizations/5e16472c-1fe3-0000-0000-bb293ba6ea20/data'
)

# FROM [dataset id]
#resp = client.query(statement='SELECT col1, col2 FROM d6509e3c-c583-48b4-b926-e9feca23893a')
#for row in resp:
#  print(row["col1"])
#  print(row["col2"])