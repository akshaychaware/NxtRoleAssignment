
from django.urls import path,include
from Attendance_app import views as v
from Attendance_app import DRF_views as d
urlpatterns = [
    path('',v.index,name="index"),
    path('addstudent/',v.add_student,name="addstudent"),
    path('studentlist/',v.student_list,name="studentlist"),
    path('updatestudent/<int:id>/',v.updatestudent,name="updatestudent"),
    path('deletestudent/<int:id>/',v.deletestudent,name="deletestudent"),


    path('api/GetAllStudent/',d.GetAllStudent_Drf),
    path('api/GetStudentById/<int:id>/',d.GetStudentById_Drf),
    path('api/createstudent',d.CreateStudent_Drf),
    path('api/updatestudent/<int:id>/',d.UpdateStudent_Drf),
    path('api/deletestudent/<int:id>/',d.DeleteStudent_Drf),
]
