# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.conf import settings
from seminuevos.sdk.semi_sdk import SDK as SemiApp
from .enums import STATUS_SOLD
from .settings import SM_USER, SM_PASSWORD

# Create your models here.
class SemiAccount(models.Model):
    dealer_id = models.CharField(max_length=150, verbose_name='ID Dealer')
    dealer_user_id = models.CharField(max_length=150, verbose_name='ID Dealer User')

    class Meta:
        verbose_name ='cuenta de seminuevos'
        verbose_name_plural = 'cuentas de seminuevos'

    def __unicode__(self):
        return self.dealer_id
    @property
    def client_id(self):
        return  SM_USER
   
    @property
    def client_secret(self):
        return SM_PASSWORD

    @property
    def client_id(self):
        return  SM_USER
    @property
    def client_secret(self):
        return SM_PASSWORD



    @property
    def user_semiapp(self):
        """
        Create a instance class of SemiApp for use the SDK
        :return: SDK Object
        """
        return SemiApp(
            client_id=self.client_id,
            client_secret=self.client_secret)

    def set_vehicle_sold(self, vehicle_id=None):
        semi_app = self.user_semiapp
        return semi_app.change_vehicle_status(
            vehicle_id=vehicle_id,
            dealer_id=self.dealer_id,
            status_id=STATUS_SOLD)


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = u'País'
        verbose_name_plural = 'Países'

    def info(self):
        return u'%s %s' % (self.id, self.name)

    def __unicode__(self):
        return self.name


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def info(self):
        return u'%s %s - %s' % (self.id, self.name, self.cities.count())

    def __unicode__(self):
        return self.name


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, related_name="cities", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ('name',)

    def info(self):
        return u'(%s %s) %s %s' % (self.state_id, self.state.name, self.id, self.name)

    def __unicode__(self):
        return self.name
