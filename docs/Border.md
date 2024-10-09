# Border

The type of border that should be applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**style** | **str** | The type of border to apply | 
**weight** | **float** | The thickness of the border, in points. Rounded to the nearest hundredth. | [optional] [default to 1]
**color** | **str** | A hex color code | [optional] [default to '#000000']

## Example

```python
from openapi_client.models.border import Border

# TODO update the JSON string below
json = "{}"
# create an instance of Border from a JSON string
border_instance = Border.from_json(json)
# print the JSON string representation of the object
print(Border.to_json())

# convert the object into a dict
border_dict = border_instance.to_dict()
# create an instance of Border from a dict
border_from_dict = Border.from_dict(border_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


