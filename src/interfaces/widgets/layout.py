"""

    This module generate a Qt layout wrapper object to arrange child widgets
    within a widget to ensure that they make good use of the available space.

"""

from PyQt5.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout, QStackedLayout


class Layout(QLayout):

    def __init__(self, widget, **kwargs):
        super(Layout, self).__init__(widget)
        
        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        l_m = get_num("l_m")
        t_m = get_num("t_m")
        r_m = get_num("r_m")
        b_m = get_num("b_m")
        space = get_num("space")

        name = get_param("name")
        align = get_param("align")

        # Set margin and spacing
        self.setContentsMargins(l_m, t_m, r_m, b_m)
        self.setSpacing(space)

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)


class HorizontalLayout(QHBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(HorizontalLayout, self).__init__(widget, **kwargs)


class VerticalLayout(QVBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(VerticalLayout, self).__init__(widget, **kwargs)


class StackLayout(QStackedLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(StackLayout, self).__init__(widget, **kwargs)