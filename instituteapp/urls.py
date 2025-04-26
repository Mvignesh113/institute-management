"""
URL configuration for institute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from instituteapp import views
from django.urls import path

urlpatterns = [
    path('', views.login_page, name=''),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/',views.dashboards,name="dashboard"),
    path('student_d1/',views.student_details1,name='student_d1'),
    path('student_d2/',views.student_details2,name='student_d2'),
    path('student_d3/<int:id>',views.student_details3,name='student_d3'),
    # path('fees_p/',views.fees_payment1,name='fees_p'),
    path('collect_fees/<int:id>/',views.collect_fees1,name="collect_fees"),
    path('fees_r/',views.fees_report1,name='fees_r'),
    path('setting/',views.settings1,name='setting'),
    path('total_std/',views.totalstd,name='total_std'),
    path('paid_std/',views.paidstd,name='paid_std'),
    path('pending_std/,',views.pendingstd,name='pending_std'),
    path('fees_s/',views.feesstrcture,name='fees_s'),
    path('fees1_s/',views.feesstrcture1,name='fees1_s'),
    path('fees2_s/<int:id>',views.feesstrctureedit,name='fees2_s'),
    path('sdelet/<int:id>',views.stddelet,name='sdelet'),
    path('coursed/<int:id>',views.coursedelet,name='coursed'),
    path('stud/',views.stud,name="stud"),
    path('stud1/',views.stud1,name="stud1"),
    path('stud2/<int:pk>',views.stud2,name="stud2"),
    path('stud3/<int:pk>',views.studdelete,name='stud3')
]