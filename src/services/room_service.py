"""
Author: Nguyen Khac Trung Kien
"""
from collections.abc import Iterable
from typing import Any, Tuple

from PyQt5.QtWidgets import QComboBox
from sqlalchemy.orm import keyfunc_mapping
from database.models.bed_type import BedType
from database.models.floor import Floor
from database.models.room import RoomType
from database.orm import Session
from database.repositories.base_repository import Repository




def bed_types() -> list[BedType]:
    """
    Return list of all available bed type in database
    """
    # TODO: use service instead to close session with singleton service
    bed_type  = Session().query(BedType).all()
    return bed_type






def floor_members(prefix = "Floor ") -> Iterable:
    """
    Get floor key, view_value  from table to load into combobox
    Use to create `ComboboxFilter()`
    """
    floors = Repository[Floor]().get_all()

    members = [(floor.id  , prefix + str(floor.id) ) for floor in floors ]
    return members
def room_type_members() -> Iterable:
    """
    Get members(key, view_value) from Enum class define (not from table) to load in combobox
    Use to create `ComboboxFilter()`
    """
    return tuple((room.name , room.name) for room in RoomType)




class FormComboboxAdapter():
    def __init__(self, combobox_members: Iterable[Tuple[Any , Any]],cmb :  QComboBox ) -> None:
        """
        @combobox_members: list(key_value , view_value)
        key_value is value which will actually interact with database
        view_value is use to display information for human readable
        For example:
        Database room have room_type_id = key_value = 1 which reference to room_type.name = view_value = 'single'
        @cmb: actual combobox item to display in gui
        """
        self.combobox_members = combobox_members
        self.combobox : QComboBox = cmb
        self.set_items()
    def set_items(self):
        self.combobox.clear()
        self.combobox.addItems(self._get_items_view())

    def _get_items_view(self):
        """
        Return a list of view to display in combobox
        Example: ["Floor 1", "Floor 2", "Floor 3"]
        """
        view =  [view_value for key , view_value in self.combobox_members]
        return view
    def set_by_key(self , key ):
        key_idx = 0
        for k , v in self.combobox_members:
            if key ==  k:
                break;
            key_idx += 1
        self.combobox.setCurrentIndex(key_idx)



    def current_key(self):
        """
        Current select key_value for database interaction
        """
        for key , value in self.combobox_members:
            if self.combobox.currentText() == value:
                return key

class ComboboxFilterAdapter():
    """
    Use to load selection for a property in table as combobox
    Auto add items for default select `all_item_selection` like select all items exist
    Example:  Floor >: All, Floor 1, Floor 2, ...
    """
    def __init__(self, combobox_members: Iterable[Tuple[Any , Any]],cmb :  QComboBox , field_name :str , all_view_value = None) -> None:
        """
        field_name use for query condition
        """
        self.combobox_members = combobox_members
        self.combobox = cmb
        self.field_name = field_name
        self.all_view_value= all_view_value
        self.set_items()
    def _get_items_view(self):
        """
        Return a list of view to display in combobox
        Example: ["Floor 1", "Floor 2", "Floor 3"]
        """
        view =  [view_value for key , view_value in self.combobox_members]
        if self.all_view_value:
            view = [self.all_view_value ] + view
        return view
    def set_items(self):
        self.combobox.clear()
        self.combobox.addItems(self._get_items_view())

    def query_condition(self):
        """
        Return a predicate to express user select filter
        Example:
        User select item have text room_type = 'single'
        'single' is room_type.name for actually record of room_type_id = 1
        => return fitler as {"room_type_id" : 1}
        """
        key = self.current_key()
        if key != None:
            return {self.field_name :  key}
        # Key is none when filter for all value of this predicate => Make it always true
        else:
            return None


    def current_key(self):
        for key , value in self.combobox_members:
            if self.combobox.currentText() == value:
                return key


        return None





def query_condition_translator(*predicates) -> str :
    """
    Use to pass a list of combobox filter to change those filter selection to raw query
    :meth:`ComboboxFilter.query_condition()`
    Example:
    Input: ({'floor_id': 2}, {'room_type': 0})
    Output: floor_id = 2 AND room_type = 0
    """
    predicates = [x for x in predicates if x ] # Remove none value
    if not predicates:
        return "1 = 1"
    conditions = []
    for predicate in predicates:
        if predicate:
            for field_name , value in predicate.items():
                condition = field_name + " = "
                if type(value) is int:
                    condition += str(value)

                # Wrap for string, date value like WHERE name = 'abc' AND date = '2024-02-24'
                else:
                    condition += f"'{str(value)}'"
                conditions.append(condition)

    return " AND ".join(conditions)