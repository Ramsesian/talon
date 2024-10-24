# Backlog For [Dwell Clicker](./dwell_clicker.py)

## General
Ordered by priority.

##### High
- Add errors and error handling
- Add a delay input. When you input a list of inputs this delay will serve to delay one input from the next. Perhaps I can do that by making a recursive function:
    - I create a function inside of action()
    - Each time I call that function I pass in an index.
    - That index is used to deal with with the current input
    - If the index isn't equal to the length of the array then call itself again
    - If a delay is put in place then the array is called with on a cron.after with the delay put in.
- Add new optional parameter that specifies whether a box is drawn on the secondary screen or not. 
- Auto offset the coords to fit the monitor. See how well ui.active_window().rect.left works to get the offset

##### Medium
- Allow option to change `paint.textsize`. You can probably go ahead and update the `dict.get` at the same time too.
- Have a default box setup that allows you to switch between games
    - Maybe have game switcher on the secondary screen so you won't accidentally hover over it
    - Probably have an option to toggle mouse visibility on the second monitor for ao3
- Add a function to draw a grid of boxes. Takes a list of lists to use as inputs with an option to display the string input as text. Also takes a name prefix. Takes box sizing and spacing values.
    - Parameters: `(x, y), (width, height), (column size, row size), gap, index, reverse=False, orientation=Horizontal/Vertical`
    - Column size and row size can take auto as an input where there's no limit. If column tries to go out of the screen it'll wrap down to the next row
    - `row_count = Math.ceil(index / column_size)`
    - `column_count = index % column_size`
    - Returns two tuples in a list `[(x, y), (width, height)]` which you can unpack into `box.add_rect` with the `**` operator.

##### Low
- Have it so that if you input negative coords it does an offset from the opposite side of the screen instead. For example `-50` would equal `screen_size - 50`
- The `dict.get(key, default)` method can return a default value if the item doesn't exist. You can probably use that to overhaul the text and rect presets. You could work it into the assign paint thing too.
- History property for going back or forward along the chain. If the next layout is different than the next in the array then remove all the ones after the next one
    - If no boxes are registered for the layout then either show a back button or a button to reset the layout to the default 
- Add a background fill color option to rect
- Have the appearance settings be in one big dict that you pass as a single option. 
    - Each one now accepts a display setting. If the display setting contains anything then the settings inside that appearance block will only show if that display matches. For example if you put in a set of layouts the appearance might change while you're in those layouts. 
    - Perhaps a new `type` option if necessary. For example text has the unique `text` option so that isn't necessary for text, but for rect it might need a type `rect` option because it doesn't have any identifiable options so far.
    - If options are left out of appearance blocks that contain a display setting have them try to fill in the gaps with settings from the normal appearance block. If the normal appearance block doesn't containt anything then take settings from the box/text global default.
    - Have `invisible` appear in the rect appearance block.
    - Probably make a function that accepts two dictionaries. 
        - If the second dictionary is empty then return the first. 
        - If the second dictionary isn't empty then return a new combined dictionary where the 2nd dictionary is placed over the 1st
        - If the second dictionary has keys that aren't in the first then return an error.
- Add a toggleable setting that will move between the last layout and the layout change:
    - Add a `toggle` option that accepts a boolean.
    - Add the `toggle_from` option that takes a set of layouts. If left on default it'll equal the layouts the rectangle can show on. `toggle_from` is layout it'll switch back to and when the rectangle is considered toggled off. Add the layouts `toggle_from` to the layouts rect will show up on just in case.
    - Add the `toggle_to` option that takes a set of layouts. If left on default it'll equal the layouts the rectangle switches to. Add `toggle_to` layouts to the layouts rect will show up on and switch to. `toggle_to` are the layouts that'll be switched to when toggled on and the layouts in which the rectangle will be considered toggle on.
- Change comparisons to use `==` over `is` where applicable
- Change `rectangle["active]` to `rectangle["clicked"]` to make more sense semantically


## Game Specific Support
##### Slay the spire
- Add support for item selection and ending combat

##### Support in General
- Sanctuary RPG
- Omori
- Chess.com