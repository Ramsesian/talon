def centered_text(paint: object, rect: object, text: str) -> tuple[int, int]:
    """Calculates the starting coordinates of a length of text to be centered inside the provided rectangle."""
    text_width = paint.measure_text(text)[0]
    
    text_height = paint.textsize    

    rect_center_x = rect.x + (rect.width - text_width) / 2
    rect_center_y = rect.y + (rect.height + text_height) / 2

    return (rect_center_x, rect_center_y) 
    

def attr_from_dict(obj: object, attr_dict: dict) -> None:
    """If attr_dict has a key of the same name as an attribute in obj then set that attribute to the value in attr_dict"""

    for attr in [x for x in attr_dict if hasattr(obj, x) and x is not None]:
        setattr(obj, attr, attr_dict[attr])
