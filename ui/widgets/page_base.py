from PyQt5.QtWidgets import(
        QWidget,
        QVBoxLayout,
        QHBoxLayout,
        QLabel
)

def page_base(title, desc):
        page = QWidget()
        l = QVBoxLayout(page)
        l.setContentsMargins(20,18,20,18)
        l.setSpacing(13)
        h = QHBoxLayout()
        h.addWidget(QLabel(title, objectName="PageTitle"))
        h.addStretch()
        h.addWidget(QLabel(desc, objectName="Muted"))
        l.addLayout(h)
        return page, l