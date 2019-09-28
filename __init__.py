# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SLCadaster
                                 A QGIS plugin
 To Check the Cadaster Plan in Sri Lanka 
                             -------------------
        begin                : 2019-09-26
        copyright            : (C) 2019 by Prabhath W.J.K.A.N. Survey Dept. of Sri Lanka
        email                : npjasinghe@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SLCadaster class from file SLCadaster.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .SL_Cadaster import SLCadaster
    return SLCadaster(iface)
