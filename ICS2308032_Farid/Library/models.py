from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=4,primary_key = True)
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=40)
    published_year = models.IntegerField(max_length=4, default='2003')

class Student(models.Model):
    student_id = models.CharField(max_length=4,primary_key = True)
    student_name = models.TextField(max_length = 50)
    student_phone = models.CharField(max_length = 10)
    student_email = models.TextField(max_length = 40)
    stud_status = models.TextField(max_length = 10, default='Active')

class Borrowing(models.Model):
    borrow_id = models.CharField(max_length = 4, primary_key = True)
    book_id = models.ForeignKey(Book, on_delete = models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    borrow_date = models.DateField(max_length=10)
    return_date = models.DateField(max_length = 10)

class Mentor(models.Model):
    menid=models.CharField(max_length=8, primary_key=True)
    menname=models.TextField(max_length=225)
    menroomno=models.CharField(max_length=3, default='sk2')

class Course(models.Model):
    code=models.CharField(max_length=10, primary_key=True)
    description=models.TextField(max_length=50)