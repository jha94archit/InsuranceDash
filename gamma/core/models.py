from django.db import models


class Fuel(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Vehicle_Segment(models.Model):
    segment = models.CharField(max_length=8)

    def __str__(self):
        return self.segment


class Customer_Income_Group(models.Model):
    income_group = models.CharField(max_length=255)

    def __str__(self):
        return self.income_group


class Customer_Region(models.Model):
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.region


class Policy(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    policy_id = models.CharField(primary_key=True, max_length=255)
    date_of_purchase = models.DateField()
    customer_id = models.CharField(max_length=255)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    vehicle_segment = models.ForeignKey(
        Vehicle_Segment, on_delete=models.CASCADE)
    premiun = models.IntegerField(blank=False)
    bodily_injury_liablility = models.BooleanField(default=False)
    personal_injury_protection = models.BooleanField(default=False)
    property_damage_liablility = models.BooleanField(default=False)
    collision = models.BooleanField(default=False)
    comprehensive = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=8, choices=GENDER_CHOICES, default="Male")
    customer_income_group = models.ForeignKey(
        Customer_Income_Group, on_delete=models.CASCADE)
    customer_region = models.ForeignKey(
        Customer_Region, on_delete=models.CASCADE)
    customer_marital_status = models.BooleanField(default=False)
