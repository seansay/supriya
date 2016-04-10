# -*- encoding: utf -*-


def bind(source, target, target_range=None, exponent=None):
    from supriya.tools import bindingtools
    binding = bindingtools.Binding()
    binding.bind(source, target, target_range=target_range, exponent=exponent)
    return binding
