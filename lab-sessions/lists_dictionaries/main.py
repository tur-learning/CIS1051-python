from utils import *

filename = "rome.json"
# Using load_data function to access
# data contained in the filename
rome_data = load_data(filename)

# print info related to data to investigate
# its content
#
# print(type(rome_data)) # type -> dict
# print(rome_data.keys()) # keys of the dict
# rome_data.values() # to get values
# rome_data.items()  # to get key, value pairs

# Extract values associated to "features" key
features = rome_data.get("features", None)
# features = rome_data["features"]
# print(type(features))
# print(len(features))


# Accessing first element of the features list
element = features[0]
# print(type(element))
# print_dict(element)
# print(element.keys())

# Accessing values of the element by using the 
# get method for dictionaries
el_properties = element.get("properties", None)
el_name = el_properties.get("name", "unknown name")

el_geometry = element.get("geometry", None)
el_type = el_geometry.get("type", "no type")
print("NAME: ", el_name, " TYPE: ", el_type)


# Doing the same as before within a for loop,
# cycling through all the elements contained
# in the features list
data = []   # initialization of empty lists to store data
nasoni = []
for el in features:
    el_properties = el.get("properties", None)
    # defaulting get method to "drinking_water" because we
    # know what is contained in the data
    el_name = el_properties.get("name", "drinking_water")

    el_geometry = el.get("geometry", None)
    el_coords = el_geometry.get("coordinates", None)
    el_coords = extract_coords(el_coords)    

    el_dict = {
            "name": el_name,
            "coordinates": el_coords
        }

    # Distinguishing between two cases
    # to store the data in different lists
    if el_name != "drinking_water":
        # appending to data list
        data.append(el_dict)
        print("NAME: ", el_name, " TYPE: ", el_coords)
    elif el_name == "drinking_water":
        # appending to nasoni list
        nasoni.append(el_dict)

# Setting the name of a building/monument 
# to search inside the "data" list 
search_name = "colosseo"
monument = []
for el in data:
    # lower() method applied to a string
    # changes it to lowercase letters
    if el["name"].lower() == search_name:
        print_dict(el)
        monument.append(el)

# Initializing an empty "distances" list
# to store distances between the monuments
# extracted and all the "nasoni"
distances = []
for mon in monument:
    # getting monuments coordinates
    # no need to use get method because
    # we constructed the data to surely have
    # this key and values associated
    mon_coords = mon["coordinates"]
    
    for nas in nasoni:
        # getting nasoni coordinates
        nas_coords = nas["coordinates"]
        # calculating distance and appending to the list
        dist = calculate_distance(mon_coords, nas_coords)
        distances.append(dist)

# getting the nearest nasone to the given monument
nearest_nasone = get_nearest(distances, nasoni)
print(f"NEAREST NASONE TO {search_name.upper()}")

# printing the result
print_dict(nearest_nasone)

# getting the google maps link with location
# of the nearest nasone. You can click it
# and it will redirect you to the google maps
# webpage
link2map(nearest_nasone)