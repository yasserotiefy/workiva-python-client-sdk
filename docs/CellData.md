# CellData

Data in a cell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | String, numeric, or boolean value of the cell. If the cell is a formula, this value will be the formula string. | [optional] 
**calculated_value** | **object** | String, numeric, or boolean value result value of the cell. If the cell is a formula, this value will be the calculated result. | [optional] 
**formats** | [**Formats**](Formats.md) |  | [optional] 
**effective_formats** | [**EffectiveFormats**](EffectiveFormats.md) |  | [optional] 

## Example

```python
from openapi_client.models.cell_data import CellData

# TODO update the JSON string below
json = "{}"
# create an instance of CellData from a JSON string
cell_data_instance = CellData.from_json(json)
# print the JSON string representation of the object
print(CellData.to_json())

# convert the object into a dict
cell_data_dict = cell_data_instance.to_dict()
# create an instance of CellData from a dict
cell_data_from_dict = CellData.from_dict(cell_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


