import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#hours = [ "6:00 AM", "6:30 AM","7:00 AM", "7:30 AM","8:00 AM", "8:30 AM","9:00 AM", "9:30 AM","10:00 AM", "10:30 AM","11:00 AM", "11:30 AM","12:00 PM", "12:30 PM","1:00 PM", "1:30 PM","2:00 PM", "2:30 PM","3:00 PM", "3:30 PM","4:00 PM", "4:30 PM","5:00 PM", "5:30 PM","6:00 PM", "6:30 PM","7:00 PM", "7:30 PM","8:00 PM", "8:30 PM","9:00 PM", "9:30 PM","10:00 PM", "10:30 PM","11:00 PM", "11:30 PM","12:00 AM", "12:30 AM","1:00 AM", "1:30 AM","2:00 AM", "2:30 AM","3:00 AM", "3:30 AM","4:00 AM", "4:30 AM","5:00 AM", "5:30 AM"]
hours = ["0600","0630","0700","0730","0800","0830","0900","0930","1000","1030","1100","1130","1200","1230","1300","1030","1400","1430","1500","1530","1600","1630","1700","1730","1800","1830","1900","1930","2000","2030","2100","2130","2200","2230","2300","2330","2400","2430","0000","0030","0100","0130","0200","0230","0300","0330","0400","0430","0500","0530"]
weekdays = ["", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days = [1,2,3,4,5,6,7]
resSlots = []
def index(request):
    global days
    #weekdays = ["", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [i for i in range(7)]
    #hours = [i for i in range(12,48)]
    return render(request, "BookingPage.html", { 'days' : days, 'weekdays' : weekdays , 'hours' : hours})

def renderSlots(request):
    selectedBranch = request.POST['branch']
    selectedDate = request.POST['selectedDate']
    selected_date_obj = datetime.datetime.strptime(selectedDate, "%m/%d/%Y")
    for i in range(1,8):
        dt = selected_date_obj + datetime.timedelta(days=i-1)
        weekdays[i] = dt.strftime("%d %B %y - %a")
        days[i-1] = dt.strftime("%d%m%y")
    #print("The selected date is ::: ", selectedBranch , " --- ", selectedDate)
    resSlots = reservedSlots() #cALLING FUNCTION TO check the reserved slots from db
    return render(request, "BookingPage.html", { 'days' : days, 'weekdays' : weekdays , 'hours' : hours, 'resSlots' : resSlots})

def reservedSlots():
    slots = ['0900040716', '0700050716'] #TODO - Write DB query here to get the reserved slots between dates
    return slots

def bookslots(request):
    slots = []
    for key in list(request.POST.keys()):
        if key[:4]=='slot':
            dt = key[9:]
            dt_date = datetime.datetime.strptime(dt, "%d%m%y")
            test = str(dt_date.strftime("%d %B %y - %a"))
            test += " " + key[4:8]
            slots.append(test)

    if not slots :
        return HttpResponse(json.dumps({'errors':"Oops. You haven't selected any slots !!"}), content_type="application/json")
        #return render(request, "BookingPage.html", { 'days' : days, 'weekdays' : weekdays , 'hours' : hours, 'resSlots' : resSlots, 'errors' : 'Select slots!!'})
    else:
        print("IN THE ELSE CONDITION >>>>>>> ")
        return render(request, 'BookingConfirm.html', { 'slots' : slots })
        #Note that this refreshes the page. You need to do ajax to not refresh the page and show error.


def confirmBooking(request):
    booked_slots = ""
    booking_details = {}
    booking_details['BookingId'] = "D3L4FS"
    booking_details['Name'] = request.POST['name']
    booking_details['Phno'] = request.POST['mobile']
    for key in list(request.POST.keys()):
        if key[:4]!='csrf' and key[:4]=='slot':
            booked_slots += str(request.POST[key]) + " , "
    booking_details['slots'] = booked_slots
    return render(request,'Confirmation.html',{'booking_details':booking_details})
