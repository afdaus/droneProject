from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QStyledItemDelegate,
    QStyle,
    QStyleOptionViewItem,
)

class CustomeDelegate(QStyledItemDelegate):

    def __init__(self, rules):
        super().__init__()
        self.rules = rules

    def paint(self, painter, option, index):
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        
        if options.widget:
            style = options.widget.style()
        else:
            style = QApplication.style()

        doc = QtGui.QTextDocument()
        doc.setHtml(options.text)
        
        options.text = ''
        for rule in self.rules:
            # print("ini doc ", doc.toPlainText())
            marked_string = f"<b style=""background-color:red;""> {} </b>".format(doc.toPlainText())
            if (doc.toPlainText() == rule):
                doc.setHtml(marked_string)

        style.drawControl(QStyle.CE_ItemViewItem, options, painter)
        ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()

        textRect = style.subElementRect(QtWidgets.QStyle.SE_ItemViewItemText, options)

        painter.save()

        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        painter.translate(0, 0.5*(options.rect.height() - doc.size().height()))
        doc.documentLayout().draw(painter, ctx)

        painter.restore()
