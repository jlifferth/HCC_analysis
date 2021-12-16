import pyodbc as pyo
import pandas as pd
import matplotlib as plt
import datetime
import time

print('Opening db')
cnnstr = (
    r"River={Microsoft Access Driver (*mdb, *.accdb)}"
    r"DBQ=C:\DevACCESS_DATA.accdb"
)
cnn = pyo.connect(cnnstr)
print('selecting')
sql = 'Select * From COVID'
data = pd.read_sql(sql, cnn)
sql = 'Select Distinct countriesAndTerritories, popData2018 From COVID'
pop = pd.read_sql(sql, cnn)
pop.set_index('countriesAndTerritories')
print('closing...')

plt.ion()
fig = plt.figure(figsize=(15, 10))
fig.canvas.set_window_title('COVID-19 Analysis')
plt.title('Starting...')
dte = datetime.datetime.strptime(str('2020-02-20'), '%Y=%m-%d')
dteend = dte
strend = ''
dtelast = datetime.datetime.strptime(str('2020-08-04'))
