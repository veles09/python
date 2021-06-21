import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np

# selenium

# получение курса ( берёт пока среднее значение)
# path_to_chromedriver = 'E:/python/chromedriver' # change path as needed
# browser = webdriver.Chrome(executable_path = path_to_chromedriver)
# url = 'https://finance.rambler.ru/currencies/consensus/USD/'
# browser.get(url)
# kurs = browser.find_element_by_class_name('currency-forecast-table__mid-value').text
# c = float(kurs)

# получение прогнозов
tables = pd.read_html("https://finance.rambler.ru/currencies/consensus/?updated")
sr = (tables[1][1][0]+tables[1][1][1]+tables[1][1][2]+tables[1][1][3])/4
print(tables)
print(tables[0][1])
# float64 to float

x = np.float64(sr)
pyval = x.item()

# результат

# if pyval < c:
# 	print('покупай')
# else:
# 	print('продавай')


