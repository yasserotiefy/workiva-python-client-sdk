# SheetUpdateClearBorders

Clears borders in ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to clear borders | 

## Example

```python
from openapi_client.models.sheet_update_clear_borders import SheetUpdateClearBorders

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateClearBorders from a JSON string
sheet_update_clear_borders_instance = SheetUpdateClearBorders.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateClearBorders.to_json())

# convert the object into a dict
sheet_update_clear_borders_dict = sheet_update_clear_borders_instance.to_dict()
# create an instance of SheetUpdateClearBorders from a dict
sheet_update_clear_borders_from_dict = SheetUpdateClearBorders.from_dict(sheet_update_clear_borders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


