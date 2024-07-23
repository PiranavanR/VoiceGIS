import speech_recognition as sr
import re 
from geopy.geocoders import Nominatim
import winsound

zoomin = ["zooming", "zoomin", "zoom in", "room in"]
zoomout = ["zoom out", "zoomout", "room out", "robot"]
navigate = ["navigate", "navigate to", "locate", "go to", "head to", "get direction to", "take me to"]
street_view = ["street", "road", "sweets"]
terrain_view = ["topographic", "terrain", "tyranno", "train", "elevation", "topography", "animations"]
satellite_view = ["satellite", "celestial", "aerial"]
traffic_view = ["traffic"]
hide = ["hide"]
remove_marker = ["remove marker on", "remove marker at", "remove mark on", "remove mark at", "remove marker", "remove mark", "delete mark", "delete marker", "remove markers", "remove all marks", "remove all markers", "remove all mark"]
add_marker = ["add marks to", "add marks on", "add marks", "add marker to", "add mark to", "add march to", "add marker on", "add mark on", "add marker", "mark", "add mark", "marker",  "march", "ad marker to", "ad mark to", "ad march to", "ad marker on", "ad mark on", "ad marker", "ad mark", "admark to", "admark on", "admark"]

def classify_query(q):
    print("Classifying Query...")
    if any(zi in q for zi in zoomin):
        pattern = "|".join(map(re.escape, zoomin))
        place = re.sub(pattern, "", q)
        if len(place.replace(" ", ""))>0:
            coordinates = get_coordinates(place)
            return "Zoom In", coordinates
        return "Zoom In", None
    elif any(zo in q for zo in zoomout):
        return "Zoom Out", None
    elif any(n in q for n in navigate):
        pattern = "|".join(map(re.escape, navigate))
        place = re.sub(pattern, "", q)
        coordinates = get_coordinates(place)
        return "Navigate", coordinates
    elif any(n in q for n in remove_marker):
        if not " all " in q:
            pattern = "|".join(map(re.escape, remove_marker))
            place = re.sub(pattern, "", q)
            print(place)
            if len(place.replace(" ", ""))>0:
                coordinates = get_coordinates(place)
                return "Remove Markers", coordinates
        return "Remove Markers", None
    elif any(n in q for n in add_marker):
        pattern = "|".join(map(re.escape, add_marker))
        place = re.sub(pattern, "", q)
        coordinates = get_coordinates(place)
        return "Mark", coordinates
    elif any(v in q for v in street_view):
        return "Street View", None
    elif any(v in q for v in terrain_view):
        return "Terrain View", None
    elif any(v in q for v in satellite_view):
        return "Satellite View", None
    elif any (v in q for v in traffic_view):
        return "Traffic View", None
    elif any(v in q for v in hide):
        return "Hide Layers", None
    else:
        return "No Output", None

def get_coordinates(q):
    print("Getting Coordinates...")
    geolocator = Nominatim(user_agent="VoiceGIS")
    location = geolocator.geocode(q)
    print(location)
    #print(location.address)
    return [location.latitude, location.longitude]

def recognize():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        r.adjust_for_ambient_noise(source, 1)
        print("Say something!")
        winsound.Beep(500,250)
        try:
            audio = r.listen(source, phrase_time_limit=5)
            print("Processing...")
            query = r.recognize_google(audio, language='en-IN').lower()
            print("Processsed audio!")
            print("Query: " + query)
            print("Output Generated!")
            classified_query, coordinates = classify_query(query)
            print("Classified Query: " + classified_query)
            print(f"Coordinates : {coordinates}")
            if coordinates:
                formatted_command = f"{classified_query}:{coordinates[0]},{coordinates[1]}"
            else:
                formatted_command = f"{classified_query}:"
            print(formatted_command)
            return formatted_command
        except Exception as e:
            print(f"An error ocuured: {e}")

#recognize()

