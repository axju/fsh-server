from pkg_resources import get_distribution, DistributionNotFound


try:
    __version__ = get_distribution('fsh').version
except:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
