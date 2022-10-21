from django.db import models


class Student(models.Model):  # modellerle işlem yaparken makemigration ve migrate işlemlerini yap!
    COUNTRIES = [
        ('TR', 'Türkiye'),
        ('US', 'America'),
        ('DE', 'Germany'),
        ('FR', 'France'),
    ]
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    number = models.IntegerField('Numara')
    about = models.TextField('Hakkında', blank=True, null=True)
    country = models.CharField(
        'Ülke', max_length=2, choices=COUNTRIES, default='TR')
    avatar = models.ImageField(
        'Resim', blank=True, null=True, upload_to='media/')
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['number']  # DESC -> ['-number']
        verbose_name_plural = 'Öğrenciler'


# https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options

# s1 = Student.objects.create(number=2, last_name....) # hem oluşturur hem kaydeder.
# q1 = Student(last_name.....) #oluştur. q1.save() ile kaydet...
# g1 = Student.objects.get(number=1)  # tek kayıt döndürür filtreleme birden fazla kayıt
# #dönecekse filter kullanılır.
# f1 = Student.objects.filter(number=1) # sorguya uyan bütün kayıtları getirir.
# f2 = Student.objects.exclude(number=1) # number'ı 1'e eşit olmayanlar gelir
# f1=Student.objects.filter(first_name__startswith='R') # R harfiyle başlayanları getirir
