from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.timezone import datetime
from django.forms import ModelForm
# from tinymce import models as tinymce_models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify
from healthylifeapp.decorators import autoconnect
from django.core.validators import URLValidator

# General models
"""
class User(models.Model):
    Model de Usuario por defecto que trae Django
    - is_staff : diferencia entre usuario particular y de empresa
"""


class Address(models.Model):
    """Modelo para las direcciones postales"""
    name = models.CharField(max_length=50, default='mi direccion')
    city = models.CharField(max_length=50, default=' ', blank=True, null=True)
    postal_code = models.CharField(max_length=5, default='00000')
    street = models.CharField(max_length=50, default=' ', blank=True, null=True)
    number = models.CharField(max_length=4, default=' ', blank=True, null=True)
    floor = models.CharField(max_length=3, default=' ', blank=True, null=True)
    door = models.CharField(max_length=3, default=' ', blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.name)

    @receiver(signals.post_save, sender=User)
    def create_user_address(sender, instance, created, **kwargs):
        """este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            Address.objects.create(user_id=instance.id)


class BankInformation(models.Model):
    """modelo para la informacion bancaria"""
    name = models.CharField(max_length=50, default='mi informacion bancaria')
    account = models.CharField(max_length=20, default=' ', blank=True, null=True)
    month = models.CharField(max_length=2, default=' ', blank=True, null=True)
    year = models.CharField(max_length=4, default=' ', blank=True, null=True)
    security_code = models.CharField(max_length=3, default=' ', blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.name)

    @receiver(signals.post_save, sender=User)
    def create_user_bank_information(sender, instance, created, **kwargs):
        if created:
            BankInformation.objects.create(user_id=instance.id)


class UserProfile(models.Model):
    """Modelo para el perfil de un usuario"""
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=100)
    phone = models.CharField(max_length=9, default='000000000')
    # is_collaborator_blog = models.BooleanField(default=False, blank=False)
    # is_collaborator_shop = models.BooleanField(default=False, blank=False)


    def __unicode__(self):
        return str(self.user.username)

    @receiver(signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """Este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            CustomUser.objects.create(user_id=instance.id)


# Sport models
class SportType(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


class SportSession(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType)
    date = models.DateField(datetime.today)
    # usuario = models.ForeignKey(User)
    duration = models.TimeField()
    calories = models.IntegerField()

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


# Nutrition models
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(datetime.today)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def addIngredient(self):
        pass


class Measure(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    fats = models.ForeignKey(Nutrient, default='')
    # carbohydrates = models.ForeignKey(Nutrient)
    # proteins = models.ForeignKey(Nutrient)
    # fiber = models.ForeignKey(Nutrient)
    # sodium = models.ForeignKey(Nutrient)
    # calories = models.ForeignKey(Nutrient)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# Health models


# Statistics models
class GeneralStatistics(models.Model):
    pass


class SpecificStatistics(models.Model):
    pass


# Blog models
@autoconnect
class Category(models.Model):
    """Modelo para las categorias del blog"""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def pre_save(self):
        """metodo de la clase Category para calcular el slug de una categoria"""
        self.slug = self.name.replace(" ", "_").lower()
        print(self.slug)


@autoconnect
class Post(models.Model):
    """Modelo para los articulos del blog"""
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=False)
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=200, blank=False)
    content = models.TextField(default=" ", blank=False)
    category = models.ForeignKey(Category, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photos", default='/image.jpg', blank=False)
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.title

    def publishPost(self):
        """metodo de la clase post para publicar en redes sociles un post"""
        pass

    def pre_save(self):
        """metodo de la clase post para para calcular el slug de un post"""
        self.slug = self.title.replace(" ", "_").lower()


class Comment(models.Model):
    """Modelo para los comentarios del blog"""
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=3, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1)
    post = models.ForeignKey(Post, default=1)

    def __unicode__(self):
        return self.title

# Shop models
class Product(models.Model):
    """modelo para los productos de la tienda"""
    pass


class Discount(models.Model):
    name = models.CharField(max_length=50)
    DiscountType = ((1, "Cantidad"), (2, "Porcentaje"))
    discount = models.IntegerField(choices=DiscountType, default=1)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Company(models.Model):
    """modelo para las empresa de la tienda"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=9, default='000000000')
    web =  models.TextField(validators=[URLValidator()])
    address = models.OneToOneField(Address, default=1)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Awards models
class Award(models.Model):
    """modelo para los premios de los usuarios"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # discount = models.
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
