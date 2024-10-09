# GraphAttachmentUploadResponse

Contains a pre-signed url that can be used to upload an attachment. The Location header also contains a url for an [`Operation`](ref:platform-operations#operation) that can be polled to find out if the upload was successful. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** | The URL to make a PUT request to, to upload the attachment. Include the file content of the attachment as the body of the request. This is a temporary URL; it should be used immediately when the response is received.  | [optional] 

## Example

```python
from openapi_client.models.graph_attachment_upload_response import GraphAttachmentUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphAttachmentUploadResponse from a JSON string
graph_attachment_upload_response_instance = GraphAttachmentUploadResponse.from_json(json)
# print the JSON string representation of the object
print(GraphAttachmentUploadResponse.to_json())

# convert the object into a dict
graph_attachment_upload_response_dict = graph_attachment_upload_response_instance.to_dict()
# create an instance of GraphAttachmentUploadResponse from a dict
graph_attachment_upload_response_from_dict = GraphAttachmentUploadResponse.from_dict(graph_attachment_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


