import tcod as libtcod
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Entity
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from render_functions import RenderOrder

def get_constants():
    # global vars
    WINDOW_TITLE = "SimpleRL"
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    LIMIT_FPS = 20
    MAP_WIDTH = 80
    MAP_HEIGHT = 43

    # FOV constants
    FOV_ALGORITHM = 0
    FOV_LIGHT_WALLS = True
    FOV_RADIUS = 10

    # room constants
    MAX_MONSTERS_PER_ROOM = 3
    MAX_ITEMS_PER_ROOM = 2
    MAX_ROOMS = 30
    ROOM_MAX_SIZE = 10
    ROOM_MIN_SIZE = 6

    # UI constants
    BAR_WIDTH = 20
    PANEL_HEIGHT = 7
    PANEL_Y = SCREEN_HEIGHT-PANEL_HEIGHT
    MESSAGE_X = BAR_WIDTH + 2
    MESSAGE_WIDTH = SCREEN_WIDTH-BAR_WIDTH-2
    MESSAGE_HEIGHT = PANEL_HEIGHT-1
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }
    constants = {
        'window_title': WINDOW_TITLE,
        'screen_width': SCREEN_WIDTH,
        'screen_height': SCREEN_HEIGHT,
        'bar_width': BAR_WIDTH,
        'panel_height': PANEL_HEIGHT,
        'panel_y': PANEL_Y,
        'message_x': MESSAGE_X,
        'message_width': MESSAGE_WIDTH,
        'message_height': MESSAGE_HEIGHT,
        'map_width': MAP_WIDTH,
        'map_height': MAP_HEIGHT,
        'room_max_size': ROOM_MAX_SIZE,
        'room_min_size': ROOM_MIN_SIZE,
        'max_rooms': MAX_ROOMS,
        'fov_algorithm': FOV_ALGORITHM,
        'fov_light_walls': FOV_LIGHT_WALLS,
        'fov_radius': FOV_RADIUS,
        'max_monsters_per_room': MAX_MONSTERS_PER_ROOM,
        'max_items_per_room': MAX_ITEMS_PER_ROOM,
        'colors': colors
    }
    return constants

def get_game_variables(constants):
    fighter_component = Fighter(hp=30, defense=2, power=5)
    inventory_component = Inventory(26)
    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component)
    entities = [player]

    game_map = GameMap(constants['SCREEN_WIDTH'], constants['SCREEN_HEIGHT'])
    game_map.make_map(constants['MAX_ROOMS'], constants['ROOM_MIN_SIZE'], constants['ROOM_MAX_SIZE'], constants['SCREEN_WIDTH'], constants['SCREEN_HEIGHT'], player, entities, constants['MAX_MONSTERS_PER_ROOM'], constants['MAX_ITEMS_PER_ROOM'])
    message_log = MessageLog(constants['MESSAGE_X'], constants['MESSAGE_WIDTH'], constants['MESSAGE_HEIGHT'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state