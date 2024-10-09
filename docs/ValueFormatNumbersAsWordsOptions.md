# ValueFormatNumbersAsWordsOptions

Options relevant when showing numbers as words. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. In order for these options to take effect showNumbersAsWords must be set to true. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capitalize_first_word** | **bool** | Capitalize the first word. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] [default to False]
**display_zero_as** | **str** | The word to use for zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] [default to 'ZERO']

## Example

```python
from openapi_client.models.value_format_numbers_as_words_options import ValueFormatNumbersAsWordsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormatNumbersAsWordsOptions from a JSON string
value_format_numbers_as_words_options_instance = ValueFormatNumbersAsWordsOptions.from_json(json)
# print the JSON string representation of the object
print(ValueFormatNumbersAsWordsOptions.to_json())

# convert the object into a dict
value_format_numbers_as_words_options_dict = value_format_numbers_as_words_options_instance.to_dict()
# create an instance of ValueFormatNumbersAsWordsOptions from a dict
value_format_numbers_as_words_options_from_dict = ValueFormatNumbersAsWordsOptions.from_dict(value_format_numbers_as_words_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


