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



class JSCapture(Select2SingleSelectField):

    def generate_output(self, display_on):
        r=super(JSCapture, self).generate_output(display_on)
	
	r_js=['<script location="%s">%s</script>' % (location, str(js_call)) for js_call, location in self._js_calls]
	r = str(r) + "\n".join(r_js) if r_js else ""
	return "<wrap>"+r+"</wrap>" 

class TestSelect2SingleSelectFieldPreselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
	    
    widget = JSCapture
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 'value': 'Red'}
    params = {}
    # wrap=True doesn't work due to bug in strainer 0.1.4, so we wrap it hardcoded
    expected = """<wrap>
            <select id="select2-test" name="select2-test">
            <option></option><option selected="selected" value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>
            <script location="bodybottom">jQuery("#select2-test").select2({"allow_single_deselect": true})</script>
            <script location="bodybottom">jQuery("#select2-test").select2("val", ["Red"])</script>
            </wrap>"""



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
