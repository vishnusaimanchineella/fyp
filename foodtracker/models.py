from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.IntegerField(default=5)
    height = models.IntegerField(default=40)
    weightt=models.IntegerField(default=4)
    neededcalories = models.IntegerField(default=0)
    neededcalorieslow=models.IntegerField(default=0)
    neededcalorieshigh=models.IntegerField(default=0)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    CLIMATE_CHOICES = [
        ('C', 'Cool'),
        ('H', 'Hot'),
        ('M', 'Mild')
    ]
    climate=models.CharField(max_length=1,default='M',choices=CLIMATE_CHOICES)
    gender = models.CharField(max_length=1,default='M', choices=GENDER_CHOICES)
    def __str__(self):
        return f'{self.username}'
 

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return f'{self.category_name}'

    @property
    def count_food_by_category(self):
        return Food.objects.filter(category=self).count()


class Food(models.Model):
    food_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    calories = models.DecimalField(default=0,decimal_places=2,max_digits=7)
    fat = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_category')

    def __str__(self):
        return f'{self.food_name} - category: {self.category}'


class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='get_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.image}'


class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.food_name}'


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.user.username} - {self.weight} kg on {self.entry_date}'
    
