from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100) # Todo의 제목
    description = models.TextField(blank=True) # Todo에 대한 설명
    created = models.DateTimeField(auto_now_add=True) # Todo 생성 일자
    complete = models.BooleanField(default=False) # Todo 완료 여부
    important = models.BooleanField(default=False) # Todo 중요 여부

    def __str__(self):
        return self.title