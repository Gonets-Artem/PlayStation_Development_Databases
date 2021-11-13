from rest_framework import serializers
from .models import *
from . import models


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = "__all__"


class DesignSerializer(serializers.ModelSerializer):
    designers = DesignerSerializer(many=True)
    class Meta:
        model = Design
        fields = ('design_id', 'name', 'colour', 'style', 'status', 'designers')


class DualshockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dualshock
        fields = "__all__"


class PSVRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSVR
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"


class SoftwareSerializer(serializers.ModelSerializer):
    developers = DeveloperSerializer(many=True)
    class Meta:
        model = Software
        fields = ('software_id', 'type', 'version', 'status', 'developers')


class FormFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFactor
        fields = "__all__"


class PrototypeSerializer(serializers.ModelSerializer):
    softwares = SoftwareSerializer(many=True)
    form_factors = FormFactorSerializer(many=True)
    class Meta:
        model = Prototype
        fields = ('prototype_id', 'name', 'date', 'ssd_type', 'type_storage_device', 'specifications', 'softwares', 'form_factors')


class ConsoleSerializer(serializers.ModelSerializer):
    prototype = PrototypeSerializer()
    class Meta:
        model = Console
        fields = ('console_id', 'name', 'date', 'weight', 'ram', 'rom', 'prototype')


class AdvertisingDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingDepartment
        fields = "__all__"


class InvestorSerializer(serializers.ModelSerializer):
    advertising_department = AdvertisingDepartmentSerializer()
    class Meta:
        model = Investor
        fields = ('investor_id', 'name', 'email', 'phone', 'advertising_department')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class TargetAudienceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer()
    class Meta:
        model = TargetAudience
        fields = ('region', 'description', 'feedback')


class PRManagerSerializer(serializers.ModelSerializer):
    advertising_department = AdvertisingDepartmentSerializer()
    feedbacks = FeedbackSerializer(many=True)
    class Meta:
        model = PRManager
        fields = ('pr_manager_id', 'name', 'role', 'email', 'phone', 'advertising_department', 'feedbacks')


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = "__all__"


class MarketAnalysisSerializer(serializers.ModelSerializer):
    competitors = CompetitorSerializer(many=True)
    class Meta:
        model = MarketAnalysis
        fields = ('market_analysis_id', 'quality', 'predicted_price', 'potential', 'competitors')


class ProductManagerSerializer(serializers.ModelSerializer):
    advertising_department = AdvertisingDepartmentSerializer()
    market_analysises = MarketAnalysisSerializer(many=True)
    class Meta:
        model = ProductManager
        fields = ('product_manager_id', 'name', 'role', 'email', 'phone', 'advertising_department', 'market_analysises')


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"


class StorageRoomSerializer(serializers.ModelSerializer):
    plant = PlantSerializer()
    class Meta:
        model = StorageRoom
        fields = ('storage_room_id', 'location', 'capacity', 'plant')


class ComponentSerializer(serializers.ModelSerializer):
    storage_room = StorageRoomSerializer()
    class Meta:
        model = Component
        fields = ('component_id', 'name', 'description', 'storage_room')


class SupplierSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)
    class Meta:
        model = Supplier
        fields = ('supplier_id', 'name', 'email', 'phone', 'components')


class EquipmentSerializer(serializers.ModelSerializer):
    plant = PlantSerializer()
    class Meta:
        model = Equipment
        fields = ('equipment_id', 'name', 'description', 'plant')


class EquipmentConditionSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer()
    class Meta:
        model = EquipmentCondition
        fields = ('service_ability', 'noise_level', 'temperature', 'wear_level', 'errors_number', 'equipment')


class EmployeeSerializer(serializers.ModelSerializer):
    equipments = EquipmentSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('employee_id', 'name', 'role', 'email', 'phone', 'equipments')


class KitSerializer(serializers.ModelSerializer):
    advertising_department = AdvertisingDepartmentSerializer()
    plant = PlantSerializer()
    design = DesignSerializer()
    console = ConsoleSerializer()
    dualshock = DualshockSerializer()
    psvr = PSVRSerializer()
    class Meta:
        model = Kit
        fields = ('kit_id', 'name', 'date', 'advertising_department', 'plant', 'design', 'console', 'dualshock', 'psvr')
