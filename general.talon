# regular short hands
forge: key(delete)
where: key(backspace)
daughter: ". "
cool gap: ": "
pad right: key(space left)
replace [<number>]:
    remove = number or 1
    key("backspace:{remove} space")

# new insides
inside angle: user.insert_between("<", ">")
inside scare: user.insert_between('"', '"')
inside slash: user.insert_between('/', '/')
inside dock string: user.insert_between('"""', '"""')

# word fixes
word console: "console"
word aline: "align"
word git: "git"
word clothes: "close"
word misc: "misc"

# additional file extensions
dot tzo: ".tzo" 

# allow aces to new symbols
symbol long dash: "—"

# spacing commands
dust line: key(enter:2 up)
dust fat arrow: " => "
dust arrow: " -> "
dust match: " == "
dust strict match: " === "
dust <user.letter>: " {letter} "
dust <user.symbol_key>: " {symbol_key} "

# miscellaneous commands
capitalize that:
    mimic("before that")
    mimic("select word")
    mimic("title that")

#test:   
    #insert("test")
    #c#user.engine_mimic("capitalize that")

