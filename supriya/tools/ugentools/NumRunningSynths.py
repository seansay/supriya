# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.InfoUGenBase import InfoUGenBase


class NumRunningSynths(InfoUGenBase):
    r'''Number of running synths info unit generator.

    ::

        >>> from supriya.tools import ugentools
        >>> ugentools.NumRunningSynths.ir()
        NumRunningSynths.ir()

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        rate=None,
        ):
        InfoUGenBase.__init__(
            self,
            rate=rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def kr(cls, **kwargs):
        from supriya.tools import synthdeftools
        rate = synthdeftools.Rate.CONTROL
        ugen = cls._new_expanded(
            rate=rate,
            **kwargs
            )
        return ugen
