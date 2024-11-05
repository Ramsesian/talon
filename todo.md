# Backlog For [Dwell Clicker](./dwell_clicker.py)

## General
Ordered by priority.

##### High
- Add a delay input. When you input a list of inputs this delay will serve to delay one input from the next. Perhaps I can do that by making a recursive function:
    - I create a function inside of action()
    - Each time I call that function I pass in an index.
    - That index is used to deal with with the current input
    - If the index isn't equal to the length of the array then call itself again
    - If a delay is put in place then the array is called with on a cron.after with the delay put in.
- Add new optional parameter that specifies whether a box is drawn on the secondary screen or not. 
- Auto offset the coords to fit the monitor. See how well ui.active_window().rect.left works to get the offset

##### Medium
- Have a default box setup that allows you to switch between games
    - Maybe have game switcher on the secondary screen so you won't accidentally hover over it
    - Probably have an option to toggle mouse visibility on the second monitor for ao3
- Add a function to draw a grid of boxes. Takes a list of lists to use as inputs with an option to display the string input as text. Also takes a name prefix. Takes box sizing and spacing values.
    - Parameters: `(x, y), (width, height), (column size, row size), gap, index, reverse=False, orientation=Horizontal/Vertical`
    - Column size and row size can take auto as an input where there's no limit. If column tries to go out of the screen it'll wrap down to the next row
    - `row_count = Math.ceil(index / column_size)`
    - `column_count = index % column_size`
    - Returns two tuples in a list `[(x, y), (width, height)]` which you can unpack into `box.add_rect` with the `**` operator.
    - Any inputs that have element or index in a string get those words replaced with the element or index respectively

##### Low
- Have it so `auto` fills the remaining screen instead of the height/width of the screen. For example:
    - `y: 0` `height: "auto"` would equal `y: 0` `height: 1080`
    - `y: 100` `height: "auto"` would equal `y: 100` `height: 980`
    - `y: -100` `height: "auto"` would equal `y: 0` `height: 980`
- Handle the offcase in which the only input is `["auto"]`
- If "auto" is in a larger string it's auto filled and then the equation is calculated. For example: 
    - `y: 100` `height: "auto - 100"` ->
    - `y: 100` `height: "980 - 100"` ->
    - `y: 100` `height: 880`
    - Could be done by saying `auto = 980` and then `eval(auto - 100)`
- History property for going back or forward along the chain. If the next layout is different than the next in the array then remove all the ones after the next one
    - If no boxes are registered for the layout then either show a back button or a button to reset the layout to the default 
- Add a toggleable setting that will move between the last layout and the layout change:
    - Add a `toggle` option that accepts a boolean.
    - Add the `toggle_from` option that takes a set of layouts. If left on default it'll equal the layouts the rectangle can show on. `toggle_from` is layout it'll switch back to and when the rectangle is considered toggled off. Add the layouts `toggle_from` to the layouts rect will show up on just in case.
    - Add the `toggle_to` option that takes a set of layouts. If left on default it'll equal the layouts the rectangle switches to. Add `toggle_to` layouts to the layouts rect will show up on and switch to. `toggle_to` are the layouts that'll be switched to when toggled on and the layouts in which the rectangle will be considered toggle on.


## Game Specific Support
##### Scroll
- Have a toggleable cursor button in the corner. It takes cordinates for it's location so it can be used in other games

##### Slay the spire
- Add support for item selection and ending combat

##### Support in General
- Sanctuary RPG
- Omori
- Chess.com
- Anki