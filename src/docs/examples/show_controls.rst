.. _example_show_controls:

Showing Controller Properties
=============================

.. image:: show_controls_screenshot.png

This example will get the first available controller, then show (using the curses library) all the buttons and axes
and their values, along with any button presses detected, on the command line. It's an example of how you might query
for what controls are present on a connected controller - for example you might want to do this to check whether the
controller supports ever axis you're going to use later.

.. literalinclude:: ../../../scripts/show_controls.py
    :language: python
    :linenos: