from objectpack.actions import ObjectPack, BaseAction, ObjectSaveAction
from objectpack.ui import ModelEditWindow
from objectpack.observer.base import Observer, ObservableController
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from .ui import UserAddWindow, PermissionAddWindow



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
    parents = ['content_type']
    add_to_menu = True
    can_delete = True
    add_window = edit_window = PermissionAddWindow 
    def __init__(self):
        super(PermissionPack, self).__init__()


