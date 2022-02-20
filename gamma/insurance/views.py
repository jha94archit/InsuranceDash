from calendar import calendar
from django.shortcuts import render
from matplotlib.font_manager import json_dump
from core.models import Policy, Fuel, Vehicle_Segment, Customer_Income_Group, Customer_Region
from .serializers import PolicySerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import TruncMonth
from django.db.models import Count
import datetime
import calendar


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


@api_view(['GET'])
def PolicyByMonthView(request):
    data = []
    queryset = Policy.objects.annotate(month=TruncMonth('date_of_purchase')).values(
        'month').annotate(c=Count('policy_id')).values('month', 'c')
    for query in queryset:
        date = datetime.datetime.strptime(str(query['month']), "%Y-%m-%d")
        data_dict = {
            'month': calendar.month_name[date.month],
            'policies': query['c']
        }
        data.append(data_dict)
    return Response(data)


@api_view(['GET'])
def PolicyByRegion(request):
    data = []
    region_queryset = Customer_Region.objects.all()
    for query in region_queryset:
        policies = Policy.objects.filter(
            customer_region__region__contains=query).count()
        data_dict = {
            'region': query.region,
            'policies': policies,
        }
        data.append(data_dict)
    return Response(data)
