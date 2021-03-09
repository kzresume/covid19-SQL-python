import pandas as pd

x = pd.read_html('https://pl.wikipedia.org/wiki/ISO_3166-1_alfa-3')[0]
f = open('polish_title','w')
insert_into = 'INSERT INTO codes (country_code, polish_title) VALUES '

for i in range(len(x)):
    polish = x.iloc[i]['polska nazwa skrócona']
    kod = x.iloc[i]['kod alfa-3']
    sql_line = insert_into + '(\'{}\', \'{}\');\n'.format(kod, polish)
    f.write(sql_line)
