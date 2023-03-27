from datetime import datetime

from Bungie_Enums import (BungieMembershipType, DestinyComponentType,
                          FriendRelationshipState, MembershipType,
                          PresenceStatus)
from pydantic import BaseModel


class DestinyComponentTypesList(BaseModel):
    '''A list of components to return when using the Bungie API.'''
    components: list[DestinyComponentType]


class UserInfoCard(BaseModel):
    """A model that represents a user's info card."""
    icon_path: str
    cross_save_override: int
    app_icon: str
    supplemental_display_name: str
    is_public: bool
    membership_type: MembershipType
    membership_id: str
    display_name: str


class PlatformFriend(BaseModel):
    """
    A model that represents a friend on a specific platform.
    """
    membership_id: str | None
    unique_name: str | None
    display_name: str | None
    profile_picture: str | None
    last_online_status_change: datetime | None
    online_status: PresenceStatus | None
    relationship: FriendRelationshipState | None
    platform_type: BungieMembershipType | None
    status_text: str | None
    date_last_played: datetime | None
    is_following: bool | None
    show_activity: bool | None
    avatar_path: str | None
    theme_light: str | None
    theme_dark: str | None
    default_avatar: str | None
    profile_theme: str | None


class BungieMembership(BaseModel):
    id: int
    type: BungieMembershipType
    deleted: bool
    starred: bool
    isOverridden: bool
    membershipType: BungieMembershipType
    membershipId: str
    displayName: str
    crossSaveOverride: list[BungieMembershipType] = []


class Friend(BaseModel):
    bungie_net_user: UserInfoCard  # BungieNetUserInfoCard
    friendship_date: str
    relationship_state: FriendRelationshipState
    is_online: bool | None
    platform_friends: list[PlatformFriend] | None
