from django.shortcuts import render
from datetime import date,datetime
import calendar
import random
from main.models import UserEmoji

from datetime import date

def home(request):
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

def index(request):
    res = {
        "Angry" : 0,
        "Sad" : 0,
        "Neutral" : 0,
        "Happy" : 0,
        "Ecstatic" : 0,
        "TotalUser" : 0,
        "Percentage" : "",
        "Time" : "",
        "Location" : ""
    }

    # Get time
    today = date.today().strftime("Today, %B %d %Y")
    today_split = today.split(" ")
    if today_split[2][-1] == "1":
        today_split[2] = today_split[2] + "st"
    elif today_split[2][-1] == "2":
        today_split[2] = today_split[2] + "nd"
    elif today_split[2][-1] == "3":
        today_split[2] = today_split[2] + "rd"
    else:
        today_split[2] = today_split[2] + "th"
    res["Time"] = " ".join(today_split)

    res["Location"] = "Blue Care Tangara Retirement Village"

    user_emoji = UserEmoji.objects.all()
    for user in user_emoji:
        res["TotalUser"] += 1
        user_emoji_key = user.emoji
        if user_emoji_key.name == "Angry":
            res["Angry"] += 1
        if user_emoji_key.name == "Sad":
            res["Sad"] += 1
        if user_emoji_key.name == "Neutral":
            res["Neutral"] += 1
        if user_emoji_key.name == "Happy":
            res["Happy"] += 1
        if user_emoji_key.name == "Ecstatic":
            res["Ecstatic"] += 1

    res["Percentage"] = str(int(res["Happy"] / res["TotalUser"] * 100))

    return render(request, 'desktop2.html', res)
