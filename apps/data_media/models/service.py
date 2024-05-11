from django.db import models

ISFREE=(
    ('free', 'Беслатно'),
    ('paid', 'Платно')
)


class Service(models.Model):
    content = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ISFREE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги '

    def __str__(self):
        return self.content
