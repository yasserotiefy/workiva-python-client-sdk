# ValueFormat

Value Formats. Fields that are omitted will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_format_type** | **str** | The value format type of the content. Setting this property will clear any other ValueFormat properties that are not valid for the new value format type. | [optional] 
**entered_in** | **str** | The scale cell values are entered in. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, and NUMBER. | [optional] 
**shown_in** | **str** | The scale cell values are displayed in. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, and NUMBER. | [optional] 
**precision** | [**ValueFormatPrecision**](ValueFormatPrecision.md) |  | [optional] 
**show_currency_symbol** | **bool** | Render numbers with a currency symbol. Valid for ACCOUNTING and CURRENCY. | [optional] 
**currency_symbol** | [**ValueFormatCurrencySymbol**](ValueFormatCurrencySymbol.md) |  | [optional] 
**percent_symbol** | **str** | Render numbers with a percent symbol. Valid for PERCENT. | [optional] 
**symbol_align** | **str** | Where to render the symbol relative to the value. All values valid for ACCOUNTING and CURRENCY. Left values valid for NUMBER. Right values valid for PERCENT. | [optional] 
**show_leading_zero** | **bool** | Include a leading zero for decimal numbers with no whole number part. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**show_thousands_separator** | **bool** | Render the thousands separator. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**use_parens_for_negatives** | **bool** | Render parentheses around the number instead of a negative symbol. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**show_numbers_as_words** | **bool** | Render the number as words instead of digits. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**display_zero_as** | **str** | The symbol to use for zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. This field controls the symbol to use for zero when not using showNumbersAsWords.  | [optional] 
**numbers_as_words_options** | [**ValueFormatNumbersAsWordsOptions**](ValueFormatNumbersAsWordsOptions.md) |  | [optional] 
**show_sign_rounded_zero** | **bool** | Render the sign on values rounded to zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**show_positive_sign** | **bool** | Render the positive sign on numbers greater than zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. | [optional] 
**date_uppercase_all** | **bool** | Uppercase all characters in the date string. Valid for DATE. | [optional] 
**date_abbreviate_month** | **bool** | Use month abbreviations instead of full month names. Valid for DATE. | [optional] 
**date_format_string** | **str** | Format to use when rendering the date. Valid for DATE. | [optional] 
**period_format** | [**ValueFormatPeriodFormat**](ValueFormatPeriodFormat.md) |  | [optional] 
**prefix** | **str** | Custom prefix value to render in the cell. Valid for ACCOUNTING, CURRENCY, NUMBER, PERCENT, and DATE. | [optional] 
**suffix** | **str** | Custom suffix value to render in the cell. Valid for ACCOUNTING, CURRENCY, NUMBER, PERCENT, and DATE. | [optional] 

## Example

```python
from openapi_client.models.value_format import ValueFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormat from a JSON string
value_format_instance = ValueFormat.from_json(json)
# print the JSON string representation of the object
print(ValueFormat.to_json())

# convert the object into a dict
value_format_dict = value_format_instance.to_dict()
# create an instance of ValueFormat from a dict
value_format_from_dict = ValueFormat.from_dict(value_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


