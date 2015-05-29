from toffee.element import ElementPool
from toffee.element.PreElement import PreElement
from toffee.element.IncludeElement import IncludeElement
from toffee.element.ClassElement import ClassElement
from toffee.element.MetaElement import MetaElement
from toffee.element.NodeElement import NodeElement
from toffee.element.ModelElement import ModelElement
from toffee.element.AudioElement import AudioElement


ElementPool.addElement(PreElement)
ElementPool.addElement(IncludeElement)
ElementPool.addElement(ClassElement)
ElementPool.addElement(MetaElement)
ElementPool.addElement(NodeElement)
ElementPool.addElement(ModelElement)
ElementPool.addElement(AudioElement)
