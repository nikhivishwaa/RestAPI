from rest_framework import serializers
from .models import Vendor, HistoricalPerformance, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_field = ['vendor_code']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_field = ['po_number', 'vendor', 'order_date']


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
        read_only_field = ['vendor', 'date']
