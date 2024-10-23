from rest_framework import generics
from .models import Opportunity
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from .serializers import OpportunitySerializer

class OpportunityListCreate(generics.ListCreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class OpportunitySummary(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_revenue = Opportunity.objects.aggregate(total_revenue=Sum('revenue_potential'))
        avg_success = Opportunity.objects.aggregate(average_success=Avg('probability_of_success'))

        return Response({
            'total_revenue': total_revenue,
            'average_success_rate': avg_success,
        })

class OpportunityReportView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        
        stages_summary = Opportunity.objects.values('stage').annotate(stage_count=Count('opportunity_id'))
        category_revenue = Opportunity.objects.values('category').annotate(total_revenue=Sum('revenue_potential'))
        region_avg_revenue = Opportunity.objects.values('region').annotate(avg_revenue=Avg('revenue_potential'))
        monthly_summary = Opportunity.objects.annotate(month=TruncMonth('date_created')).values('month').annotate(opportunity_count=Count('opportunity_id'))
        closed_vs_open = Opportunity.objects.values('status').annotate(status_count=Count('opportunity_id'))
        competitor_summary = Opportunity.objects.values('competitor').annotate(competitor_count=Count('opportunity_id'))
        lead_source_success = Opportunity.objects.values('lead_source').annotate(avg_success=Avg('probability_of_success'))
        top_5_opportunities = Opportunity.objects.order_by('-revenue_potential')[:5]
        top_5_opportunities_serialized = OpportunitySerializer(top_5_opportunities, many=True).data
        high_priority_opportunities = Opportunity.objects.filter(priority_level='High').aggregate(total_high_priority_revenue=Sum('revenue_potential'))




        
        return Response({
            'stages_summary': stages_summary,
            'category_revenue': category_revenue,
            'region_avg_revenue': region_avg_revenue,
            'monthly_summary': monthly_summary,
            'closed_vs_open': closed_vs_open,
            'competitor_summary': competitor_summary,
            'lead_succes_rate': lead_source_success,
            'top_5_opportunities': top_5_opportunities_serialized,
            'high_priority_opportunities': high_priority_opportunities
        })
