# courtesy of https://github.com/timo/
# see https://github.com/timo/talon_scripts

from talon import Context, Module, actions, canvas, cron, ctrl, screen, settings, ui
from talon.skia import Paint, Rect
from talon.types.point import Point2d
#from typing import tuple, list, set

mod = Module()
ctx = Context()


class DwellClick:
    def __init__(self, default_layout: set[str]) -> None:
        # Initialize rectangle coordinates and dimensions
        
        self.mcanvas = None
        self.rectangles: dict = {}
        self.active_layouts: set = default_layout
        self.history: list = [default_layout]

        self.rect_style = {
            "color": "00ff007f",  # Green color with some transparency
            "stroke_width": 2,
            "style": Paint.Style.STROKE
        }

        self.text_style = {
            "color": "fff",  # Green color with some transparency
            "stroke_width": 18,
            "style": Paint.Style.FILL
            #"text_size": 20

        }

    def rect_settings(self, settings: dict):
        export = {
            "hover_duration": "250ms",
            "continual_clicking": False,
            "text": None,
            "text_style": self.text_style,
            "rect_style": self.rect_style,
            "invisible": False,
            "log": None
        }

        for option in ["hover_duration", "continual_clicking", "text", "invisible", "log"]:
            if option in settings: export[option] = settings[option]


        for style in ["text", "rect"]:
            possible_style_options = (f"{style}_color", f"{style}_stroke_width", f"{style}_style", f"text_textsize")
            # use the list comprehension. 
            included_style_options = [x for x in possible_style_options if x in settings]
            if len(included_style_options) == 0: continue
            #
            export[f"{style}_style"] = getattr(self, f"{style}_style").copy()
            for x in included_style_options:
                cutoff = len(style) + 1
                export[f"{style}_style"][x[cutoff:]] = settings[x] #cuts off the first text_ 


        return export



    #def add_rect(self, layouts: set[str], name:str, pos: tuple[int, int], size: tuple[int, int], inputs: list[int | str | set], hover_duration: str="250ms", continual_clicking: bool=False) -> None:
    def add_rect(self, layouts: set[str] | None, name:str, pos: tuple[int, int], size: tuple[int, int], inputs: list[int | str | set[str] | tuple[int, int]], settings: dict={}) -> None:
        # cron.after doesn't allow me to pass any parameters to my function. To get around it I have to curry the function.

        settings = self.rect_settings(settings)

        def action():
            rectangle = self.rectangles[name]
            # Simulate they keypress at the cursor position

            
            for x in inputs:
                if isinstance(x, str): actions.key(x); continue
                if isinstance(x, int): ctrl.mouse_click(button=x); continue
                if isinstance(x, tuple): actions.mouse_scroll(y=x[1]); continue
                if callable(x): x(); continue
                if isinstance(x, set): 
                    self.active_layouts = x
                    if len(self.history) != 1 and self.history[-2] == x:
                        self.history.pop(-1)     
                    else:
                        self.history.append(x)
                    continue
            # Reset the hover timer after the click
            if settings["continual_clicking"]: rectangle["active"] = False
            rectangle["hover_timer"] = None  # Reset the hover timer


        self.rectangles[name] = {
            "zone": Rect(pos[0] + 1920, pos[1], *size),
            "layouts": layouts,
            "action": action,

            "hover_timer": None,
            "hover_duration": settings["hover_duration"],
            "active": False,

            "rect_style": settings["rect_style"],
            "text": settings["text"],
            "text_style": settings["text_style"],

            "invisible": settings["invisible"],
            "log": settings["log"]
        }




    def matching_layout(self, layout: set[str]) -> bool:
        return None is layout or not layout.isdisjoint(self.active_layouts) 

    def apply_paint_settings(self, paint: object, settings: dict) -> None:
        paint.color = settings["color"]
        paint.stroke_width = settings["stroke_width"]
        paint.style = settings["style"]
        
        #paint.textsize = getattr(settings, "textsize", 16)
        if "textsize" in settings: paint.textsize = settings["textsize"]
        

    def centered_text(self, paint: object, rect: dict) -> tuple[str, int, int]:

        text_width = paint.measure_text(rect["text"])[0]
        text_height = paint.textsize    

        rect_center_x = rect["zone"].x + (rect["zone"].width - text_width) / 2
        rect_center_y = rect["zone"].y + (rect["zone"].height + text_height) / 2
        return (rect["text"], rect_center_x, rect_center_y)
            # Draw text at the calculated position
        

    def show(self) -> None:
        # Create a canvas from the main screen
        self.mcanvas = canvas.Canvas.from_screen(ui.main_screen())
        # Register the draw method to be called when the canvas is drawn
        self.mcanvas.register("draw", self.draw)
        # Start tracking the mouse position and checking for hover
        cron.interval(f"100ms", self.check_hover)
        self.mcanvas.freeze()

    def draw(self, canvas) -> None:
        # Create a paint object for configuring drawing styles
        
        paint = canvas.paint

        # Draw the rectangle on the canvas
        # Draws the rectangles if a layout of theirs matches any of the active_layouts
        # None acts as a wildcard. It belongs to no layout and so it's alwsays present
        
        for rect in self.rectangles.values():
            if not self.matching_layout(rect["layouts"]): continue
            if rect["invisible"]: continue
            self.apply_paint_settings(paint, rect["rect_style"])
            canvas.draw_rect(rect["zone"])

            if not rect["text"]: continue
            # Calculate the position to center the text inside the rectangle
            self.apply_paint_settings(paint, rect["text_style"])
            canvas.draw_text(*self.centered_text(paint, rect))
            

        self.mcanvas.freeze()
        

    def check_hover(self) -> None:
        # Get the current mouse position
        mouse_pos = ctrl.mouse_pos()
        mouse = Point2d(mouse_pos[0], mouse_pos[1])

        for key, rectangle in self.rectangles.items():
            if not self.matching_layout(rectangle["layouts"]): continue
            
            # None if it isn't in use
            # cron job if it's going to click
            # "click_complete" if continual click is off. Having hover_timer be filled with anything stops the next cron job from happenin


            # Check if mouse is inside the rectangle. If it is call 
            if rectangle["zone"].contains(mouse):
                # if hover_timer is empty then put self.action(rectangle) on a cron job
                if rectangle["active"]: continue

                rectangle["active"] = True
                if rectangle["log"]: print(f"{key}: {rectangle['log']}")

                rectangle["hover_timer"] = cron.after(rectangle["hover_duration"], rectangle["action"]) 
            # reset hover_timer is mouse is outside the rectangle
            
            else:
                rectangle["active"] = False  # Mark as not active
                if rectangle["hover_timer"]:
                    cron.cancel(rectangle["hover_timer"])
                    rectangle["hover_timer"] = None  # Reset the hover timer

    def history_back(self) -> None:
        """
        Returns the last layout used. 
        You use it by passing this function without calling it and into the add_rect input parameter
        """
        print(self.history)


        if len(self.history) == 1: return
        self.history.pop(-1)  
        self.active_layouts = self.history[-1]



    def close(self) -> None:
        # Unregister the draw method and stop the cron jobs
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
#
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

    box.add_rect({"combat"}, "reset_cursor", (1790, 960), (100, height), [move_center], {"text": "Go Center"})
    box.add_rect({"combat"}, "stop_drag", (1790, 960 - spacing), (100, height), [0], {"text": "Stop Dragging"})
    box.add_rect({"combat"}, "level_up", (1790, 960 - spacing * 2), (100, height), [{"level_up"}], {"text": "Level Up"})
    box.add_rect({"combat"}, "reward_accept", (1790, 960 - spacing * 3), (100, height), [{"done"}], {"text": "Accept Reward"})
    
    reward_hover = {"hover_duration": "500ms"}
    box.add_rect({"done"}, "done", (820, 830), (280, 80), [0, {"combat"}], reward_hover)
    box.add_rect({"level_up"}, "items", (660, 268), (600, 690), [0, {"combat"}], reward_hover)


    box.show()

    #   moves mouse to the center of the screen
    #   holds down mouse key
    
    
    
    # add box that takes in move()
    # add box that allows you to click to disengage move()
    # add box that spawns the accept reward button
    #   reward box clicks and then activates move()







### GAMES

#website_scroll(50) #ao3
#website_scroll(300) #pinterest
inverted_fate()
#slay_the_spire()
#vampire_survivors()

mouse_pos = ctrl.mouse_pos()
print(mouse_pos[0], mouse_pos[1])
print(mouse_pos[0] - 1920, mouse_pos[1])







