from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Economics.models import Expense, AccountAction
from Economics.serializers import AccountActionSerializer


class Estimates(APIView):

    def get_db(self, short_name):
        return Expense.objects.get(short_name__exact=short_name).value

    amount = Expense.objects.get(short_name__exact='СырьеКоличество').value
    price = Expense.objects.get(short_name__exact='СырьеЦена').value
    exp_service = Expense.objects.get(short_name__exact='УслугиЭксп').value
    rate = Expense.objects.get(short_name__exact='Курс').value
    customs_exp = Expense.objects.get(short_name__exact='ТаможРасходы').value
    bank_exp = Expense.objects.get(short_name__exact='БанкРасходы').value
    percent = Expense.objects.get(short_name__exact='ПроцентКредит').value
    rate_nsd = Expense.objects.get(short_name__exact='СтавкаНСД').value
    rate_tax = Expense.objects.get(short_name__exact='НалогОборот').value
    rate_tax_income = Expense.objects.get(short_name__exact='СтавкаНалогПрибыль').value

    def calc_expenses(self, impl):

        field_11 = self.amount * self.price
        field_12 = self.amount * self.exp_service
        field_13 = self.amount * Decimal(impl)
        field_14 = field_13 * self.rate * self.customs_exp
        field_15 = field_13 * self.rate * self.bank_exp
        field_16 = field_13 * self.rate - field_15
        field_17 = field_11 + field_12 + field_14
        field_18 = field_17 * self.percent
        field_19 = (field_11 + field_12) * self.rate_nsd / (1 + self.rate_nsd)
        field_20 = field_16 - field_17 - field_18
        field_26 = field_11 + field_12 + field_14 + field_15 + field_18 - field_19
        field_27 = -(field_13 * self.rate * self.rate_tax)
        field_28 = field_13 * self.rate - field_26 + field_27
        field_29 = -(field_28 * self.rate_tax_income)
        field_31 = field_27 + field_29
        field_33 = field_20 + field_19 + field_31

        return {
            'Приобретение товара': round(field_11),
            'Оплата услуг экпедиторов': round(field_12),
            'Стоимость реализации': round(field_13),
            'Таможеные расходы': round(field_14),
            'Оплата банковских услуг': round(field_15),
            'Поступление денежных средств': round(field_16),
            'Получение кредита': round(field_17),
            'Проценты по кредиту': round(field_18),
            'Возмещение процентного НДС': round(field_19),
            'Остаток денежных средств': round(field_20),
            'Затраты (без НДС)': round(field_26),
            'Налог с оборота': round(field_27),
            'Прибыль до налогообложения': round(field_28),
            'Налог на прибыль': round(field_29),
            'Налоги': round(field_31),
            'Всего остаток ДС': round(field_33),
        }

    def get(self, request):
        calc_imp = request.GET.get('max-sale')
        zero_profitability = request.GET.get('zero-profitability')

        if calc_imp is not None:
            for i in range(100000000):
                result = self.calc_expenses(i / 100)
                if result.get('Остаток денежных средств') > 0:
                    result['Цена реализации 1 тонны сырья($)'] = i / 100
                    return Response(result, status.HTTP_200_OK)

        if zero_profitability is not None:
            for i in range(100000000):
                result = self.calc_expenses(i / 100)
                if result.get('Прибыль до налогообложения') > 0:
                    result['Цена реализации 1 тонны сырья($)'] = i / 100
                    return Response(result, status.HTTP_200_OK)

        impl = self.get_db('СырьеРеализация')

        return Response(self.calc_expenses(impl), status.HTTP_200_OK)


class ActionList(APIView):
    model = AccountAction
    serializer = AccountActionSerializer

    def get(self, request):
        data = self.model.objects.all()
        serializer = self.serializer(instance=data, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
