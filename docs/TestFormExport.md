# TestFormExport

Describes parameters for exporting a test form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format to export the test form to—currently, only .XLSX | [optional] 

## Example

```python
from openapi_client.models.test_form_export import TestFormExport

# TODO update the JSON string below
json = "{}"
# create an instance of TestFormExport from a JSON string
test_form_export_instance = TestFormExport.from_json(json)
# print the JSON string representation of the object
print(TestFormExport.to_json())

# convert the object into a dict
test_form_export_dict = test_form_export_instance.to_dict()
# create an instance of TestFormExport from a dict
test_form_export_from_dict = TestFormExport.from_dict(test_form_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


