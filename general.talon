# regular short hands
forge: key(delete)
where: key(backspace)
daughter: ". "
cool gap: ": "

# new insides
inside angle: user.insert_between("<", ">")
inside scare: user.insert_between('"', '"')
inside slash: user.insert_between('/', '/')
inside dock string: user.insert_between('"""', '"""')

# word fixes
word console: "console"
word flatpack: "flatpak"
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
dust <user.symbol_key>: " {symbol_key} "