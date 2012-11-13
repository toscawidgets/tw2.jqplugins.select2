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
    ondemand = twc.Param(
        """If true no select or option elements are created but all is 
           handled through a hidden input element.
           You need this if you want load data on demand (through ajax).""",
        default=False)


    def options2data(self, options):
        """Turn the options data into a list of 
        dict(id=<idvalue>, text=<textvalue> as select2
        expects them if set on initialization."""

        data=[]
        while options:
            entry=options.pop(0)
            if isinstance(entry, basestring):
                data.append(dict(id=entry, text=entry))
            elif isinstance(entry, tuple):
                # if the 2nd value in the tuple is a list, then our 
                # entry represents a group and we simply
                # push the elements of the group into our todo list
                if len(entry)>1:
                    if isinstance(entry[1], list): 
                        options[:0] = entry[1]
                    else:
                        data.append(dict(id=entry[0], text=entry[1]))
        return data

    def prepare(self):
	self.opts = self.opts.copy()

        # if we are a subclass of MultipleSelectField
        # we need to tell select2, we want multiple selection
        multiple = issubclass(self.__class__, 
                              twf.MultipleSelectField)
	if self.ondemand:
	    self.template = "tw2.forms.templates.input_field"
	    self.css_class = "big_drop"
	    self.type = "hidden"

            # only tell select2 if its attached to an input element
            self.opts["multiple"] = multiple

	    # if we have something in self.options turn it into an 
            # array of {id:, text:} dicts
	    # but don't try it if there is a data entry in opt already
	    if self.options and "data" not in self.opts:
                data = self.options2data(self.options[:])
		if data:
		    self.opts["data"] = data
		    
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

                if isinstance(self.value, basestring):
                    self.value = [dict(id=self.value, text=self.value)]

                if not isinstance(self.value, list):
                    self.value = [self.value]
                else:
                    # all plain text entries are turned into dicts
                    def str2dict(elem):
                        if isinstance(elem, basestring):
                            return dict(id=elem, text=elem)
                        return elem
                    self.value = map(str2dict, self.value)
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
                            temp_dict[field] = unicode(getattr(row, field))
                    else:
                        for field in fields:
                            temp_dict[field] = unicode(row[field])

                    values.append(temp_dict)

                # if not attached to input element, we are
                # dealing only with plain values
                if not self.ondemand:
                    values = [entry["id"] for entry in values 
                              if entry.has_key("id")]
                if not multiple and len(values) > 0:
                    values = values[0]

                if values:
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
    #template = "tw2.forms.templates.input_field"
    #css_class = "big_drop"
    #type = "hidden"
    ondemand=True
