from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from .ui import UserAddWindow


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    can_delete = True
    add_window = edit_window = UserAddWindow # ModelEditWindow.fabricate(model=User)

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    can_delete = True
    add_window = edit_window =  ModelEditWindow.fabricate(model=ContentType)

class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)

class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)