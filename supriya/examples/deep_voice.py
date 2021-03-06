#! /usr/bin/env python
# -*- encoding: utf-8 -*-
from abjad import *
from supriya import servertools
from supriya import synthdeftools
from supriya import ugentools


def run_demo():

    server = servertools.Server().boot()

    stereo_input_buses = server.audio_input_bus_group[:2]
    stereo_output_buses = server.audio_output_bus_group[:2]

    synthdef_builder = synthdeftools.SynthDefBuilder(
        pitch_ratio=5. / 7.,
        )
    with synthdef_builder:
        microphone_input = stereo_input_buses.ar()
        compressor = ugentools.Compander.ar(
            source=microphone_input,
            control=ugentools.Mix.new(microphone_input),
            clamp_time=0.01,
            relax_time=0.01,
            slope_above=0.5,
            slope_below=1,
            threshold=0.25,
            )
        pitch_shift = ugentools.PitchShift.ar(
            pitch_dispersion=0.05,
            pitch_ratio=ugentools.Lag.kr(
                source=synthdef_builder['pitch_ratio'],
                lag_time=2.0,
                ),
            source=compressor,
            time_dispersion=0.05,
            window_size=0.2,
            )
        reverb = ugentools.FreeVerb.ar(
            damping=0.8,
            mix=0.33,
            room_size=0.5,
            source=pitch_shift,
            )
        speaker_output = ugentools.Out.ar(
            bus=stereo_output_buses,
            source=reverb,
            )

    synthdef = synthdef_builder.build()
    synth = servertools.Synth(synthdef)
    synth.allocate(
        sync=True,
        target_node=server,
        )

    server.meters.allocate()

    return server, synthdef, synth


if __name__ == '__main__':
    server, synthdef, synth = run_demo()
