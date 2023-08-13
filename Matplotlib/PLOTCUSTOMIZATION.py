import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

# years = [2014 + x for x in range(8)]
# incomes = [55,56,62,61,72,72,73,75]
# income_ticet = list(range(50,81,2))

# plt.plot(years, incomes)
# plt.title('Income of Jhon', fontsize=30)
# plt.xlabel('Year')
# plt.ylabel('Income in US Dollar')
# plt.yticks(income_ticet, [f'{x}k USD' for x in income_ticet])
# plt.show()

stock_a = [100,102,99,101,101,100,102]
stock_b = [90,95,102,104,105,103,109]
stock_c = [110,115,100,105,100,98,95]

plt.plot(stock_a, label='Company1')
plt.plot(stock_b,label='Company2')
plt.plot(stock_c,label='Company3')
plt.legend(loc='lower right')
plt.show()