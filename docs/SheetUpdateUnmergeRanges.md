# SheetUpdateUnmergeRanges

Unmerge merges that intersect the provided ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to unmerge | 

## Example

```python
from openapi_client.models.sheet_update_unmerge_ranges import SheetUpdateUnmergeRanges

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateUnmergeRanges from a JSON string
sheet_update_unmerge_ranges_instance = SheetUpdateUnmergeRanges.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateUnmergeRanges.to_json())

# convert the object into a dict
sheet_update_unmerge_ranges_dict = sheet_update_unmerge_ranges_instance.to_dict()
# create an instance of SheetUpdateUnmergeRanges from a dict
sheet_update_unmerge_ranges_from_dict = SheetUpdateUnmergeRanges.from_dict(sheet_update_unmerge_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


