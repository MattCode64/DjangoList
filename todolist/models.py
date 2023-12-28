from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        # Return all the information about the collection
        return f"\nTitle: {self.title}\nSlug: {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Collection, self).save(*args, **kwargs)


class Task(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        # Return information about the task
        string = (f"\nTitle: {self.title}\nSlug: {self.slug}\nDescription: {self.description}\nCompleted: "
                  f"{self.completed}\nCreated: {self.created}\nCollection: {self.collection}")
        return string

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Task, self).save(*args, **kwargs)
