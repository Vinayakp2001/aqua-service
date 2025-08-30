from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., fas fa-globe)")
    image = models.ImageField(upload_to='service_images/', help_text="Upload an image for the service card (e.g., service-webdev.jpg)")
    description = models.TextField()
    cost = models.CharField(max_length=100, blank=True, null=True)
    features = models.TextField(help_text="Comma-separated list of features (e.g., Feature 1, Feature 2)")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/', help_text="Upload an image for the project card (e.g., project-creative.jpg)")
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title