def validate_list_coords(list_of_coords):

    if not isinstance(list_of_coords, list):
        raise ValueError("not a list")

    if not len(list_of_coords) == 2:
        raise ValueError("incorrect length of array")

    if not all(isinstance(coord, (int, float)) for coord in list_of_coords):
        raise ValueError(
            "Both coordinates in starting point must be numbers (int or float)."
        )

    longitude, latitude = list_of_coords

    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be and int or float between -180 and 180.")

    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be and int or float between -90 and 90.")

    return list_of_coords
