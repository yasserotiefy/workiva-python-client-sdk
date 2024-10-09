# FileImport

Details about a file import including the file name and target kind. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the file to upload. Supported extensions include .XLSX, .CSV, .DOCX, .PPTX, .VSDX. | [optional] 
**kind** | **str** | The Workiva file type to upload to. (Document, Spreadsheet, Presentation) | [optional] 

## Example

```python
from openapi_client.models.file_import import FileImport

# TODO update the JSON string below
json = "{}"
# create an instance of FileImport from a JSON string
file_import_instance = FileImport.from_json(json)
# print the JSON string representation of the object
print(FileImport.to_json())

# convert the object into a dict
file_import_dict = file_import_instance.to_dict()
# create an instance of FileImport from a dict
file_import_from_dict = FileImport.from_dict(file_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


