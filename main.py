import os as cmd
import pandas as pd

data = pd.read_excel('src/database.xlsx')

print(data)

df = pd.DataFrame(data, columns=['IP'])
print(df)

qntRows = len(df)

for row in range(qntRows):

  response = cmd.popen(f"ping {df.at[row, 'IP']}").read()
  print(response)

  if 'Recebidos = 4' in response:
    print(f"UP {df.at[row, 'IP']} Ping Successful")
    data.loc[row,'Ping'] = 'UP'
    
  elif 'Received = 4' in response:
    print(f"UP {df.at[row, 'IP']} Ping Successful")
    data.loc[row,'Ping'] = 'UP'
    
  else:
    print(f"DOWN {df.at[row, 'IP']} Ping Unsuccessful")
    data.loc[row, 'Ping'] = 'DOWN'

data.to_excel('databaseII.xlsx')

