Title: Python
Date: 2015-12-03 10:20
Category: Review

```python
"""
This module defines the data structure of a Menu.
"""
from django.db import models

from .fields import ShortUUIDField


class Menu(models.Model):
    """
    Describes a menu with many categories and items
    eg. Breakfast Menu, Lunch Menu, Weekend Menu
    """

    uuid = ShortUUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return str(self.title)


class MenuCategory(models.Model):
    """
    A section of a menu that has many menu items
    eg. Entrees, Sides, Dessert
    """

    title = models.CharField(max_length=150)
    description = models.TextField()
    menu = models.ForeignKey(to=Menu, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.title)


class MenuItem(models.Model):
    """
    Describes an item belonging to a Menu
    eg. Burger, Quesadilla, Pad Thai
    """

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(
        to=MenuCategory,
        null=False,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.title)


class AddonSection(models.Model):
    """
    A section of addons
    eg. Choice of Side, Size, Spiciness
    """

    title = models.CharField(max_length=150)
    description = models.TextField()
    required = models.BooleanField()
    menu_item = models.ForeignKey(to=MenuItem,
                                  null=False,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Addon(models.Model):
    """
    Describes additional options for a menu item
    eg. Extra Salsa, Side of Fries, Toasted
    """

    SELECTION_TYPES = [
        ("R", "Radio"),
        ("M", "Multiple Selection"),
    ]

    description = models.CharField(max_length=150)
    selection = models.CharField(max_length=1,
                                 choices=SELECTION_TYPES,
                                 default=SELECTION_TYPES[0][0])
    section = models.ForeignKey(
        to=AddonSection,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.description)
```