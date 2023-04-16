app: obsidian
-

# go related commands
go settings: key(ctrl-,)
go back: key(ctrl-alt-left)
go forward: key(ctrl-alt-right)

# text manipulation
text bold: key(ctrl-b)

# various note insertions
insert comment: user.insert_between('%% ', ' %%')
insert ordered: "1. "
insert unordered: "- "
insert line: "___"
insert location: key("right ( ctrl-v )")
insert heading <number>: key("#:{number} space")
    
# tags
tag primary: "#meta/primary "
tag code:    "#code "
tag linux:   "#os/linux"

# window manipulation
tab last: key(ctrl-shift-tab)
tab next: key(ctrl-tab)
tab close: key(ctrl-w)
tab new: key(ctrl-t)


# fold plug in commands
fold all: key(alt-f)
insert fold: "%% fold %%"

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

template note bottom:
    """
    ___
    Links: [[Index]]
    """

template note bottom short:
    """
    ___
    Tags: 
    Links: [[Index]]
    """