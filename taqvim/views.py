from django.shortcuts import render
import requests
import datetime
from datetime import date
now = datetime.datetime.now()
formatted_time = now.strftime("%H:%M:%S")
print(formatted_time)
today = date.today()




# Create your views here.
def taqvim(request):
    shahar = 'Toshkent'
    url = "http://api.aladhan.com/v1/calendarByCity"
    params = {
            "city": shahar,
            "country": "Uzbekistan",
            "method": "2",
            "school": "1",
            "month": datetime.date.today().month,
            "year": datetime.date.today().year,
            "adjustment": "0"
        }
    response = requests.get(url , params=params)
    data = response.json()
    i = datetime.date.today().day

    now = datetime.datetime.now()
    date = now.strftime("%I:%M %p")

    fajr = data["data"][i]["timings"]["Fajr"]
    Sunrise = data["data"][i]["timings"]["Sunrise"]
    dhuhr = data["data"][i]["timings"]["Dhuhr"]
    asr = data["data"][i]["timings"]["Asr"]
    maghrib = data["data"][i]["timings"]["Maghrib"]
    isha = data["data"][i]["timings"]["Isha"]
    data = response.json()
    if request.method == 'POST':
        shahar = request.POST.get('dropdown-value')
        url = "http://api.aladhan.com/v1/calendarByCity"
        params = {
            "city": shahar,
            "country": "Uzbekistan",
            "method": "2",
            "school": "1",
            "month": datetime.date.today().month,
            "year": datetime.date.today().year,
            "adjustment": "0"
        }
        response = requests.get(url, params=params)
        data = response.json()


        i = datetime.datetime.now().day
        now = datetime.datetime.now()
        date = now.strftime("%I:%M %p")


        fajr = data["data"][i]["timings"]["Fajr"]
        Sunrise = data["data"][i]["timings"]["Sunrise"]
        dhuhr = data["data"][i]["timings"]["Dhuhr"]
        asr = data["data"][i]["timings"]["Asr"]
        maghrib = data["data"][i]["timings"]["Maghrib"]
        isha = data["data"][i]["timings"]["Isha"]
        return render(request, 'taqvim.html', {'today':date,'shahar': shahar,'bomdod': fajr,
        'quyosh': Sunrise,
        'peshin': dhuhr,
        'asr': asr,
        'shom': maghrib,
        'xufton': isha})


    return render(request,'taqvim.html',{'today':date,'shahar': shahar,'bomdod': fajr,
        'quyosh': Sunrise,
        'peshin': dhuhr,
        'asr': asr,
        'shom': maghrib,
        'xufton': isha})







def jadval(request):
    shahar = 'Toshkent'
    url = "http://api.aladhan.com/v1/calendarByCity"
    params = {
            "city": shahar,
            "country": "Uzbekistan",
            "method": "2",
            "school": "1",
            "month": datetime.date.today().month,
            "year": datetime.date.today().year,
            "adjustment": "0"
        }
    response = requests.get(url , params=params)
    data = response.json()
    i = datetime.date.today().day

    now = datetime.datetime.now()
    date = now.strftime("%I:%M %p")

    oy = []

    for i in range(30):
        fajr = data["data"][i]["timings"]["Fajr"]
        Sunrise = data["data"][i]["timings"]["Sunrise"]
        dhuhr = data["data"][i]["timings"]["Dhuhr"]
        asr = data["data"][i]["timings"]["Asr"]
        maghrib = data["data"][i]["timings"]["Maghrib"]
        isha = data["data"][i]["timings"]["Isha"]
        oy.append({'bomdod': fajr[:-6],
            'quyosh': Sunrise[:-6],
            'peshin': dhuhr[:-6],
            'asr': asr[:-6],
            'shom': maghrib[:-6],
            'xufton': isha[:-6]})
        if request.method == 'POST':
            shahar = request.POST.get('dropdown-value')
            url = "http://api.aladhan.com/v1/calendarByCity"
            params = {
                    "city": shahar,
                    "country": "Uzbekistan",
                    "method": "2",
                    "school": "1",
                    "month": datetime.date.today().month,
                    "year": datetime.date.today().year,
                    "adjustment": "0"
                }
            response = requests.get(url , params=params)
            data = response.json()
            i = datetime.date.today().day

            now = datetime.datetime.now()
            date = now.strftime("%I:%M %p")

            oy = []

            for i in range(30):
                fajr = data["data"][i]["timings"]["Fajr"]
                Sunrise = data["data"][i]["timings"]["Sunrise"]
                dhuhr = data["data"][i]["timings"]["Dhuhr"]
                asr = data["data"][i]["timings"]["Asr"]
                maghrib = data["data"][i]["timings"]["Maghrib"]
                isha = data["data"][i]["timings"]["Isha"]
                oy.append({'bomdod': fajr[:-6],
                    'quyosh': Sunrise[:-6],
                    'peshin': dhuhr[:-6],
                    'asr': asr[:-6],
                    'shom': maghrib[:-6],
                    'xufton': isha[:-6]})
        return render(request,'jadval.html',{'today':date,'shahar': shahar,'oys':oy})
    


    return render(request,'jadval.html',{'today':date,'shahar': shahar,'oys':oy})



