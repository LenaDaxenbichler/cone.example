from cone.app import main_hook
from cone.example.browser import static_resources
from cone.example.model import AppNode
from cone.example.model import AppNodeLeaf
from cone.app import register_entry
import cone.app


@main_hook
def example_main_hook(config, global_config, local_config):
    """Function which gets called at application startup to initialize
    this plugin.
    """
    # register static resources view
    config.add_view(static_resources, name='example-static')

    # register static resources to be delivered
    cone.app.cfg.css.public.append('example-static/example.css')
    cone.app.cfg.js.public.append('example-static/example.js')

    # register plugin entry node
    register_entry('child_1', AppNode)
    register_entry('child_2', AppNode)
    register_entry('child_3', AppNode)

    register_entry('child_4', AppNodeLeaf)
    register_entry('child_5', AppNodeLeaf)
    register_entry('child_6', AppNodeLeaf)

    # scan browser package
    config.scan('cone.example.browser')
