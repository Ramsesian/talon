app: mpv
-

# base commands
show progress: user.hold_key("o", 1500)

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
audio delay downer: key(ctrl--)
audio delay upper: key(ctrl-+)
mute switch: "m"

speed downer: "["
speed upper: "]"

contrast downer: "1"
contrast upper: "2"

brightness downer: "3"
brightness upper: "4"

gamma downer: "5"
gamma upper: "6"

saturation downer: "7"
saturation upper: "8"

volume downer: "9"
volume upper: "0"

zoom out: "w"
zoom in: "e"

# subtitles
sub switch: "v"
sub last: "J"
sub next: "j"

sub delay downer: "x"
sub delay upper: "z"

sub up: "r"
sub down: "t"