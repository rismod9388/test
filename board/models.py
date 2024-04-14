from django.db import models

# Create your models here.
class NoticeBoardPost(models.Model):#Board
   
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    id = models.AutoField(primary_key=True)


class Comment(models.Model):
    commentId = models.ForeignKey(NoticeBoardPost, on_delete=models.CASCADE)
    text = models.TextField()
