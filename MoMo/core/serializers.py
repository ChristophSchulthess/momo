'''
Create API serializers for all models using ModelSerializer.
'''

from rest_framework import serializers
from core.models import (
    Payment,
    PspAdapter,
    PaymentServiceProvider,
    SaasInstance
)

class PaymentSerializer(serializers.ModelSerializer):
    '''
    Serializer for model Payment. At the moment, we do not want to hide specific
    fields, so we include all of them.
    '''
    class Meta:
        model = Payment
        fields = (
            'id',
            'reference_id',
            'amount',
            'date_received',
            'account_id',
            'psp'
        )

    def create(self, data):
        return Payment.objects.create(**data)

class PspAdapterSerializer(serializers.ModelSerializer):
    '''
    Serializer for model PspAdapter
    '''
    class Meta:
        model = PspAdapter
        fields = (
            'id',
            'psp',
            'port',
            'activated'
        )

    def create(self, data):
        return PspAdapter.objects.create(**data)

class PspSerializer(serializers.ModelSerializer):
    '''
    Serializer for model PaymentServiceProvider (PSP)
    '''
    class Meta:
        model = PaymentServiceProvider
        fields = (
            'id',
            'fullname'
        )

    def create(self, data):
        return PaymentServiceProvider.objects.create(**data)

class SaasInstanceSerializer(serializers.ModelSerializer):
    '''
    Serializer for model SaasInstance
    '''
    class Meta:
        model = SaasInstance
        fields = (
            'id',
            'fullname',
            'url'
        )

    def create(self, data):
        return SaasInstance.objects.create(**data)
