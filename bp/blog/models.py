from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 


    likes = models.ManyToManyField(User,through='Like',through_fields=('blog','user'),related_name='likes') #다대다 관계 설정를 위한 중계모델

    def like_count(self): #self는 블로그 객체
        return self.likes.count()
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('data published')
    c_writer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)



class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)