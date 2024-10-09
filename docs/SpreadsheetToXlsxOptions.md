# SpreadsheetToXlsxOptions

Optional options to export the spreadsheet as a Microsoft Excel (.XLSX) file. If no options are provided, `exportAsFormulas` defaults to False, and `exportPrecision` defaults to `fullPrecision`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_precision** | **str** | How to export values in the sheet when exporting to .XLSX \&quot;fullPrecision\&quot; by default.  | [optional] [default to 'fullPrecision']
**export_as_formulas** | **bool** | Whether to export cells that contain formulas as the formula or its result when exporting to .XLSX. False by default. | [optional] [default to False]

## Example

```python
from openapi_client.models.spreadsheet_to_xlsx_options import SpreadsheetToXlsxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetToXlsxOptions from a JSON string
spreadsheet_to_xlsx_options_instance = SpreadsheetToXlsxOptions.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetToXlsxOptions.to_json())

# convert the object into a dict
spreadsheet_to_xlsx_options_dict = spreadsheet_to_xlsx_options_instance.to_dict()
# create an instance of SpreadsheetToXlsxOptions from a dict
spreadsheet_to_xlsx_options_from_dict = SpreadsheetToXlsxOptions.from_dict(spreadsheet_to_xlsx_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


