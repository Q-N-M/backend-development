from django.shortcuts import render
from datetime import date,datetime
import calendar
import random
def index(request):
    return render(request, 'desktop2.html')

def emoji(request):
    list_name = ['Ray','Harold','Zahran','Al Taaj','Angelin','Hanifah']
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    today = date.today().strftime(day+", %B %d %Y")
    today_split = today.split(" ")
    if today_split[2][-1] == "1":
        today_split[2] = today_split[2] + "st"
    elif today_split[2][-1] == "2":
        today_split[2] = today_split[2] + "nd"
    elif today_split[2][-1] == "3":
        today_split[2] = today_split[2] + "rd"
    else:
        today_split[2] = today_split[2] + "th"
    today = " ".join(today_split)
    num_rand = random.randint(0,5)
    name = list_name[num_rand]
    data = {'date':today,'name':name}

    if request.method == "POST":
        value = request.POST.copy()
        print(value)

    return render(request, 'home.html',data)