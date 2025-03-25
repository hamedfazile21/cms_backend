from django.db import models

# Create your models here.
class CreateCustomer(models.Model):
    DEFAULT_ECONOMIC_CHOSES = "N"
    ECONOMIC_CHOSES = [
        ("G" , "Good"),
        (DEFAULT_ECONOMIC_CHOSES , "Normal"),
        ("B" , "Bad"),
    ]
    user_name = models.CharField(max_length=255 )
    last_name = models.CharField(max_length=2555 )
    age = models.IntegerField(null= True)
    job = models.CharField(max_length=255 , null=True)
    education_degree = models.CharField(max_length=255 , null=True)
    economic_status = models.CharField(max_length=2 , choices=ECONOMIC_CHOSES , default=DEFAULT_ECONOMIC_CHOSES )
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255 , null=True)
    work_address = models.CharField(max_length=255 , null=True)
    
    
    def __str__(self):
        return self.user_name


class CustomerStatus(models.Model):
    EXCELLENT_HEALTH = "EH"
    GOOD_HEALTH = "GH"
    NORMAL_HEALTH  = 'NH'
    BAD_HEALTH = 'BH'
    HEALTH_NOW_CHOICES = [
        (EXCELLENT_HEALTH , "Excellent"),
        (GOOD_HEALTH , "Good"),
        (NORMAL_HEALTH , "Normal"),
        (BAD_HEALTH , "Bad"),
    
    ]
    TRUE = "YE"
    FALSE = 'NO'
    TRUE_FALSE_CHOICES = [
        (TRUE , 'Yes'),
        (FALSE , 'No'),
    ]
    related_to = models.OneToOneField(CreateCustomer , on_delete=models.CASCADE , primary_key=True)
    health_now = models.CharField(max_length=2 , choices=HEALTH_NOW_CHOICES , default=GOOD_HEALTH)
    last_examination = models.DateTimeField(null=True)
    is_under_care_now = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    have_surgery = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    have_blood_pressure = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    have_sugar = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    bee_hospitalization = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    have_allergy = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    used_milicent = models.CharField(max_length=255 , null=True)
    description = models.TextField()
    
    
class CustomerDiseases(models.Model):
    TRUE = "YE"
    FALSE = 'NO'
    TRUE_FALSE_CHOICES = [
        (TRUE , 'Yes'),
        (FALSE , 'No'),
    ]
    related_to = models.OneToOneField(CreateCustomer , on_delete=models.CASCADE , primary_key=True) # //سکته قلبی
    heart_attack = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE) # پیس میکر
    pacemaker = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE) # سکته مغزی
    stroke = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE) # ناراحتی عصبی
    nervous_disorder = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    asthma = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE) 
    epilepsy = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    kidney_disorder = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    liver_disorder = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    addiction = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    tuberculosis = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    stomach_ulcer = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    allergy = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    aids = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    hepatitis = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    insomnia = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    cancer = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    radiotherapy = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)
    women_pregnancy = models.CharField(max_length=2 , choices=TRUE_FALSE_CHOICES , default=FALSE)