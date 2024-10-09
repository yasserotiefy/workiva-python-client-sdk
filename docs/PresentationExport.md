# PresentationExport

Details about the presentation export, including its format and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The file format to export the presentation as - .PDF or .PPTX. | 
**slides** | **List[str]** | The IDs of the slides of the presentation to export. Omit to export the entire presentation. | [optional] 
**pdf_options** | [**PresentationToPdfOptions**](PresentationToPdfOptions.md) |  | [optional] 
**pptx_options** | [**PresentationToPptxOptions**](PresentationToPptxOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.presentation_export import PresentationExport

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationExport from a JSON string
presentation_export_instance = PresentationExport.from_json(json)
# print the JSON string representation of the object
print(PresentationExport.to_json())

# convert the object into a dict
presentation_export_dict = presentation_export_instance.to_dict()
# create an instance of PresentationExport from a dict
presentation_export_from_dict = PresentationExport.from_dict(presentation_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


