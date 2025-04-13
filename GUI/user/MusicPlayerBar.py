from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DTO.DTOBaiHat import DTOBaiHat
class MusicPlayerBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1500, 100)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setStyleSheet("""
            background-color: #ffffff;
            border-top: 1px solid #f2f2f2;
        """)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        # ==== PHẦN 1: Thông tin bài hát (30%) ====
        part1_layout = QHBoxLayout()  # Layout chính nằm ngang

        # Label hiển thị ảnh bài hát
        self.image_label = QLabel()
        pixmap = QPixmap("assets/AnhBaiHat/0.png")
        scaled_pixmap = pixmap.scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setFixedSize(90, 90)

        # Tạo một layout dọc để chứa tên bài hát và tên ca sĩ
        text_layout = QVBoxLayout()
        self.song_label = QLabel("Tên bài hát: Unknown")
        self.artist_label = QLabel("Ca sĩ: Unknown")

        # Cập nhật style và căn lề cho tên bài hát:
        self.song_label.setStyleSheet("font-size: 18px; color: #333; border: none;")
        self.song_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        # Cập nhật style cho ca sĩ (có thể giữ như cũ)
        self.artist_label.setStyleSheet("font-size: 12px; color: #666; border: none;")
        self.artist_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        text_layout.addWidget(self.song_label)
        text_layout.addWidget(self.artist_label)

        # Thêm ảnh và layout text vào layout chính (nằm ngang)
        part1_layout.addWidget(self.image_label)
        part1_layout.addLayout(text_layout)

        layout.addLayout(part1_layout, 3)  # Phần 1 chiếm 30% layout

        # ==== PHẦN 2: Điều khiển & Tiến trình (40%) ====
        part2_layout = QVBoxLayout()
        part2_layout.setContentsMargins(0, 5, 0, 0)
        part2_layout.setSpacing(5)

        # Nút điều khiển
        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)

        self.prev_button = QPushButton()
        self.play_button = QPushButton()
        self.next_button = QPushButton()
        self.repeat_button = QPushButton()

        buttons = [self.prev_button, self.play_button, self.next_button, self.repeat_button]
        icons = ["prev", "pause", "next", "repeat"]

        for btn, icon in zip(buttons, icons):
            btn.setIcon(QIcon(f"assets/icon/{icon}.png"))
            if btn == self.play_button:
                btn.setIconSize(QSize(26, 26))
                btn.setFixedSize(40, 40)
            else:
                btn.setIconSize(QSize(18, 18))
                btn.setFixedSize(30, 30)
            btn.setStyleSheet("background: none; border: none;")

        self.prev_button.clicked.connect(self.prev_song)
        self.play_button.clicked.connect(self.toggle_play_pause)
        self.next_button.clicked.connect(self.next_song)
        self.repeat_button.clicked.connect(self.toggle_repeat)

        button_layout.addStretch()
        for btn in buttons:
            button_layout.addWidget(btn)
        button_layout.addStretch()

        # Thanh tiến trình
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(5, 0, 5, 0)
        progress_layout.setSpacing(5)

        self.time_current_label = QLabel("00:00")
        self.time_current_label.setStyleSheet("font-size: 12px; color: #666; border: none;")

        self.progress_slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_slider.setMinimum(0)
        self.progress_slider.setMaximum(100)
        self.progress_slider.setValue(0)
        self.progress_slider.setStyleSheet("""
            QSlider {
                border: none;
            }
            QSlider::groove:horizontal {
                border: none;
                height: 4px;
                background: #ccc;  /* Màu nền của groove */
                margin: 0px;
                padding: 0px;
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: #0078d7;  /* Màu của đầu kéo */
                border: none;
                height: 12px;
                width: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::sub-page:horizontal {
                background: #0078d7;  /* Màu phần đã kéo */
                border-radius: 2px;
            }
        """)


        self.time_total_label = QLabel("--:--")
        self.time_total_label.setStyleSheet("font-size: 12px; color: #666; border: none;")

        progress_layout.addWidget(self.time_current_label)
        progress_layout.addWidget(self.progress_slider)
        progress_layout.addWidget(self.time_total_label)

        part2_layout.addLayout(button_layout)
        part2_layout.addLayout(progress_layout)
        layout.addLayout(part2_layout, 4)  # Phần 2 chiếm 40% layout

        # ==== PHẦN 3: Âm lượng (30%) ====
        part3_layout = QHBoxLayout()
        part3_layout.setContentsMargins(0, 0, 0, 0)  # Đặt margins = 0 để bỏ khoảng cách thừa
        part3_layout.setSpacing(10) 

        part3_layout.addStretch()
        self.volume_icon = QLabel()
        self.volume_icon.setPixmap(QIcon("assets/icon/volume.png").pixmap(22, 22))

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setFixedWidth(100)
        self.volume_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 6px;
                background: #ccc;  /* Màu nền của groove */
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #0078d7;  /* Màu của đầu kéo */
                border: none;
                width: 12px;
                height: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::sub-page:horizontal {
                background: #0078d7;  /* Màu phần đã kéo */
                border-radius: 3px;
            }
            QSlider {
                border: none;  /* Ensure no border */
            }
        """)

        part3_layout.addWidget(self.volume_icon)
        part3_layout.addWidget(self.volume_slider)

        layout.addLayout(part3_layout, 3)  # Phần 3 chiếm 30% layout

        self.setLayout(layout)

        self.is_playing = True
        self.is_repeat = False
        self.songs = []
        self.current_index = 0
        
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.mediaStatusChanged.connect(self.on_media_status_changed)
        self.progress_slider.sliderPressed.connect(self.on_slider_pressed)
        self.progress_slider.sliderReleased.connect(self.on_slider_released)
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_time)
        self.update_timer.start(1000)  # Cập nhật mỗi giây
        self.media_player.positionChanged.connect(self.update_progress)
        self.is_slider_pressed = False

        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.on_volume_changed)

    def on_volume_changed(self, value):
        self.audio_output.setVolume(value / 100)

    def update_song(self, song):
        self.song = song
        self.song_label.setText(f"Tên bài hát: {song.getTieuDe()}")
        self.artist_label.setText(f"Ca sĩ: {', '.join(song.getCaSi())}")
        self.time_current_label.setText("00:00")
        self.progress_slider.setValue(0)

        image_path = song.getAnh() 
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        file_path = QUrl.fromLocalFile(song.getFileNhac())
        self.media_player.setSource(file_path)
        QTimer.singleShot(100, self.update_duration_in_update_song)
        self.media_player.play()


    def update_duration_in_update_song(self):
        # Lấy tổng thời gian bài hát (duration) và cập nhật giao diện
        duration_ms = self.media_player.duration()
        self.time_total_label.setText(self.format_time(duration_ms))

    def update_time(self):
        # Cập nhật thời gian hiện tại mỗi giây
        position = self.media_player.position()
        self.time_current_label.setText(self.format_time(position))

    def on_slider_pressed(self):
        self.is_slider_pressed = True
        self.update_timer.stop()

    def on_slider_released(self):
        # Tiếp tục cập nhật khi người dùng thả slider
        self.is_slider_pressed = False
        self.update_timer.start(1000)

        # Lấy vị trí mới từ slider
        position = int(self.progress_slider.value() * self.media_player.duration() / 100)  # Ép kiểu về int

        # Đặt vị trí mới cho bài hát
        self.media_player.setPosition(position)
        if self.media_player.playbackState() != QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.play()
        self.update_time_label(position)

    def update_time_label(self, position):
        # Cập nhật thời gian hiện tại (chuyển từ ms sang định dạng mm:ss)
        self.time_current_label.setText(self.format_time(position))

    def format_time(self, ms):
        # Chuyển thời gian từ milisecond sang mm:ss
        seconds = ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"


    def load_song_list(self, songs):
        self.songs = songs
        self.current_index = 0
        if self.songs:
            self.update_song(self.songs[0])

    def toggle_play_pause(self):
        self.is_playing = not self.is_playing
        icon_path = "assets/icon/pause.png" if self.is_playing else "assets/icon/play.png"
        self.play_button.setIcon(QIcon(icon_path))

        if self.is_playing:
            self.media_player.play()
        else:
            self.media_player.pause()


    def next_song(self):
        if self.songs and self.current_index + 1 < len(self.songs):
            # Chuyển đến bài hát tiếp theo
            self.current_index += 1
            self.is_playing = True
            
            # Cập nhật biểu tượng nút Play/Pause
            self.play_button.setIcon(QIcon("assets/icon/pause.png"))
            
            # Cập nhật UI bài hát (có thể là tiêu đề, ca sĩ, hình ảnh...)
            self.update_song(self.songs[self.current_index])
            
            # Phát bài hát mới
            self.media_player.play()


    def prev_song(self):
        if self.songs and self.current_index > 0:
            # Chuyển về bài hát trước
            self.current_index -= 1
            self.is_playing = True

            # Cập nhật biểu tượng nút Play/Pause
            self.play_button.setIcon(QIcon("assets/icon/pause.png"))

            # Dừng bài hát hiện tại (nếu đang phát)
            self.media_player.stop()

            # Cập nhật UI bài hát
            self.update_song(self.songs[self.current_index])

    def update_progress(self, position):
        if self.is_slider_pressed:
            return  # Đang kéo, không cập nhật để tránh xung đột

        duration = self.media_player.duration()
        if duration > 0:
            progress = (position / duration) * 100
            self.progress_slider.setValue(int(progress))
            self.update_time_label(position)

    def toggle_repeat(self):
        self.is_repeat = not self.is_repeat
        if self.is_repeat:
            self.repeat_button.setIcon(QIcon("assets/icon/repeat_clicked.png"))
        else:
            self.repeat_button.setIcon(QIcon("assets/icon/repeat.png"))


    def on_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.is_repeat:
                self.update_song(self.songs[self.current_index])
            else:
                # Nếu đang là bài cuối thì return, không phát tiếp
                if self.current_index >= len(self.songs) - 1:
                    return
                else:
                    self.next_song()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo 3 bài hát
    demo_bai_hat_1 = DTOBaiHat(
        MaBaiHat=1,
        NgayPhatHanh="2023-01-01",
        TieuDe="Nơi này có anh",
        Anh="assets/AnhBaiHat/1.png",
        MaXuatXu=1,
        TenXuatXu="Việt Nam",
        MaTheLoai=2,
        TenTheLoai="Pop",
        FileNhac="assets/FileNhac/1.mp3",
        CaSi=["Sơn Tùng MTP", "Jack"]
    )

    demo_bai_hat_2 = DTOBaiHat(
        MaBaiHat=2,
        NgayPhatHanh="2022-12-15",
        TieuDe="Đừng lo",
        Anh="assets/AnhBaiHat/2.png",
        MaXuatXu=2,
        TenXuatXu="Hàn Quốc",
        MaTheLoai=3,
        TenTheLoai="R&B",
        FileNhac="assets/FileNhac/2.mp3",
        CaSi=["IU", "G-Dragon"]
    )

    demo_bai_hat_3 = DTOBaiHat(
        MaBaiHat=3,
        NgayPhatHanh="2023-03-10",
        TieuDe="Shape of You",
        Anh="assets/AnhBaiHat/3.png",
        MaXuatXu=3,
        TenXuatXu="UK",
        MaTheLoai=1,
        TenTheLoai="Pop",
        FileNhac="assets/FileNhac/3.mp3",
        CaSi=["Ed Sheeran"]
    )

    window = MusicPlayerBar()
    # Load 3 bài hát vào player
    window.load_song_list([demo_bai_hat_1, demo_bai_hat_2, demo_bai_hat_3])
    window.show()

    sys.exit(app.exec())