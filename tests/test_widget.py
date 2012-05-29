from tw2.core.testbase import WidgetTest
from tw2.jqplugins.chosen import *

class Chosen(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Chosen
    # Initilization args. go here 
    attrs = {'id':'chosen-test'}
    params = {}
    expected = """<div id="chosen-test"></div>"""
