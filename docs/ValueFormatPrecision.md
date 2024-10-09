# ValueFormatPrecision

Precision to use when rounding numbers for display. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, NUMBER, and PERCENT.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | **bool** | Render with automatic precision based on the value in the cell | [optional] [default to False]
**value** | **int** | Explicit precision value to use. Required unless auto is true. | [optional] 

## Example

```python
from openapi_client.models.value_format_precision import ValueFormatPrecision

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormatPrecision from a JSON string
value_format_precision_instance = ValueFormatPrecision.from_json(json)
# print the JSON string representation of the object
print(ValueFormatPrecision.to_json())

# convert the object into a dict
value_format_precision_dict = value_format_precision_instance.to_dict()
# create an instance of ValueFormatPrecision from a dict
value_format_precision_from_dict = ValueFormatPrecision.from_dict(value_format_precision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


