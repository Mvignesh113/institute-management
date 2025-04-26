from django.shortcuts import redirect, render
from django.template import loader
from django.contrib import messages
from django.db.models import Count
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from .models import*
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import*
# Create your views here.
 
def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            name = request.POST.get('username')     
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("/dashboard/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("")
    
    return render(request, "login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect("")
def dashboards(request):
    total_s=students_details.objects.aggregate(Count('id'))
    paidfeessum=students_details.objects.aggregate(Sum('paidfees'))['paidfees__sum']
    pendingfeessum=students_details.objects.aggregate(Sum('pendingfees'))['pendingfees__sum']
    print(pendingfeessum)
    print(paidfeessum)
    return render(request,'index.html',{'total_s':total_s,'paidfees':paidfeessum,'pending':pendingfeessum},)

def student_details1(request):
    std=students_details.objects.all()
    return render(request,'student_details1.html',{"std":std})

def student_details2(request):
    std=students_details.objects.all()
    if request.method=="POST":
       idnums=request.POST["idnum"]
       names=request.POST['Name']
       genders=request.POST['Gender']
       courses=request.POST['course']
       durations=request.POST['duration']
       phnums=request.POST['phnum']
       places=request.POST['place']
       std=students_details.objects.create(idnum=idnums,Name=names,Gender=genders,course=courses,duration=durations,phnum=phnums,place=places)
       std.save()
       return redirect('/student_d1/')
    return render(request,'student_details2.html',{"std":std})
def stddelet(request,id):
    a=students_details.objects.get(id=id)
    a.delete()
    return redirect('/student_d1/')
 
def student_details3(request,id):
    a=students_details.objects.get(id=id)
    if request.method=="POST":
       idnums=request.POST["idnum"]
       names=request.POST['Name']
       genders=request.POST['Gender']
       courses=request.POST['course']
       durations=request.POST['duration']
       phnums=request.POST['phnum']
       places=request.POST['place']
       a.idnum=idnums
       a.Name=names
       a.Gender=genders
       a.course=courses
       a.duration=durations
       a.phnum=phnums
       a.place=places
       a.save()
       return redirect("/student_d1/")
    return render(request,'student_details3.html',{"a":a})
 

def collect_fees1(request, id):
    # Fetch the student details for the given ID
    try:
        std = students_details.objects.get(id=id)
    except students_details.DoesNotExist:
        return render(request, 'error.html', {"message": "Student not found."})
    
    # Ensure paidfees and total_fees are initialized properly if None
    if std.paidfees is None:
        std.paidfees = 0.0
    if std.total_fees is None:
        std.total_fees = 0.0
    
    # Calculate the initial pending fees
    std.pendingfees = std.total_fees - std.paidfees
    print(f"DEBUG: Initial - total_fees={std.total_fees}, paidfees={std.paidfees}, pending_fees={std.pendingfees}")
    
    if request.method == "POST":
        # Get the total fees and paid fees from the form submission
        totalfees_input = request.POST.get('totalfees')
        paidfees_input = request.POST.get('paidfees')
        
        try:
            # Update total_fees if a valid value is provided
            if totalfees_input:
                totalfees_input = float(totalfees_input)
                std.total_fees = totalfees_input
            
            # Update paid_fees if a valid value is provided
            if paidfees_input:
                paidfees_input = float(paidfees_input)
                # Add the new paid fees to the existing amount
                std.paidfees += paidfees_input

            # Recalculate pending fees
            std.pendingfees = std.total_fees - std.paidfees
            print(f"DEBUG: After save - total_fees={std.total_fees}, paidfees={std.paidfees}, pending_fees={std.pendingfees}")

            # Save the updated details (both total fees and paid fees)
            std.save()

            # Redirect after successfully saving the data
            return redirect("/student_d1/")  # Adjust URL as needed
        
        except ValueError:
            # Handle the case where inputs are not valid numbers
            return render(request, 'collectfees.html', {
                "std": std,
                "pending_fees": std.pendingfees,
                "error": "Invalid input. Please enter valid numbers for total fees and paid fees."
            })
    
    # Render the 'collectfees.html' template with the student details and pending fees
    return render(request, 'collectfees.html', {
        "std": std,
        "pending_fees": std.pendingfees
    })




def fees_report1(request):
    std=students_details.objects.all()
    return render(request,'feesreport.html',{"std":std})

def settings1(request):
    return render(request,'settings.html')

def totalstd(request):
    std=students_details.objects.all()
    return render(request,'totalstudents.html',{"std":std})

def paidstd(request):
    std=students_details.objects.all()
    return render(request,'paid_student.html',{"std":std})

def pendingstd(request):
    std=students_details.objects.all()
    return render(request,'pending_students.html',{"std":std})

def feesstrcture(request):
    std=course.objects.all()
    return render(request,'fees_strcture.html',{"std":std})

def feesstrcture1(request):
  std=course.objects.all()
  if request.method=="POST":
         courses=request.POST["coursename"]
         feess=request.POST["coursefees"]
         std=course.objects.create(coursename=courses,coursefees=feess)
         std.save()
         return redirect('/fees_s/')
  return render(request,'fees_strctre1.html',{"std":std})  
#   return render(request,'fees_strctre1.html')

def feesstrctureedit(request,id):
  a=course.objects.get(id=id)
  if request.method=="POST":
         courses=request.POST["coursename"]
         feess=request.POST["coursefees"]
         a.coursename=courses
         a.coursefees=feess
         a.save()
         return redirect('/fees_s/')
  return render(request,'fees_strcture2.html',{"a":a})
#   return render(request,'fees_strcture2.html')

def coursedelet(request,id):
    a=course.objects.get(id=id)
    a.delete()
    return redirect('/fees_s/')

@api_view(['GET'])
def stud(request):
    datas=students_details.objects.all()
    serializer=studentsdetailsserializer(datas,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def stud1(request):
     serializer=studentsdetailsserializer(data= request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
     else:
         return Response({"data":"The data is required"})  
     
@api_view(['PUT'])
def stud2(request,pk):
    data=students_details.objects.get(id=pk)
    serializer=studentsdetailsserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter an data"})   
    
@api_view(['DELETE'])
def studdelete(request,pk):
    data=students_details.objects.get(id=pk)
    serializer=studentsdetailsserializer(data,many=False)
    data.delete()
    return Response(serializer.data)