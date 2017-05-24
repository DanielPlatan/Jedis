from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Название планеты')

    def __str__(self):
        return  self.name

class Candidate(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Имя')
    planet = models.ForeignKey('Planet', null=True, verbose_name=u'Планета')
    age = models.IntegerField(verbose_name=u'Возраст')
    email = models.EmailField(max_length=64, verbose_name=u'Почта')
    master = models.ForeignKey('Jedi', null=True)

    def __str__(self):
        return self.name

class Jedi(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Имя')
    planet = models.ForeignKey('Planet', null=True, verbose_name=u'Планета проживания')

    def __str__(self):
        return self.name

class Questions(models.Model):
    text = models.CharField(max_length=640, default= '', verbose_name=u'Текст вопроса')
    def __str__(self):
        return self.text

class Results(models.Model):
    candidate = models.ForeignKey('Candidate', null=True, verbose_name=u'Исполнитель задания')
    question = models.CharField(max_length=64, null=False, default='', verbose_name=u'Вопрос')
    result = models.CharField(max_length=64, default='', verbose_name=u'Ответ')

class Auth(models.Model):
    jedi = models.ForeignKey('Jedi', null=False, verbose_name=u'Джедай')



