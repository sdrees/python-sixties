# -*- coding: utf-8 -*-

# [[[fill git_describe()]]]
__version__ = '2022.7.17'
# [[[end]]]
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
