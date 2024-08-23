from django.db import models
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator, MaxValueValidator


class Character(models.Model):
    name = models.TextField(verbose_name="Name")
    image = models.ImageField(verbose_name="Image", upload_to="dravenverse")
    banner = models.ImageField(verbose_name="Banner", upload_to="dravenverse")
    birthplace = RichTextField(verbose_name="Birth Place")
    age = models.IntegerField(verbose_name="Age")
    backstory = RichTextField(verbose_name="Backstory")
    description_short = models.TextField(verbose_name="Short Description")
    role = models.TextField(verbose_name="Role")
    slug = models.SlugField(unique=True)

    attack_stats = models.IntegerField(verbose_name="Attack Stats", validators=[MinValueValidator(0), MaxValueValidator(100)])
    defense_stats = models.IntegerField(verbose_name="Defense Stats", validators=[MinValueValidator(0), MaxValueValidator(100)])
    intelligence_stats = models.IntegerField(verbose_name="Intelligence Stats", validators=[MinValueValidator(0), MaxValueValidator(100)])
    speed_stats = models.IntegerField(verbose_name="Speed Stats", validators=[MinValueValidator(0), MaxValueValidator(100)])
    hp_stats = models.IntegerField(verbose_name="HP Stats", validators=[MinValueValidator(0), MaxValueValidator(100)])

    history = HistoricalRecords(verbose_name="History")

class Stats(models.Model):
    pass