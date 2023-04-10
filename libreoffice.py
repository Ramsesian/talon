from talon import Context, Module, actions, ctrl
 
mod = Module()
context = Context()
context.matches = """
app: Soffice
"""

@mod.action_class
class ToolbarActions:
    def tool_into(down_count: int = 1):
        """goes down a certain number of times and then selects right"""
        actions.key(f"down:{down_count} right")
    def tool_select(down_count: int = 1):
        """goes down a certain number of times and then selects enter"""
        actions.key(f"down:{down_count} enter")
    def go_file():
        """goes to file on the toolbar"""
        ctrl.mouse_move(29, 91)
        ctrl.mouse_click(0)
        actions.sleep("100ms")
    def go_format():
        """goes to format on the toolbar"""
        actions.user.go_file()
        actions.key("right:4")
    def go_spacing():
        """goes to spacing underneath format on the toolbar"""
        actions.user.go_format()
        actions.user.tool_into(2)