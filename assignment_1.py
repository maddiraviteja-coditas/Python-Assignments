from typing import TypedDict, Required

details = TypedDict('details', {'name': str, 'id': Required[int]}, total=True)

information: details = {
    "name": "Raviteja",  # if we comment this key it will also generate a warning as all fields are not mentioned,
    # to avoid it we can either use the not required from the typing or we can set total to false
    "id": 5591,  # if this field is commented it will generate a warning as required field is not provided
    # "tech" : "genAI"  => generates a warning as an extra key is being added
}

