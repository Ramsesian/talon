# courtesy of https://github.com/timo/
# see https://github.com/timo/talon_scripts

from talon import Context, Module, actions, canvas, cron, ctrl, screen, settings, ui
from talon.skia import Paint, Rect
from talon.types.point import Point2d
from typing import Callable
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

        # Default styles for rectangle and text. 
        # I have this here so that I can pass in a reference when possible to speed things up.
        self.rect_style = {
            "color": "00ff007f",  
            "stroke_width": 2,
            "style": Paint.Style.STROKE
        }

        self.text_style = {
            "color": "fff",  
            "stroke_width": 18,
            "style": Paint.Style.FILL
        }

    def rect_settings(self, settings: dict) -> dict:
        """
        Handles the optional inputs for add_rect()
        
        hover_duration (str): the hover time required before a rectangle is activated
        continual_clicking: if true the rectangle will be clicked every hover_duration without needing the mouse to leave the rectangle
        text (str): the text displayed inside the rectangle
        text/rect_style: see possible_style_options for input syntax and see self.rect_style and self.text_style for what it should look like
        invisible: if true the rectangle won't be drawn
        log (str): prints the text to the terminal every time check_hover() is run.
        """

        export = {
            "hover_duration": "250ms", 
            "continual_clicking": False,
            "text": None,
            "text_style": self.text_style,
            "rect_style": self.rect_style,
            "invisible": False,
            "log": None
        }

        # If the option is passed in then assign it to export
        for option in ("hover_duration", "continual_clicking", "text", "invisible", "log"):
            if option in settings: export[option] = settings[option]

        # Assigns the style options
        # If no style options are present for text/rect then use the reference instead of duplicating data
        # TODO CHANGE THIS. THIS IS DISGUSTING
        for style in ("text", "rect"):
            possible_style_options = (f"{style}_color", f"{style}_stroke_width", f"{style}_style", f"text_textsize")
            
            # gets all style options that match for the style block (rect or text). Skips if nothing
            included_style_options = [x for x in possible_style_options if x in settings]
            if len(included_style_options) == 0: continue
            
            # Copies the default style block (self.rect_style or self.text_style) and overwrites the reference in export
            export[f"{style}_style"] = getattr(self, f"{style}_style").copy()

            # Cuts off the rect_/text_ identifier in the possible_style_options and then assigns it to export
            for x in included_style_options:
                cutoff = len(style) + 1
                export[f"{style}_style"][x[cutoff:]] = settings[x]

        return export



    def add_rect(self, layouts: set[str] | None, name:str, pos: tuple[int, int], size: tuple[int, int], inputs: list[int | str | set[str] | tuple[int, int] | Callable[[], None]], settings: dict={}) -> None:
        """
        Creates and stores rectangles
        Layouts: Rectangles will be drawn when their layout matches the current one. At least one rectangle should match the default layout in __init__
        Name: Name of the rectangle. If duplicately named rectangles exist an error will be thrown
        pos and size: x,y and width x height. 
        Inputs: passed into action() to be executed
            - int: accepts 0 and 1 for left and right mouse click
            - str: text entered will be run through actions.key
            - set: accepts a set of layouts. Will switch to the layouts provided
            - tuple: scroll data. Left is horizontal scroll and right is vertical scroll
            - callable: Will execute provided nullary function
        Settings: optional settings handled by rect_settings()
        """

        settings = self.rect_settings(settings)

        def action() -> None:
            """
            Responsible for executing inputs. This function is run when hovered.
            This function only exists here because cron.after accepts a nullary function. To get around it I have to curry.
            """
            rectangle = self.rectangles[name]

            # handles provided inputs
            for x in inputs:
                if isinstance(x, str): actions.key(x); continue
                if isinstance(x, int): ctrl.mouse_click(button=x); continue
                if isinstance(x, tuple): actions.mouse_scroll(y=x[1]); continue
                if callable(x): x(); continue
                if isinstance(x, set): 
                    self.active_layouts = x # changes the current layout
                    # checks to see if you returned to the previous layout. 
                    # If so then "move back" along history otherwise add the layout to history
                    if len(self.history) != 1 and self.history[-2] == x: self.history.pop(-1)     
                    else: self.history.append(x)
                    continue
            
            # If continual clicking is true then allow the rectangle to be clicked again without leaving the rectangle
            if settings["continual_clicking"]: rectangle["clicked"] = False
            
            # Resets the hover timer
            rectangle["hover_timer"] = None 

        if name in self.rectangles: 
            print(f"Error: Rectangle {name} already exists") 
            return

        self.rectangles[name] = {
            "zone": Rect(pos[0] + 1920, pos[1], *size),
            "layouts": layouts,
            "action": action,

            "hover_timer": None,
            "hover_duration": settings["hover_duration"],
            "clicked": False,

            "rect_style": settings["rect_style"],
            "text": settings["text"],
            "text_style": settings["text_style"],

            "invisible": settings["invisible"],
            "log": settings["log"]
        }




    def matching_layout(self, layout: set[str]) -> bool:
        """Checks to see if any of the set of layouts matches a layout in the current layout"""
        return None is layout or not layout.isdisjoint(self.active_layouts) 

    def apply_paint_settings(self, paint: object, settings: dict) -> None:
        """applies paint styling from a provided dict"""
        paint.color = settings["color"]
        paint.stroke_width = settings["stroke_width"]
        paint.style = settings["style"]
        
        #paint.textsize = getattr(settings, "textsize", 16)
        if "textsize" in settings: paint.textsize = settings["textsize"]
        

    def centered_text(self, paint: object, rect: dict) -> tuple[str, int, int]:
        """Calculates the starting coordinates of a length of text to be centered inside the provided rectangle."""
        text_width = paint.measure_text(rect["text"])[0]
        text_height = paint.textsize    

        rect_center_x = rect["zone"].x + (rect["zone"].width - text_width) / 2
        rect_center_y = rect["zone"].y + (rect["zone"].height + text_height) / 2

        return (rect_center_x, rect_center_y) 
        
        # Draw text at the calculated position
        

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
            if rect["invisible"]: continue                      

            # if a rectangle or text uses a different appearance all future boxes drawn will share the same settings
            # that's why you have to set it each time before you draw just to double check
            self.apply_paint_settings(paint, rect["rect_style"])
            canvas.draw_rect(rect["zone"])

            # draws the text
            if not rect["text"]: continue
            self.apply_paint_settings(paint, rect["text_style"])
            canvas.draw_text(rect["text"], *self.centered_text(paint, rect))
            

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



        



def slay_the_spire():
        box = DwellClick({"combat"})

        slow = {"hover_duration": "500ms"}
        click = {"continual_clicking": True}
        slow_click = {**slow, **click}
        
        box.add_rect({"combat"                  }, "end_turn"       , (1550, 830), (170, 80 ), ["e"                            ], {"hover_duration":"750ms"})
        box.add_rect({"combat"                  }, "draw_pile"      , (30  , 960), (100, 100), ["a"     , {"return"           }])
        box.add_rect({"combat"                  }, "discard_pile"   , (1790, 960), (100, 100), ["s"     , {"return"           }])
        box.add_rect({"combat"                  }, "map"            , (1700, 5  ), (60 , 55 ), ["m"     , {"return"           }])
        box.add_rect({"combat"                  }, "deck"           , (1775, 10 ), (60 , 50 ), ["d"     , {"return"           }])
        box.add_rect({"combat"                  }, "settings"       , (1850, 10 ), (55 , 50 ), ["escape", {"return", "restart"}])
        box.add_rect({"return"                  }, "return"         , (0   , 860), (250, 70 ), [0       , {"combat"           }])
        box.add_rect({"restart"                 }, "restart"        , (0   , 733), (250, 70 ), [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "potions"        , (580 , 10 ), (160, 50 ), [0       , {"potion_select"    }], {**slow_click            })
        box.add_rect({"potion_select"           }, "potion_select"  , (450 , 140), (310, 110), [0       , {"combat"           }], {**slow_click            })
        box.add_rect({"enemies", "potion_select"}, "enemies"        , (950 , 400), (790, 350), [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "exhausted_cards", (1820, 865), (60 , 60 ), ["x"     , {"return"           }])
        #box.add_rect(None, "back", (800, 800), (100, 100), [box.history_back], {"text": "Back"})
        
        #box.add_rect({"proceed"}, "proceed"        , 1600, 730, 140, 70 , 0   , None, None, 1000)

        for i, card in enumerate([*range(1, 10), 0]):
            # slay the spire goes from 1-9, 0 so I need to reflect that
            box.add_rect({"combat", "enemies"}, f"card_{card}", (1200 - i*120, 150), (100, 100), [f"{card}", {"enemies"}], {"text": f"{card}"})

        box.show()

def website_scroll(scroll_distance):
    box = DwellClick({"scroll"})
    settings = {"continual_clicking":True, "invisible": True}
    box.add_rect({"scroll"}, "scroll_up", (0, 0), (1920, 200), [(0, -1 * scroll_distance)], settings)
    box.add_rect({"scroll"}, "scroll_down", (0, 1080 - 350), (1920, 350), [(0, scroll_distance)], settings)
    # add box that toggles cursor visibility
    box.show()
    ctrl.cursor_visible(False)

def inverted_fate():
    box = DwellClick({"comic"})
    settings = {"hover_duration": "500ms", "text_textsize": 30}
    
    box.add_rect({"comic"}, "back", (0, 0), (520, 1080), ["left"], {**settings, "text": "left"})
    box.add_rect({"comic"}, "next_right", (1400, 0), (520, 1080), ["right"], {**settings, "text": "right"})
    box.add_rect({"comic"}, "next_bottom", (620, 810), (680, 260), ["right"], {**settings, "text": "right"})
    # add box that toggles cursor visibility
    box.show()
    #ctrl.cursor_visible(False)

def vampire_survivors():
    box = DwellClick({"combat"})

    def move_center():
        rect = ui.active_window().rect
        ctrl.mouse_move(1920 + (rect.width / 2), rect.top + (rect.height / 2) - 30)
        ctrl.mouse_click(button=0, down=True)

    height = 100
    spacing = 50 + height

    box.add_rect({"combat"}, "reset_cursor ", (1790, 960              ), (100, height), [move_center ], {"text": "Go Center"    })
    box.add_rect({"combat"}, "stop_drag    ", (1790, 960 - spacing    ), (100, height), [0           ], {"text": "Stop Dragging"})
    box.add_rect({"combat"}, "level_up     ", (1790, 960 - spacing * 2), (100, height), [{"level_up"}], {"text": "Level Up"     })
    box.add_rect({"combat"}, "reward_accept", (1790, 960 - spacing * 3), (100, height), [{"done"}    ], {"text": "Accept Reward"})
    
    reward_hover = {"hover_duration": "500ms"}
    box.add_rect({"done"    }, "done ", (820, 830), (280, 80 ), [0, {"combat"}], reward_hover)
    box.add_rect({"level_up"}, "items", (660, 268), (600, 690), [0, {"combat"}], reward_hover)

    box.show()



### GAMES

#website_scroll(50) #ao3
#website_scroll(300) #pinterest
#inverted_fate()
slay_the_spire()
#vampire_survivors()

mouse_pos = ctrl.mouse_pos()
print(f"Mouse position on monitor one: x: {mouse_pos[0]       }, y: {mouse_pos[1]}")
print(f"Mouse position on monitor two: x: {mouse_pos[0] - 1920}, y: {mouse_pos[1]}")