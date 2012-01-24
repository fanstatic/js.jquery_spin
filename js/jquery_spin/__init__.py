from fanstatic import Library, Resource
from js.spin import spin

library = Library('jquery.spin', 'resources')
spin = Resource(library, 'jquery.spin.js', depends=[spin])
