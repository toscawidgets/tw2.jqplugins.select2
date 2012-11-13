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

# single select, ondemand=False, one selected
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
            <script location="bodybottom">jQuery("#select2-test").select2("val", "Red")</script>
            </wrap>"""


# single select, ondemand=False, two selected
class TestSelect2SingleSelectField2Preselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
	    
    widget = JSCapture
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value': ['Red', 'Blue']}
    params = {}
    # wrap=True doesn't work due to bug in strainer 0.1.4, so we wrap it hardcoded
    expected = """<wrap>
            <select id="select2-test" name="select2-test">
            <option></option><option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>
            <script location="bodybottom">jQuery("#select2-test").select2({"allow_single_deselect": true})</script>
            <script location="bodybottom">jQuery("#select2-test").select2("val", "Red")</script>
            </wrap>"""

# single select, ondemand=True, one selected
class TestSelect2SingleSelectFieldOnDemandPreselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
	    
    widget = JSCapture
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value': 'Red', 'ondemand':True}
    params = {}
    # wrap=True doesn't work due to bug in strainer 0.1.4, so we wrap it hardcoded
    expected = """<wrap>
            <input class="big_drop" name="select2-test" id="select2-test"/>
<script location="bodybottom">jQuery("#select2-test").select2({"allow_single_deselect": true, "multiple": false, "data": [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}]})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", {"text": "Red", "id": "Red"})</script>
            </wrap>"""


# single select, ondemand=True, two selected
class TestSelect2SingleSelectFieldOnDemand2Preselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
	    
    widget = JSCapture
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value': ['Red', 'Blue'], 'ondemand':True}
    params = {}
    # wrap=True doesn't work due to bug in strainer 0.1.4, so we wrap it hardcoded
    expected = """<wrap>
            <input class="big_drop" name="select2-test" id="select2-test"/>
<script location="bodybottom">jQuery("#select2-test").select2({"allow_single_deselect": true, "multiple": false, "data": [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}]})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", {"text": "Red", "id": "Red"})</script>
            </wrap>"""

class JSCaptureMulti(Select2MultipleSelectField):

    def generate_output(self, display_on):
        r=super(JSCaptureMulti, self).generate_output(display_on)
	
	r_js=['<script location="%s">%s</script>' % (location, str(js_call)) for js_call, location in self._js_calls]
	r = str(r) + "\n".join(r_js) if r_js else ""
	return "<wrap>"+r+"</wrap>" 

# multiple select, ondemand=False, none selected
class TestSelect2MultipleSelectField0Preselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue']}
    params = {}
    expected = """<wrap>
    <select multiple="multiple" id="select2-test" name="select2-test">
            <option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>
<script location="bodybottom">jQuery("#select2-test").select2({})</script>
</wrap>"""

# multiple select, ondemand=False, one selected
class TestSelect2MultipleSelectField1Preselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 'value':"Red"}
    params = {}
    expected = """<wrap>
    <select multiple="multiple" id="select2-test" name="select2-test">
            <option selected="selected" value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>
<script location="bodybottom">jQuery("#select2-test").select2({})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", ["Red"])</script>
</wrap>"""

# multiple select, ondemand=False, two selected
class TestSelect2MultipleSelectField2Preselect(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value':["Red", "Blue"]}
    params = {}
    expected = """<wrap>
    <select multiple="multiple" id="select2-test" name="select2-test">
            <option selected="selected" value="Red">Red</option><option
            selected="selected" value="Blue">Blue</option>
            </select>
<script location="bodybottom">jQuery("#select2-test").select2({})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", ["Red", "Blue"])</script>
</wrap>"""

# multiple select, ondemand=True, none selected
class TestSelect2MultipleSelectFieldOnDemand0(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 'ondemand':True}
    params = {}
    expected = """<wrap>
<input multiple="multiple" class="big_drop" name="select2-test" id="select2-test"/>
<script location="bodybottom">jQuery("#select2-test").select2({"data": [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}], "multiple": true})</script>
</wrap>"""

# multiple select, ondemand=True, one selected
class TestSelect2MultipleSelectFieldOnDemand1(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value':["Red"], 'ondemand':True}
    params = {}
    expected = """<wrap>
<input multiple="multiple" class="big_drop" name="select2-test" id="select2-test"/>
<script location="bodybottom">jQuery("#select2-test").select2({"data": [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}], "multiple": true})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", [{"text": "Red", "id": "Red"}])</script>
</wrap>"""

# multiple select, ondemand=True, two selected
class TestSelect2MultipleSelectFieldOnDemand2(WidgetTest):
    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = JSCaptureMulti
    # Initialization args. go here
    attrs = {'id': 'select2-test', 'options': ['Red', 'Blue'], 
             'value':["Red", "Blue"], 'ondemand':True}
    params = {}
    expected = """<wrap>
<input multiple="multiple" class="big_drop" name="select2-test" id="select2-test"/>
<script location="bodybottom">jQuery("#select2-test").select2({"data": [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}], "multiple": true})</script>
<script location="bodybottom">jQuery("#select2-test").select2("val", [{"text": "Red", "id": "Red"}, {"text": "Blue", "id": "Blue"}])</script>
</wrap>"""
