from json import loads, dumps


json_string = '''
{
    "_id": "_b_mountains",
    "name": "Горы",
    "changed": false,
    "enter condition": {},
    "zones": [
        "_z_plateau", 
        "_z_scarp", 
        "_z_rocks", 
        "_z_nek"
    ]
}
'''

data = loads(json_string)

# >>> type(data)
# <class 'dict'>
# >>>
# >>> data
# {'_id': '_b_mountains', 'name': 'Горы', 'changed': False, 'enter condition': {}, 'zones': ['_z_plateau', '_z_scarp', '_z_rocks', '_z_nek']}

data['zones'].append('_z_cirkus')

# >>> dumps(data, ensure_ascii=False)
# '{"_id": "_b_mountains", "name": "Горы", "changed": false, "enter condition": {}, "zones": ["_z_plateau", "_z_scarp", "_z_rocks", "_z_nek", "_z_cirkus"]}'
# >>> 
# >>> dumps(data, ensure_ascii=False, indent=2)
# '{\n  "_id": "_b_mountains",\n  "name": "Горы",\n  "changed": false,\n  "enter condition": {},\n  "zones": [\n    "_z_plateau",\n    "_z_scarp",\n    "_z_rocks",\n    "_z_nek",\n    "_z_cirkus"\n  ]\n}'
# >>>
# >>> print(dumps(data, ensure_ascii=False, indent=2))
# {
#   "_id": "_b_mountains",
#   "name": "Горы",
#   "changed": false,
#   "enter condition": {},
#   "zones": [
#     "_z_plateau",
#     "_z_scarp",
#     "_z_rocks",
#     "_z_nek",
#     "_z_cirkus"
#   ]
# }

