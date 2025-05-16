from django.shortcuts import render, redirect
from .models import User

def success(request):
    return render(request, 'success.html')

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        blood_group = request.POST.get("blood_group")
        phone_number = request.POST.get("phone_number")
        location = request.POST.get("location")

        # Simple validation
        if not all([name, email, blood_group, phone_number]):
            error = "Please fill all required fields."
            return render(request, "register.html", {"error": error})

        # Create user record
        User.objects.create(
            name=name,
            email=email,
            blood_group=blood_group,
            phone_number=phone_number,
            location=location,
        )
        return redirect("success")  # replace with your success URL

    # GET request
    return render(request, "register.html")
