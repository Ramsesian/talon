app: mpv
-

# base commands
show progress:
    key(o:down)
    sleep(1500ms)
    key(o:up)

go full: key(f)
go exit: key(q)

# navigation
frame last: key(,)
frame next: key(.)

seek last: key(left)
seek next: key(right)

minute last: key(down)
minute next: key(up)

# playback
audio delay lower: key(ctrl--)
audio delay upper: key(ctrl-+)
mute switch: key(m)

speed lower: key("[")
speed upper: key("]")

contrast lower: key(1)
contrast upper: key(2)

brightness lower: key(3)
brightness upper: key(4)

gamma lower: key(5)
gamma upper: key(6)

saturation lower: key(7)
saturation upper: key(8)

volume lower: key(9)
volume upper: key(0)

zoom out: key(w)
zoom in: key(e)

# subtitles
sub switch: key(v)
sub last: key(shift-j)
sub next: key(j)

sub delay lower: key(x)
sub delay upper: key(z)

sub up: key(r)
sub down: key(t)