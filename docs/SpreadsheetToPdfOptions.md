# SpreadsheetToPdfOptions

Optional options to export the spreadsheet as a portable document file (.PDF). If no options are provided, all options default to False except:   - `pageHeight`, which defaults to 11   - `pageWidth`, which defaults to 8.5   - `pageOrientation`, which defaults to \"portrait\"   - `pageScale`, which defaults to \"actualSize\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_hyperlinks** | **bool** | Whether to include hyperlinks when exporting to .PDF. False by default. | [optional] [default to False]
**include_leader_dots** | **bool** | Whether to include leader dots when exporting to .PDF. False by default. | [optional] [default to False]
**show_cell_fills** | **bool** | Whether to show cell fills when exporting to .PDF. False by default. | [optional] [default to False]
**show_gridlines** | **bool** | Whether to show gridlines when exporting to .PDF. False by default. | [optional] [default to False]
**use_cmyk_colorspace** | **bool** | Whether to use CMYK colorspace when exporting to .PDF. False by default. | [optional] [default to False]
**include_draft_watermark** | **bool** | Whether to include draft watermark when exporting to .PDF. False by default. | [optional] [default to False]
**include_comments** | **bool** | Whether to include comments when exporting to .PDF False by default. | [optional] [default to False]
**include_track_changes** | **bool** | Whether to include track changes when exporting to .PDF. False by default. | [optional] [default to False]
**only_export_print_areas** | **bool** | Whether to only export print areas when exporting to .PDF. False by default. | [optional] [default to False]
**page_height** | **float** | The height of the exported .PDF, in inches. 11 by default. | [optional] [default to 11]
**page_width** | **float** | The width of the exported .PDF, in inches. 8.5 by default. | [optional] [default to 8.5]
**page_orientation** | **str** | The orientation of the exported .PDF, such as \&quot;portrait\&quot; or \&quot;landscape\&quot;. \&quot;portrait\&quot; by default.  | [optional] [default to 'portrait']
**page_scale** | **str** | The scale of the exported .PDF. \&quot;actualSize\&quot; by default. | [optional] [default to 'actualSize']

## Example

```python
from openapi_client.models.spreadsheet_to_pdf_options import SpreadsheetToPdfOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetToPdfOptions from a JSON string
spreadsheet_to_pdf_options_instance = SpreadsheetToPdfOptions.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetToPdfOptions.to_json())

# convert the object into a dict
spreadsheet_to_pdf_options_dict = spreadsheet_to_pdf_options_instance.to_dict()
# create an instance of SpreadsheetToPdfOptions from a dict
spreadsheet_to_pdf_options_from_dict = SpreadsheetToPdfOptions.from_dict(spreadsheet_to_pdf_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


