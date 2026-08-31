from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
     QFrame,
     QSplitter,
     QVBoxLayout,
     QHBoxLayout,
     QLabel,
     QPushButton,
     QWidget,
     QGridLayout,
     QSizePolicy
)

from ui.widgets.rupiah import rupiah
from ui.widgets.make_table import make_table
from ui.widgets.StatCard import StatCard
from ui.widgets.page_base import page_base
from ui.widgets.SalesBarChart import SalesBarChart

def dashboard_page():
    page,l = page_base("Dashboard","Ringkasan bisnis hari ini")
    grid = QGridLayout()
    # grid.setSpacing(12)
    cards = [
        StatCard("Penjualan Hari Ini",rupiah(8500000),"126 transaksi"),
        StatCard("Laba Kotor",rupiah(2100000),"HPP menggunakan FIFO"),
        StatCard("Pembelian Hari Ini",rupiah(4200000),"4 invoice"),
        StatCard("Stok Perlu Perhatian","8 produk","3 habis • 5 rendah"),
    ]
    for c, card in enumerate(cards):
        grid.addWidget(card,0,c)
        grid.setColumnStretch(c,1)
    l.addLayout(grid)

    split = QSplitter(Qt.Horizontal)
    split.setChildrenCollapsible(False)

    sales = QFrame(); sales.setObjectName("Panel")
    sl = QVBoxLayout(sales)
    sl.setContentsMargins(16, 14, 16, 14)
    # sl.setSpacing(10)

    # Header + period summary
    sales_header = QHBoxLayout()
    title_box = QVBoxLayout()
    title_box.setSpacing(2)
    title_box.addWidget(QLabel("Penjualan 7 Hari Terakhir", objectName="PanelTitle"))
    title_box.addWidget(QLabel("Tren omzet harian", objectName="Muted"))
    sales_header.addLayout(title_box)
    sales_header.addStretch()

    total_7_days = sum([5.5, 7.2, 4.8, 8.8, 6.4, 9.2, 7.6]) * 100000
    average_7_days = total_7_days / 7

    summary_box = QVBoxLayout()
    summary_box.setSpacing(0)
    total_label = QLabel(rupiah(total_7_days))
    total_label.setAlignment(Qt.AlignRight)
    total_label.setStyleSheet("font-size:21px;font-weight:700;")
    summary_box.addWidget(total_label)
    avg_label = QLabel("Rata-rata " + rupiah(average_7_days) + "/hari", objectName="Muted")
    avg_label.setAlignment(Qt.AlignRight)
    summary_box.addWidget(avg_label)
    sales_header.addLayout(summary_box)
    sl.addLayout(sales_header)

    # Responsive line chart with connected data points.
    values = [5.5, 7.2, 4.8, 8.8, 6.4, 9.2, 7.6]
    days = ["Jum", "Sab", "Min", "Sen", "Sel", "Rab", "Kam"]

    chart = SalesBarChart(values, days)
    chart.setMinimumHeight(250)
    chart.setMaximumHeight(600)
    sl.addWidget(chart, 1, Qt.AlignTop)

     # Tabel 5 transaksi terakhir di bawah chart.
    transaction_header = QHBoxLayout()
    transaction_header.addWidget(
        QLabel("Transaksi Terakhir", objectName="PanelTitle")
    )
    transaction_header.addStretch()
    transaction_header.addWidget(
        QLabel("5 transaksi terakhir", objectName="Muted")
    )
    sl.addLayout(transaction_header)

    transactions = make_table(
        ["No. Transaksi", "Waktu", "Pelanggan", "Item", "Total", "Pembayaran"],
        [
            ("INV-1025", "13:42", "Budi", "2", "Rp 2.400.000", "QRIS"),
            ("INV-1024", "12:18", "Umum", "1", "Rp 3.200.000", "Cash"),
            ("INV-1023", "11:05", "Andi", "3", "Rp 2.700.000", "Transfer"),
            ("INV-1022", "10:31", "Toko Jaya", "2", "Rp 2.800.000", "QRIS"),
            ("INV-1021", "09:47", "Umum", "1", "Rp 3.000.000", "Cash"),
        ]
    )
    transactions.setMinimumHeight(190)
    transactions.setMaximumHeight(240)
    transactions.setSizePolicy(
        QSizePolicy.Expanding,
        QSizePolicy.Preferred
    )
    
    sl.addWidget(transactions, 0)

    split.addWidget(sales)

    stock=QFrame(); stock.setObjectName("Panel")
    st=QVBoxLayout(stock)
    st.addWidget(QLabel("Stok Perlu Perhatian",objectName="PanelTitle"))
    st.addWidget(make_table(["Kode","Produk","Stok","Status"],[
        ("A001","GS Astra NS40","2","Rendah"),
        ("A015","Yuasa N70","0","Habis"),
        ("A022","Incoe NS60","1","Rendah"),
        ("A034","Bosch N50","0","Habis"),
    ]),1)

    # 3 tagihan supplier terdekat.
    billing_header = QHBoxLayout()
    billing_header.addWidget(
        QLabel("Tagihan Terdekat", objectName="PanelTitle")
    )
    billing_header.addStretch()
    billing_header.addWidget(
        QLabel("3 tagihan", objectName="Muted")
    )
    st.addLayout(billing_header)

    bills = make_table(
        ["Invoice", "Supplier", "Jatuh Tempo", "Total"],
        [
            ("INV-PT-028", "PT ABC Battery", "02/09/2026", "Rp 15.500.000"),
            ("INV-PT-031", "PT XYZ Motor", "05/09/2026", "Rp 8.250.000"),
            ("INV-PT-034", "CV Sumber Aki", "08/09/2026", "Rp 6.750.000"),
        ]
    )
    bills.setMinimumHeight(145)
    bills.setMaximumHeight(190)
    bills.setSizePolicy(
        QSizePolicy.Expanding,
        QSizePolicy.Preferred
    )
    st.addWidget(bills, 0)

    split.addWidget(stock)
    split.setStretchFactor(0,2); split.setStretchFactor(1,1)
    l.addWidget(split,1)
    return page