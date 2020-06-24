from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
contaner = soup.find("title")
print(contaner.text)

plt.style.use('seaborn')

for i_2021 in df.loc[filt_2020,'Source']:
    source_counter_2021.update(i_2021.split(';'))
department_2021 = []
amount_2021 = []
for a in source_counter_2021.keys():
    department_2021.append(a)
for b in source_counter_2021.values():
    amount_2021.append(b)