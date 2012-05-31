import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

__all__ = [
    'chosen_img',
    'chosen_js',
    'chosen_css',
    'ChosenSingleSelectField',
    'ChosenMultipleSelectField']


chosen_img = twc.Link(filename='static/chosen-sprite.png')
chosen_js = twc.JSLink(
    filename='static/chosen.jquery.js',
    resources=[twj.jquery_js],
    location='headbottom')
chosen_css = twc.CSSLink(filename='static/chosen.css')


class ChosenMixin(twc.Widget):
    '''Mixin for Chosen SelectFields'''
    resources = [chosen_js, chosen_css]

    selector = twc.Variable("Escaped id.  jQuery selector.")
    opts = twc.Variable(
        'Arguments for the javascript init function',
        default=dict())

    placeholder = twc.Param(
        'Placeholder text, prompting user for selection',
        default='')
    no_results_text = twc.Param(
        'Text shown when the search term returned no results',
        default='')

    def prepare(self):
        super(ChosenMixin, self).prepare()
        # put code here to run just before the widget is displayed
        if 'id' in self.attrs:
            self.selector = "#" + self.attrs['id'].replace(':', '\\:')

        if self.placeholder:
            self.attrs['data-placeholder'] = self.placeholder
        if self.no_results_text:
            self.opts['no_results_text'] = self.no_results_text

        self.add_call(twj.jQuery(self.selector).chosen(self.opts))


class ChosenSingleSelectField(ChosenMixin, twf.SingleSelectField):
    '''SingleSelectField, enhanced with Chosen javascript'''
    def prepare(self):
        # If field is not required, this adds a button for deselection
        if not self.required:
            self.opts['allow_single_deselect'] = True
        super(ChosenSingleSelectField, self).prepare()


class ChosenMultipleSelectField(ChosenMixin, twf.MultipleSelectField):
    '''MultipleSelectField, enhanced with Chosen javascript'''
    pass
