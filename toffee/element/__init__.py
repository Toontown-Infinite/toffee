from toffee.element import ElementPool
from toffee.element.PreElement import PreElement
from toffee.element.IncludeElement import IncludeElement
from toffee.element.ClassElement import ClassElement
from toffee.element.MetaElement import MetaElement
from toffee.element.SceneElement import SceneElement


ElementPool.addElement(PreElement)
ElementPool.addElement(IncludeElement)
ElementPool.addElement(ClassElement)
ElementPool.addElement(MetaElement)
ElementPool.addElement(SceneElement)
