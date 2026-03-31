wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}


def dept(ward):
    department = {}
    for key, value in ward.items():
        for people in value:
            if people in department['name']:
               department['name'] = {
               'Dept.' = key
               } 
            department['name'] = people
            

    


dept(wards)
