wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}


def dept(ward):
    department = {}
    for dept, docs in ward.items():
        for doc in docs:
            # if doc in department:
            #     department[doc] = {"Dept.": [dept]}
            # department = {'Name': doc}
            # if doc in department:
            #     department[doc] = {
            #         "Dept.": dept
            #     }
            if doc not in department:
                department[doc] = []
            department[doc].append(dept)
    print(department)
        
            

    


dept(wards)
