import logging  # Used to log each action of the program

# ROOM_CONFIG
DESCRIPTION: str = "Bafoon"  # The room description
SHINY_ROOM_NAME: str = "Shiny Pokemon!"  # Room name for shiny game
NORMAL_ROOM_NAME: str = "aim-bot"  # Room name for normal game
SHAKESPEARE_POEM: str = (
    """O, fairest of days, how dost thou shine so bright? ... (truncated for brevity)"""  # An o'l good poem
)


# Saved Images
IMAGE_PATHS: dict[str, str] = {
    'main'        : 'images/main_menu'                  + '.png',
    'create'      : 'images/create_menu'                + '.png',
    'close'       : 'images/close_button'               + '.png',
    'waiting'     : 'images/waiting_for_player'         + '.png',
    'left'        : 'images/player_left'                + '.png',
    'menu'        : 'images/main_menu_button'           + '.png',
    'host'        : 'images/host'                       + '.png',
    'room_name'   : 'images/room_name'                  + '.png',
    'description' : 'images/description'                + '.png',
    'shiny'       : 'images/shiny'                      + '.png',
    'create_room' : 'images/create_room_button'         + '.png',
    'white'       : 'images/white_wins'                 + '.png',
    'black'       : 'images/black_wins'                 + '.png',
    'invite'      : 'images/invite_button'              + '.png',
    'host_left'   : 'images/host_left'                  + '.png',
    'failure'     : 'images/pending_connection_failure' + '.png'
}


# Basic Config Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
