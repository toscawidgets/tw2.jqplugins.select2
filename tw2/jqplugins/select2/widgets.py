import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

__all__ = [
    'select2_spinner_img',
    'select2_sprite_img',
    'select2_js',
    'select2_css',
    'Select2SingleSelectField',
    'Select2MultipleSelectField',
    'Select2AjaxSingleSelectField',
]


select2_spinner_img = twc.Link(
    modname=__name__,
    filename='static/spinner.gif')
select2_sprite_img = twc.Link(
    modname=__name__,
    filename='static/select2.png')
select2_js = twc.JSLink(
    modname=__name__,
    filename='static/select2.min.js',
    resources=[twj.jquery_js],
    location='headbottom')
select2_css = twc.CSSLink(
    modname=__name__,
    filename='static/select2.css')


class Select2Mixin(twc.Widget):
    '''Mixin for Select2 SelectFields'''
    resources = [select2_js, select2_css]

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
        super(Select2Mixin, self).prepare()
        # put code here to run just before the widget is displayed
        if 'id' in self.attrs:
            self.selector = "#" + self.attrs['id'].replace(':', '\\:')

        if self.placeholder:
            self.attrs['data-placeholder'] = self.placeholder
        if self.no_results_text:
            self.opts['no_results_text'] = self.no_results_text

        self.add_call(twj.jQuery(self.selector).select2(self.opts))

        if hasattr(self, "value"):
            if self.value is not None:
                values = []

                if isinstance(self.value, str):
                    self.value = [dict(id=self.value)]

                if not isinstance(self.value, list):
                    self.value = [self.value]

                for row in self.value:
                    temp_dict = {}
                    if hasattr(self, "fields"):
                        fields = [a.key for a in self.fields]
                    elif hasattr(row, "__table__"):
                        fields = row.__table__.columns.keys()
                    else:
                        fields = row.keys()

                    if hasattr(row, "__table__"):
                        for field in fields:
                            temp_dict[field] = str(getattr(row, field))
                    else:
                        for field in fields:
                            temp_dict[field] = str(row[field])

                    values.append(temp_dict)

                if "multiple" in self.opts:
                    if self.opts['multiple'] is False and len(values) > 0:
                        values = values[0]

                self.add_call(twj.jQuery(self.selector).select2("val", values))


class Select2SingleSelectField(Select2Mixin, twf.SingleSelectField):
    '''SingleSelectField, enhanced with Select2 javascript'''
    def prepare(self):
        # If field is not required, this adds a button for deselection
        if not self.required:
            self.opts['allow_single_deselect'] = True
        super(Select2SingleSelectField, self).prepare()


class Select2MultipleSelectField(Select2Mixin, twf.MultipleSelectField):
    '''MultipleSelectField, enhanced with Select2 javascript'''
    pass


class Select2AjaxSingleSelectField(Select2SingleSelectField):
    ''' SingleSelectField that can get its values via ajax. '''
    template = "tw2.forms.templates.input_field"
    css_class = "big_drop"
    type = "hidden"
