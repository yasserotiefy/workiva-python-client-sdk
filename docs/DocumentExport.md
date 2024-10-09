# DocumentExport

Details about the document export, including its format and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The file format to export the document as. | 
**sections** | **List[str]** | The IDs of the sections of the document to export. Omit to export the entire document. | [optional] 
**pdf_options** | [**DocumentToPdfOptions**](DocumentToPdfOptions.md) |  | [optional] 
**docx_options** | [**DocumentToDocxOptions**](DocumentToDocxOptions.md) |  | [optional] 
**xhtml_options** | [**DocumentToXhtmlOptions**](DocumentToXhtmlOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_export import DocumentExport

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentExport from a JSON string
document_export_instance = DocumentExport.from_json(json)
# print the JSON string representation of the object
print(DocumentExport.to_json())

# convert the object into a dict
document_export_dict = document_export_instance.to_dict()
# create an instance of DocumentExport from a dict
document_export_from_dict = DocumentExport.from_dict(document_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


