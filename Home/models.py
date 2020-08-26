from django.db import models
# Create your models here.
class Location(models.Model):
    area = models.CharField(max_length=64)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.area} ({self.pincode})"

class Teacher(models.Model):
    CLASS_CHOICES = (('1-5', 'First to Fifth'),
                    ('6-8', 'Sixth to Eigth'),
                    ('9-10', 'Ninth to Tenth'),
                    ('11-12', 'Eleventh to Twelfth'),
                    ('9-12', 'Ninth to Twelfth')
    )

    TUTOR_CHOICES = ( 
                    ('Home Tutor', 'HT'),
                    ('Tution Center Teacher', 'TT')
                    )

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    experience = models.DecimalField(max_digits=4, decimal_places=2)
    classes = models.CharField(max_length=6, choices=CLASS_CHOICES)
    phone = models.CharField(max_length=10)
    photo = models.ImageField(blank=True, null=True, upload_to='teachers/%Y/%m/%D/')
    teacher_type = models.CharField(max_length=30 ,choices=TUTOR_CHOICES, blank=True)
    address = models.CharField(max_length=100, blank=True)
    subject1 = models.CharField(max_length = 64, blank=True)
    subject2 = models.CharField(max_length = 64, blank=True)
    subject3 = models.CharField(max_length = 64, blank=True)

    def __str__(self):
        return f"{self.name} | Experience - {self.experience} | Location - {self.location} | Classes - {self.classes} "