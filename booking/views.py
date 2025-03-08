from django.shortcuts import render,redirect
from .forms import BookingForm
from .models import Booking
def home(request):
    return render(request, 'booking/homepage.html')

def about(request):
    return render(request,'booking/about.html')

#view for  the new form page
def book_demo(request):
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')

        print("Form Data:", name, email, phone, date)

        # You can save this data to the database here or process it as needed
        booking=Booking(name=name,email=email,phone=phone,demo_date=date)
        booking.save()


        # Redirect to the thank-you page after submission
        return redirect('thank_you')

    return render(request,'booking/new-form.html')

def thank_you(request):
    return render(request,'booking/thank_you.html')


# Create your views here.
