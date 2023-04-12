os: linux
-
keyboard switch: key(super-space)
keyboard change input:
    mouse_move(1757, 17)
    mouse_click(0)
    sleep(200ms)
    mouse_move(1739, 156)
    mouse_click(0)
    sleep(200ms)
    mouse_move(1749, 231)
    mouse_click(0)
    sleep(200ms)

tux search: key(super)
tux lock: key(super-escape)
tux up: key(ctrl-super-up)
tux down: key(ctrl-super-down)
tux shift up: key(shift-super-up)
tux shift down: key(shift-super-down)
tux rotate: key(super-o)

tux focus <user.arrow_key>: key("super-{arrow_key}")
tux switch: key(super-m)

# app runners
# alt-f2  opens the command runner
tux open term: key(super-t)
tux open term normal: key(super-c)
tux open browse: key(super-b)
tux open firefox: key(super-w)
tux open files: key(super-f)
tux open settings: key(super-s)

tux open commandline:
    key(alt-f2)
    sleep(200ms)

tux open tor:
    mimic("tux open commandline")
    user.template("flatpak run com.github.micahflee.torbrowser-launcher[enter]")

tux open torrent:
    mimic("tux open commandline")
    user.template("flatpak run org.qbittorrent.qBittorrent[enter]")

tux open office: 
    mimic("tux open commandline")
    user.template("libreoffice[enter]")
    
tux open study:
    mimic("tux open commandline")
    user.template("flatpak run net.ankiweb.Anki[enter]")

tux open code:  
    mimic("tux open commandline")
    user.template("code[enter]")

tux open obsidian:
    mimic("tux open commandline")
    user.template("flatpak run md.obsidian.Obsidian[enter]")

tux open discord:
    mimic("tux open commandline")
    user.template("flatpak run com.discordapp.Discord[enter]")

tux open telegram:
    mimic("tux open commandline")
    user.template("flatpak run org.telegram.desktop[enter]")

# opens popular locations in code   
code open assignment tracker:  
    mimic("tux open commandline")
    user.template("code my-stuff/scripts/assignment-tracker/[enter]")
    
code open talon:
    mimic("tux open commandline")
    user.template("code .talon[enter]")

code open web:
    mimic("tux open commandline")
    user.template("code my-stuff/web/step-1/[enter]")

# dismisses the telegram notifications I occasionally get
telegram dismiss:
    mouse_move(1899, 1013)
    mouse_click(0)
