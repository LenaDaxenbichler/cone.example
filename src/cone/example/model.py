from cone.app.model import BaseNode


class AppNode(BaseNode):

    @property
    def properties(self):
        props = super().properties
        props.icon = 'bi bi-kanban'
        props.in_navtree = True
        props.mainmenu_display_children = True
        return props

    def __iter__(self):
        return iter(['child_1', 'child_2', 'child_3'])

    def __getitem__(self, key):
        return AppNode(name=key, parent=self)
            
class AppNodeLeaf(BaseNode):

    @property
    def properties(self):
        props = super().properties
        props.icon = 'bi bi-mouse'
        props.in_navtree = True
        return props
