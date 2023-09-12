from django.db import models
# from django.contrib.auth.models import User  # For user authentication

# Define the Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tagline = models.CharField(max_length=50, help_text="A short and crisp tagline. Ex: 'Sustainable Materials', 'Classic'", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/', help_text="Try to provide the image in the landscape format")
    stock = models.PositiveIntegerField()
    CATEGORY_CHOICES = (
        ('Electronics','Electronics'),
        ('Clothing','Clothing'),
        ('Books','Books'),
        ('Home','Home'),
        ('Kids','Kids'),
        ('Cosmetics','Cosmetics'),
        ('Fashion','Fashion'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

# # Define the Order model
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderItem')
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.IntegerField()
#     # Add more fields like shipping address, total price, etc.

#     def __str__(self):
#         return f'Order #{self.id}'
