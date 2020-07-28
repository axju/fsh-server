from fsh import __version__


def fsh(request):
    return {'fsh': {'version': __version__}}
