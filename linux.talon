os: linux
-

# window movement commands
tux move up: key(shift-super-up)
tux move down: key(shift-super-down)
tux rotate: key(super-o)

# window focus commands
tux up: key(ctrl-super-up)
tux down: key(ctrl-super-down)
tux focus <user.arrow_key>: key("super-{arrow_key}")
tux focus max: key(super-m)
tux full: key(f11)

# shut down menu commands
tux lock: key(super-escape)
tux menu: user.move_click(1860, 12)
tux shutdown:
    mimic("tux menu")
    sleep(200ms)
    key(down:9 right down:2)

# keyboard commands
keyboard switch: key(super-space)
keyboard change input:
    user.move_click(1757, 17)
    sleep(200ms)
    key(down:3 right down enter)

# miscellaneous system commands
tux search: key(super)

# app runners
# alt-f2  opens the command runner
tux open term: key(super-t)
tux open term normal: key(super-c)
tux open browse: key(super-b)
tux open firefox: key(super-w)
tux open files: key(super-f)
tux open settings: key(super-s)

# not key bound app runners
tux open commandline:
    key(alt-f2)
    sleep(200ms)

tux open code:  
    mimic("tux open commandline")
    auto_insert("code\n")

tux open discord:
    mimic("tux open commandline")
    auto_insert("flatpak run com.discordapp.Discord\n")

tux open obs:
    mimic("tux open commandline")
    auto_insert("flatpak run com.obsproject.Studio\n")

tux open obsidian:
    mimic("tux open commandline")
    auto_insert("flatpak run md.obsidian.Obsidian\n")

tux open office: 
    mimic("tux open commandline")
    auto_insert("libreoffice\n")
    
tux open study:
    mimic("tux open commandline")
    auto_insert("flatpak run net.ankiweb.Anki\n")

tux open telegram:
    mimic("tux open commandline")
    auto_insert("flatpak run org.telegram.desktop\n")

tux open tor:
    mimic("tux open commandline")
    auto_insert("flatpak run com.github.micahflee.torbrowser-launcher\n")

tux open torrent:
    mimic("tux open commandline")
    auto_insert("flatpak run org.qbittorrent.qBittorrent\n")

# opens popular locations in code   
code open assignment tracker:  
    mimic("tux open commandline")
    auto_insert("code my-stuff/scripts/assignment-tracker/\n")
    
code open talon:
    mimic("tux open commandline")
    auto_insert("code .talon\n")

code open web:
    mimic("tux open commandline")
    auto_insert("code /home/rowan/my-stuff/web/\n")

# dismisses the telegram notifications I occasionally get
telegram dismiss: move_click(1899, 1013)