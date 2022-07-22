import re
value = str(value).upper()
value = value.replace("'S","")
value = re.sub(r' (INC|LLC|CO.|& CO.)+','',value)
if re.search(r'([A-Za-z]+)(\.)([A-Za-z]+)',value):
    value = value.replace("."," ")
else:
    value = value.replace(".","")

if re.search(r'([A-Za-z]+)(,)([A-Za-z]+)',value):
    value = value.replace(","," ")
else:
    value = value.replace(",","")

value = re.sub(r' (&) .*','',value)
value = re.sub(r'(ICE CREAM)','ICECREAM',value)
value = value.replace(" INC","").replace(" LLC","")
value = value.strip()
return value