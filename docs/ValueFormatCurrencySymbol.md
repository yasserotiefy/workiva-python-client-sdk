# ValueFormatCurrencySymbol

The currency symbol to display. Valid for ACCOUNTING and CURRENCY. Either generic or currency should be set, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic** | **str** | Generic currency options | [optional] 
**currency** | [**ValueFormatCurrencySymbolCurrency**](ValueFormatCurrencySymbolCurrency.md) |  | [optional] 

## Example

```python
from openapi_client.models.value_format_currency_symbol import ValueFormatCurrencySymbol

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormatCurrencySymbol from a JSON string
value_format_currency_symbol_instance = ValueFormatCurrencySymbol.from_json(json)
# print the JSON string representation of the object
print(ValueFormatCurrencySymbol.to_json())

# convert the object into a dict
value_format_currency_symbol_dict = value_format_currency_symbol_instance.to_dict()
# create an instance of ValueFormatCurrencySymbol from a dict
value_format_currency_symbol_from_dict = ValueFormatCurrencySymbol.from_dict(value_format_currency_symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


