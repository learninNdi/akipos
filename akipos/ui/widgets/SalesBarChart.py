from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QWidget,
    QSizePolicy,

)

from ui.widgets.rupiah import rupiah

class SalesBarChart(QWidget):
    """Responsive 7-day sales bar chart without dots."""

    def __init__(self, values, days, parent=None):
        super().__init__(parent)
        self.setObjectName("painterBackgroundColor")
        self.values = values
        self.days = days
        self.setMinimumHeight(300)
        self.setMaximumHeight(500)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def paintEvent(self, event):
        from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # painter.setObjec

        text = self.palette().text().color()
        # painter.fillRect(self.rect(), self.palette().window().color())
        # painter.fillRect(self.rect(), QColor(11, 18, 32))

        left, right, top, bottom = 150, 18, 30, 42
        chart_w = max(1, self.width() - left - right)
        chart_h = max(1, self.height() - top - bottom)

        max_value = max(10.0, max(self.values) * 1.15)

        font = painter.font()
        font.setPointSize(9)
        painter.setFont(font)
        # painter.setPen(QColor(148, 163, 184))

        # Grid lines and scale labels.
        grid_pen = QPen(
            QColor(text.red(), text.green(), text.blue(), 55)
        )
        grid_pen.setStyle(Qt.DotLine)
        grid_pen.setWidth(1)

        for tick in [0, 2.5, 5, 7.5, 10]:
            y = top + chart_h - (tick / max_value) * chart_h

            painter.setPen(grid_pen)
            painter.drawLine(
                left, int(y),
                self.width() - right, int(y)
            )

            painter.setPen(text)
            painter.drawText(
                0, int(y - 9), left - 10, 20,
                Qt.AlignRight | Qt.AlignVCenter,
                rupiah(tick * 100000)
            )

        # Calculate each bar from the same chart coordinate system.
        count = len(self.values)
        slot_w = chart_w / max(1, count)
        bar_w = max(24.0, min(64.0, slot_w * 0.55))
        bar_color = QColor("#3b82f6")

        for i, (day, value) in enumerate(zip(self.days, self.values)):
            center_x = left + slot_w * (i + 0.5)

            bar_h = (value / max_value) * chart_h
            x = center_x - bar_w / 2
            y = top + chart_h - bar_h

            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(bar_color))
            painter.drawRoundedRect(
                int(x), int(y),
                int(bar_w), max(1, int(bar_h)),
                5, 5
            )

            # Value centered exactly above its own bar.
            # painter.setPen(text)
            painter.setPen(QColor(148, 163, 184))
            painter.drawText(
                int(center_x - 55), int(y - 24),
                110, 20,
                Qt.AlignCenter,
                rupiah(value * 100000)
            )

            # Day centered exactly below its own bar.
            painter.drawText(
                int(center_x - 35),
                self.height() - bottom + 8,
                70, 24,
                Qt.AlignCenter,
                day
            )

        painter.end()