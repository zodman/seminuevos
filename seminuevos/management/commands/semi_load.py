# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from seminuevos.sdk.semi_sdk import SDK
from seminuevos.utils import json_process
from seminuevos.models import Country, State, City

import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Start load data'
    # def add_arguments(self, parser):
    #     parser.add_argument('origin', type=str)
    #     parser.add_argument('destiny', type=str)

    def handle(self, *args, **options):
        logger.info('start')
        seminuevos = SDK()
        country_id = getattr(settings, 'SEMINUEVOS_COUNTRY_ID', 1)
        country_name = getattr(settings, 'SEMINUEVOS_COUNTRY_NAME', 'México')

        country = Country()
        country.id = country_id
        country.name = country_name
        country.save()
        resp = seminuevos.catalog('provinces').json()
        states = json_process(resp['data'])

        for state_data in states:
            state = State()
            state.id = state_data.id
            state.name = state_data.name
            state.country = country
            state.save()

        resp = seminuevos.catalog('cities').json()
        cities = json_process(resp['data'])
        for city_data in cities:
            city = City()
            city.name = city_data.name
            city.id = city_data.id
            city.state = State.objects.get(id=city_data.idProvince)
            city.save()

        logger.info('done!')
