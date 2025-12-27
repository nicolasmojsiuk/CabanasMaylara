from django.shortcuts import render

def home(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def rooms(request):
    return render(request, 'web/rooms.html')

def room_details(request):
    return render(request, 'web/room-details.html')

def amenities(request):
    return render(request, 'web/amenities.html')

def location(request):
    return render(request, 'web/location.html')

def restaurant(request):
    return render(request, 'web/restaurant.html')

def offers(request):
    return render(request, 'web/offers.html')

def events(request):
    return render(request, 'web/events.html')

def gallery(request):
    return render(request, 'web/gallery.html')

def booking(request):
    return render(request, 'web/booking.html')

def contact(request):
    return render(request, 'web/contact.html')

def terms(request):
    return render(request, 'web/terms.html')

def privacy(request):
    return render(request, 'web/privacy.html')