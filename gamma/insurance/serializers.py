from pyexpat import model
from rest_framework import serializers
from core.models import Fuel, Vehicle_Segment, Customer_Income_Group, Customer_Region, Policy


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('type',)


class VehicleSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Segment
        fields = ('segment',)


class CustomerIncomeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Income_Group
        fields = ('income_group',)


class CustomerRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Region
        fields = ('region',)


class PolicySerializer(serializers.ModelSerializer):

    fuel = FuelSerializer()
    vehicle_segment = VehicleSegmentSerializer()
    customer_income_group = CustomerIncomeGroupSerializer()
    customer_region = CustomerRegionSerializer()

    class Meta:
        model = Policy
        fields = '__all__'
        read_only = ('date_of_purchase',)
        depth = 1

    def validateBooleans(self, data):
        if 'bodily_injury_liablility' in data:
            if data['bodily_injury_liablility'] == "true":
                data['bodily_injury_liablility'] = True
            else:
                data['bodily_injury_liablility'] = False
        if 'personal_injury_protection' in data:
            if data['personal_injury_protection'] == "true":
                data['personal_injury_protection'] = True
            else:
                data['personal_injury_protection'] = False
        if 'property_damage_liablility' in data:
            if data['property_damage_liablility'] == "true":
                data['property_damage_liablility'] = True
            else:
                data['property_damage_liablility'] = False
        if 'collision' in data:
            if data['collision'] == "true":
                data['collision'] = True
            else:
                data['collision'] = False
        if 'comprehensive' in data:
            if data['comprehensive'] == "true":
                data['comprehensive'] = True
            else:
                data['comprehensive'] = False
        if 'customer_marital_status' in data:
            if data['customer_marital_status'] == "true":
                data['customer_marital_status'] = True
            else:
                data['customer_marital_status'] = False
        return data

    def update(self, instance, validated_data):
        fuel_data = validated_data.pop('fuel')
        vehicle_segment_data = validated_data.pop('vehicle_segment')
        customer_income_group_data = validated_data.pop(
            'customer_income_group')
        customer_region_data = validated_data.pop('customer_region')

        instance.date_of_purchase = validated_data.get(
            'date_of_purchas', instance.date_of_purchase)
        instance.customer_id = validated_data.get(
            'customer_id', instance.customer_id)
        instance.premiun = validated_data.get('premiun', instance.premiun)
        instance.bodily_injury_liablility = validated_data.get(
            'bodily_injury_liablility', instance.bodily_injury_liablility)
        instance.personal_injury_protection = validated_data.get(
            'personal_injury_protection', instance.personal_injury_protection)
        instance.property_damage_liablility = validated_data.get(
            'property_damage_liablility', instance.property_damage_liablility)
        instance.collision = validated_data.get(
            'collision', instance.collision)
        instance.comprehensive = validated_data.get(
            'comprehensive', instance.comprehensive)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()

        fuel = instance.fuel
        fuel.type = fuel_data.get('type', fuel.type)
        fuel.save()

        vehicle_segment = instance.vehicle_segment
        vehicle_segment.segment = vehicle_segment_data.get(
            'segment', vehicle_segment.segment)
        vehicle_segment.save()

        customer_income_group = instance.customer_income_group
        customer_income_group.income_group = customer_income_group_data.get(
            'income_group', customer_income_group.income_group)
        customer_income_group.save()

        customer_region = instance.customer_region
        customer_region.region = customer_region_data.get(
            'region', customer_region.region)
        customer_region.save()

        return instance
