import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj


chosen_js = twc.JSLink(
    filename='static/chosen.jquery.js',
    resources=[twj.jquery_js]),
chosen_css = twc.CSSLink(filename='static/chosen.css'),


class Chosen(twf.MultipleSelectionField):
    #template = "mako:tw2.jqplugins.chosen.templates.chosen"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [chosen_js, chosen_css]

    selector = twc.Variable("Escaped id.  jQuery selector.")

    def prepare(self):
        super(Chosen, self).prepare()
        # put code here to run just before the widget is displayed
        if 'id' in self.attrs:
            self.selector = "#" + self.attrs['id'].replace(':', '\\:')
        self.add_call(twj.jQuery(self.selector).chosen())
