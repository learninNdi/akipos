from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QLabel,
    QPushButton
)

from config import APP_NAME
from config import APP_VERSION
from config import APP_LOGO

from ui.pages.dashboard.page import dashboard_page
from ui.pages.sales.page import SalesPage
from ui.styles.theme import apply_theme

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setMinimumSize(1000, 650)
        self.setWindowIcon(QIcon(APP_LOGO))
        self.current_theme = "dark"
        self.nav_buttons = []
        self.pages = QStackedWidget()

        central = QWidget()
        root = QHBoxLayout(central)
        root.setContentsMargins(0,0,0,0)
        root.setSpacing(0)
        root.addWidget(self.create_sidebar())

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.setSpacing(0)
        content_layout.addWidget(self.create_topbar())
        content_layout.addWidget(self.pages, 1)
        root.addWidget(content, 1)
        self.setCentralWidget(central)

        self.create_pages()
        self.select_page(0)

    def select_page(self,index):
        self.pages.setCurrentIndex(index)
        titles=["Dashboard","Penjualan","Produk & Stok","Pembelian",
                "Pelanggan","Supplier","Laporan","Pengaturan"]
        self.page_title.setText(titles[index])
        for i,b in enumerate(self.nav_buttons):
            b.setProperty("active",i==index)
            b.style().unpolish(b); b.style().polish(b)

    def create_sidebar(self):
        side = QFrame()
        side.setObjectName("Sidebar")
        side.setFixedWidth(300)
        l = QVBoxLayout(side)
        l.setContentsMargins(13,18,13,13)
        l.setSpacing(4)

        self.image_label = QLabel(self)

        # title_label = QLabel(f"{APP_NAME}", objectName="Brand")
        # title_label = QLabel("FOCUS\nBATTERY\nPOS", objectName="Brand")
        # title_label.setWordWrap(True)
        
        pixmap = QPixmap("logo-fbc.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)
        l.addWidget(self.image_label)
        # l.addWidget(QLabel("Point of Sale • Toko Aki", objectName="BrandSub"))
        
        l.addSpacing(20)

        menus = ["Dashboard","Penjualan","Produk & Stok","Pembelian",
                    "Pelanggan","Supplier","Laporan","Pengaturan"]
        icons = ["⌂","▣","▤","↓","♙","▰","▥","⚙"]
        for i, title in enumerate(menus):
            b = QPushButton(f"{icons[i]}   {title}")
            b.setObjectName("Nav")
            b.setProperty("active", False)
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(lambda checked=False, x=i: self.select_page(x))
            self.nav_buttons.append(b)
            l.addWidget(b)
        l.addStretch()
        l.addWidget(QLabel(f"{APP_NAME} {APP_VERSION}", objectName="BrandSub"))
        return side

    def update_datetime(self):
        current = QDateTime.currentDateTime()

        datetime_text = current.toString(
            "dddd, dd MMMM yyyy  •  HH:mm:ss"
        )

        self.datetime_label.setText(
            datetime_text
        )

    def create_topbar(self):
        bar = QFrame()
        bar.setObjectName("TopBar")
        bar.setMinimumHeight(66)
        l = QHBoxLayout(bar)
        l.setContentsMargins(22,0,22,0)

        self.page_title = QLabel()
        self.page_title.setObjectName("PageTitle")
        l.addWidget(self.page_title)
        l.addStretch()

        self.datetime_label = QLabel()
        self.datetime_label.setObjectName("Muted")

        l.addWidget(self.datetime_label)

        self.update_datetime()

        self.datetime_timer = QTimer(self)
        self.datetime_timer.timeout.connect(
            self.update_datetime
        )

        self.datetime_timer.start(1000)
        
        self.theme_button = QPushButton("☀  Light")
        self.theme_button.setObjectName("Theme")
        self.theme_button.setCursor(Qt.PointingHandCursor)
        self.theme_button.clicked.connect(self.toggle_theme)
        l.addWidget(self.theme_button)
        return bar

    def toggle_theme(self):
        self.current_theme = (
            "light"
            if self.current_theme == "dark"
            else "dark"
        )

        apply_theme(self, self.current_theme)

        self.theme_button.setText(
            "☀  Light" if self.current_theme == "dark"
            else "☾  Dark"
        )

    def create_pages(self):
        self.sales_page = SalesPage(self)

        self.pages.addWidget(
            dashboard_page()
        )

        self.pages.addWidget(
            self.sales_page
        )

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_F11:
            self.showNormal() if self.isMaximized() else self.showMaximized()
            event.accept()
            return
        super().keyPressEvent(event)
