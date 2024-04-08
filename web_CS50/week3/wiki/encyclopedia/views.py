from django.shortcuts import render
from django.shortcuts import redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry_page(request, entry_title):
    entry_content = util.get_entry(entry_title)
    if entry_content:
        return render(request, "encyclopedia/entry.html", {
            "entry_title": entry_title,
            "entry_content": entry_content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "entry_title": entry_title
        })
    
def search(request):
    link = request.GET
    get_str = link["q"]
    list = util.list_entries()
    in_list = [x for x in list if x.lower() == get_str.lower()]
    if in_list:
        return redirect(f"wiki/{in_list[0]}")
    else:
        matching = [s for s in list if get_str.lower() in s.lower()]
        if matching:
            print(matching)
            return render(request, "encyclopedia/suggestions.html", {
                "matching": matching
            })
        else:
            print("NO MATCH")
            return render(request, "encyclopedia/error.html", {
            "entry_title": get_str
        })
        
def suggestions(request):
    return render(request, "suggestions.html")