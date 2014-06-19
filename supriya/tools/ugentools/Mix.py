# -*- encoding: utf-8 -*-
from abjad.tools import sequencetools
from supriya.tools.ugentools.PseudoUGen import PseudoUGen


class Mix(PseudoUGen):
    r'''Mix signals down to mono.

    ::

        >>> from supriya.tools import synthdeftools
        >>> from supriya.tools import ugentools

    ::

        >>> oscillators = [ugentools.DC.ar(1) for _ in range(5)]
        >>> mix = ugentools.Mix.new(oscillators)
        >>> synthdef = synthdeftools.SynthDef('mix1')
        >>> synthdef.add_ugen(mix)
        >>> print(synthdef)
        SynthDef mix1 {
            const_0:1.0 -> 0_DC[0:source]
            const_0:1.0 -> 1_DC[0:source]
            const_0:1.0 -> 2_DC[0:source]
            const_0:1.0 -> 3_DC[0:source]
            0_DC[0] -> 4_Sum4[0:input_one]
            1_DC[0] -> 4_Sum4[1:input_two]
            2_DC[0] -> 4_Sum4[2:input_three]
            3_DC[0] -> 4_Sum4[3:input_four]
            const_0:1.0 -> 5_DC[0:source]
            4_Sum4[0] -> 6_BinaryOpUGen:ADD[0:left]
            5_DC[0] -> 6_BinaryOpUGen:ADD[1:right]
        }

    ::

        >>> oscillators = [ugentools.DC.ar(1) for _ in range(15)]
        >>> mix = ugentools.Mix.new(oscillators)
        >>> synthdef = synthdeftools.SynthDef('mix2')
        >>> synthdef.add_ugen(mix)
        >>> print(synthdef)
        SynthDef mix2 {
            const_0:1.0 -> 0_DC[0:source]
            const_0:1.0 -> 1_DC[0:source]
            const_0:1.0 -> 2_DC[0:source]
            const_0:1.0 -> 3_DC[0:source]
            0_DC[0] -> 4_Sum4[0:input_one]
            1_DC[0] -> 4_Sum4[1:input_two]
            2_DC[0] -> 4_Sum4[2:input_three]
            3_DC[0] -> 4_Sum4[3:input_four]
            const_0:1.0 -> 5_DC[0:source]
            const_0:1.0 -> 6_DC[0:source]
            const_0:1.0 -> 7_DC[0:source]
            const_0:1.0 -> 8_DC[0:source]
            5_DC[0] -> 9_Sum4[0:input_one]
            6_DC[0] -> 9_Sum4[1:input_two]
            7_DC[0] -> 9_Sum4[2:input_three]
            8_DC[0] -> 9_Sum4[3:input_four]
            const_0:1.0 -> 10_DC[0:source]
            const_0:1.0 -> 11_DC[0:source]
            const_0:1.0 -> 12_DC[0:source]
            const_0:1.0 -> 13_DC[0:source]
            10_DC[0] -> 14_Sum4[0:input_one]
            11_DC[0] -> 14_Sum4[1:input_two]
            12_DC[0] -> 14_Sum4[2:input_three]
            13_DC[0] -> 14_Sum4[3:input_four]
            const_0:1.0 -> 15_DC[0:source]
            const_0:1.0 -> 16_DC[0:source]
            const_0:1.0 -> 17_DC[0:source]
            15_DC[0] -> 18_Sum3[0:input_one]
            16_DC[0] -> 18_Sum3[1:input_two]
            17_DC[0] -> 18_Sum3[2:input_three]
            4_Sum4[0] -> 19_Sum4[0:input_one]
            9_Sum4[0] -> 19_Sum4[1:input_two]
            14_Sum4[0] -> 19_Sum4[2:input_three]
            18_Sum3[0] -> 19_Sum4[3:input_four]
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PUBLIC METHODS ###

    @staticmethod
    def new(sources):
        from supriya.tools import synthdeftools
        from supriya.tools import ugentools
        sources = synthdeftools.UGenArray(sources)
        summed_sources = []
        parts = sequencetools.partition_sequence_by_counts(
            sources,
            [4],
            cyclic=True,
            overhang=True,
            )
        for part in parts:
            if len(part) == 4:
                summed_sources.append(ugentools.Sum4(*part))
            elif len(part) == 3:
                summed_sources.append(ugentools.Sum3(*part))
            elif len(part) == 2:
                summed_sources.append(part[0] + part[1])
            else:
                summed_sources.append(part[0])
        if len(summed_sources) == 1:
            return summed_sources[0]
        return Mix.new(summed_sources) 
