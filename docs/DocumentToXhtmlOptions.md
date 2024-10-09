# DocumentToXhtmlOptions

Optional options to export the document as .XHTML. If no options are provided, `editableXhtml` will be true and all other options will be false. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_external_hyperlinks** | **bool** | Whether to include external hyperlinks when exporting to .XHTML. False by default. | [optional] [default to False]
**include_headers_and_footers** | **bool** | Whether to include the headers and footers when exporting to .XHTML. False by default. | [optional] [default to False]
**editable_xhtml** | **bool** | Whether the resulting XHTML is editable when exporting to .XHTML. False by default. If set to true, other options must be false. When exporting XHTML that you plan to edit or modify, use this option. Otherwise, the export retains fidelity so it visually matches the document as it appears in the browser.  | [optional] [default to False]
**editable_simple** | **bool** | Whether to produce simplified editable XHTML. This option produces editable XHTML that is simpler than the  editableXHTML option. Use this option when you only need the textual and numeric content of a document, but not  any of the images or complex formatting. When this option is true, all other XHTML export options must be false.  | [optional] [default to False]

## Example

```python
from openapi_client.models.document_to_xhtml_options import DocumentToXhtmlOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentToXhtmlOptions from a JSON string
document_to_xhtml_options_instance = DocumentToXhtmlOptions.from_json(json)
# print the JSON string representation of the object
print(DocumentToXhtmlOptions.to_json())

# convert the object into a dict
document_to_xhtml_options_dict = document_to_xhtml_options_instance.to_dict()
# create an instance of DocumentToXhtmlOptions from a dict
document_to_xhtml_options_from_dict = DocumentToXhtmlOptions.from_dict(document_to_xhtml_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


