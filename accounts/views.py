from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializer import StudentSerializer, TeacherSerializer
#
#
# @api_view(['POST'])
# def signup_student(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": 'Successful'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['POST'])
# def signup_teacher(request):
#     serialized = TeacherSerializer(data=request.data)
#     if serialized.is_valid():
#         return Response({"message": 'Successful'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

