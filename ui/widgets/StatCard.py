from PyQt5.QtWidgets import(
    QFrame,
    QVBoxLayout,
    QSizePolicy,
    QLabel
)

class StatCard(QFrame):
    def __init__(self, title, value, note):
        super().__init__()
        self.setObjectName("Card")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        l = QVBoxLayout(self)
        l.setContentsMargins(16,14,16,14)
        l.addWidget(QLabel(title, objectName="CardTitle"))
        l.addWidget(QLabel(value, objectName="CardValue"))
        l.addWidget(QLabel(note, objectName="Muted"))