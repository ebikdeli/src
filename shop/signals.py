from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender='shop.Product')
def change_empty_stock_unavailable(sender, instance=None, *args, **kwargs):
    """If 'stock' is empty or 0, turn is_available to False"""
    if not instance.stock and instance.is_available:
        instance.is_available = False


@receiver(pre_save, sender='shop.Product')
def change_unempty_stock_available(sender, instance=None, *args, **kwargs):
    """If 'stock' is not empty, turn is_available to True"""
    if instance.stock and not instance.is_available:
        instance.is_available = True


@receiver(pre_save, sender='shop.Product')
def calculate_price_end_after_price(sender, instance=None, **kwargs):
    """Calculate 'price_end' afer 'price' value and discounts on the 'price'"""
    # Implementing discounts later
    instance.price_end = instance.price
