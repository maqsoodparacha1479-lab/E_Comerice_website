from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Order

def home(request):
    return render(request, 'home.html')

def web(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', 'Unknown Product')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        payment = request.POST.get('payment', 'Cash on Delivery')

        Order.objects.create(
            product_name=product_name,
            phone=phone,
            email=email,
            payment_method=payment
        )

        # Send email to admin
        send_mail(
            subject="New Order Received",
            message=f"Product: {product_name}\nEmail: {email}\nPhone: {phone}\nPayment: {payment}",
            from_email="your_email@gmail.com",
            recipient_list=["admin@gmail.com"],
            fail_silently=False,
        )

        return render(request, 'description.html', {'product_name': product_name})

    return render(request, 'web.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def audio(request):
    return render(request, 'audio.html')

def wearables(request):
    return render(request, 'wearables.html')

def drones(request):
    return render(request, 'drones.html')

def accessories(request):
    return render(request, 'accessories.html')

def watches(request):
    return render(request, 'watches.html')

def bags(request):
    return render(request, 'bags.html')

def eyewear(request):
    return render(request, 'eyewear.html')

def all_products(request):
    return render(request, 'all_products.html')

def head_p(request):
    return render(request, 'head_p.html')

def shop(request):
    return render(request, 'shop.html')

def card_page(request):
    return render(request, 'card_page.html')

def description(request):
    return render(request, 'description.html')

def product_detail(request, product_id):
    product = {
        "id": product_id,
        "name": "SkyVision Pro X1",
        "old_price": 899,
        "price": 764,
        "features": ["4K 60fps", "30min Flight", "3-axis Gimbal"]
    }

    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        payment = request.POST.get('payment')

        # Send email to admin
        send_mail(
            subject="New Order Received",
            message=f"Product: {product['name']}\nEmail: {email}\nPhone: {phone}\nPayment: {payment}",
            from_email="your_email@gmail.com",
            recipient_list=["admin@gmail.com"],
            fail_silently=False,
        )

        return render(request, 'thank_you.html', {'product': product})

    return render(request, 'product_detail.html', {'product': product})
