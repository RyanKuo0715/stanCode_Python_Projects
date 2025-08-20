"""
Stanford CS106AP Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Sonja Johnson-Yu, Kylie Jue, and Nick Bowman.

This file defines the functions needed to create the GUI for
the Baby Names project.

You should not modify any of the contents of this file.
"""

import tkinter


# provided function to build the GUI
def make_gui(top, width, height, names, draw_names, search_names):
    """
    Set up the GUI elements for Baby Names, returning the Canvas to use.
    top is TK root, width/height is canvas size, names is BabyNames dict.
    """
    # name entry field
    label = tkinter.Label(top, text="Names:")
    label.grid(row=0, column=0, sticky='w')
    # 框框左上角的文字：name
    entry = tkinter.Entry(top, width=40, name='entry', borderwidth=2)
    entry.grid(row=0, column=1, sticky='w')
    entry.focus()
    # 輸入name的欄位
    error_out = tkinter.Text(top, height=2, width=70, name='errorout', borderwidth=2)
    error_out.grid(row=0, column=2, sticky='w')
    # name欄位右邊用於顯示錯誤訊息的欄位

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.grid(row=1, columnspan=12, sticky='w')

    space = tkinter.LabelFrame(top, width=10, height=10, borderwidth=0)
    space.grid(row=2, columnspan=12, sticky='w')

    # Search field etc. at the bottom
    label = tkinter.Label(top, text="Search:")
    label.grid(row=3, column=0, sticky='w')
    # 框框左下角的文字：search
    search_entry = tkinter.Entry(top, width=40, name='searchentry')
    search_entry.grid(row=3, column=1, sticky='w')
    # 輸入search名字的欄位
    search_out = tkinter.Text(top, height=2, width=70, name='searchout', borderwidth=2)
    search_out.grid(row=3, column=2, sticky='w')
    # 顯示搜尋名字的欄位

    # When <return> key is hit in a text field .. connect to the handle_draw()
    # and handle_search() functions to do the work.
    entry.bind("<Return>", lambda event: handle_draw(entry, canvas, names, error_out, draw_names))
    # 給entry欄位的指令，也就是輸入名字之後要做的事
    # "<Return>"代表按下enter鍵後就要執行指令
    # lambda event代表按下enter鍵後要執行的指令
    search_entry.bind("<Return>", lambda event: handle_search(search_entry, search_out, names, search_names))
    # 給search_entry欄位的指令，也就是輸入搜尋文字後要做的事

    top.update()
    return canvas


def handle_draw(entry, canvas, names, error_out, draw):
    """
    (provided)
    Called when <return> key hit in given entry text field.
    Gets search text from given entry, draws results
    to the given canvas.
    """
    text = entry.get()
    lookups = [name[0].upper() + name[1:].lower() for name in text.split()]  # handles casing

    invalid_names = [name for name in lookups if name not in names]
    lookups = [name for name in lookups if name in names]

    # Handle error message
    error_out.delete('1.0', tkinter.END)
    if invalid_names:
        if len(invalid_names) == 1:
            out = invalid_names[0] + ' is not contained in the name database.'
        else:
            out = ', '.join(invalid_names) + ' are not contained in the name database.'
        error_out.insert('1.0', out)

    draw(canvas, names, lookups)


def handle_search(search_entry, search_out, names, search):
    """
    (provided) Called for <return> key in lower search field.
    Calls babynames.search() and displays results in GUI.
    Gets search target from given search_entry, puts results
    in given search_out text area.
    """
    target = search_entry.get().strip()
    if target:
        # Call the search_names function in babynames.py
        result = search(names, target)
        out = ' '.join(result)
        search_out.delete('1.0', tkinter.END)
        search_out.insert('1.0', out)
