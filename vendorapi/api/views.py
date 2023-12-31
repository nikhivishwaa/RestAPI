from django.shortcuts import render
from rest_framework.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import VendorSerializer, Vendor
from rest_framework import status


class VendorAPIView(APIView):
    def get(self, request, vc: str | None = None, format=None):
        if vc is not None:
            vendor = Vendor.objects.get(vendor_code=vc)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        vendor = Vendor.objects.all()
        serializer = VendorSerializer(vendor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        vendor = VendorSerializer(data=request.data)
        if vendor.is_valid():
            vendor.save()
            return Response(vendor.data, status=status.HTTP_201_CREATED)
        return Response(vendor.errors, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, vc: str, format=None):
        try:
            vendor = Vendor.objects.get(vendor_code=vc)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
            return Response(vendor.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "invalid vendor"}, status= status.HTTP_404_NOT_FOUND)

    def delete(self, request, vc: str | None = None, format=None):
        if vc is not None:
            try:
                vendor = Vendor.objects.get(vendor_code=vc)
                print(vendor)
                vendor.delete()
                return Response({"message": "vendor deleted", "vendor_code": vc})
            except Exception as e:
                return Response({"error": "invalid vendor"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "vendor not found"}, status=status.HTTP_404_NOT_FOUND)
