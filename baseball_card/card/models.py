from django.db import models


class Profile(models.Model):
    name = models.CharField('Имя', max_length=200)
    created_date = models.DateTimeField('Created')
    birth_date = models.DateField('Birth date', null=True, blank=True)
    photo = models.CharField(max_length=500, null=True, blank=True)
    sociotype = models.CharField(max_length=300, null=True, blank=True)

    thinking = models.IntegerField('Рационал/Иррационал', null=True, blank=True)
    sensing = models.IntegerField('Сенсорик/Интуит', null=True, blank=True)
    extraversion = models.IntegerField('Экстраверт/Интроверт', null=True, blank=True)
    judging = models.IntegerField("Логик/Этик", null=True, blank=True)
    determination = models.IntegerField("Решительность/Рассудительность", null=True, blank=True)
    subjectivism = models.IntegerField("Субъективизм/Объективизм", null=True, blank=True)
    stubbornness = models.IntegerField("Упрямство/Уступчивость", null=True, blank=True)
    carelessness = models.IntegerField("Беспечность/Предусмотрительность", null=True, blank=True)
    result = models.IntegerField("Результат/Процесс", null=True, blank=True)
    constructivism = models.IntegerField("Конструктивизм/Эмотивизм", null=True, blank=True)
    questimity = models.IntegerField("Квестимность/Деклатимность", null=True, blank=True)
    tactics = models.IntegerField("Тактика/Стратегия", null=True, blank=True)
    dynamics = models.IntegerField("Динамика/Статика", null=True, blank=True)
    positive = models.IntegerField("Позитивизм/Негативизм", null=True, blank=True)
    aristocracy = models.IntegerField("Аристократия/Демократия", null=True, blank=True)

    comment = models.TextField('Комментарий', null=True, blank=True)

    def __str__(self):
        return self.name
