#!/usr/bin/env python

##############################################################################
##
## This file is part of Sardana
##
## http://www.tango-controls.org/static/sardana/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## Sardana is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Sardana is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

"""This module is part of the Python Pool library. It defines the base classes
for PoolTriggerGate"""

__all__ = ["PoolTriggerGate"]

__docformat__ = 'restructuredtext'

from sardana import ElementType

from sardana.pool.poolelement import PoolElement
from sardana.sardanaattribute import SardanaAttribute

class Index(SardanaAttribute):

    def __init__(self, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)

class PoolTriggerGate(PoolElement):

    def __init__(self, **kwargs):
        kwargs['elem_type'] = ElementType.TriggerGate
        PoolElement.__init__(self, **kwargs)        
        self._index = Index(self)
    
    def get_index_attribute(self):
        """Returns the index attribute object for this trigger/gate
        
        :return: the index attribute
        :rtype: :class:`~sardana.sardanaattribute.SardanaAttribute`"""
        return self._index
    
    # --------------------------------------------------------------------------
    # default acquisition channel
    # --------------------------------------------------------------------------

    def get_default_attribute(self):
        return self.get_index_attribute()
