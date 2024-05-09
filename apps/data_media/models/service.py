from django.db import models


class Head(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки '

    def __str__(self):
        return self.title


ISFREE=(
    ('free', 'Беслатно'),
    ('paid', 'Платно')
)


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ISFREE)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги '

    def __str__(self):
        return self.title
