# -*- encoding: utf-8 -*-
from supriya.library.responselib.ServerResponse import ServerResponse


class NSetItem(ServerResponse):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_control_index_or_name',
        '_control_value',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        control_index_or_name=None,
        control_value=None,
        ):
        self._control_index_or_name = control_index_or_name
        self._control_value = control_value

    ### PUBLIC PROPERTIES ###

    @property
    def control_index_or_name(self):
        return self._control_index_or_name

    @property
    def control_value(self):
        return self._control_value