from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_desc=models.TextField()
    dep_img = models.ImageField(upload_to='departments')


    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=250)
    doc_spec=models.CharField(max_length=250)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    Patient_Name=models.CharField(max_length=255)
    Patient_Contact=models.CharField(max_length=255)
    Patient_Email=models.EmailField()
    Doctor_Name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_Date=models.DateField()
    Booked_On=models.DateField(auto_now=True)

class Career(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    job_title=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    location=models.CharField(max_length=200)

class Job(models.Model):
    job_post=models.CharField(max_length=250)
    qualification=models.CharField(max_length=300)
    experience=models.CharField(max_length=250)
    job_img=models.ImageField(upload_to='job')

    def __str__(self):
        return self.job_post

class contact(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.EmailField()
    Contact=models.CharField(max_length=250)
    Message=models.CharField(max_length=500)

# class Signup(models.Model):
#     name=models.CharField(max_length=250)
#     email=models.EmailField()
#     pswrd=models.CharField(max_length=250)
#     cnfrmpswrd=models.CharField(max_length=250)