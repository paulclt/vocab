from django.db import models

# Define the Level model
class Level(models.Model):
    name = models.CharField(max_length=255, unique=True)  # A unique name for each level

    def __str__(self):
        return self.name

# Define the Unit model
class Unit(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="units")

    def __str__(self):
        return self.name

# Define the Vocabulary model
class Vocabulary(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="vocabularies")
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)

    def __str__(self):
        return self.word





