from django.db import models

# Create your models here.
# User details table
class UserBooking(models.Model):
    BookingId = models.CharField(max_length=1000, primary_key=True)
    Name = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    EmailAddress = models.EmailField(max_length=250)
    def __str__(self):
        return self.Name + " " + self.PhoneNumber + " " + self.BookingId

class BookingSlots(models.Model):
    BookingId = models.ForeignKey(UserBooking, on_delete=models.CASCADE)
    SlotDate = models.DateField()
    SlotTime = models.CharField(max_length=10)
    def __str__(self):
        return self.BookingId.BookingId + " " + str(self.SlotDate) + " " + self.SlotTime


#Name, PhNo(Primary key) , EmailAddress(optional), BookingId(ForeignKey)
# Foreign Key to id
#id(primary key),BookingId(), Date, Slot
# Slots Table # Can use the query by date between filter to find slots by week.
