from pyramid.static import static_view

static_resources = static_view('static', use_subpath=True)

from cone.app.browser.layout import ProtectedContentTile
from cone.example.model import AppNode
from cone.tile import tile

@tile(name='content',
      path='templates/example.pt',
      interface=AppNode,
      permission='login')
class ExamplePluginContent(ProtectedContentTile):
    pass
