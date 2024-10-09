# ValueFormatPeriodFormat

Options for formatting a duration string. Valid for PERIOD

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | Method of displaying the period value | 
**separator** | **str** | The separator to use between denominations if multiple are displayed | [optional] [default to 'COMMA']
**precision** | **int** | Precision to use when rounding decimal numbers for display. Renders with automatic precision if null. | [optional] 
**show_labels** | **bool** | Render a label after each denomination | [optional] [default to True]
**show_numbers_as_words** | **bool** | Render the numbers as words instead of digits | [optional] [default to False]
**capitalize_first_word** | **bool** | Capitalize the first word | [optional] [default to False]

## Example

```python
from openapi_client.models.value_format_period_format import ValueFormatPeriodFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormatPeriodFormat from a JSON string
value_format_period_format_instance = ValueFormatPeriodFormat.from_json(json)
# print the JSON string representation of the object
print(ValueFormatPeriodFormat.to_json())

# convert the object into a dict
value_format_period_format_dict = value_format_period_format_instance.to_dict()
# create an instance of ValueFormatPeriodFormat from a dict
value_format_period_format_from_dict = ValueFormatPeriodFormat.from_dict(value_format_period_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


