from django.db import models

# Create your models here.


class Course(models.Model):
    RELIGION_CHOICES = (
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
        ('Sikh', 'Sikh'),
        ('Parsi', 'Parsi'),
        ('Other', 'Other'),)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),)
    STATE_CHOICES = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttarakhand', 'Uttarakhand'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
        ('Daman and Diu', 'Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
    )
    COURSE_CHOICES = (
        ('KG', 'KG'),
        ('Class 1', 'Class 1'),
        ('Class 2', 'Class 2'),
        ('Class 3', 'Class 3'),
        ('Class 4', 'Class 4'),
        ('Class 5', 'Class 5'),
        ('Class 6', 'Class 6'),
        ('Class 7', 'Class 7'),
        ('Class 8', 'Class 8'),
        ('Class 9', 'Class 9'),
        ('Class 10', 'Class 10'),
        ('Class 11', 'Class 11'),
        ('Class 12', 'Class 12'),
        ('Diploma', 'Diploma'),
        ('Graduation', 'Graduation'),
        ('Post Graduation', 'Post Graduation'),
        ('PhD', 'PhD'),
        ('Post Doctoral', 'Post Doctoral'),
        ('ITI', 'ITI'),
        ('Others', 'Others'),
    )
    CATEGORY_CHOICES = (
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('GENERAL', 'GENERAL'),
        ('ST-PVGT', 'ST-PVGT'),
        ('APST', 'APST'),
    )
    PHYSICAL_CHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    date_of_birth = models.DateField()
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    religion = models.CharField(max_length=16, choices=RELIGION_CHOICES)
    annual_income = models.PositiveIntegerField()
    phone_regex = RegexValidator(
        regex=r'^\+?\d{8,15}$', message="Enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    current_course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_interested_in = models.CharField(max_length=50, choices=COURSE_CHOICES)
    physically_challenged = models.CharField(max_length=10, choices=PHYSICAL_CHOICE)

    def __str__(self):
        return self.name
