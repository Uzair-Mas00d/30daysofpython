# Day 21: 30 Days of python programming
from collections import Counter
# Exercises: Level 1

# Question 1 

class Statistics:
    def __init__(self,ages):
        self.ages = ages

    def count(self):
        return len(self.ages)

    def sum(self):
        self.total = 0
        for i in self.ages:
            self.total += i
        return self.total

    def min(self):
        self.mins = min(self.ages)
        return self.mins

    def max(self):
        self.maxs = max(self.ages)
        return self.maxs

    def range(self):
        self.ranges = self.max() - self.min()
        return self.ranges

    def mean(self):
        self.Avg =sum(self.ages)/len(ages)
        return round(self.Avg)
    
    def median(self):
        self.ages = sorted(self.ages)
        self.index = len(self.ages) // 2
        if len(self.ages) % 2 != 0:
            return self.ages[self.index]
        return (self.ages[self.index -1] + self.ages[self.index]) / 2

    def mode(self):
        self.dic = {}
        self.data = Counter(self.ages)
        self.data = self.data.most_common(1)
        for i in self.data:
             self.dic["mode"] = i[0]
             self.dic["count"] = i[1]
        return self.dic
    def std(self):
        self.summ = 0
        self.div = 0
        self.means = self.mean()
        for x in self.ages:
            self.summ += (x - self.means)**2
            self.div = self.summ/len(self.ages)
        return (self.div ** 0.5)

    def var(self):
        self.means = self.mean()
        self.summ = 0
        for i in self.ages:
            self.summ += (i-self.means)**2
        return self.summ / len(self.ages) 

    def freq_dist(self):
        self.lst = []
        for i in set(self.ages):
            self.lst.append((self.ages.count(i) * 4.0, i))
        self.lst.sort(reverse=True)
        return self.lst

    def describe(self):
        return 'Count: %d\nSum: %d\nMin: %d\nMax: %d\nRange: %d\nMean: %d\nMedian: %d\nMode: %s\nStandard Deviation: ' \
               '%.2f\nVariance: %.2f\nFrequency Distribution: %s' % (
                   self.count(), self.sum(), self.min(), self.max(), self.range(), self.mean(), self.median(),
                   self.mode(),self.std(), self.var(), self.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.describe())

# Exercises: Level 2

# Question 1 
class PersonAccount:
    def __init__(self,firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        return self.incomes

    def  total_expense(self):
        return self.expenses
    
    def account_info(self):
        return f"FullName: {self.firstname} {self.lastname}, Total income:{self.incomes} and Expense:{self.expenses}"
    
    def add_income(self,income):
        for k, v in income.items():
            self.incomes[k] = v            
        return self.incomes
    
    def add_expense(self,expense):
        for k, v in expense.items():
            self.expenses[k] = v
        return self.expenses

    def account_balance(self):
        self.total_income = 0
        self.total_expense = 0

        for v in self.incomes:
            self.total_income += self.incomes[v] 
        for v in self.expenses:
            self.total_expense += self.expenses[v]
        
        self.total_balance = self.total_income - self.total_expense
        return self.total_balance

person =PersonAccount('Ahmed', 'Ali', {'Salary': 150000, 'Bonus': 5500}, {'Rent': 20000, 'General': 4500})
print(person.account_info())
print("Total income of person is",person.total_income())
print("Total expense of person is",person.total_expense())
print(person.add_income({"Eidi":1800,"Gift":5000}))
print(person.add_expense({'Tax': 2500, 'Fuel': 5000}))
print("Total Balance of person is",person.account_balance())