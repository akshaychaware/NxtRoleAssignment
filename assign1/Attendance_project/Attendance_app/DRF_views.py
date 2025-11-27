from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer



@api_view(['GET'])
def GetAllStudent_Drf(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def GetStudentById_Drf(request,id):
    students=Student.objects.get(id=id)
    serializer=StudentSerializer(students)
    return Response(serializer.data)



@api_view(['POST'])
def CreateStudent_Drf(request):
    Student.objects.create(
        name=request.data.get('name'),
        roll_no=request.data.get('roll_no'),
        student_class=request.data.get('student_class'),
        email=request.data.get('email')
    )
    serializer=StudentSerializer()
    return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['PUT'])
def UpdateStudent_Drf(request,id):
    try:
        students = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'})
    serializer=StudentSerializer(students,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"record updated successfully"})
    return Response(serializer.errors)



@api_view(['DELETE'])
def DeleteStudent_Drf(request,id):
    try:
        students=Student.objects.get(id=id)
    except Exception as e:
        return Response({"message":"student record does not exist"})
    students.delete()
    return Response({"message":"student deleted successfully"})