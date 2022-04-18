from django.db import models
from django.conf import settings

class Macro(models.Model):
    BASIC = 'basic'
    ADVANCED = 'advanced'
    PYTHON = 'python'
    MACRO_TYPE_CHOICES = (
            (BASIC, 'basic'),
            (ADVANCED, 'advanced'),
            (PYTHON, 'python')
            )
    alias = models.CharField(max_length = 10)
    code = models.CharField(max_length=1024)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    m_type = models.CharField(
            max_length=10,
            choices = MACRO_TYPE_CHOICES,
            default = BASIC,
            )
    public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.alias

