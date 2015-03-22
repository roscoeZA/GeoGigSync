# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoGig
                                 A QGIS plugin
 This plugin simplifies the GeoGig workflow .
                             -------------------
        begin                : 2015-03-18
        copyright            : (C) 2015 by Roscoe Lawrence
        email                : roscoelawrence@gmail.com
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
    """Load GeoGig class from file GeoGig.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geogig_module import GeoGig
    return GeoGig(iface)
