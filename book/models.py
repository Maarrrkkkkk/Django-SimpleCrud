from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    is_deleted = models.BooleanField(default=False)
    

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def hard_delete(self):
        super(Book, self).delete()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title