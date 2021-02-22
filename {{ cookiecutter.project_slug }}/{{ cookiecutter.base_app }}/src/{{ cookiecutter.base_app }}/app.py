#!/usr/bin/env python
# coding=utf-8
"""
A simple application using cmd2 which demonstrates 8 key features:

    * Settings
    * Commands
    * Argument Parsing
    * Generating Output
    * Help
    * Shortcuts
    * Multiline Commands
    * History
"""
import argparse

import cmd2
from cmd2 import with_argparser, with_category, CommandSet, Cmd
from {{ cookiecutter.base_app }}.common.screen import banner
from typing import Optional, Iterable
from pluginlib import PluginLoader


def add_settables_from_plugin(cmd: Cmd):
    """ this function will search for plugins with an entrypoint of 
    cmd2_settables and then add settables from them """

    #get all external plugins
    loader = PluginLoader(entry_point='cmd2_settables')
    plugins = loader.plugins

    #If there were any 'Settables' plugins 
    if 'Settables' in plugins.keys():
         
        settable_plugins = [o() for o in plugins.Settables.values()]
        [p.set(cmd) for p in settable_plugins]

class App(Cmd):
    """A simple cmd2 application."""

    def __init__(self, command_sets: Optional[Iterable[CommandSet]] = None):

        shortcuts = cmd2.DEFAULT_SHORTCUTS
        shortcuts.update({'&': 'speak'})
        super().__init__(multiline_commands=['orate'], shortcuts=shortcuts, command_sets=command_sets)

        #set banner
        self.intro = banner()

        #Add settables from external plugins
        add_settables_from_plugin(self)

        # Make maxrepeats settable at runtime
        self.maxrepeats = 3
        self.add_settable(cmd2.Settable('maxrepeats', int, 'max repetitions for speak command'))

    speak_parser = argparse.ArgumentParser()
    speak_parser.add_argument('-p', '--piglatin', action='store_true', help='atinLay')
    speak_parser.add_argument('-s', '--shout', action='store_true', help='N00B EMULATION MODE')
    speak_parser.add_argument('-r', '--repeat', type=int, help='output [n] times')
    speak_parser.add_argument('words', nargs='+', help='words to say')

    @cmd2.with_argparser(speak_parser)
    def do_speak(self, args):
        """Repeats what you tell me to."""
        words = []
        for word in args.words:
            if args.piglatin:
                word = '%s%say' % (word[1:], word[0])
            if args.shout:
                word = word.upper()
            words.append(word)
        repetitions = args.repeat or 1
        for _ in range(min(repetitions, self.maxrepeats)):
            # .poutput handles newlines, and accommodates output redirection too
            self.poutput(' '.join(words))

    # orate is a synonym for speak which takes multiline input
    do_orate = do_speak


