# -*- coding: utf-8 -*-

import sys
import os

import sublime


VERSION = '0.0.1'

_SETTINGS = None
_ENV = {k: v for k, v in os.environ.items()}


def fix_env():
    for k, v in get_env_to_fix().items():
        os.environ[k] = v


def get_env_to_fix():
    return {
        str(k).upper(): v
        for k, v in _SETTINGS.get('env', {}).items()
    }


def _plugin_loaded():
    global _SETTINGS
    _SETTINGS = sublime.load_settings('SublimeFixMacEnv.sublime-settings')
    _SETTINGS.clear_on_change('sublimefixmacenv-reload')
    _SETTINGS.add_on_change('sublimefixmacenv-reload', fix_env)

    fix_env()


def _plugin_unloaded():
    for k in get_env_to_fix().keys():
        v = _ENV.get(k)
        if v:
            os.environ[k] = v

    global _SETTINGS
    _SETTINGS.clear_on_change('sublimefixmacenv-reload')


is_darwin = sys.platform == 'darwin'
if is_darwin:
    plugin_loaded = _plugin_loaded
    plugin_unloaded = _plugin_unloaded
else:
    print('`FixMacEnv` will not be loaded because OS ({0}) not supported;'
          ' Plugin supports only OS X'.format(sys.platform))
