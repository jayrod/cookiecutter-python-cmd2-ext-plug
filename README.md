
Cookiecutter CMD2 Basic Project 
-------------------------------

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python [CMD2](https://github.com/python-cmd2/cmd2) base application that uses
a plugin from a separate package.

* GitHub repo: https://github.com/jayrod/cookiecutter-python-cmd2-ext-plug
* Documentation: COMING SOON
* Free software: BSD license

Features of generated Applications
--------
* Base Application
* Plugin
* Plugin Settables

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/jayrod/cookiecutter-python-cmd2-ext-plug.git


Reasoning
---------

I wanted to create a more advanced usage example for Cmd2 applications. Through the use of 
the [pluginlib](https://pypi.org/project/pluginlib/) library you can create an extremely 
dynamic cmd2 application. Each plugin created must be installed as a separate application
but will be available in the main cmd2 application. 


This format makes it easy to create a stand alone plugin application while allowing a 
developer to create a composite application based on installed plugins.

