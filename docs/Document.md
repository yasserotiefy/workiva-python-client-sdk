# Document

Details about the document, including its ID, name, and milestone dates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the document | [optional] [readonly] 
**name** | **str** | Name of the document | [optional] [readonly] 
**template** | **bool** | Whether the document is a template | [optional] [readonly] 
**created** | [**Action**](Action.md) |  | [optional] 
**modified** | [**Action**](Action.md) |  | [optional] 
**sections** | [**List[Section]**](Section.md) | An array of information about the sections in the document. Included in the response only when the $expand query parameter is provided.  | [optional] [readonly] 

## Example

```python
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


