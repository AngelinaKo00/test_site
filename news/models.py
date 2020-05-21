from django.db import models

# Create your models here.
class Articles(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=120) #заголовок длиной в 120 символов
    post = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        #т.о. при вызове title будет вызваться не объект класса, а содержания заголовка
        return self.title
