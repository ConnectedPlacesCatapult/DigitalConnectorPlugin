# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DigitalConnectorPlugin
                                 A QGIS plugin
 Digital Connector Plugin
                             -------------------
        begin                : 2018-03-22
        copyright            : (C) 2018 by Future Cities Catapult
        email                : tbantis@futurecities.catapult.org.uk
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
    """Load DigitalConnectorPlugin class from file DigitalConnectorPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .digital_connector_plugin import DigitalConnectorPlugin
    return DigitalConnectorPlugin(iface)
