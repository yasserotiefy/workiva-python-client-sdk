# GraphAttachmentsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`GraphAttachment`](ref:platform-testforms#graphattachment) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GraphAttachment]**](GraphAttachment.md) | A list of &#x60;GraphAttachment&#x60; objects | 
**next_link** | **str** | The pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.graph_attachments_list_result import GraphAttachmentsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of GraphAttachmentsListResult from a JSON string
graph_attachments_list_result_instance = GraphAttachmentsListResult.from_json(json)
# print the JSON string representation of the object
print(GraphAttachmentsListResult.to_json())

# convert the object into a dict
graph_attachments_list_result_dict = graph_attachments_list_result_instance.to_dict()
# create an instance of GraphAttachmentsListResult from a dict
graph_attachments_list_result_from_dict = GraphAttachmentsListResult.from_dict(graph_attachments_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


