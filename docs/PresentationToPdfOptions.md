# PresentationToPdfOptions

Optional options to export the presentation as a portable document file (.PDF). If no options are provided, all options default to False. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_hyperlinks** | **bool** | Whether to include hyperlinks when exporting to .PDF. False by default. | [optional] [default to False]
**include_leader_dots** | **bool** | Whether to include leader dots when exporting to .PDF. False by default. | [optional] [default to False]
**include_alternate_row_fill** | **bool** | Whether to include alternate row fill in the presentation&#39;s tables when exporting to .PDF. False by default. | [optional] [default to False]
**tag_for_web_accessibility** | **bool** | Whether to tag for web accessibility when exporting to .PDF. False by default. | [optional] [default to False]
**use_cmyk_colorspace** | **bool** | Whether to use CMYK colorspace when exporting to .PDF. False by default. | [optional] [default to False]
**include_draft_watermark** | **bool** | Whether to include a \&quot;Draft\&quot; watermark when exporting to .PDF. False by default. | [optional] [default to False]
**include_comments** | **bool** | Whether to include comments when exporting to .PDF. False by default. When True, all comments are included, even those already resolved. | [optional] [default to False]

## Example

```python
from openapi_client.models.presentation_to_pdf_options import PresentationToPdfOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationToPdfOptions from a JSON string
presentation_to_pdf_options_instance = PresentationToPdfOptions.from_json(json)
# print the JSON string representation of the object
print(PresentationToPdfOptions.to_json())

# convert the object into a dict
presentation_to_pdf_options_dict = presentation_to_pdf_options_instance.to_dict()
# create an instance of PresentationToPdfOptions from a dict
presentation_to_pdf_options_from_dict = PresentationToPdfOptions.from_dict(presentation_to_pdf_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

