# SpreadsheetToCsvOptions

Optional options to export the spreadsheet as a comma-separated values (.CSV) file. If no options are provided, `exportAsFormulas` defaults to False.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_as_formulas** | **bool** | Whether to export cells containing formulas as the formula or the formula result. False by default. | [optional] [default to False]

## Example

```python
from openapi_client.models.spreadsheet_to_csv_options import SpreadsheetToCsvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetToCsvOptions from a JSON string
spreadsheet_to_csv_options_instance = SpreadsheetToCsvOptions.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetToCsvOptions.to_json())

# convert the object into a dict
spreadsheet_to_csv_options_dict = spreadsheet_to_csv_options_instance.to_dict()
# create an instance of SpreadsheetToCsvOptions from a dict
spreadsheet_to_csv_options_from_dict = SpreadsheetToCsvOptions.from_dict(spreadsheet_to_csv_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


