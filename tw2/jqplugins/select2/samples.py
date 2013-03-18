"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
from widgets import *

# note: this may be subject to change
APIKEY = "ju6z9mjyajq2djue3gbvv26t"

class DemoSelect2SingleSelectField(Select2SingleSelectField):
    options = [('Group 1', ['Item1', 'Item2']),
               ('Group 2', ['Item3', 'Item4', 'Item5', 'Item6'])]
    value = 'Item2'
    attrs = dict(style='width: 200px')
    ondemand=True

class DemoSelect2AjaxSingleSelectField(Select2AjaxSingleSelectField):

    resources = [twc.CSSSource(location="headbottom",
        src=""" 
            .zebra { background-color: #efefef; }
             img.flag { height: 10px; width: 15px; padding-right: 10px; }
            .movie-result td {vertical-align: top }
            .movie-image { width: 60px; }
            .movie-image img { height: 80px; width: 60px;  }
            .movie-info { padding-left: 10px; vertical-align: top; }
            .movie-title { font-size: 1.2em; padding-bottom: 15px; }
            .movie-synopsis { font-size: .8em; color: #888; }
            .select2-highlighted .movie-synopsis { font-size: .8em; color: #eee; }
            .bigdrop.select2-container .select2-results {max-height: 300px;}
            .bigdrop .select2-results {max-height: 300px;}
            """
            )]

    attrs = dict(style='width: 100%;')
    options = []
    opts = dict(
        #placeholder=dict(title="Search for a movie", id=""),
        placeholder="Search for a movie...",
        minimumInputLength=2,
        ajax=dict(
            # instead of writing the function to execute the
            # request we use Select2's convenient helper
            url="http://api.rottentomatoes.com/api/public/v1.0/movies.json",
            dataType='jsonp',
            data=twc.js_callback(
                """
                function (term, page) {
                    return {
                        q: term, // search term
                        page_limit: 10,
                        apikey: "%s"
                    };
                }
                """ % APIKEY ),
            results=twc.js_callback(
                """
                function (data, page) {
                    // parse the results into the format expected by Select2.
                    // since we are using custom formatting functions we do
                    // not need to alter remote JSON data
                    return {results: data.movies};
                }
                """),
        ),
        initSelection=twc.js_callback("""
            function(element, callback) {
             // the input tag has a value attribute preloaded that points to a 
             //preselected movie's id.  This function resolves that id attribute
             // to an object that select2 can render using its formatResult 
             // renderer - that way the movie name is shown preselected
                var id=$(element).val();
                if (id!=="") {
                  $.ajax("http://api.rottentomatoes.com/api/public/v1.0/movies/"+id+".json", {
                    data: {
                      apikey: "%s"
                    },
                    dataType: "jsonp"
                  }).done(function(data) { callback(data); });
                }
             }
            """ % APIKEY),
        formatSelection=twc.js_callback(
            """
            function (movie) {
                return movie.title;
            }
            """),
        formatResult=twc.js_callback(
            """
            function (movie) {
                var markup = "<table class='movie-result'><tr>";
                if (movie.posters !== undefined && movie.posters.thumbnail !== undefined) {
                    markup += "<td class='movie-image'><img src='" + movie.posters.thumbnail + "'/></td>";
                }
                markup += "<td class='movie-info'><div class='movie-title'>" + movie.title + "</div>";
                if (movie.critics_consensus !== undefined) {
                    markup += "<div class='movie-synopsis'>" + movie.critics_consensus + "</div>";
                }
                else if (movie.synopsis !== undefined) {
                    markup += "<div class='movie-synopsis'>" + movie.synopsis + "</div>";
                }
                markup += "</td></tr></table>"
                return markup;
            }
            """),
    )


class DemoSelect2MultipleSelectField(Select2MultipleSelectField):
    options = [('Group 1', ['Item 1', 'Item 2']),
        ('Group 2', ['Item 3', 'Item 4', 'Item 5', 'Item 6'])]
    #value = ['Item 2', 'Item 5']
    placeholder = 'Select an item, you won\'t regret it'
    attrs = dict(style='width: 400px')
