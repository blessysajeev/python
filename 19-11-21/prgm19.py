year1=int(input('enter the current year'))
year2=int(input('enter the final year'))
for year in range(year1,year2):
    if(year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print(year)

