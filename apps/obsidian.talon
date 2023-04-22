app: obsidian
-

# go related commands
go settings: key(ctrl-,)
go daily note: user.template("[ctrl-p]daily\n")

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
go tab <number>: key("ctrl-{number}")

# fold plug in commands
fold all: key(alt-f)
insert fold: "%% fold %%"

# archive plug in commands
archive all: key(alt-a)

# templater commands
insert template: key(alt-e)

# tags
tag primary: "#meta/primary "
tag code:    "#code "
tag linux:   "#os/linux "
tag windows: "#os/windows "

# templates
template links: """`= this.links`\n"""
template front links: user.insert_between('links: "Links: [[', ']]" ')
template tags: """Tags: \n"""
template sources: """`= this.sources`\n"""
template front sources: user.insert_between('sources: "Sources: ', '"')
template front matter:
    """
    ---
    description: 
    links: "Links: [[Index]]"
    ---\n
    """

template note top: 
    mimic("template front matter")
    mimic("template tags")
    mimic("template links")
    auto_insert("___\n")

template note bottom:
    auto_insert("___\n")
    mimic("template links")

template note bottom short:
    auto_insert("___\n")
    mimic("template tags")
    mimic("template links")