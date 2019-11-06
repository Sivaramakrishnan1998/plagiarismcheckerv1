import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
randomid = uuid.uuid4()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (randomid, ext)
    return os.path.join('documents/', filename)

class Profile(models.Model):
    # created_by=models.ForeignKey(User, related_name='created_by_user')
    created_by=models.ForeignKey(User, on_delete='created_by_user')


class Subuser(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING,related_name = 'user')
    created_by = models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING,related_name='created_by_user')

class Data(models.Model):
    data = models.TextField()
    user = models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING,)
    def __str__(self):
        return self.data

	# keywords = models.CharField(max_length=500)
#
class Apidocument(models.Model):
    iden = models.CharField(max_length=255)
    document = models.FileField(upload_to='media/documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Institution(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    flag = models.IntegerField(blank = True,default = 1)
    name = models.CharField(max_length = 30,blank = True,default='')
    mobile_no = models.IntegerField(blank=  True,default = 0)
    designation = models.CharField(max_length = 30,blank = True, default = '')
    contact_person = models.CharField(max_length = 30,blank  = True,default = '')
    institution_name = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    pincode = models.CharField(max_length=255, blank=True, default='')
    def __str__(self):
        return self.user
    

class Credits(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.DecimalField(max_digits=8, decimal_places=0,default="1000")



@receiver(post_save, sender=User)
def create_user_credits(sender, instance, created, **kwargs):
    if created:
        Credits.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_credits(sender, instance, **kwargs):
    instance.credits.save()


@receiver(post_save, sender=User)
def create_user_institution(sender, instance, created, **kwargs):
    if created:
        Institution.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_institution(sender, instance, **kwargs):
    instance.institution.save()

class Document(models.Model):

    user = models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING,)
    result = models.DecimalField(max_digits=50,decimal_places=5,null=True)
    credits = models.DecimalField(max_digits=8, decimal_places=0,default="1000")
    description = models.CharField(max_length=255, blank=True, default='')
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document
