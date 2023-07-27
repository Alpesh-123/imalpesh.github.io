from django.db import models

class Contact(models.Model):
    sno = models.AutoField(auto_created = True,primary_key = True)
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    def __str__(self):
        return 'Message from' + self.name + ' - ' + self.email
    
    
        
    
