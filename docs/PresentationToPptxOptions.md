# PresentationToPptxOptions

Optional options to export the presentation as a Microsoft Powerpoint File (.pptx). If no options are provided, all options default to False. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_unused_layout_slides** | **bool** | Whether to include unused layout slides. False by default. | [optional] [default to False]

## Example

```python
from openapi_client.models.presentation_to_pptx_options import PresentationToPptxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationToPptxOptions from a JSON string
presentation_to_pptx_options_instance = PresentationToPptxOptions.from_json(json)
# print the JSON string representation of the object
print(PresentationToPptxOptions.to_json())

# convert the object into a dict
presentation_to_pptx_options_dict = presentation_to_pptx_options_instance.to_dict()
# create an instance of PresentationToPptxOptions from a dict
presentation_to_pptx_options_from_dict = PresentationToPptxOptions.from_dict(presentation_to_pptx_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


