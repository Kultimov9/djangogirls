from django.db import models
from django.utils import timezone


class Post(models.Model):# для определения объектов ОТПРАВИТЬ
    author = models.ForeignKey('auth.User') #АВТОР
    title = models.CharField(max_length=200) #Заголовок = модель.СимволПоле(максимальная длина = 200)
    text = models.TextField() #Текст ПОле
    created_date = models.DateTimeField(
            default=timezone.now) #дата создания = модель.ДатаВремяПоле(по умолчанию = Время.сейчас
    published_date = models.DateTimeField(
            blank=True, null=True) #дата публикации = Может быть пустым

    def publish(self): #Функция публиш
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title