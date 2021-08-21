#!/usr/bin/python

class Config:
    WINDOW_TITLE          = 'League of Legends'
    WINDOW_BUGSPLAT_TITLE = 'Whoops! Something broke.'

    CHAMPION_NAME    = 'Yi'

    VIDEO_FILE_LOC   = rf'Media/Login/{CHAMPION_NAME}.mp4'
    CLOSE_BUTTON_LOC = r'Media/Close.png'
    WINDOW_ICON_LOC  = r'Media/Logos/League.png'
    LEAGUE_LOGO_LOC  = r'Media/Logos/LeagueLogoBordered.png'

    LOGIN_SIZE       = (1450, 750)
    VERSION_NUMBER   = 'V7.3-3845603.3845421'

    BUGSPLAT_STATICTEXT = ('A problem has been encountered and the program '
    'needs to close. \n\nReporting this error help us make our product better. '
    'Please send this error report\n using the "Send Error Report" button below. '
    'All information is trated as confidential.'
    '\n\nPlease describe the events just before this dialog appeared:')

    COMBO_BOX_REGION_LIST = (
        'EU Nordic and East',
        'Brazil',
        'EU West',
        'Latin America North',
        'Latin America South'
    )

    LOGIN_USERNAME = 'dummy'
    LOGIN_PASSWORD = 'password'
