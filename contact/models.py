from django.db import models
from django.utils import timezone

# Create your models here.
#nossa "tabela" entre muitas aspas
class Contact(models.Model):
    #id (PK) criada automaticamente pelo Django
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) #NULLABLE
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) #NULLABLE
    created_date = models.DateTimeField(default=timezone.now) #Declara SYSDATE na entrada dos dados
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') 
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'