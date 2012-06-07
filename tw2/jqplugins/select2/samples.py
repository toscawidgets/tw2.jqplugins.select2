"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from widgets import *


class DemoSelect2SingleSelectField(Select2SingleSelectField):
    options = [('Group 1', ['Item 1', 'Item 2']),
        ('Group 2', ['Item 3', 'Item 4', 'Item 5', 'Item 6'])]
    value = 'Item 2'
    attrs = dict(style='width: 200px')


class DemoSelect2MultipleSelectField(Select2MultipleSelectField):
    options = [('Group 1', ['Item 1', 'Item 2']),
        ('Group 2', ['Item 3', 'Item 4', 'Item 5', 'Item 6'])]
    #value = ['Item 2', 'Item 5']
    placeholder = 'Select an item, you won\'t regret it'
    attrs = dict(style='width: 400px')
