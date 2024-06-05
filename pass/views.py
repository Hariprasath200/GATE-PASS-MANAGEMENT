from django.shortcuts import render,redirect
from .forms import HodStatusForm, StdForm
from .models import *
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Std

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as auth_login, logout as auth_logout


#from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'pass/home.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StdForm
from django.contrib.auth.decorators import login_required

from .models import Std  # Import the Std model

@login_required
def student(request):
    # Check if the logged-in user has the role 'student'
    if hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'student':
        students = Std.objects.all()
        if request.method == 'POST':
            form = StdForm(request.POST)
            if form.is_valid():
                student = form.save()

                # Generate QR code for the submitted student data
                
                form=student
                messages.success(request, 'Form submitted successfully!')
                return render(request, 'pass/student.html', {'form': form, 'students': students})
            else:
                # If the form is not valid, show form errors as alert messages
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Error in {field}: {error}')
        else:
            form = StdForm()
        return render(request, 'pass/student.html', {'form': form, 'students': students})
    else:
        # If the user is authenticated but does not have the role 'student', return a forbidden response
        return render(request, 'pass/forbidden.html')



@login_required
def incharge(request):
    # Check if the logged-in user has the role 'incharge'
    if request.user.userprofile.role == 'incharge':
        students = Std.objects.all()
        return render(request, 'pass/incharge.html', {'students': students})
    else:
        # If the user has a different role, return a forbidden response
        return render(request, 'pass/forbidden.html')

@login_required
def hod(request):
    # Check if the logged-in user has the role 'hod'
    if request.user.userprofile.role == 'hod':
        students = Std.objects.all()
        hod_status_form = HodStatusForm()  # Create a form instance for updating HOD status
        return render(request, 'pass/hod.html', {'students': students, 'hod_status_form': hod_status_form})
    else:
        # If the user has a different role, return a forbidden response
        return render(request, 'pass/forbidden.html')

@login_required
def warden(request):
    # Check if the logged-in user has the role 'warden'
    if request.user.userprofile.role == 'warden':
        students = Std.objects.all()
        return render(request, 'pass/warden.html', {'students': students})
    else:
        # If the user has a different role, return a forbidden response
        return render(request, 'pass/forbidden.html')

@login_required
def security(request):
    # Check if the logged-in user has the role 'security'
    if request.user.userprofile.role == 'security':
        return render(request, 'pass/security.html')
    else:
        # If the user has a different role, return a forbidden response
        return render(request, 'pass/forbidden.html')


def security(request):
    return render(request, 'pass/security.html')

def success(request):
    return render(request,'pass/success.html')





from django.contrib import messages

def update_hod_status(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Std.objects.get(id=student_id)
        form = HodStatusForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('hod')  # Redirect to some success URL after updating the HOD status
    # If the request method is not POST or form is invalid, redirect to some error URL
    return redirect('hod')

from django.shortcuts import render, redirect
from .forms import QRCodeForm
import qrcode
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import QRCodeForm
import qrcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # Get form data
            data = form.cleaned_data

            # Create a QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            # Add form data to the QR code
            qr_data = ""
            for field_name, value in data.items():
                qr_data += f"{field_name}: {value}\n"

            qr.add_data(qr_data)
            qr.make(fit=True)
            # Create an image from the QR code instance
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image to the specified path
            qr_image_path = "static/images/qrc.png"  # Specify the desired path
            img.save(qr_image_path, "PNG")

            # Redirect to the student page with the QR code image path
            return redirect(reverse('student') + f'?qr_image={qr_image_path}')
    else:
        form = QRCodeForm()

    return render(request, 'pass/qr.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'pass/register.html', {'form': form})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect user based on their role
                if role == 'student':
                    return redirect('student')  # Redirect to student page
                elif role == 'incharge':
                    return redirect('incharge')  # Redirect to incharge page
                elif role == 'hod':
                    return redirect('hod')  # Redirect to hod page
                elif role == 'warden':
                    return redirect('warden')  # Redirect to warden page
                elif role == 'security':
                    return redirect('security')  # Redirect to security page
                else:
                    # Handle other roles or unknown roles
                    pass
    else:
        form = LoginForm()
    return render(request, 'pass/login.html', {'form': form})
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to home page after logout
def update_status(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        status = request.POST.get('status')
        
        try:
            student = Std.objects.get(pk=student_id)
            student.incharge_status = status
            student.save()
            messages.success(request, 'Incharge status updated successfully!')
        except Std.DoesNotExist:
            messages.error(request, 'Student does not exist!')
    
    return redirect('incharge')



# views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def my_view(request):
    if not request.session.get('visited_my_page', False):
        # Set the session variable to indicate that the user has visited the page
        request.session['visited_my_page'] = True
    return render(request, 'pass/my_template.html')


from django.shortcuts import render
import cv2
from pyzbar.pyzbar import decode

def scan_qr_code(request):
    if request.method == 'POST':
        # Access the webcam
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()

            # Find and decode QR codes in the frame
            decoded_objects = decode(frame)

            # Check if QR code is detected
            if decoded_objects:
                for obj in decoded_objects:
                    qr_data = obj.data.decode('utf-8')
                    # Process QR data here, maybe save it to database or perform some action
                    return render(request, 'pass/result.html', {'qr_data': qr_data})

            # Display the frame
            cv2.imshow('QR Code Scanner', frame)

            # Check for key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    return render(request, 'pass/scan.html')
