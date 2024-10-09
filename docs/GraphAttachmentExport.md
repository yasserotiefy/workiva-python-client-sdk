# GraphAttachmentExport

Details about the attachment export including its format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format to export the attachment to — currently, .PDF only | [optional] 

## Example

```python
from openapi_client.models.graph_attachment_export import GraphAttachmentExport

# TODO update the JSON string below
json = "{}"
# create an instance of GraphAttachmentExport from a JSON string
graph_attachment_export_instance = GraphAttachmentExport.from_json(json)
# print the JSON string representation of the object
print(GraphAttachmentExport.to_json())

# convert the object into a dict
graph_attachment_export_dict = graph_attachment_export_instance.to_dict()
# create an instance of GraphAttachmentExport from a dict
graph_attachment_export_from_dict = GraphAttachmentExport.from_dict(graph_attachment_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


