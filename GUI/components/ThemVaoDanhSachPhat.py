from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QWidget
from PyQt6.QtCore import Qt
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from GUI.components.TaoPlayList import TaoPlayList
class ThemVaoDanhSachPhat(QDialog):
    def __init__(self, idtaikhoan , bllphatnhac):
        super().__init__()
        self.idtaikhoan = idtaikhoan
        self.bllphatnhac = bllphatnhac
        self.idbaihat = -1
        self.setFixedSize(300, 120)  # Tổng chiều cao 120px
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                color: black;
            }
            * {
                color: black;
                background-color: transparent;
            }
            QPushButton {
                font-size: 13px;
                padding: 2px 6px;
                text-align: left;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            QPushButton#createButton {
                font-weight: bold;
                background-color: #e0e0e0;
            }
            QPushButton#createButton:hover {
                background-color: #d0d0d0;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(4)

        # Nút tạo playlist
        create_button = QPushButton("➕ Tạo danh sách phát")
        create_button.setObjectName("createButton")
        create_button.clicked.connect(self.mo_form_tao_danh_sach) 
        main_layout.addWidget(create_button)

        # Scroll area cho danh sách phát
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Hiện khi cần

        playlist_widget = QWidget()
        playlist_layout = QVBoxLayout()
        playlist_layout.setContentsMargins(0, 0, 0, 0)
        playlist_layout.setSpacing(2)

        # Danh sách playlist (thêm nhiều để test cuộn)
        self.playlists = self.bllphatnhac.layDanhSachPhat(self.idtaikhoan)
        for playlist in self.playlists:
            btn = QPushButton(playlist.tieu_de)
            btn.clicked.connect(lambda _, p=playlist: self.handle_click_playlist(p))
            playlist_layout.addWidget(btn)

        playlist_widget.setLayout(playlist_layout)
        scroll_area.setWidget(playlist_widget)

        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def mo_form_tao_danh_sach(self):
        form = TaoPlayList(self.bllphatnhac,self.idtaikhoan,self.cap_nhat_danh_sach)
        form.exec()

    def handle_click_playlist(self, playlist):
        self.bllphatnhac.themBaiHatVaoDanhSachPhat(self.idbaihat, playlist.ma_danh_sach_phat)
        self.accept()  

    def set_id_bai_hat(self, idbaihat):
        self.idbaihat = idbaihat

    def cap_nhat_danh_sach(self):
        self.playlists = self.bllphatnhac.layDanhSachPhat(self.idtaikhoan)
        scroll_area = self.findChild(QScrollArea)
        if scroll_area:
            playlist_widget = QWidget()
            playlist_layout = QVBoxLayout()
            playlist_layout.setContentsMargins(0, 0, 0, 0)
            playlist_layout.setSpacing(2)

            for playlist in self.playlists:
                btn = QPushButton(playlist.tieu_de)
                btn.clicked.connect(lambda _, p=playlist: self.handle_click_playlist(p))
                playlist_layout.addWidget(btn)

            playlist_widget.setLayout(playlist_layout)
            scroll_area.setWidget(playlist_widget)
