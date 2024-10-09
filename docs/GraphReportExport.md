# GraphReportExport

Details about a graph report export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format to export the graph report to - curently, only .CSV | 

## Example

```python
from openapi_client.models.graph_report_export import GraphReportExport

# TODO update the JSON string below
json = "{}"
# create an instance of GraphReportExport from a JSON string
graph_report_export_instance = GraphReportExport.from_json(json)
# print the JSON string representation of the object
print(GraphReportExport.to_json())

# convert the object into a dict
graph_report_export_dict = graph_report_export_instance.to_dict()
# create an instance of GraphReportExport from a dict
graph_report_export_from_dict = GraphReportExport.from_dict(graph_report_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


