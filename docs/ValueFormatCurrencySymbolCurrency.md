# ValueFormatCurrencySymbolCurrency

An ISO currency format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The ISO currency identifier | 
**display** | **str** | How to display the currency. CODE simply displays the ISO currency code while SYMBOL displays the corresponding currency symbol. For codes where we support two different symbols, SYMBOL and SYMBOL2 display as follows:   | code | SYMBOL | SYMBOL2 |   | ---- | ------ | ------- |   | INR  | ₹      | Rs      |   | RSD  | дин    | din     |   | UAH  | ₴      | грн     |  | 

## Example

```python
from openapi_client.models.value_format_currency_symbol_currency import ValueFormatCurrencySymbolCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormatCurrencySymbolCurrency from a JSON string
value_format_currency_symbol_currency_instance = ValueFormatCurrencySymbolCurrency.from_json(json)
# print the JSON string representation of the object
print(ValueFormatCurrencySymbolCurrency.to_json())

# convert the object into a dict
value_format_currency_symbol_currency_dict = value_format_currency_symbol_currency_instance.to_dict()
# create an instance of ValueFormatCurrencySymbolCurrency from a dict
value_format_currency_symbol_currency_from_dict = ValueFormatCurrencySymbolCurrency.from_dict(value_format_currency_symbol_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


