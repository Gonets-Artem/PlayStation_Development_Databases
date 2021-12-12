from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


def get_all(model, model_ser):
    subjects = model.objects.all()
    serializer = model_ser(subjects, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_one(model_ser, get):
    serializer = model_ser(get)
    return JsonResponse(serializer.data, safe=False)


def post(model_ser, data):
    serializer = model_ser(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


def put(obj, model_ser, data):
    serializer = model_ser(obj, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def designer(request):
    if request.method == "GET":
        return get_all(Designer, DesignerSerializerGet)

    elif request.method == "POST":
        return post(DesignerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Designer.objects.all().delete()
        # return JsonResponse({'message': '{} designers were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def designer_id(request, id):
    try:
        designer = Designer.objects.get(designer_id=id)
    except Designer.DoesNotExist:
        return JsonResponse({'message': 'The does not exist'}, status=404)

    if request.method == "GET":
        return get_one(DesignerSerializerGet, designer)

    elif request.method == "PUT":
        return put(designer, DesignerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # designer.delete()
        # return JsonResponse({'message': 'designer was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def design(request):
    if request.method == "GET":
        return get_all(Design, DesignSerializerGet)

    elif request.method == "POST":
        return post(DesignSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Design.objects.all().delete()
        # return JsonResponse({'message': '{} designs were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def design_id(request, id):
    try:
        design = Design.objects.get(design_id=id)
    except Design.DoesNotExist:
        return JsonResponse({'message': 'The design does not exist'}, status=404)

    if request.method == "GET":
        return get_one(DesignSerializerGet, design)

    elif request.method == "PUT":
        return put(design, DesignSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # design.delete()
        # return JsonResponse({'message': 'design was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def dualshock(request):
    if request.method == "GET":
        return get_all(Dualshock, DualshockSerializerGet)

    elif request.method == "POST":
        return post(DualshockSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Dualshock.objects.all().delete()
        # return JsonResponse({'message': '{} dualshocks were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def dualshock_id(request, id):
    try:
        dualshock = Dualshock.objects.get(dualshock_id=id)
    except Dualshock.DoesNotExist:
        return JsonResponse({'message': 'The dualshock does not exist'}, status=404)

    if request.method == "GET":
        return get_one(DualshockSerializerGet, dualshock)

    elif request.method == "PUT":
        return put(dualshock, DualshockSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # dualshock.delete()
        # return JsonResponse({'message': 'dualshock was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def ps_vr(request):
    if request.method == "GET":
        return get_all(PSVR, PSVRSerializerGet)

    elif request.method == "POST":
        return post(PSVRSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = PSVR.objects.all().delete()
        # return JsonResponse({'message': '{} ps_vrs were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def ps_vr_id(request, id):
    try:
        ps_vr = PSVR.objects.get(ps_vr_id=id)
    except PSVR.DoesNotExist:
        return JsonResponse({'message': 'The ps_vr does not exist'}, status=404)

    if request.method == "GET":
        return get_one(PSVRSerializerGet, ps_vr)

    elif request.method == "PUT":
        return put(ps_vr, PSVRSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # ps_vr.delete()
        # return JsonResponse({'message': 'ps_vr was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def developer(request):
    if request.method == "GET":
        return get_all(Developer, DeveloperSerializerGet)

    elif request.method == "POST":
        return post(DeveloperSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Developer.objects.all().delete()
        # return JsonResponse({'message': '{} developers were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def developer_id(request, id):
    try:
        developer = Developer.objects.get(developer_id=id)
    except Developer.DoesNotExist:
        return JsonResponse({'message': 'The developer does not exist'}, status=404)

    if request.method == "GET":
        return get_one(DeveloperSerializerGet, developer)

    elif request.method == "PUT":
        return put(developer, DeveloperSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # developer.delete()
        # return JsonResponse({'message': 'developer was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def software(request):
    if request.method == "GET":
        return get_all(Software, SoftwareSerializerGet)

    elif request.method == "POST":
        return post(SoftwareSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Software.objects.all().delete()
        # return JsonResponse({'message': '{} softwares were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def software_id(request, id):
    try:
        software = Software.objects.get(software_id=id)
    except Software.DoesNotExist:
        return JsonResponse({'message': 'The software does not exist'}, status=404)

    if request.method == "GET":
        return get_one(SoftwareSerializerGet, software)

    elif request.method == "PUT":
        return put(software, SoftwareSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # software.delete()
        # return JsonResponse({'message': 'software was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def form_factor(request):
    if request.method == "GET":
        return get_all(FormFactor, FormFactorSerializerGet)

    elif request.method == "POST":
        return post(FormFactorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = FormFactor.objects.all().delete()
        # return JsonResponse({'message': '{} form_factors were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def form_factor_id(request, id):
    try:
        form_factor = FormFactor.objects.get(form_factor_id=id)
    except FormFactor.DoesNotExist:
        return JsonResponse({'message': 'The form_factor does not exist'}, status=404)

    if request.method == "GET":
        return get_one(FormFactorSerializerGet, form_factor)

    elif request.method == "PUT":
        return put(form_factor, FormFactorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # form_factor.delete()
        # return JsonResponse({'message': 'form_factor was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def prototype(request):
    if request.method == "GET":
        return get_all(Prototype, PrototypeSerializerGet)

    elif request.method == "POST":
        return post(PrototypeSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Prototype.objects.all().delete()
        # return JsonResponse({'message': '{} prototypes were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def prototype_id(request, id):
    try:
        prototype = Prototype.objects.get(prototype_id=id)
    except FormFactor.DoesNotExist:
        return JsonResponse({'message': 'The prototype does not exist'}, status=404)

    if request.method == "GET":
        return get_one(PrototypeSerializerGet, prototype)

    elif request.method == "PUT":
        return put(prototype, PrototypeSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # prototype.delete()
        # return JsonResponse({'message': 'prototype was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def console(request):
    if request.method == "GET":
        return get_all(Console, ConsoleSerializerGet)

    elif request.method == "POST":
        return post(ConsoleSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Console.objects.all().delete()
        # return JsonResponse({'message': '{} consoles were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def console_id(request, id):
    try:
        console = Console.objects.get(console_id=id)
    except Console.DoesNotExist:
        return JsonResponse({'message': 'The console does not exist'}, status=404)

    if request.method == "GET":
        return get_one(ConsoleSerializerGet, console)

    elif request.method == "PUT":
        return put(console, ConsoleSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # console.delete()
        # return JsonResponse({'message': 'console was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def advertising_department(request):
    if request.method == "GET":
        return get_all(AdvertisingDepartment, AdvertisingDepartmentSerializerGet)

    elif request.method == "POST":
        return post(AdvertisingDepartmentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = AdvertisingDepartment.objects.all().delete()
        # return JsonResponse({'message': '{} advertising_departments were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def advertising_department_id(request, id):
    try:
        advertising_department = AdvertisingDepartment.objects.get(advertising_department_id=id)
    except AdvertisingDepartment.DoesNotExist:
        return JsonResponse({'message': 'The advertising_department does not exist'}, status=404)

    if request.method == "GET":
        return get_one(AdvertisingDepartmentSerializerGet, advertising_department)

    elif request.method == "PUT":
        return put(advertising_department, AdvertisingDepartmentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # advertising_department.delete()
        # return JsonResponse({'message': 'advertising_department was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def investor(request):
    if request.method == "GET":
        return get_all(Investor, InvestorSerializerGet)

    elif request.method == "POST":
        return post(InvestorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Investor.objects.all().delete()
        # return JsonResponse({'message': '{} investors were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def investor_id(request, id):
    try:
        investor = Investor.objects.get(investor_id=id)
    except Investor.DoesNotExist:
        return JsonResponse({'message': 'The investor does not exist'}, status=404)

    if request.method == "GET":
        return get_one(InvestorSerializerGet, investor)

    elif request.method == "PUT":
        return put(investor, InvestorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # investor.delete()
        # return JsonResponse({'message': 'investor was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def feedback(request):
    if request.method == "GET":
        return get_all(Feedback, FeedbackSerializerGet)

    elif request.method == "POST":
        return post(FeedbackSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Feedback.objects.all().delete()
        # return JsonResponse({'message': '{} feedbacks were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def feedback_id(request, id):
    try:
        feedback = Feedback.objects.get(feedback_id=id)
    except Feedback.DoesNotExist:
        return JsonResponse({'message': 'The feedback does not exist'}, status=404)

    if request.method == "GET":
        return get_one(FeedbackSerializerGet, feedback)

    elif request.method == "PUT":
        return put(feedback, FeedbackSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # feedback.delete()
        # return JsonResponse({'message': 'feedback was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def target_audience(request):
    if request.method == "GET":
        return get_all(TargetAudience, TargetAudienceSerializerGet)

    elif request.method == "POST":
        return post(TargetAudienceSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = TargetAudience.objects.all().delete()
        # return JsonResponse({'message': '{} target_audiences were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def target_audience_id(request, id):
    try:
        target_audience = TargetAudience.objects.get(feedback=id)
    except TargetAudience.DoesNotExist:
        return JsonResponse({'message': 'The target_audience does not exist'}, status=404)

    if request.method == "GET":
        return get_one(TargetAudienceSerializerGet, target_audience)

    elif request.method == "PUT":
        return put(target_audience, TargetAudienceSerializer, request.data)

    elif request.method == "DELETE":
        target_audience.delete()
        return JsonResponse({'message': 'target_audience was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def pr_manager(request):
    if request.method == "GET":
        return get_all(PRManager, PRManagerSerializerGet)

    elif request.method == "POST":
        return post(PRManagerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = PRManager.objects.all().delete()
        # return JsonResponse({'message': '{} pr_managers were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def pr_manager_id(request, id):
    try:
        pr_manager = PRManager.objects.get(pr_manager_id=id)
    except PRManager.DoesNotExist:
        return JsonResponse({'message': 'The pr_manager does not exist'}, status=404)

    if request.method == "GET":
        return get_one(PRManagerSerializerGet, pr_manager)

    elif request.method == "PUT":
        return put(pr_manager, PRManagerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # pr_manager.delete()
        # return JsonResponse({'message': 'pr_manager was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def competitor(request):
    if request.method == "GET":
        return get_all(Competitor, CompetitorSerializerGet)

    elif request.method == "POST":
        return post(CompetitorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Competitor.objects.all().delete()
        # return JsonResponse({'message': '{} competitors were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def competitor_id(request, id):
    try:
        competitor = Competitor.objects.get(competitor_id=id)
    except Competitor.DoesNotExist:
        return JsonResponse({'message': 'The competitor does not exist'}, status=404)

    if request.method == "GET":
        return get_one(CompetitorSerializerGet, competitor)

    elif request.method == "PUT":
        return put(competitor, CompetitorSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # competitor.delete()
        # return JsonResponse({'message': 'competitor was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def market_analysis(request):
    if request.method == "GET":
        return get_all(MarketAnalysis, MarketAnalysisSerializerGet)

    elif request.method == "POST":
        return post(MarketAnalysisSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = MarketAnalysis.objects.all().delete()
        # return JsonResponse({'message': '{} market_analysises were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def market_analysis_id(request, id):
    try:
        market_analysis = MarketAnalysis.objects.get(market_analysis_id=id)
    except MarketAnalysis.DoesNotExist:
        return JsonResponse({'message': 'The market_analysis does not exist'}, status=404)

    if request.method == "GET":
        return get_one(MarketAnalysisSerializerGet, market_analysis)

    elif request.method == "PUT":
        return put(market_analysis, MarketAnalysisSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # market_analysis.delete()
        # return JsonResponse({'message': 'market_analysis was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def product_manager(request):
    if request.method == "GET":
        return get_all(ProductManager, ProductManagerSerializerGet)

    elif request.method == "POST":
        return post(ProductManagerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = ProductManager.objects.all().delete()
        # return JsonResponse({'message': '{} product_managers were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def product_manager_id(request, id):
    try:
        product_manager = ProductManager.objects.get(product_manager_id=id)
    except ProductManager.DoesNotExist:
        return JsonResponse({'message': 'The product_manager does not exist'}, status=404)

    if request.method == "GET":
        return get_one(ProductManagerSerializerGet, product_manager)

    elif request.method == "PUT":
        return put(product_manager, ProductManagerSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # product_manager.delete()
        # return JsonResponse({'message': 'product_manager was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def plant(request):
    if request.method == "GET":
        return get_all(Plant, PlantSerializerGet)

    elif request.method == "POST":
        return post(PlantSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Plant.objects.all().delete()
        # return JsonResponse({'message': '{} plants were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def plant_id(request, id):
    try:
        plant = Plant.objects.get(plant_id=id)
    except Plant.DoesNotExist:
        return JsonResponse({'message': 'The plant does not exist'}, status=404)

    if request.method == "GET":
        return get_one(PlantSerializerGet, plant)

    elif request.method == "PUT":
        return put(plant, PlantSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # plant.delete()
        # return JsonResponse({'message': 'plant was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def storage_room(request):
    if request.method == "GET":
        return get_all(StorageRoom, StorageRoomSerializerGet)

    elif request.method == "POST":
        return post(StorageRoomSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = StorageRoom.objects.all().delete()
        # return JsonResponse({'message': '{} storage_rooms were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def storage_room_id(request, id):
    try:
        storage_room = StorageRoom.objects.get(storage_room_id=id)
    except StorageRoom.DoesNotExist:
        return JsonResponse({'message': 'The storage_room does not exist'}, status=404)

    if request.method == "GET":
        return get_one(StorageRoomSerializerGet, storage_room)

    elif request.method == "PUT":
        return put(storage_room, StorageRoomSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # storage_room.delete()
        # return JsonResponse({'message': 'storage_room was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def component(request):
    if request.method == "GET":
        return get_all(Component, ComponentSerializerGet)

    elif request.method == "POST":
        return post(ComponentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Component.objects.all().delete()
        # return JsonResponse({'message': '{} components were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def component_id(request, id):
    try:
        component = Component.objects.get(component_id=id)
    except Component.DoesNotExist:
        return JsonResponse({'message': 'The component does not exist'}, status=404)

    if request.method == "GET":
        return get_one(ComponentSerializerGet, component)

    elif request.method == "PUT":
        return put(component, ComponentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # component.delete()
        # return JsonResponse({'message': 'component was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def supplier(request):
    if request.method == "GET":
        return get_all(Supplier, SupplierSerializerGet)

    elif request.method == "POST":
        return post(SupplierSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Supplier.objects.all().delete()
        # return JsonResponse({'message': '{} suppliers were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def supplier_id(request, id):
    try:
        supplier = Supplier.objects.get(supplier_id=id)
    except Supplier.DoesNotExist:
        return JsonResponse({'message': 'The supplier does not exist'}, status=404)

    if request.method == "GET":
        return get_one(SupplierSerializerGet, supplier)

    elif request.method == "PUT":
        return put(supplier, SupplierSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # supplier.delete()
        # return JsonResponse({'message': 'supplier was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def equipment(request):
    if request.method == "GET":
        return get_all(Equipment, EquipmentSerializerGet)

    elif request.method == "POST":
        return post(EquipmentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Equipment.objects.all().delete()
        # return JsonResponse({'message': '{} equipments were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def equipment_id(request, id):
    try:
        equipment = Equipment.objects.get(equipment_id=id)
    except Equipment.DoesNotExist:
        return JsonResponse({'message': 'The equipment does not exist'}, status=404)

    if request.method == "GET":
        return get_one(EquipmentSerializerGet, equipment)

    elif request.method == "PUT":
        return put(equipment, EquipmentSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # equipment.delete()
        # return JsonResponse({'message': 'equipment was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def equipment_condition(request):
    if request.method == "GET":
        return get_all(EquipmentCondition, EquipmentConditionSerializerGet)

    elif request.method == "POST":
        return post(EquipmentConditionSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = EquipmentCondition.objects.all().delete()
        # return JsonResponse({'message': '{} equipment_conditions were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def equipment_condition_id(request, id):
    try:
        equipment_condition = EquipmentCondition.objects.get(equipment=id)
    except EquipmentCondition.DoesNotExist:
        return JsonResponse({'message': 'The equipment_condition does not exist'}, status=404)

    if request.method == "GET":
        return get_one(EquipmentConditionSerializerGet, equipment_condition)

    elif request.method == "PUT":
        return put(equipment_condition, EquipmentConditionSerializer, request.data)

    elif request.method == "DELETE":
        equipment_condition.delete()
        return JsonResponse({'message': 'equipment_condition was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def employee(request):
    if request.method == "GET":
        return get_all(Employee, EmployeeSerializerGet)

    elif request.method == "POST":
        return post(EmployeeSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Employee.objects.all().delete()
        # return JsonResponse({'message': '{} employees were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_id(request, id):
    try:
        employee = Employee.objects.get(employee_id=id)
    except Employee.DoesNotExist:
        return JsonResponse({'message': 'The employee does not exist'}, status=404)

    if request.method == "GET":
        return get_one(EmployeeSerializerGet, employee)

    elif request.method == "PUT":
        return put(employee, EmployeeSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # employee.delete()
        # return JsonResponse({'message': 'employee was deleted successfully!'}, status=204)


@api_view(['GET', 'POST', 'DELETE'])
def kit(request):
    if request.method == "GET":
        return get_all(Kit, KitSerializerGet)

    elif request.method == "POST":
        return post(KitSerializer, request.data)

    elif request.method == "DELETE":
        pass
        # count = Kit.objects.all().delete()
        # return JsonResponse({'message': '{} kits were deleted successfully!'.format(count[0])}, status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def kit_id(request, id):
    try:
        kit = Kit.objects.get(kit_id=id)
    except Kit.DoesNotExist:
        return JsonResponse({'message': 'The kit does not exist'}, status=404)

    if request.method == "GET":
        return get_one(KitSerializerGet, kit)

    elif request.method == "PUT":
        return put(kit, KitSerializer, request.data)

    elif request.method == "DELETE":
        kit.delete()
        return JsonResponse({'message': 'kit was deleted successfully!'}, status=204)
