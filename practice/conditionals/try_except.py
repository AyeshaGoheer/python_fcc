#condituonals try/except
astr="hello world"

try:
    istr=int(astr)
except:
    istr=-1

print("first", istr)


temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    print(cel)
