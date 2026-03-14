def validation(employee):
    if employee is None:
        return False
    if employee["name"] is None or employee["name"] == "":
        return False
    if employee["department"] is None or employee["department"] == "":
        return False
    if employee["salary"] is None or employee["salary"] <= 0:
        return False
    return True