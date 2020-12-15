export const ACTION_TABLE_COLUMNS = [
    {
        title: 'Наименование операции',
        key: 'operation',
        dataIndex: 'operation.name',
    },
    {
        title: 'Дата',
        key: 'currencyDate',
        dataIndex: 'currency.date',
    },
    {
        title: 'НДС',
        key: 'vat',
        dataIndex: 'vat',
    },
    {
        title: 'Налог с оборота',
        key: 'revsTax',
        dataIndex: 'revsTax',
    },
    {
        title: 'Налог на прибыль',
        key: 'revenueTax',
        dataIndex: 'revenueTax',
    },
    {
        title: 'Деньги',
        key: 'money',
        dataIndex: 'money',
    },
    {
        title: 'Поступление',
        key: 'additions',
        dataIndex: 'additions',
    },
    {
        title: 'Списано',
        key: 'subtractions',
        dataIndex: 'subtractions',
    },
    {
        title: 'Валюта',
        key: 'currencyName',
        dataIndex: 'currency.name',
    },
    {
        title: 'Курс',
        key: 'currencyValue',
        dataIndex: 'currency.value',
    },
    {
        title: 'НДС',
        key: 'vatValue',
        dataIndex: 'vat_value',
    },
    {
        title: 'Налог с оборота',
        key: 'taxValue',
        dataIndex: 'tax_value',
    },
    {
        title: 'Доход/затраты',
        key: 'moneyChange',
        dataIndex: 'money_change',
    },
]