def car_info(manufacturer, model, **other_info):
    other_info["manufacturer_name"] = manufacturer
    other_info["model_name"] = model
    return other_info