from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.author_name

class Publisher(models.Model):
    pub_name = models.CharField(max_length=100)  

    def __str__(self):
        return self.pub_name 

class Book(models.Model):
    slug = models.SlugField(max_length=100,blank=True,null=True)
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_page = models.IntegerField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("table", kwargs={"table_slug": self.slug})
    


    def get_author_name(self):
        # return ' , '.join([i.author_name for i in self.author.all()])
        return ' , '.join(list(self.author.all().values_list("author_name",flat=True)))

    def get_author_age(self):
        return ' '.join(str(tuple(self.author.all().values_list("age",flat=True))))

    def __str__(self):
        return self.book_name

