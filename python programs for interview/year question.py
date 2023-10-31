given=int(input('enter the days:'))
year=given//365
remining=given%365
month=remining//12
days=month%12
print(year,'years,', month,'months,',days,'days.')
