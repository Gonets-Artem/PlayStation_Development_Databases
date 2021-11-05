from django.db import models


class Designer(models.Model):
    designer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)


class Design(models.Model):
    design_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    colour = models.CharField(max_length=20)
    style = models.CharField(max_length=30)
    status = models.BooleanField()

    designers = models.ManyToManyField(Designer)


class Dualshock(models.Model):
    dualshock_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    connection_type = models.CharField(max_length=30)
    compatibility = models.CharField(max_length=60)
    weight = models.FloatField()
    colour = models.CharField(max_length=30)
    action_radius = models.FloatField()
    battery_power = models.FloatField()


class PSVR(models.Model):
    ps_vr_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    type_display = models.CharField(max_length=30)
    diagonal = models.FloatField()
    permission = models.FloatField()
    viewing_angle = models.FloatField()


class Developer(models.Model):
    developer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)


class Software(models.Model):
    software_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    version = models.CharField(max_length=15)
    status = models.BooleanField()

    developers = models.ManyToManyField(Developer)


class FormFactor(models.Model):
    form_factor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    form = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()


class Prototype(models.Model):
    prototype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()
    consumption = models.FloatField()
    ssd_type = models.CharField(max_length=30)
    type_storage_device = models.CharField(max_length=30)
    specifications = models.CharField(max_length=200)

    softwares = models.ManyToManyField(Software)
    form_factors = models.ManyToManyField(FormFactor)


class Console(models.Model):
    console_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()
    weight = models.FloatField()
    ram = models.IntegerField()
    rom = models.IntegerField()

    prototype = models.ForeignKey(Prototype, on_delete=models.CASCADE)


class AdvertisingDepartment(models.Model):
    advertising_department_id = models.AutoField(primary_key=True)
    contacts = models.CharField(max_length=50)


class Investor(models.Model):
    investor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    advertising_department = models.ForeignKey(AdvertisingDepartment, on_delete=models.CASCADE)


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    evaluation = models.SmallIntegerField()
    path_comment = models.CharField(max_length=50)


class TargetAudience(models.Model):
    # target_audience_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    # feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    feedback = models.OneToOneField(Feedback, on_delete=models.CASCADE, primary_key=True)


class PRManager(models.Model):
    pr_manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    advertising_department = models.ForeignKey(AdvertisingDepartment, on_delete=models.CASCADE)

    feedbacks = models.ManyToManyField(Feedback)


class Competitor(models.Model):
    competitor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class MarketAnalysis(models.Model):
    market_analysis_id = models.AutoField(primary_key=True)
    quality = models.SmallIntegerField()
    predicted_price = models.FloatField()
    potential = models.CharField(max_length=50)

    competitors = models.ManyToManyField(Competitor)


class ProductManager(models.Model):
    product_manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    advertising_department = models.ForeignKey(AdvertisingDepartment, on_delete=models.CASCADE)

    market_analysises = models.ManyToManyField(MarketAnalysis)


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    specifications = models.CharField(max_length=200)


class StorageRoom(models.Model):
    storage_room_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    capacity = models.CharField(max_length=200)

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


class Component(models.Model):
    component_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    storage_room = models.ForeignKey(StorageRoom, on_delete=models.CASCADE)


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    components = models.ManyToManyField(Component)


class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


class EquipmentCondition(models.Model):
    # equipment_condition_id = models.AutoField(primary_key=True)
    service_ability = models.BooleanField()
    noise_level = models.FloatField()
    temperature = models.FloatField()
    wear_level = models.FloatField()
    errors_number = models.IntegerField()

    # equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    equipments = models.ManyToManyField(Equipment)


class Kit(models.Model):
    kit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()

    advertising_department = models.ForeignKey(AdvertisingDepartment, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    # dualshock = models.ForeignKey(Dualshock, on_delete=models.CASCADE, null=True)
    # psvr = models.ForeignKey(PSVR, on_delete=models.CASCADE, null=True)
    dualshock = models.OneToOneField(Dualshock, on_delete=models.CASCADE, null=True)
    psvr = models.OneToOneField(PSVR, on_delete=models.CASCADE, null=True)