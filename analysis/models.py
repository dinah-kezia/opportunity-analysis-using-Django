from django.db import models

class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    opportunity_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    revenue_potential = models.IntegerField()
    probability_of_success = models.IntegerField()
    stage = models.CharField(max_length=50)
    date_created = models.DateField()
    close_date = models.DateField()
    competitor = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    description = models.TextField()
    priority_level = models.CharField(max_length=50)
    lead_source = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.opportunity_name

