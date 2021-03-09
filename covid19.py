from  urllib.request import urlopen
import json

f = open('data_to_datebase.txt','w')

insert_into = 'INSERT INTO covid19 (date_value, country_code, confirmed, deaths) VALUES '

data = urlopen('https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2020-03-01/2021-03-08')
data = data.read()
data = json.loads(data)
for i in data['data']:
    for j in data['data'][i]:
        x = data['data'][i][j]
        if x['confirmed'] == None:
            x['confirmed'] = 0
        if x['deaths'] == None:
            x['deaths'] = 0
        sql_line = insert_into +'(\'{}\', \'{}\', {}, {}); \n'.format(x['date_value'],x['country_code'],x['confirmed'],x['deaths'])
        f.write(sql_line)