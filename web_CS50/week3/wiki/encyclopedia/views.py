from django.shortcuts import render
from django.shortcuts import redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# def text(request, text):
#     entries = util.list_entries
#     return render(request, "encyclopedia/test.html", {
#         "entries": entries
#     })
    
def entry_page(request, entry_title):
    entry_content = util.get_entry(entry_title)
    if entry_content:
        return render(request, "encyclopedia/entry.html", {
            "entry_content": entry_content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "entry_title": entry_title
        })
    
    