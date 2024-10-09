# SheetUpdateEditRange

Edit all of the cells in a contiguous range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**Range**](Range.md) |  | 
**values** | **List[List[Optional[object]]]** | Row-major ordered two-dimensional array of cell values | 
**options** | [**SheetUpdateEditRangeOptions**](SheetUpdateEditRangeOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.sheet_update_edit_range import SheetUpdateEditRange

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateEditRange from a JSON string
sheet_update_edit_range_instance = SheetUpdateEditRange.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateEditRange.to_json())

# convert the object into a dict
sheet_update_edit_range_dict = sheet_update_edit_range_instance.to_dict()
# create an instance of SheetUpdateEditRange from a dict
sheet_update_edit_range_from_dict = SheetUpdateEditRange.from_dict(sheet_update_edit_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


