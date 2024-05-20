from django.urls import path
from . import views

app_name = 'app1'

urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup, name='signup'),
    path('doctor/',views.doctor, name='doctor'),
    path('patient/',views.patient, name='patient'),
    path('donor/',views.donor, name='donor'),
    path('usershow/',views.user_show,name='usershow'),
    path('askquestion/',views.questions,name='askquestion'),
    #path('answer/',views.answer,name='answer'),
    path('hospital/',views.hospitalReg,name="hospital"),
    path('addService/',views.addService,name="addService"),
    path('bookService/',views.bookService,name="bookService"),
    #path('editService/',views.add,name="editService")
    path('viewques/',views.viewQues,name="viewques"),
    path('donorview/',views.donorview,name="donorview"),
    path("done/",views.done,name="done"),
    path("sorry/",views.sorry,name="sorry"),
    path("logout/",views.logout_view,name="logout"),
    path("booking/<int:id>/",views.booking,name="booking"),
   # path("search_results/",views.search_results,name="search_results")

]