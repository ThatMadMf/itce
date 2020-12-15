from rest_framework import serializers

from Economics.models import AccountAction, CurrencyState, Operation


class CurrencyStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyState
        fields = [
            'name',
            'date',
            'value',
        ]


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['name']


class AccountActionSerializer(serializers.ModelSerializer):
    operation = OperationSerializer(many=False, required=True)
    currency = CurrencyStateSerializer(many=False, required=True)

    class Meta:
        model = AccountAction
        fields = [
            'operation',
            'vat',
            'revs_tax',
            'revenue_tax',
            'money',
            'currency',
            'money_change',
            'vat_value',
            'tax_value',
        ]
