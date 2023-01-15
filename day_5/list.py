# Day 5: 30 Days of python programming

# Exercises: Level 1

# Question 1
lis = []

# Question 2
lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Question 3
print("Length of string is:",len(lis))

# Question 4
print("First item:", lis[0], "Middle item:",lis[len(lis)//2], "Last item:", lis[len(lis)-1])

# Question 5
lis = ["Jhon", "10", "6.2", "False", "street 20"]

# Question 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Question 7
print(it_companies)

# Question 8
print("Number of companies in a list is:", len(it_companies))

# Question 9
print("First company:", it_companies[0], "Middle company:",it_companies[(len(lis)//2)+1], "Last company:", it_companies[len(lis)-1])

# Question 10
it_companies[0] = "Meta"
print(it_companies)

# Question 11
it_companies.append("OpenAi")
print(it_companies)

# Question 12
pos = it_companies[len(it_companies)//2]
it_companies.insert(it_companies.index(pos), "Nvidia")
print("Inserting element at middle:", it_companies)

# Question 13
print("Captalize company name:",it_companies[3].upper())

# Question 14
print("# ".join(it_companies))

# Question 15
search = "OpenAi" in it_companies
print("For finding certain company.", search)

# Question 16
print("Sorting list")
it_companies.sort()
print(it_companies)

# Question 17
print("Reversing list")
it_companies.reverse()
print(it_companies)

# Question 18
print("Slicing 1-3 company")
del it_companies[0:3]
print(it_companies)

# Question 19
print("Slicing Last 3 company")
del it_companies[-3:-1]
print(it_companies)

# Question 20
print("Slicing Middel company")
pos = it_companies[len(it_companies)//2]
it_companies.remove(pos)
print(it_companies)

# Question 21
print("Slicing Last 3 company")
del it_companies[0]
print(it_companies)

# Question 22
print("Slicing Middel company")
pos = it_companies[len(it_companies)//2]
it_companies.remove(pos)
print(it_companies)

# Question 23
print("Slicing Last company")
del it_companies[-1]
print(it_companies)

# Question 24
print("Remove all companies")
it_companies.clear()
print(it_companies)

# Question 25
print("Delete list")
del it_companies

# Question 25
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
print("After joining list:", join)

# Question 26
full_stack = join.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Exercises: Level 2

# Question 1.1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

# Question 1.2
max = max(ages)
print("Max age is:", max)
min = min(ages)
print("Min age is:", min)

# Question 1.3
mid1 = ages[len(ages)//2]
mid2 = ages[(len(ages)//2) + 1]
pos1 = ages.index(mid1)
pos2 = ages.index(mid2)
median = int((ages[pos1] + ages[pos2]) / 2)
print("Median of ages is:", median)

# Question 1.4
Avg = sum(ages)/len(ages)
print("Average of ages is:", Avg)

# Question 1.5
rnge = max - min
print("Range of ages is:", rnge)

# Question 1.6
absMax = abs(min - Avg)
absMin = abs(max - Avg)
print("Comparing value of (min - average) and (max - average):", absMin == absMax)

# Question 1
countries = [
  'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas',
  'Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei',
  'Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros',
  'Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic',
  'East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon',
  'Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India',
  'Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait',
  'Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia',
  'Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar',
  'Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay',
  'Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino',
  'Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands',
  'Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand',
  'Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States',
  'Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
]
print("Middel country is: ", countries[len(countries)//2])
print()
# Question 2
print(countries)
print()

# Question 3
lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a, b, c , *scandic = lst
print(a)     
print(b)    
print(c)     
print(scandic)