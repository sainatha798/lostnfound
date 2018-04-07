from django.db import models
from lostnfound.settings import DATE_INPUT_FORMATS
from django.core.exceptions import ValidationError
# Create your models here.


def validate(phone):
    if len(phone)!=10:
        raise ValidationError(_("mobile no should have only 10 digits"))


class LostAndFound(models.Model):
    date = models.DateField(null=True,blank=True,)
    subject = models.CharField(null=False,blank=True,max_length=200)
    description = models.TextField(null=True,blank=True)
    contact_id = models.CharField(null=True,blank=True,validators=[validate],max_length=13)
    location = models.CharField(null=True,blank=True,max_length=50)
    lost_or_found = models.CharField(null=False,blank=False,choices=(('Lost','Lost'),('Found','Found')),default='Lost',max_length=10)
    image = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.subject+'--'+self.contact_id
