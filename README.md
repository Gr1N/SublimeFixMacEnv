# SublimeFixMacEnv

Inspired by [Fix Mac Path](https://github.com/int3h/SublimeFixMacPath) plugin.

On OS X, Sublime Text has its PATH set by launchctl, not by your shell<sup>1</sup>. Commands like `make` run by Sublime Text are then unable to find non-system binaries, including those installed by Homebrew or MacPorts.

*SublimeFixMacEnv* is a very simple plugin for Sublime Text 3 which sets any env variable correctly os OS X.

<sup>1: This isn't true if you launch Sublime Text from within your shell (e.g., with the `subl` command.)</sup>

# Install

*SublimeFixMacEnv* is for Sublime Text 3 running on Mac OS X. (Other platforms don't suffer from the problem this plugin fixes, to my knowledge, so it isn't needed.)

To install *SublimeFixMacEnv*, run:

    git clone https://github.com/Gr1N/SublimeFixMacEnv.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/SublimeFixMacEnv

# Configuration

You can set up any environment variable, e.g.:

    {
      "env": {
        "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin",
        "GOPATH": "/Users/username/Go"
      }
    }

# TODO

- [ ] Submit package to [Package Control](http://wbond.net/sublime_packages/package_control)

# License

*SublimeFixMacEnv* is licensed under the MIT license. See the license file for details.
