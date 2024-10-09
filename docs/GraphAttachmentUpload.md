# GraphAttachmentUpload

Details about a graph attachment upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The file name of the graph attachment | [optional] 

## Example

```python
from openapi_client.models.graph_attachment_upload import GraphAttachmentUpload

# TODO update the JSON string below
json = "{}"
# create an instance of GraphAttachmentUpload from a JSON string
graph_attachment_upload_instance = GraphAttachmentUpload.from_json(json)
# print the JSON string representation of the object
print(GraphAttachmentUpload.to_json())

# convert the object into a dict
graph_attachment_upload_dict = graph_attachment_upload_instance.to_dict()
# create an instance of GraphAttachmentUpload from a dict
graph_attachment_upload_from_dict = GraphAttachmentUpload.from_dict(graph_attachment_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


