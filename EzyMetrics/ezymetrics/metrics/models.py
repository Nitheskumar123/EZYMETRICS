from django.db import models

class Campaign(models.Model):
    campaign_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    lead_generated = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    revenue_generated = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cost_per_lead = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    lead_id = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    source = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=True, null=False)
    assigned_to = models.CharField(max_length=255, blank=True, null=False)
    priority = models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=1)
    updated_at = models.DateTimeField(auto_now=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="leads")

    def __str__(self):
        return self.name
