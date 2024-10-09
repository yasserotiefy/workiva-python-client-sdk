# FileImportResponse

Response to a file import including the URL to upload the file to. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** | The signed URL used to upload the file. Make a PUT request to this URL whose body is the contents of the file to upload. | [optional] 

## Example

```python
from openapi_client.models.file_import_response import FileImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileImportResponse from a JSON string
file_import_response_instance = FileImportResponse.from_json(json)
# print the JSON string representation of the object
print(FileImportResponse.to_json())

# convert the object into a dict
file_import_response_dict = file_import_response_instance.to_dict()
# create an instance of FileImportResponse from a dict
file_import_response_from_dict = FileImportResponse.from_dict(file_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


