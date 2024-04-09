from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
import markdown2
import os

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Title",
                "required": "required",
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Write content here in Markdown",
                "style": "height: 100px",
                "required": "required",
            }
        )
    )


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry_page(request, entry_title):
    entry_content = util.get_entry(entry_title)
    if entry_content:
        return render(
            request,
            "encyclopedia/entry.html",
            {
                "entry_title": entry_title,
                "entry_content": markdown2.markdown(entry_content),
            },
        )
    else:
        return render(
            request,
            "encyclopedia/error.html",
            {"error_message": f"WIKI { entry_title } Not Found"},
        )


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
            return render(
                request, "encyclopedia/suggestions.html", {"matching": matching}
            )
        else:
            print("NO MATCH")
            return render(request, "encyclopedia/error.html", {"entry_title": get_str})


def suggestions(request):
    return render(request, "suggestions.html")


def add_page(request):
    if request.method == "POST":
        submited_form = NewEntryForm(request.POST)
        if submited_form.is_valid():
            # print(submited_form)
            title = submited_form.cleaned_data["title"]
            existing_entries = util.list_entries()
            if title in existing_entries:
                return render(
                    request,
                    "encyclopedia/error.html",
                    {"error_message": f"Wiki '{title}' already exists"},
                )
            subdirectory_path = "entries/"
            path_title = title.replace(" ", "_")
            file_path = os.path.join(subdirectory_path, f"{path_title}.md")
            content = submited_form.cleaned_data["content"]
            print(file_path)
            with open(file_path, "w") as file:
                file.write(f"#{title}\n\n")
                file.write(content)
            return redirect(f"wiki/{path_title}")

    return render(request, "encyclopedia/add_page.html", {"form": NewEntryForm()})
