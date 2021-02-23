from django.db import models

# Create your models here.

class Products(models.Model):
    #Product_id = models.AutoField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image= models.ImageField(upload_to="media/img", default="")
    type= models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Products"
    def __str__(self):
        return '%s %s' % (self.name, self.price)

class Categories(models.Model):
  name = models.CharField(max_length=255)
  category = models.ManyToManyField('self', blank=True)
  is_parent = models.BooleanField()

  def __str__(self):
     return self.name