from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to = 'image/')
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']

    def save_product(self):
        self.save()
    @classmethod
    def get_product(cls):
        products = cls.objects.all();
        return products 

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    description = models.TextField()
     
    

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  
    def update_image(self):
        self.update() 

    @classmethod
    def get_image(cls):
        image = Image.objects.get(id=id)
        return image  