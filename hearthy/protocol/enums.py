"""
Hearthstone enums
"""

from enum import IntEnum


class GameTag(IntEnum):
    IGNORE_DAMAGE = 1
    MISSION_EVENT = 6
    TIMEOUT = 7
    TURN_START = 8
    TURN_TIMER_SLUSH = 9
    PREMIUM = 12
    GOLD_REWARD_STATE = 13
    PLAYSTATE = 17
    LAST_AFFECTED_BY = 18
    STEP = 19
    TURN = 20
    FATIGUE = 22
    CURRENT_PLAYER = 23
    FIRST_PLAYER = 24
    RESOURCES_USED = 25
    RESOURCES = 26
    HERO_ENTITY = 27
    MAXHANDSIZE = 28
    STARTHANDSIZE = 29
    PLAYER_ID = 30
    TEAM_ID = 31
    TRIGGER_VISUAL = 32
    RECENTLY_ARRIVED = 33
    PROTECTING = 34
    PROTECTED = 35
    DEFENDING = 36
    PROPOSED_DEFENDER = 37
    ATTACKING = 38
    PROPOSED_ATTACKER = 39
    ATTACHED = 40
    EXHAUSTED = 43
    DAMAGE = 44
    HEALTH = 45
    ATK = 47
    COST = 48
    ZONE = 49
    CONTROLLER = 50
    OWNER = 51
    DEFINITION = 52
    ENTITY_ID = 53
    ELITE = 114
    MAXRESOURCES = 176
    CARD_SET = 183
    CARDTEXT_INHAND = 184
    CARDNAME = 185
    CARD_ID = 186
    DURABILITY = 187
    SILENCED = 188
    WINDFURY = 189
    TAUNT = 190
    STEALTH = 191
    SPELLPOWER = 192
    DIVINE_SHIELD = 194
    CHARGE = 197
    NEXT_STEP = 188
    CLASS = 199
    CARDRACE = 200
    FACTION = 201
    CARDTYPE = 202
    RARITY = 203
    STATE = 204
    SUMMONED = 205
    FREEZE = 208
    ENRAGED = 212
    RECALL = 215
    LOYALTY = 216
    DEATHRATTLE = 217
    BATTLECRY = 218
    SECRET = 219
    COMBO = 220
    CANT_HEAL = 221
    CANT_DAMAGE = 222
    CANT_SET_ASIDE = 223
    CANT_REMOVE_FROM_GAME = 224
    CANT_READY = 225
    CANT_EXHAUST = 226
    CANT_ATTACK = 227
    CANT_TARGET = 228
    CANT_DESTROY = 229
    CANT_DISCARD = 230
    CANT_PLAY = 231
    CANT_DRAW = 232
    INCOMING_HEALING_MULTIPLIER = 233
    INCOMING_HEALING_ADJUSTMENT = 234
    INCOMING_HEALING_CAP = 235
    INCOMING_DAMAGE_MULTIPLIER = 236
    INCOMING_DAMAGE_ADJUSTMENT = 237
    INCOMING_DAMAGE_CAP = 238
    CANT_BE_HEALED = 239
    CANT_BE_DAMAGED = 240
    CANT_BE_SET_ASIDE = 241
    CANT_BE_REMOVED_FROM_GAME = 242
    CANT_BE_READIED = 243
    CANT_BE_EXHAUSTED = 244
    CANT_BE_ATTACKED = 245
    CANT_BE_DESTROYED = 247
    CANT_BE_SUMMONING_SICK = 253
    FROZEN = 260
    JUST_PLAYED = 261
    LINKEDCARD = 262
    ZONE_POSITION = 263
    CANT_BE_FROZEN = 264
    COMBO_ACTIVE = 266
    CARD_TARGET = 267
    NUM_CARDS_PLAYED_THIS_TURN = 269
    CANT_BE_TARGETED_BY_OPPONENTS = 270
    NUM_TURNS_IN_PLAY = 271
    NUM_TURNS_LEFT = 272
    OUTGOING_DAMAGE_CAP = 273
    OUTGOING_DAMAGE_ADJUSTMENT = 274
    OUTGOING_DAMAGE_MULTIPLIER = 275
    OUTGOING_HEALING_CAP = 276
    OUTGOING_HEALING_ADJUSTMENT = 277
    OUTGOING_HEALING_MULTIPLIER = 278
    INCOMING_ABILITY_DAMAGE_ADJUSTMENT = 279
    INCOMING_COMBAT_DAMAGE_ADJUSTMENT = 280
    OUTGOING_ABILITY_DAMAGE_ADJUSTMENT = 281
    OUTGOING_COMBAT_DAMAGE_ADJUSTMENT = 282
    OUTGOING_ABILITY_DAMAGE_MULTIPLIER = 283
    OUTGOING_ABILITY_DAMAGE_CAP = 284
    INCOMING_ABILITY_DAMAGE_MULTIPLIER = 285
    INCOMING_ABILITY_DAMAGE_CAP = 286
    OUTGOING_COMBAT_DAMAGE_MULTIPLIER = 287
    OUTGOING_COMBAT_DAMAGE_CAP = 288
    INCOMING_COMBAT_DAMAGE_MULTIPLIER = 289
    INCOMING_COMBAT_DAMAGE_CAP = 290
    CURRENT_SPELLPOWER = 291
    ARMOR = 292
    MORPH = 293
    IS_MORPHED = 294
    TEMP_RESOURCES = 295
    RECALL_OWED = 296
    NUM_ATTACKS_THIS_TURN = 297
    NEXT_ALLY_BUFF = 302
    MAGNET = 303
    FIRST_CARD_PLAYED_THIS_TURN = 304
    MULLIGAN_STATE = 305
    TAUNT_READY = 306
    STEALTH_READY = 307
    CHARGE_READY = 308
    CANT_BE_TARGETED_BY_ABILITIES = 311
    SHOULDEXITCOMBAT = 312
    CREATOR = 313
    CANT_BE_DISPELLED = 314
    PARENT_CARD = 316
    NUM_MINIONS_PLAYED_THIS_TURN = 317
    PREDAMAGE = 318
    TARGETING_ARROW_TEXT = 325
    ENCHANTMENT_BIRTH_VISUAL = 330
    ENCHANTMENT_IDLE_VISUAL = 331
    CANT_BE_TARGETED_BY_HERO_POWERS = 332
    HEALTH_MINIMUM = 337
    SILENCE = 339
    COUNTER = 340
    ARTISTNAME = 342
    HAND_REVEALED = 348
    ADJACENT_BUFF = 350
    FLAVORTEXT = 351
    FORCED_PLAY = 352
    LOW_HEALTH_THRESHOLD = 353
    IGNORE_DAMAGE_OFF = 354
    SPELLPOWER_DOUBLE = 356
    HEALING_DOUBLE = 357
    NUM_OPTIONS_PLAYED_THIS_TURN = 358
    NUM_OPTIONS = 359
    TO_BE_DESTROYED = 360
    AURA = 362
    POISONOUS = 363
    HOW_TO_EARN = 364
    HOW_TO_EARN_GOLDEN = 365
    TAG_HERO_POWER_DOUBLE = 366
    TAG_AI_MUST_PLAY = 367
    NUM_MINIONS_PLAYER_KILLED_THIS_TURN = 368
    NUM_MINIONS_KILLED_THIS_TURN = 369
    AFFECTED_BY_SPELL_POWER = 370
    EXTRA_DEATHRATTLES = 371
    START_WITH_1_HEALTH = 372
    IMMUNE_WHILE_ATTACKING = 373
    MULTIPLY_HERO_DAMAGE = 374
    MULTIPLY_BUFF_VALUE = 375
    CUSTOM_KEYWORD_EFFECT = 376
    TOPDECK = 377
    CANT_BE_TARGETED_BY_BATTLECRIES = 379
    OVERKILL = 380
    DEATHRATTLE_SENDS_BACK_TO_DECK = 382
    STEADY_SHOT_CAN_TARGET = 383
    DISPLAYED_CREATOR = 385
    POWERED_UP = 386
    SPARE_PART = 388
    FORGETFUL = 389
    CAN_SUMMON_MAXPLUSONE_MINION = 390


class AccountInfoRequest(IntEnum):
    LAST_LOGIN = 1
    DECK_LIST = 2
    COLLECTION = 3
    MEDAL_INFO = 4
    MEDAL_HISTORY = 5
    BOOSTERS = 6
    CARD_BACKS = 7
    PLAYER_RECORD = 8
    GAMES_PLAYED = 9
    DECK_LIMIT = 10
    CAMPAIGN_INFO = 11
    NOTICES = 12
    MOTD = 13
    CLIENT_OPTIONS = 14
    CARD_VALUES = 15
    DISCONNECTED = 16
    ARCANE_DUST_BALANCE = 17
    FEATURES = 18
    REWARD_PROGRESS = 19
    GOLD_BALANCE = 20
    HERO_XP = 21
    PVP_QUEUE = 22
    MASSIVE_LOGIN = 23
    BOOSTER_TALLY = 24


class CardSet(IntEnum):
    INVALID = 0
    TEST_TEMPORARY = 1
    CORE = 2
    EXPERT1 = 3
    REWARD = 4
    MISSIONS = 5
    DEMO = 6
    NONE = 7
    CHEAT = 8
    BLANK = 9
    DEBUG_SP = 10
    PROMO = 11
    FP1 = 12
    PE1 = 13
    FP2 = 14
    PE2 = 15
    CREDITS = 16


class BeginPlayingMode(IntEnum):
    COUNTDOWN = 1
    READY = 2


class CardRarity(IntEnum):
    INVALID = 0
    COMMON = 1
    FREE = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5


class Step(IntEnum):
    INVALID = 0
    BEGIN_FIRST = 1
    BEGIN_SHUFFLE = 2
    BEGIN_DRAW = 3
    BEGIN_MULLIGAN = 4
    MAIN_BEGIN = 5
    MAIN_READY = 6
    MAIN_RESOURCE = 7
    MAIN_DRAW = 8
    MAIN_START = 9
    MAIN_ACTION = 10
    MAIN_COMBAT = 11
    MAIN_END = 12
    MAIN_NEXT = 13
    FINAL_WRAPUP = 14
    FINAL_GAMEOVER = 15
    MAIN_CLEANUP = 16
    MAIN_START_TRIGGERS = 17


class Zone(IntEnum):
    INVALID = 0
    PLAY = 1
    DECK = 2
    HAND = 3
    GRAVEYARD = 4
    REMOVEDFROMGAME = 5
    SETASIDE = 6
    SECRET = 7


class CardType(IntEnum):
    INVALID = 0
    GAME = 1
    PLAYER = 2
    HERO = 3
    MINION = 4
    SPELL = 5
    ENCHANTMENT = 6
    WEAPON = 7
    ITEM = 8
    TOKEN = 9
    HERO_POWER = 10


class Faction(IntEnum):
    INVALID = 0
    HORDE = 1
    ALLIANCE = 2
    NEUTRAL = 3


class GoldRewardState(IntEnum):
    INVALID = 0
    ELIGIBLE = 1
    WRONG_GAME_TYPE = 2
    ALREADY_CAPPED = 3
    BAD_RATING = 4
    SHORT_GAME = 5


class MetaType(IntEnum):
    TARGET = 1
    DAMAGE = 2
    HEALING = 3


class MulliganState(IntEnum):
    INVALID = 0
    INPUT = 1
    DEALING = 2
    WAITING = 3
    DONE = 4


# Enum for mtypes.Option.Type
class OptionType(IntEnum):
    PASS = 1
    END_TURN = 2
    POWER = 3


class PacketType(IntEnum):
    GET_GAME_STATE = 1
    CHOOSE_OPTION = 2
    CHOOSE_ENTITIES = 3
    PRE_CAST = 4
    DEBUG_MESSAGE = 5
    CLIENT_PACKET = 6
    START_GAME_STATE = 7
    FINISH_GAME_STATE = 8
    TURN_TIMER = 9
    NACK_OPTION = 10
    GIVE_UP = 11
    GAME_CANCELLED = 12
    FORCED_ENTITY_CHOICE = 13
    ALL_OPTIONS = 14
    USER_UI = 15
    GAME_SETUP = 16
    ENTITY_CHOICE = 17
    PRE_LOAD = 18
    POWER_HISTORY = 19
    NOTIFICATION = 21
    SPECTATOR_HANDSHAKE = 22
    SERVER_RESULT = 23
    SPECTATOR_NOTIFY = 24
    INVITE_TO_SPECTATE = 25
    REMOVE_SPECTATORS = 26

    AUTO_LOGIN = 103
    BEGIN_PLAYING = 113
    DEBUG_CONSOLE_COMMAND = 123
    DEBUG_CONSOLE_RESPONSE = 124
    GAME_STARTING = 114
    PING = 115
    PONG = 116
    AURORA_HANDSHAKE = 168


class PlayState(IntEnum):
    INVALID = 0
    PLAYING = 1
    WINNING = 2
    LOSING = 3
    WON = 4
    LOST = 5
    TIED = 6
    DISCONNECTED = 7
    QUIT = 8


class PowSubType(IntEnum):
    ATTACK = 1
    CONTINOUS = 2
    POWER = 3
    SCRIPT = 4
    TRIGGER = 5
    DEATHS = 6
    PLAY = 7
    FATIGUE = 8


class Race(IntEnum):
    INVALID = 0
    BLOODELF = 1
    DRAENEI = 2
    DWARF = 3
    GNOME = 4
    GOBLIN = 5
    HUMAN = 6
    NIGHTELF = 7
    ORC = 8
    TAUREN = 9
    TROLL = 10
    UNDEAD = 11
    WORGEN = 12
    GOBLIN2 = 13
    MURLOC = 14
    DEMON = 15
    SCOURGE = 16
    MECHANICAL = 17
    ELEMENTAL = 18
    OGRE = 19
    PET = 20
    TOTEM = 21
    NERUBIAN = 22
    PIRATE = 23
    DRAGON = 24


class TagState(IntEnum):
    INVALID = 0
    LOADING = 1
    RUNNING = 2
    COMPLETE = 3


class TrackWhat(IntEnum):
    TRACK_COLLECTION_MANAGER = 1
    TRACK_PLAY_PRACTICE_WITH_CUSTOM_DECK = 2
    TRACK_PLAY_PRACTICE_WITH_PRECON_DECK = 3
    TRACK_PLAY_CASUAL_WITH_CUSTOM_DECK = 4
    TRACK_PLAY_CASUAL_WITH_PRECON_DECK = 5
    TRACK_PLAY_TOURNAMENT_WITH_CUSTOM_DECK = 6
    TRACK_PLAY_TOURNAMENT_WITH_PRECON_DECK = 7
    TRACK_CHALLENGE_FRIEND_WITH_CUSTOM_DECK = 8
    TRACK_CHALLENGE_FRIEND_WITH_PRECON_DECK = 9
    TRACK_ACCEPT_FRIEND_GAME_WITH_CUSTOM_DECK = 10
    TRACK_ACCEPT_FRIEND_GAME_WITH_PRECON_DECK = 11
    TRACK_BUTTON_TOURNAMENT = 12
    TRACK_BUTTON_DRAFT = 13
    ZZ_DEPRECATED_TRACK_BUTTON_CASUAL = 14
    TRACK_BUTTON_PRACTICE = 15
    TRACK_START_TUTORIAL = 16
    TRACK_DISPLAYED_WIN_SCREEN = 17
    TRACK_DISPLAYED_LOSS_SCREEN = 18
    TRACK_DISPLAYED_TIE_SCREEN = 19
    TRACK_RECEIVED_BOOSTER_PACK = 20
    TRACK_LOGIN_FINISHED = 21
    TRACK_LOGOUT_STARTING = 22
    TRACK_GAME_START = 23
    TRACK_CANCEL_MATCHMAKER = 24
    TRACK_VISIT_PACK_OPEN_SCREEN = 25
    TRACK_TOGGLE_DECK_TYPE = 26
    TRACK_BOOSTER_OPENED = 27
    TRACK_CM_MANA_FILTER_CLICKED = 28
    TRACK_CM_MANA_FILTER_OFF = 29
    TRACK_CM_CARDS_SEARCHED = 30
    TRACK_CM_SHOW_CARDS_I_DONT_OWN_TURNED_ON = 31
    TRACK_CM_SHOW_CARDS_I_DONT_OWN_TURNED_OFF = 32
    TRACK_CM_NEW_DECK_CREATED = 33
    TRACK_CM_PAGE_TURNED = 34
    TRACK_BOX_SCREEN_VISIT = 35
    TRACK_AUTO_COMPLETE_DECK_CLICKED = 36
    TRACK_CM_SHOW_PREMIUMS_NOT_OWNED = 37
    TRACK_CM_HIDE_PREMIUMS_NOT_OWNED = 38
    TRACK_PLAY_FORGE_QUEUE = 39

class GameOption:
    AI_MODE = 0x30
    BACKGROUND_SOUND = 20
    BUNDLE_JUST_PURCHASE_IN_HUB = 0x6c
    CARD_BACK = 0x1c
    CARD_BACK2 = 0x1d
    CHANGED_CARDS_DATA = 0x24
    CONNECT_TO_AURORA = 0x1f
    COVER_MOUSE_OVERS = 0x2f
    CURSOR = 3
    DECK_PICKER_MODE = 0x36
    FAKE_PACK_COUNT = 14
    FAKE_PACK_OPENING = 13
    FRIENDS_LIST_CURRENTGAME_SECTION_HIDE = 0x3a
    FRIENDS_LIST_FRIEND_SECTION_HIDE = 0x3b
    FRIENDS_LIST_NEARBYPLAYER_SECTION_HIDE = 60
    FRIENDS_LIST_RECRUIT_SECTION_HIDE = 0x3d
    FRIENDS_LIST_REQUEST_SECTION_HIDE = 0x39
    GFX_FULLSCREEN = 10
    GFX_FXAA = 0x19
    GFX_HEIGHT = 9
    GFX_MSAA = 0x18
    GFX_QUALITY = 12
    GFX_TARGET_FRAME_RATE = 0x1a
    GFX_VSYNC = 0x1b
    GFX_WIDTH = 8
    GFX_WIN_CAMERA_CLEAR = 0x17
    GFX_WIN_POSX = 0x26
    GFX_WIN_POSY = 0x27
    HAS_ACKED_ARENA_REWARDS = 0x66
    HAS_ADDED_CARDS_TO_DECK = 0x58
    HAS_BEEN_NUDGED_TO_CM = 0x57
    HAS_CLICKED_TOURNAMENT = 0x3e
    HAS_CRAFTED = 0x5e
    HAS_DISENCHANTED = 0x5b
    HAS_ENTERED_NAXX = 0x6a
    HAS_FINISHED_A_DECK = 70
    HAS_LOST_IN_ARENA = 100
    HAS_OPENED_BOOSTER = 0x3f
    HAS_PLAYED_EXPERT_AI = 90
    HAS_PLAYED_NAXX = 0x6d
    HAS_RUN_OUT_OF_QUESTS = 0x65
    HAS_SEEN_100g_REMINDER = 0x61
    HAS_SEEN_ALL_BASIC_CLASS_CARDS_COMPLETE = 0x56
    HAS_SEEN_BRM = 0x73
    HAS_SEEN_CINEMATIC = 11
    HAS_SEEN_COLLECTIONMANAGER = 0x41
    HAS_SEEN_COLLECTIONMANAGER_AFTER_PRACTICE = 0x72
    HAS_SEEN_CRAFTING_INSTRUCTION = 0x5d
    HAS_SEEN_CUSTOM_DECK_PICKER = 0x55
    HAS_SEEN_DECK_HELPER = 0x52
    HAS_SEEN_EXPERT_AI = 80
    HAS_SEEN_EXPERT_AI_UNLOCK = 0x51
    HAS_SEEN_FORGE = 0x47
    HAS_SEEN_FORGE_1WIN = 0x4c
    HAS_SEEN_FORGE_2LOSS = 0x4d
    HAS_SEEN_FORGE_CARD_CHOICE = 0x49
    HAS_SEEN_FORGE_CARD_CHOICE2 = 0x4a
    HAS_SEEN_FORGE_HERO_CHOICE = 0x48
    HAS_SEEN_FORGE_PLAY_MODE = 0x4b
    HAS_SEEN_FORGE_RETIRE = 0x4e
    HAS_SEEN_GOLD_QTY_INSTRUCTION = 0x62
    HAS_SEEN_HEROIC_WARNING = 0x68
    HAS_SEEN_HUB = 0x45
    HAS_SEEN_LEVEL_3 = 0x63
    HAS_SEEN_MULLIGAN = 0x4f
    HAS_SEEN_NAXX = 0x69
    HAS_SEEN_NAXX_CLASS_CHALLENGE = 0x6b
    HAS_SEEN_PACK_OPENING = 0x53
    HAS_SEEN_PRACTICE_MODE = 0x54
    HAS_SEEN_PRACTICE_TRAY = 0x44
    HAS_SEEN_SHOW_ALL_CARDS_REMINDER = 0x5c
    HAS_SEEN_STEALTH_TAUNTER = 0x67
    HAS_SEEN_THE_COIN = 0x60
    HAS_SEEN_TOURNAMENT = 0x40
    HAS_STARTED_A_DECK = 0x71
    HEALTHY_GAMING_DEBUG = 15
    HUD = 4
    IDLE_KICK_TIME = 0x13
    IDLE_KICKER = 0x12
    IN_RANKED_PLAY_MODE = 0x5f
    INTRO = 0x2c
    INVALID = 0
    JUST_FINISHED_TUTORIAL = 0x42
    KELTHUZADTAUNTS = 0x25
    LAST_CUSTOM_DECK_CHOSEN = 0x35
    LAST_FAILED_DOP_VERSION = 0x29
    LAST_PRECON_HERO_CHOSEN = 0x34
    LAST_SCENE_MODE = 0x10
    LAST_SELECTED_STORE_ADVENTURE_ID = 0x70
    LAST_SELECTED_STORE_BOOSTER_ID = 0x6f
    LOCAL_TUTORIAL_PROGRESS = 30
    LOCALE = 0x11
    MUSIC = 2
    MUSIC_VOLUME = 7
    NEARBY_PLAYERS = 0x16
    PAGE_MOUSE_OVERS = 0x2e
    PREFERRED_CDN_INDEX = 40
    PREFERRED_REGION = 0x15
    RECONNECT = 0x21
    RECONNECT_RETRY_TIME = 0x23
    RECONNECT_TIMEOUT = 0x22
    SEASON_END_THRESHOLD = 0x20
    SELECTED_ADVENTURE = 0x37
    SELECTED_ADVENTURE_MODE = 0x38
    SHOW_ADVANCED_COLLECTIONMANAGER = 0x43
    SHOWN_GFX_DEVICE_WARNING = 0x2b
    SOUND = 1
    SOUND_VOLUME = 6
    SPECTATOR_OPEN_JOIN = 110
    STREAMING = 5
    TIP_CRAFTING_UNLOCKED = 0x59
    TIP_FORGE_PROGRESS = 0x33
    TIP_PLAY_PROGRESS = 50
    TIP_PRACTICE_PROGRESS = 0x31
    TOUCH_MODE = 0x2a
    TUTORIAL_LOST_PROGRESS = 0x2d
