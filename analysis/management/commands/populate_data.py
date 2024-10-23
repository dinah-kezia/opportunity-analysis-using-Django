import pandas as pd
from django.core.management.base import BaseCommand
from analysis.models import Opportunity

class Command(BaseCommand):
    help = 'Populates the database with the 5000-row dataset'

    def handle(self, *args, **kwargs):
        # Load the CSV dataset
        df = pd.read_csv(r'C:\Users\dinah\opportunity_analysis_dataset.csv')

        for index, row in df.iterrows():
            Opportunity.objects.create(
                opportunity_name=row['Opportunity Name'],
                category=row['Category'],
                region=row['Region'],
                company_name=row['Company Name'],
                contact_name=row['Contact Name'],
                contact_email=row['Contact Email'],
                revenue_potential=row['Revenue Potential'],
                probability_of_success=row['Probability of Success'],
                stage=row['Stage'],
                date_created=row['Date Created'],
                close_date=row['Close Date'],
                competitor=row['Competitor'],
                industry=row['Industry'],
                description=row['Description'],
                priority_level=row['Priority Level'],
                lead_source=row['Lead Source'],
                status=row['Status']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 5000 rows'))
