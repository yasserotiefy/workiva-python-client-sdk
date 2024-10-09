# GraphAttachment

Details about a graph attachment. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the graph attachment | [optional] [readonly] 
**file_name** | **str** | The filename of the graph attachment | [optional] 

## Example

```python
from openapi_client.models.graph_attachment import GraphAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of GraphAttachment from a JSON string
graph_attachment_instance = GraphAttachment.from_json(json)
# print the JSON string representation of the object
print(GraphAttachment.to_json())

# convert the object into a dict
graph_attachment_dict = graph_attachment_instance.to_dict()
# create an instance of GraphAttachment from a dict
graph_attachment_from_dict = GraphAttachment.from_dict(graph_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


