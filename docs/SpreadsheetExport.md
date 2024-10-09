# SpreadsheetExport

Details about a spreadsheet export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The file format to export the spreadsheet as. | 
**sheets** | **List[str]** | The IDs of the sheets within the spreadsheet to export. Omit to export the entire spreadsheet.  Note: When exporting to .CSV, you can export only the entire spreadsheet or a single sheet. When exporting the entire spreadsheet, the resulting file is a .ZIP of .CSV files, with one .CSV file per sheet. | [optional] 
**xlsx_options** | [**SpreadsheetToXlsxOptions**](SpreadsheetToXlsxOptions.md) |  | [optional] 
**pdf_options** | [**SpreadsheetToPdfOptions**](SpreadsheetToPdfOptions.md) |  | [optional] 
**csv_options** | [**SpreadsheetToCsvOptions**](SpreadsheetToCsvOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.spreadsheet_export import SpreadsheetExport

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetExport from a JSON string
spreadsheet_export_instance = SpreadsheetExport.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetExport.to_json())

# convert the object into a dict
spreadsheet_export_dict = spreadsheet_export_instance.to_dict()
# create an instance of SpreadsheetExport from a dict
spreadsheet_export_from_dict = SpreadsheetExport.from_dict(spreadsheet_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


