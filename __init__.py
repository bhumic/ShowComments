from binaryninja import *

def show_comments(bv):
    comments = []
    for func in bv.functions:
        if func.comments:
            for offset, value in func.comments.iteritems():
                comments.append((offset, value))
    comments = [str(hex(offset)).strip("L") + ": " + value for offset, value in sorted(comments, key = lambda tup: tup[0])]
    choice   = get_choice_input("Show Comments", "Comments", comments)
    if choice:
        offset = int(comments[choice].split(":", 1)[0], 16)
        bv.navigate(bv.view, offset)
    
PluginCommand.register("Comments...", "Show defined comments", show_comments)