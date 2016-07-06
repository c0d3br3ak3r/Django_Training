import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hours = [ "6:00 AM", "6:30 AM","7:00 AM", "7:30 AM","8:00 AM", "8:30 AM","9:00 AM", "9:30 AM","10:00 AM", "10:30 AM","11:00 AM", "11:30 AM","12:00 PM", "12:30 PM","1:00 PM", "1:30 PM","2:00 PM", "2:30 PM","3:00 PM", "3:30 PM","4:00 PM", "4:30 PM","5:00 PM", "5:30 PM","6:00 PM", "6:30 PM","7:00 PM", "7:30 PM","8:00 PM", "8:30 PM","9:00 PM", "9:30 PM","10:00 PM", "10:30 PM","11:00 PM", "11:30 PM","12:00 AM", "12:30 AM","1:00 AM", "1:30 AM","2:00 AM", "2:30 AM","3:00 AM", "3:30 AM","4:00 AM", "4:30 AM","5:00 AM", "5:30 AM"]
weekdays = ["", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def index(request):
    #weekdays = ["", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [i for i in range(7)]
    #hours = [i for i in range(12,48)]
    return render(request, "BookingPage.html", { 'days' : days, 'weekdays' : weekdays , 'hours' : hours})

def checkSlots(request):
    selectedBranch = request.POST['branch']
    selectedDate = request.POST['selectedDate']
    selected_date_obj = datetime.datetime.strptime(selectedDate, "%m/%d/%Y")
    for i in range(1,8):
        dt = selected_date_obj + datetime.timedelta(days=i-1)
        weekdays[i] = dt.strftime("%d %B %y, %a")
    print("The selected date is ::: ", selectedBranch , " --- ", selectedDate)
    return index(request)

def bookslots(request):
    slots = []
    for key in list(request.POST.keys()):
        slots.append(key)
    return HttpResponse("Your selected slots are " + str(slots))
