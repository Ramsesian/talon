app: obsidian
-

# go related commands
go settings: key(ctrl-,)
go back: key(ctrl-alt-left)
go forward: key(ctrl-alt-right)

# text manipulation
text bold: key(ctrl-b)
text italic: key(ctrl-i)

# various note insertions
insert comment: user.insert_between('%% ', ' %%')
insert heading <number>: key("#:{number} space")
insert line: "___"
insert link: user.insert_between('[[', ']]')
insert location: key("right ( ctrl-v )")

insert ordered: "1. "
insert unordered: "- "

insert admonition: "> [!note]- "
insert admonition important: "> [!important]- "

# tags
tag primary: "#meta/primary "
tag code:    "#code "
tag linux:   "#os/linux"

# window manipulation
tab last: key(ctrl-shift-tab)
tab next: key(ctrl-tab)
tab close: key(ctrl-w)
tab new: key(ctrl-t)
 
# search
find new: key(ctrl-f)
find next: key(f3)
find last: key(shift-f3)
find cancel: key(escape)

# miscellaneous commands
please: key(ctrl-p)
left bar switch: user.template("[ctrl-p]toggle left s\n")
right bar switch: user.template("[ctrl-p]toggle right\n")
view switch: key(ctrl-e)

# fold plug in commands
fold all: key(alt-f)
insert fold: "%% fold %%"

# archive plug in commands
archive all: key(alt-a)




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