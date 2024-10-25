from random import randint, choice, uniform
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from metrics.models import Lead, Campaign


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Lead.objects.all().delete() #deleteing the previous data
        Campaign.objects.all().delete()
        campaigns = [] #creating the array to store all the datas of the compigns
        for _ in range(10):
            campaign = Campaign.objects.create (
                campaign_id = f'campign{randint(1000, 9999)}',
                name = f'campign-{ randint(1, 100)}',
                start_date = datetime.now() - timedelta( days=randint(1, 30) ),  
                end_date = datetime.now() + timedelta( days=randint(1, 30) ),   
                lead_generated =randint(10, 100),
                budget = round( uniform(1000, 5000), 2 ), 
                revenue_generated=round(uniform(1000, 5000), 2), 
                cost_per_lead=round(uniform(50.0, 100.0), 2) ,
            )
            campaigns.append(campaign)
        for _ in range(10):
            Lead.objects.create(
                lead_id = f'lead{randint(1000, 9999)}',
                name = f'lead-{randint(1, 100)}',
                email = f'{name}{randint(1, 100)}@ezymetricsLead.com',
                source=choice([' google' ,' facebook','instagram']),
                phone_number=f'+91 {randint(1000000000, 9999999999)}',
                assigned_to=choice( ['user-a', 'user-b', 'user-c']),
                priority=choice( [1, 2, 3] ),  
                campaign=choice(campaigns) 
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched dummy data'))