# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.UGen import UGen


class Trig(UGen):
    """
    A timed trigger.

    ::

        >>> source = ugentools.Dust.kr(1)
        >>> trig = ugentools.Trig.ar(
        ...     duration=0.1,
        ...     source=source,
        ...     )
        >>> trig
        Trig.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Trigger Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'duration',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        duration=0.1,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        duration=0.1,
        source=None,
        ):
        """
        Constructs an audio-rate Trig.

        ::

            >>> source = ugentools.Dust.kr(1)
            >>> trig = ugentools.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig
            Trig.ar()

        Returns ugen graph.
        """
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        duration=0.1,
        source=None,
        ):
        """
        Constructs a control-rate Trig.

        ::

            >>> source = ugentools.Dust.kr(1)
            >>> trig = ugentools.Trig.kr(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig
            Trig.kr()

        Returns ugen graph.
        """
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            duration=duration,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        """
        Gets `duration` input of Trig.

        ::

            >>> source = ugentools.Dust.kr(1)
            >>> trig = ugentools.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig.duration
            0.1

        Returns ugen input.
        """
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def source(self):
        """
        Gets `source` input of Trig.

        ::

            >>> source = ugentools.Dust.kr(1)
            >>> trig = ugentools.Trig.ar(
            ...     duration=0.1,
            ...     source=source,
            ...     )
            >>> trig.source
            OutputProxy(
                source=Dust(
                    calculation_rate=CalculationRate.CONTROL,
                    density=1.0
                    ),
                output_index=0
                )

        Returns ugen input.
        """
        index = self._ordered_input_names.index('source')
        return self._inputs[index]
