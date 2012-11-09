from tw2.core.testbase import WidgetTest
from tw2.jqplugins.select2.widgets import (
    Select2SingleSelectField,
    Select2MultipleSelectField,
)


class TestSelect2SingleSelectField(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = Select2SingleSelectField
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue']}
    params = {}
    expected = """
    <select id="select2-test" name="select2-test">
            <option></option><option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>"""


class TestSelect2SingleSelectField(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = Select2SingleSelectField
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 'value': 'Red'}
    params = {}
    expected = """
    <select id="select2-test" name="select2-test">
        <option></option>
        <option selected="selected" value="Red">Red</option>
        <option value="Blue">Blue</option>
    </select>"""


class TestSelect2MultipleSelectField(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = Select2MultipleSelectField
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue']}
    params = {}
    expected = """
    <select multiple="multiple" id="select2-test" name="select2-test">
            <option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>"""
