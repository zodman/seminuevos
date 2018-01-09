__author__ = 'sergio'
from .enums import *
from argparse import Namespace
import json


class ItemCar(object):
    dic_base = data

    def __init__(self, city_id, state_id, subtype_id, model_id, year, price, mileage, color, aic=False, is_auto=False):
        self.dic_base.update({
            'cityId': city_id,
            'provinceId': state_id,
            'subtypeId': subtype_id,
            'modelId': model_id,
            'builtYear': year,
            'price': price,
            'mileage': mileage,
            'colorId': color,
            'heatingSystemId': WITH_AIRCOND if aic else WITHOUT_AIRCOND,
            'transmissionId': AUTO if is_auto else MANUAL,
        })

    def set(self, key, value):
        return key, value

    def set_dealer(self, dealer_id=4643, user_id=780927):
        self.dic_base.update({
            "dealerId": dealer_id,
            "dealerUserId": user_id,
        })

    def set_provider(self, provider=None):
        if provider:
            self.dic_base['provider'] = provider

    def get_data(self):
        return self.dic_base


def json_process(json_data):
    return json.loads(
        json.dumps(json_data),
        object_hook=lambda d: Namespace(**d)
    )
