app: obsidian
-

# go related commands
go settings: key(ctrl-,)
go back: key(ctrl-alt-left)
go forward: key(ctrl-alt-right)

# text manipulation
text bold: key(ctrl-b)
insert comment: user.insert_between('%% ', ' %%')
insert ordered: "1. "
insert unordered: "- "
insert location: key("right ( ctrl-v )")
    
heading <number>: key("#:{number} space")
    

# templates
template note top: 
    """
    ---
    description: 
    ---

    Tags: 
    Links: [[Index]]
    ___
    """

# tags
tag primary: "#meta/primary "
tag code: "#code "

# window manipulation
tab last: key(ctrl-shift-tab)
tab next: key(ctrl-tab)
tab close: key(ctrl-w)
tab new: key(ctrl-t)


# fold plug in commands
fold all: key(alt-f)
insert fold: "%% fold %%"
