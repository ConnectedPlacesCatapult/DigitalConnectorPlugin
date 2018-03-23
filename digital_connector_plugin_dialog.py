# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DigitalConnectorPluginDialog
                                 A QGIS plugin
 Digital Connector Plugin
                             -------------------
        begin                : 2018-03-22
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Future Cities Catapult
        email                : tbantis@futurecities.catapult.org.uk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic, QtCore

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'digital_connector_plugin_dialog_base.ui'))


class DigitalConnectorPluginDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(DigitalConnectorPluginDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

class EditRecipe(QtGui.QDialog):
    def __init__(self, parent = None):
        super(EditRecipe, self).__init__(parent)
        
        # self.layout = QtGui.QVBoxLayout(self)
        self.layout = QtGui.QGridLayout(self)

        # OK and Cancel buttons
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)
    
    def addContent(self, position_x, position_y, datasource):
        widget = QtGui.QTextEdit()
        widget.setText(datasource)
        return self.layout.addWidget(widget,position_x,position_y)

    def getContent(self):
        updated_content = []
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for i in items:
            if isinstance(i.widget(), QtGui.QTextEdit):
                updated_content.append(i.widget().toPlainText())
        return updated_content

    # static method that reads the recipe content and returns the updated recipe
    @staticmethod
    def getRecipeContent(datasources, parent = None):
        dialog = EditRecipe(parent)
        for i, j in enumerate(datasources):
            dialog.addContent(i,i, str(j))


        result = dialog.exec_()

        mytext = dialog.getContent()

        return (datasources, mytext)