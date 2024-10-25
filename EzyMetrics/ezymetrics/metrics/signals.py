from .models import Lead, Campaign
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Lead)
def lead_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New Lead created: {instance.name} (ID: {instance.lead_id})')
    else:
        print(f'Lead updated: {instance.name} (ID: {instance.lead_id})')

@receiver(post_delete, sender=Lead)
def lead_deleted(sender, instance, **kwargs):
    print(f'Lead deleted: {instance.name} (ID: {instance.lead_id})')

@receiver(post_save, sender=Campaign)
def campaign_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New Campaign created: {instance.name} (ID: {instance.campaign_id})')
    else:
        print(f'Campaign updated: {instance.name} (ID: {instance.campaign_id})')

@receiver(post_delete, sender=Campaign)
def campaign_deleted(sender, instance, **kwargs):
    print(f'Campaign deleted: {instance.name} (ID: {instance.campaign_id})')