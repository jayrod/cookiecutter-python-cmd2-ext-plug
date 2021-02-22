import pluginlib
from cmd2 import Settable, Cmd

@pluginlib.Parent('Settables')
class BaseSettables(object):
    """ Represents a collection of Cmd2.Settable objects required by a CommandSet
        to function""" 

    def set(self, app: Cmd):
        """ Adds settables to Cmd object"""
        ...
