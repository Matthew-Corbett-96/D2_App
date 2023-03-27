from enum import Enum


class staticURLs(str, Enum):
    '''The URLs for the Bungie API.'''
    BASE = 'https://www.bungie.net/Platform'
    DESTINY2 = 'https://www.bungie.net/Platform/Destiny2'
    GetFriendsList = 'https://www.bungie.net/Platform/Social/Friends/'


class BungieMembershipType(int, Enum):
    '''The types of membership the Accounts system supports. 
    This is the external facing enum used in place of the internal-only 
    Bungie.SharedDefinitions.MembershipType.'''
    NoneMembership = 0
    Xbox = 1
    PlayStation = 2
    Steam = 3
    Blizzard = 4
    Stadia = 5
    Demon = 10
    BungieNext = 254
    All = -1


class MembershipType(int, Enum):
    '''The type of membership the player has. Not necessarily the platform they are playing on.'''
    NoneMembershipType = 0
    Xbox = 1
    PlayStation = 2
    Steam = 3
    Blizzard = 4
    Stadia = 5
    Demon = 10
    BungieNext = 254
    All = -1


class DestinyActivityModeType(Enum):
    '''The type of activity the player is currently playing.'''
    NoneActivityModeType = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    PvPIntroduction = 8
    ThreeVsThree = 9
    Control = 10
    Lockdown = 11
    Team = 12
    FreeForAll = 13
    TrialsOfOsiris = 14
    Elimination = 15
    Rift = 16
    Mayhem = 17
    ZoneControl = 18
    Racing = 19
    Arena = 20
    Supremacy = 21
    PrivateMatchesAll = 22
    Survival = 23
    Countdown = 24
    TrialsCountdown = 25
    Momentum = 26
    Dungeons = 27
    NightmareHunt = 28
    IronBanner = 29
    AllMayhem = 30
    AllPvECompetitive = 31
    PatrolMayhem = 32
    SurvivalOfTheFittest = 37
    IronBannerMayhem = 38
    ScoredNightfall = 39
    ScoredHeroicNightfall = 40
    Rumble = 41
    AllDoubles = 42
    Doubles = 43
    PrivateMatchesClash = 44
    PrivateMatchesControl = 45
    PrivateMatchesSupremacy = 46
    PrivateMatchesCountdown = 47
    PrivateMatchesSurvival = 48
    PrivateMatchesMayhem = 49
    PrivateMatchesRumble = 50
    HeroicAdventure = 51
    Showdown = 52
    LockdownControl = 53
    Scorched = 54
    ScorchedTeam = 55
    Gambit = 63
    AllPvECompetitiveWarmup = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHuntMatchmaking = 79
    EliminationSurvival = 80
    MomentumControl = 81
    DungeonLair = 82
    Sundial = 83
    TrialsOfOsirisElimination = 84
    TrialsOfOsirisSurvival = 85
    TrialsOfOsirisCountdown = 86
    MomentumElimination = 87
    Dungeon = 88
    NightmareHuntMaster = 89
    AllPvECompetitiveLabs = 90
    TrialsOfOsirisAll = 91
    EliminationFreelance = 92
    ControlFreelance = 93


class FriendRelationshipState(int, Enum):
    '''The state of the relationship between the local user and the user in question.'''
    Unknown = 0
    Friend = 1
    IncomingRequest = 2
    OutgoingRequest = 3
    Blocked = 4
    Ignored = 5
    IgnoredFriend = 6


class PresenceStatus(int, Enum):
    '''The status of the user's presence.'''
    Offline = 0
    Online = 1
    Idle = 2
    Busy = 3
    LookingForGroup = 4
    Unknown = 255


class DestinyComponentType(int, Enum):
    '''The type of component to return.'''
    None_ = 0
    Profiles = 100
    VendorReceipts = 101
    ProfileInventories = 102
    ProfileCurrencies = 103
    ProfileProgression = 104
    PlatformSilver = 105
    Characters = 200
    CharacterInventories = 201
    CharacterProgressions = 202
    CharacterRenderData = 203
    CharacterActivities = 204
    CharacterEquipment = 205
    ItemInstances = 300
    ItemObjectives = 301
    ItemPerks = 302
    ItemRenderData = 303
    ItemStats = 304
    ItemSockets = 305
    ItemTalentGrids = 306
    ItemCommonData = 307
    ItemPlugStates = 308
    ItemPlugObjectives = 309
    ItemReusablePlugs = 310
    Vendors = 400
    VendorCategories = 401
    VendorSales = 402
    Kiosks = 500
    CurrencyLookups = 600
    PresentationNodes = 700
    Collectibles = 800
    Records = 900
    Transitory = 1000
    Metrics = 1100
    StringVariables = 1200
    StringSetVariables = 1201
    LongVariables = 1300
    FlagVariables = 1400
    DateTimeVariables = 1500


class PlatformFriend(int, Enum):
    '''The type of platform the friend is on.'''
    Nonee = 0
    Xbox = 1
    PlayStation = 2
    Steam = 3
    Blizzard = 4
    Stadia = 5
    Demon = 10
    BungieNext = 254


class DestinyClass(int, Enum):
    '''The class of the character.'''
    Titan = 0
    Hunter = 1
    Warlock = 2
    Unknown = 3


class DestinyGender(int, Enum):
    '''The gender of the character.'''
    Male = 0
    Female = 1
    Unknown = 2


class DestinyRace(int, Enum):
    '''The Race of the character.'''
    Human = 0
    Awoken = 1
    Exo = 2
    Unknown = 3
