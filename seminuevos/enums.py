
#Country
MX = 1


FORTE = 15583
OPTIMA = 15781
RIO = 15507
SORENTO = 15619
SOUL = 15828
SPORTAGE = 14789
# Modelos
# {u'id': 15583, u'name': u'Forte'},
# {u'id': 15781, u'name': u'OPTIMA'},
# {u'id': 15507, u'name': u'Rio'},
# {u'id': 15619, u'name': u'Sorento'},
# {u'id': 15828, u'name': u'soul ex'},
# {u'id': 14789, u'name': u'Sportage'}],
MODELS_KIA = (
    (FORTE, "FORTE",),
    (OPTIMA, "OPTIMA"),
    (RIO, "RIO"),
    (SORENTO, 'SORENTO'),
    (SOUL, "SOUL"),
    (SPORTAGE, "SPORTAGE"),
)

MODELS_OPTIONS_SEMINUEVOS=MODELS_KIA

DF = 1
NL = 2
JAL = 3
TYPE_AUTO = 1
SUV = 12
HS_3 = 9
HS_5 = 10
AUTOS = 1
KIA_BRAND = 1466
SEDAN = 1
# Subtypes
# {u'id': 12, u'name': u'Camioneta SUV'},
# {u'id': 9, u'name': u'Hatchback (3 Puertas)'},
# {u'id': 10, u'name': u'Hatchback (5 Puertas)'},
# {u'id': 1, u'name': u'Sed\xe1n'},
SUBID_KIA = (
    (SUV, "SUV"),
    (HS_3, "HATCHBACK 3P"),
    (HS_5, "HATCHBACK 5P"),
    (SEDAN, "SEDAN"),
)

# negotiable Indica si es precio fijo o negociable o financiado o plan ahorro, 1 es fijo, 2 es negociable, 3 si es financiado, 4 si es plan de ahorro
NEGOTIABLE = 1
# adSectionIndica si un vehiculo es nuevo o usado, el valor 1 significa nuevo, el valor 2 significa usado
ADSECTION = 1


# MILEAGE TYPE {u'id': 1, u'name': u'Kms.'},
MILEAGE_TYPE = 1
# direccion steering {u'id': 1, u'idType': 1, u'name': u'N/A'}
STEERING = 1
CC = 1


# drives {u'id': 1, u'idType': 1, u'name': u'N/A'},
# 4x4 6x9
DRIVE = 1

# TRANSMISION
#           {u'id': 5, u'idType': 1, u'name': u'Autom\xe1tica'},
#           {u'id': 6, u'idType': 1, u'name': u'Manual'},

AUTO = 5
MANUAL = 6
# gasolina {u'id': 1, u'idType': 1, u'name': u'N/A'},
FUEL= 1
# heating aire
# {u'id': 1, u'idType': 1, u'name': u'N/A'},
# {u'id': 2, u'idType': 1, u'name': u'Aire Acondicionado'},
#{u'id': 7, u'idType': 1, u'name': u'Ninguno'},

WITH_AIRCOND = 2
WITHOUT_AIRCOND = 7

# data = {
#     # 1 DF  NL 2 GDL/jalisco 3
#     'provinceId': DF,
#     'subtypeId': SEDAN,
#     'modelId': FORTE,
#     'builtYear': 1,
#     'price': 1,
#     'mileage': 1000,
#     "colorId": 1,
#     "heatingSystemId": WITH_AIRCOND,
#     "transmissionId": AUTO,
#     "cityId": 1,
#     # FIXED =====================
#     'brandId': KIA_BRAND,
#     'negotiable': NEGOTIABLE,
#     'adSection': ADSECTION,
#     # CILINDRAJE DEL VEHICULO 4,6,8
#     'mileageTypeId': MILEAGE_TYPE,
#     'cc': CC,
#     'steeringId': STEERING,
#     "driveId": DRIVE,
#     "fuelId": FUEL,
#     # FIJOS
#     # Tipos carros 1
#     'typeId': TYPE_AUTO,
#     # ventanas
#     "windowId": 1,
#     # interiores plastico tela piel{u'id': 1, u'idType': 1, u'name': u'N/A'},
#     "interiorId": 1,
#     # pemdiente MXN
#     "currencyId": 1,
#     # FIXED for demo
#     "dealerId": 4643,
#     "dealerUserId": 780927,
#     "provider": "testAccount",
#     # FIXED
#     "extras": [],
#     "specialExtras": [],
#     "specialTypes": []
# }

data = {
    "cityId": 1,
    "provinceId": DF,
    "subtypeId": SEDAN,
    "modelId": FORTE,
    "builtYear": 2017,
    "price": 369000,
    "mileage": 25000,
    "colorId": 4,
    "heatingSystemId": WITH_AIRCOND,
    "transmissionId": AUTO,
    # FIJO
    "typeId": 1,
    "cc": 1,
    "steeringId": 1,
    "dealerUserId": 780927,
    "adSection": 1,
    "negotiable": 1,
    "interiorId": 1,
    "currencyId": 1,
    "mileageTypeId": 1,
    "provider": "testAccount",
    "brandId": 1466,
    "windowId": 1,
    "fuelId": 1,
    "dealerId": 4643,
    "driveId": 1,
    "extras": [1, 2],
    "specialExtras": [1, 2, 3]
}

STATUS_PUBLISHED = 1
STATUS_SOLD = 2
STATUS_PENDING = 3
STATUS_SUSPENDED = 4
STATUS_DELETED = 5
STATUS_GARBAGE = 6
