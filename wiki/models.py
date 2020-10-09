from django.db import models


# Create your models here.
class Note(models.Model):
    note_name = models.CharField(verbose_name='笔记标题', max_length=100, unique=True, null=False)
    context = models.TextField(verbose_name='笔记内容', default='')
    add_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_name
