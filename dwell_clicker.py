# courtesy of https://github.com/timo/
# see https://github.com/timo/talon_scripts

from talon import Context, Module, actions, canvas, cron, ctrl, screen, settings, ui
from talon.skia import Paint, Rect
from talon.types.point import Point2d
from typing import Callable
from .utils import *
#from typing import tuple, list, set

mod = Module()
ctx = Context() 


class DwellClick:
    def __init__(self, default_layout: set[str]) -> None:
        # Initialize rectangle storage, layouts, and history
        self.mcanvas = None
        self.rectangles: dict = {}
        self.active_layouts: set = default_layout
        self.history: list = [default_layout]


    def rect_settings(self, settings: dict, layouts: dict, name: str) -> dict:
        """
        Handles the optional inputs for add_rect()
        
        hover_duration (str): the hover time required before a rectangle is activated
        continual_clicking: if true the rectangle will be clicked every hover_duration without needing the mouse to leave the rectangle
        text (str): the text displayed inside the rectangle
        text/rect_style: see possible_style_options for input syntax and see self.rect_style and self.text_style for what it should look like
        log (str): prints the text to the terminal every time check_hover() is run.
        """

        export = {
            "hover_duration": "250ms", 
            "continual_clicking": False,
            "log": None,
            
            "text_style": [{
                "display": None, # or the default layouts
                "msg": None,     # the box's displayed text
                #"textsize": 12,

                "color": "fff",
                "stroke_width": 18,
                "style": Paint.Style.FILL
            }],

            "rect_style": [{
                "display": None, # or the default layouts
                "color": "00ff007f", # if None then border won't be drawn 
                "bg_color": None,
                "stroke_width": 2,
                "style": Paint.Style.STROKE
            }]
        }

        # If the option is passed in then assign it to export
        for option in ("hover_duration", "continual_clicking", "invisible", "log"):
            if option in settings: export[option] = settings[option]

        # Handles how style blocks are assigned to export
        def handle_style_block(style_blocks: list[dict], export_key: str) -> None:
            used_displays = [layouts] # makes sure no duplicates layouts as those simply won't show
            for i, style in enumerate(style_blocks):
                # the first input modifies the default
                if i == 0: export[export_key][0].update(style); continue

                # further style options are appended to text.
                # further style options must have a display and can't have a duplicate display or it won't work
                if "display" not in style: 
                    raise ValueError(f"Error (rect: \"{name}\"): Style blocks missing display") 
                if style["display"] in used_displays: 
                    raise ValueError(f"Error (rect: \"{name}\"): Display already exists in rectangle's style blocks")

                # style options fill in missing pieces before appending them to the list of styles
                new_style = export[export_key][0].copy()
                new_style.update(style)
                export[export_key].append(new_style)
                used_displays.append(style["display"])
                

        # Handles text styling
        if "text" in settings: 
            text = settings["text"]
            # Most of the time using the default text is enough so this allows the shortcut
            if isinstance(text, str): export["text_style"][0]["msg"] = text
            # otherwise if its a list then handle as normal
            else: handle_style_block(text, "text_style")


        # Handles rectangle styling
        if "rect" in settings:
            handle_style_block(settings["rect"], "rect_style")

        return export

    def add_rect(self, layouts: set[str] | None, name:str, pos: list[int], size: list[int | str], inputs: list[int | str | set[str] | tuple[int, int] | Callable[[], None]], settings: dict={}) -> None:
        """
        Creates and stores rectangles
        Layouts: Rectangles will be drawn when their layout matches the current one. At least one rectangle should match the default layout in __init__
        Name: Name of the rectangle. If duplicately named rectangles exist an error will be thrown
        pos: the x and y of the box as ints. A negative value positions the box relative to the opposite end of the screen.
        size: 
            - Width and height as ints. 
            - Use "auto" to equal the size of the screen. 
            - If the second value is empty the height and width will be the same
        Inputs: passed into action() to be executed
            - int: accepts 0 and 1 for left and right mouse click
            - str: text entered will be run through actions.key
            - set: accepts a set of layouts. Will switch to the layouts provided
            - tuple: scroll data. Left is horizontal scroll and right is vertical scroll
            - callable: Will execute provided nullary function
        Settings: optional settings handled by rect_settings()
        """

        settings = self.rect_settings(settings, layouts, name)



        def action() -> None:
            """
            Responsible for executing inputs. This function is run when hovered.
            This function only exists here because cron.after accepts a nullary function. To get around it I have to curry.
            """
            rectangle = self.rectangles[name]

            # handles provided inputs
            for x in inputs:
                if isinstance(x, str  ): actions.key(x)
                elif isinstance(x, int  ): ctrl.mouse_click(button=x)
                elif isinstance(x, tuple): actions.mouse_scroll(y=x[1])
                elif   callable(x       ): x()
                elif isinstance(x, set  ): 
                    self.active_layouts = x # changes the current layout
                    # checks to see if you returned to the previous layout. 
                    # If so then "move back" along history otherwise add the layout to history
                    if len(self.history) != 1 and self.history[-2] == x: self.history.pop(-1)     
                    else: self.history.append(x)
            
            # If continual clicking is true then allow the rectangle to be clicked again without leaving the rectangle
            if settings["continual_clicking"]: rectangle["clicked"] = False

            # Resets the hover timer
            rectangle["hover_timer"] = None 

        if name in self.rectangles: 
            raise ValueError(f"Error: Rectangle \"{name}\" already exists") 

        

        # If provided a only one item then assume the item is a square
        if len(size) == 1: size.append(size[0])

        # If sizes are left as auto then fill the screen
        if size[0] is "auto": size[0] = screen.main().width
        if size[1] is "auto": size[1] = screen.main().height


        # If the input is negative then have it start at the opposite end of the screen instead
        # 1920/1080 (the end of the screen) is used as a starting point. 
        # Pos is guaranteed to be negative so I don't need to subtract it
        # Offset by the size otherwise if I do -1 then the box will be off the screen
        
        # Auto calculate the negatives for positive numbers for easy conversion
        #print(f"{name}: ({-(1920 - size[0] - pos[0])}, {-(1080 - size[1] - pos[1])})")

        if pos[0] < 0: pos[0] += 1920 - size[0]
        if pos[1] < 0: pos[1] += 1080 - size[1]
        
        

        self.rectangles[name] = {
            "zone": Rect(pos[0] + 1920, pos[1], *size),
            "layouts": layouts,
            "action": action,

            "hover_timer": None,
            "hover_duration": settings["hover_duration"],
            "clicked": False,

            "rect_style": settings["rect_style"],
            "text_style": settings["text_style"],

            "log": settings["log"]
        }


    def matching_layout(self, layout: set[str]) -> bool:
        """Checks to see if any of the set of layouts matches a layout in the current layout"""
        return layout is None or not layout.isdisjoint(self.active_layouts) 

    def find_active_style(self, styles: list[dict]) -> dict:
        """
        Returns the active style block from a list of style blocks.
        The function determines the active one by listing over a reversed list of layouts and returns the first one that matches the active layout
        """
        #if len(styles) == 1: return styles[0]
        
        # Returns a list of
        layouts = [x["display"] for x in styles]

        # Loops over the list of displays in reverse because I'm thinking that everything after the first is a modified overide of the first
        for i, style_display in enumerate(reversed(layouts), 1):
            if self.matching_layout(style_display): return styles[-i]
        
        return styles[0]     

    def show(self) -> None:
        """
        This function initializes the class to start drawing boxes and etc.
        Run this method after you've added all the rectangles you want to appear
        """
        # Create a canvas from the main screen
        self.mcanvas = canvas.Canvas.from_screen(ui.main_screen())
        # Register the draw method to be called when the canvas is drawn
        self.mcanvas.register("draw", self.draw)
        # Start tracking the mouse position and checking for hover
        cron.interval(f"100ms", self.check_hover)
        self.mcanvas.freeze()

    def draw(self, canvas) -> None:
        """This function is responsible for drawing rectangles. 
           Rectangles that aren't drawn will still be listen for hover inputs."""
        
        # Create a paint object for configuring drawing styles
        paint = canvas.paint

        # Draw the rectangle on the canvas
        # Draws the rectangles if a layout of theirs matches any of the active_layouts
        # None acts as a wildcard. It belongs to no layout and so it's alwsays present
        
        # Draws each rectangle added
        for rect in self.rectangles.values():
            if not self.matching_layout(rect["layouts"]): continue # only renders rectangles with matching layouts

            # if a rectangle or text uses a different appearance all future boxes drawn will share the same settings
            # that's why you have to set it each time before you draw just to double check

            rect_style = self.find_active_style(rect["rect_style"])
            attr_from_dict(paint, rect_style)

            # sets the background color of rectangles
            # must come before setting the border color so the border can properly overlap
            if rect_style["bg_color"]:
                # the style settings assume border color so I need to make a few tweaks before I draw it
                paint.color = rect_style["bg_color"]
                paint.style = paint.Style.FILL
                canvas.draw_rect(rect["zone"])

                # reset for the border color so I don't have to run apply_paint_settings again
                paint.color = rect_style["color"]
                paint.style = rect_style["style"]

            # if border color is not None then draw it
            if rect_style["color"]:
                canvas.draw_rect(rect["zone"])

            # draws the text
            text_style = self.find_active_style(rect["text_style"])
            if not text_style["msg"]: continue

            attr_from_dict(paint, text_style)
            canvas.draw_text(text_style["msg"], *centered_text(paint, rect["zone"], text_style["msg"]))
            
        self.mcanvas.freeze()
        

    def check_hover(self) -> None:
        """Checks to see if a rectangle is being hovered over.
           This function is run every 100ms."""
        
        
        # Get the current mouse position
        mouse = Point2d(*ctrl.mouse_pos())

        for key, rectangle in self.rectangles.items():
            if not self.matching_layout(rectangle["layouts"]): continue # prevents the mouse from activating rectangles that aren't on the matching layout
            
            # Check if mouse is inside the rectangle. If it is call 
            if rectangle["zone"].contains(mouse):
                if rectangle["clicked"]: continue
                rectangle["clicked"] = True

                # Prints the contents of a rectangle's log setting if any
                if rectangle["log"]: print(f"{key}: {rectangle['log']}")

                # Simulates hovering by setting an action on a delay. 
                rectangle["hover_timer"] = cron.after(rectangle["hover_duration"], rectangle["action"]) 
                continue
            
            #If the mouse is moved off a mouse it's timer resets not letting the action execute
            rectangle["clicked"] = False  # Mark as not active
            if rectangle["hover_timer"]:
                cron.cancel(rectangle["hover_timer"])
                rectangle["hover_timer"] = None  # Reset the hover timer

    def history_back(self) -> None:
        """
        Returns the last layout used. 
        You use it by passing this function without calling it and into the add_rect input parameter
        Unfinished
        """
        print(self.history)


        if len(self.history) == 1: return
        self.history.pop(-1)  
        self.active_layouts = self.history[-1]

    def close(self) -> None:
        """Unregister the draw method and stop the cron jobs"""
        if self.mcanvas:
            self.mcanvas.unregister("draw", self.draw)
            self.mcanvas.close()
            self.mcanvas = None

        cron.cancel(self.check_hover)
        for x in self.rectangles.values():
            if x["hover_timer"]: cron.cancel(x["hover_timer"])