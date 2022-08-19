import requests


def weather():
    s = {}
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?id=703448&appid=e09e739526c9999400019b9ccb71c59f')
    r = r.json()
    num = 0
    for i in range(4):
        s['Температура'] = str(
            round(int(r['list'][num]['main']['temp']) - 273.15)) + ' °C'
        s['Влажность'] = str(r['list'][num]['main']['humidity']) + ' %'
        s['Ветер'] = str(r['list'][num]['wind']['speed']) + ' м/с'
        print('\nПрогноз погоды на: ' + r['list'][num]['dt_txt'])
        for j in s.items():
            print(j[0]+' - '+j[1])
        num += 1


weather()
