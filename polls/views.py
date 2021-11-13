from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from . import serializers


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")


def get_designer(request):
    if request.method == "GET":
        designers = Designer.objects.all()
        serializer = serializers.DesignerSerializer(designers, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_design(request):
    if request.method == "GET":
        designs = Design.objects.all()
        serializer = serializers.DesignSerializer(designs, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_dualshock(request):
    if request.method == "GET":
        dualshocks = Dualshock.objects.all()
        serializer = serializers.DualshockSerializer(dualshocks, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_ps_vr(request):
    if request.method == "GET":
        ps_vrs = PSVR.objects.all()
        serializer = serializers.PSVRSerializer(ps_vrs, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_developer(request):
    if request.method == "GET":
        developers = Developer.objects.all()
        serializer = serializers.DeveloperSerializer(developers, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_software(request):
    if request.method == "GET":
        softwares = Software.objects.all()
        serializer = serializers.SoftwareSerializer(softwares, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_form_factor(request):
    if request.method == "GET":
        form_factors = FormFactor.objects.all()
        serializer = serializers.FormFactorSerializer(form_factors, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_prototype(request):
    if request.method == "GET":
        prototypes = Prototype.objects.all()
        serializer = serializers.PrototypeSerializer(prototypes, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_console(request):
    if request.method == "GET":
        consoles = Console.objects.all()
        serializer = serializers.ConsoleSerializer(consoles, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_advertising_department(request):
    if request.method == "GET":
        advertising_departments = AdvertisingDepartment.objects.all()
        serializer = serializers.AdvertisingDepartmentSerializer(advertising_departments, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_investor(request):
    if request.method == "GET":
        investors = Investor.objects.all()
        serializer = serializers.InvestorSerializer(investors, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_feedback(request):
    if request.method == "GET":
        feedbacks = Feedback.objects.all()
        serializer = serializers.FeedbackSerializer(feedbacks, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_target_audience(request):
    if request.method == "GET":
        target_audiences = TargetAudience.objects.all()
        serializer = serializers.TargetAudienceSerializer(target_audiences, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_pr_manager(request):
    if request.method == "GET":
        pr_managers = PRManager.objects.all()
        serializer = serializers.PRManagerSerializer(pr_managers, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_competitor(request):
    if request.method == "GET":
        competitors = Competitor.objects.all()
        serializer = serializers.CompetitorSerializer(competitors, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_market_analysis(request):
    if request.method == "GET":
        market_analysises = MarketAnalysis.objects.all()
        serializer = serializers.MarketAnalysisSerializer(market_analysises, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_product_manager(request):
    if request.method == "GET":
        product_managers = ProductManager.objects.all()
        serializer = serializers.ProductManagerSerializer(product_managers, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_plant(request):
    if request.method == "GET":
        plants = Plant.objects.all()
        serializer = serializers.PlantSerializer(plants, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_storage_room(request):
    if request.method == "GET":
        storage_rooms = StorageRoom.objects.all()
        serializer = serializers.StorageRoomSerializer(storage_rooms, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_component(request):
    if request.method == "GET":
        components = Component.objects.all()
        serializer = serializers.ComponentSerializer(components, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_supplier(request):
    if request.method == "GET":
        suppliers = Supplier.objects.all()
        serializer = serializers.SupplierSerializer(suppliers, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_equipment(request):
    if request.method == "GET":
        equipments = Equipment.objects.all()
        serializer = serializers.EquipmentSerializer(equipments, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_equipment_condition(request):
    if request.method == "GET":
        equipment_conditions = EquipmentCondition.objects.all()
        serializer = serializers.EquipmentConditionSerializer(equipment_conditions, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_employee(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = serializers.EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_kit(request):
    if request.method == "GET":
        kits = Kit.objects.all()
        serializer = serializers.KitSerializer(kits, many=True)
        return JsonResponse(serializer.data, safe=False)
