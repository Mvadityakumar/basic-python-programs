given=int(input('enter the mintues:'))
days=given//(24*60)
remaining=given%(24*60)
hours=remaining//60
minutes=remaining%60
print(days,'days,', hours,'hours,',minutes,'minutes.')