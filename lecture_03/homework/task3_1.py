raw_sku = "CARROT-001"
raw_regions = ("Minsk", "Warsaw", "Berlin", "Warsaw")
raw_weight_str = "2.5"
raw_stock_str = "150"

weight_kg=float(raw_weight_str)
stock_quantity=int(raw_stock_str)

print(weight_kg, stock_quantity, type(weight_kg), type(stock_quantity))

sku_as_list=list(raw_sku)
print(sku_as_list)

regions_list=list(raw_regions)
print(regions_list)

unique_regions=set(raw_regions)
print(unique_regions)

regions_tuple=tuple(unique_regions)
print(regions_tuple)

empty_list_1=[678,6789,8765]
name = "Dasha"
empty_list_2=list(name)
print(empty_list_1, empty_list_2)

empty_dict_1={'fdkmls':78, 'fkjdslm':'fdv'}
empty_dict_2=dict(name="jdk", age=23,citvckbml=32)
print(empty_dict_1,empty_dict_2)

empty_tuple_1=("sadsf",32,8)
empty_tuple_2_var = [1, 2, 3]
empty_tuple_2=tuple(empty_tuple_2_var)
print(empty_tuple_1,empty_tuple_2)

empty_set_var=(98,90,90)
empty_set=set(empty_set_var)
print(empty_set)

empty_collection=[]
print(bool(empty_collection))

full_collection =(489,8493,57489)
print(bool(full_collection))
