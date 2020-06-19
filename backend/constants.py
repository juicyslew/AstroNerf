CONTROLS = {
    # will populate later
    # likely will involve:
    # onLeft—rotate orientation to left
    # onRight—rotate orientation to right
    # onUp—if canAdvance, move forward
    'left': (0, -1),
    'right': (0, 1),
    'forward': (1, 0),
    'jump': None,
    'tab': None,
    'recordToggle': None,
    'audioToggle': None,
    'expand': None,
    'next': None,
    'startup': None
}

STEP_SIZE = {
    'rotate': 30,    # degrees to rotate
    0: 1 / 690,  # multiple to apply to steps in degree changes
    1: 1 / 6900,
    2: 1 / 10000,
}

OSM_CV_DB = "./backend/logs/OSM_CV_DB.db"
SIDEWALK_OSM_DESC = {
    'both': 'Sidewalk reported on both sides of this road',
    'same': 'Sidewalk reported on only your side of this road',
    'different': 'Sidewalk reported on only the other side of this road',
    'right': None,
    'left': None,
    'no': 'Likely no sidewalk on this road',
    'none': 'Likely no sidewalk on this road',
}
SIDEWALK_SIDE = {
    'left': -1,
    'right': 1,
}

# THIS DIRECTLY MATCHES CV LABELS
AUDIO_SOURCE_PREFIX = 'backend/SpatialAudioTesting/Original'
GEN_AUDIO_SOURCE_PREFIX = 'backend/SpatialAudioTesting/Gen_Original'

"""AUDIO_FILE_DICT = {
    'road': AUDIO_SOURCE_PREFIX + '/RoadShort.wav',
    'park': AUDIO_SOURCE_PREFIX + '/CityParkShort.wav',
    'downtown': AUDIO_SOURCE_PREFIX + '/DowntownShort.wav',
    'residential': AUDIO_SOURCE_PREFIX + '/ResidentialShort.wav',
    'waterside': AUDIO_SOURCE_PREFIX + '/WatersideShort.wav',
    'construction': AUDIO_SOURCE_PREFIX + '/ConstructionShort.wav'
}"""

AUDIO_STRING_DICT = {
    'road': "Street",

    'crosswalk': "Crosswalk",

    'station': "T Station",
    'entrance': "T Station Entrance",

    'business': "Business",

    'construction': "Construction",

    'obstacle': "Trash may be out",

    'tree': "Tree",
    'firehydrant': "Fire hydrant",
    'streetlight': "Street light",
    'bigbelly': "Trash can",  # Should this be "Big Belly trash can"

    'safetyconcern': "Safety Concern Reported in this Area",
    'crashreport': "Crash reported in this Area",  # turn this into number of crashes

    'door': "Door",

    'park': "Park Area",
    'downtown': "Downtown Area",
    'residential': "Residential Area",
    'waterside': "Waterside Area",

    'No Sidewalk': "No Sidewalk",
    'Sidewalk': "Concrete Sidewalk",
    'Sidewalk - Brick': "Brick Sidewalk",
    'Has Median': "Road has Median",

    0: "12 o Clock",
    1: "1 o Clock",
    2: "2 o Clock",
    3: "3 o Clock",
    4: "4 o Clock",
    5: "5 o Clock",
    6: "6 o Clock",
    7: "7 o Clock",
    8: "8 o Clock",
    9: "9 o Clock",
    10: "10 o Clock",
    11: "11 o Clock",
    12: "End of audio",

    'clocktick': "[[tS]]"
}

AUDIO_FILE_DICT = {key: GEN_AUDIO_SOURCE_PREFIX + "/" + value.replace(' ', '') + ".wav"
                   for key, value in AUDIO_STRING_DICT.items()}

AUDIO_OUTPUT_FILE_PREFIX = 'backend/SpatialAudioTesting/Processed/environmentalAudio'

SIDEWALK_CV_DESC = {
    0: 'in front of you',
    1: 'to your right',
    2: 'behind you',
    3: 'to your left',
}
# Do not reorder, brick needs to come first
SIDEWALK_TYPE = {
    3: "brick sidewalk",
    1: "no or insufficient sidewalk",
    2: "sidewalk",

}
SIDEWALK_ORIGIN = {
    -1: "predicted",
    0: "reported and predicted",
    1: "reported"
}

MAX_ROTATE = 45.0  # Maximum automatic Rotation

INSTANCE_MOVE_DIST = 80  # amount to move on each advance in feet
EXTRA_MOVE_EARSHOT_INTERSECTION = 10  # Amount extra we can move to get to an intersection.
EXTRA_MOVE_EARSHOT_NORMAL = 3
ON_NODE_THRESHOLD = .1

MIN_CROSSWALK_DISTANCE = 10  # feet
MIN_SIDEWALK_DISTANCE = 5  # feet

DEFAULT_MIN_DISTANCE = 1.0

INTERACTION_DIST = 50  # Mximum distance that we know about interactions within (ex: crosswalks w/in 50 feet)

DEBUG_MODE = False

FROM_ADDR = "viaserviceolin@outlook.com"

# Diciionry of CV objects and their model type. Key is the object name, value is a tuple of
# image type (streetside or aerial) and model (object detection or classifier)
CV_TAGS = {
    'Door': ("streetside", "object"),
    'crosswalk': ("aerial", "object"),
    'TypeOfArea': ("aerial", "classifier"),
    'Sidewalk': ("streetside", "classifier")
}

# CV Model values. Each model has an iteration number, projectId, and CV threshold
# and potentially a probability breakdown by class stored in a tuple
MODEL_INFO = {
    ("streetside", "object"): ("Iteration72", "5eeace10-7df8-4f94-9b41-0c4cce783916", 0.62),
    ("streetside", "classifier"): ("Iteration35", "c1432470-7cee-42e4-87f5-048aacb5e4e4", 0.5, {'Sidewalk': 0.5, "Sidewalk - Brick": 0.75, "No Sidewalk": 0.90}),  # noqa: E501
    ("aerial", "object"): ("Iteration1", "444664bc-8294-43e3-8f02-a9d2f495bc12", 0.3),
    ("aerial", "classifier"): ("TypeOfArea_Iteration10", "7201298d-44c9-4689-bee9-743c9d2cfa89", 0.6)
}

# Image Analysis and CV constants
STREETSIDE_IMAGE_WIDTH = 1400
STREETSIDE_IMAGE_HEIGHT = 400
AERIAL_IMAGE_WIDTH = 800
AERIAL_IMAGE_HEIGHT = 800
BOSTON_LATITUDE = 42.3601
BOSTON_LONGITUDE = -71.0589
AERIAL_ZOOM = 20
STREETSIDE_ZOOM = 2
