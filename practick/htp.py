import requests

# r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

# x = (r.json())

# for i in x:
#     if i['cc'] == 'EUR':
#         print(i['rate'])


def convert(cc, count,reverse=False):  # перевод грн в валюту (True наоборот)
    r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    for i in r.json():
        print('I ^ ' ,i )
        if i['cc'] == cc:
            course = i['rate']
            break
    else:
        return None
    
    if reverse:
        return count / float(course)
    
    return count * float(course)

print(convert('USD',20))

# def raz(val, val2, count): #перевод валюты + количество
#     r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
#     for i in r.json():
#         if i['cc'] == val:
#             a = i['rate']
#         if i['cc'] == val2:
#             b = i['rate']
#     return (float(a)*count)/ float(b)

# print(raz('EUR','USD',10))

# r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
# print(r.text)

"""d = {}  # перевод ответа в словарь , а не в список
for i in r.json():
    d[i['cc']] = float(i['rate'])"""

# r = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?date=19.01.2022&json')
# print(r.text)
# for i in r.json():
#     if i['CurrencyCodeL'] == 'EUR':
#         print(i['Amount'])

# r = requests.get('https://www.metaweather.com/api/location/search/?query=chicago')

# print(r.text)