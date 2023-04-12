app: mpv
-

# base commands
show progress:
    key(o:down)
    sleep(1500ms)
    key(o:up)

go full: "f"
go exit: "q"

# navigation
frame last: ","
frame next: "."

seek last: key(left)
seek next: key(right)

minute last: key(down)
minute next: key(up)

# playback
audio delay lower: key(ctrl--)
audio delay upper: key(ctrl-+)
mute switch: "m"

speed lower: "["
speed upper: "]"

contrast lower: "1"
contrast upper: "2"

brightness lower: "3"
brightness upper: "4"

gamma lower: "5"
gamma upper: "6"

saturation lower: "7"
saturation upper: "8"

volume lower: "9"
volume upper: "0"

zoom out: "w"
zoom in: "e"

# subtitles
sub switch: "v"
sub last: "J"
sub next: "j"

sub delay lower: "x"
sub delay upper: "z"

sub up: "r"
sub down: "t"