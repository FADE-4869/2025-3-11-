import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import (QColor, QPalette, QPixmap, QPainter,
                         QLinearGradient, QBrush)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 窗口基本设置
        self.setWindowTitle("自定义背景图片示例")
        self.setGeometry(100, 100, 800, 600)

        # 设置背景图片
        self.background_image = QPixmap("background.jpg")  # 替换为你的图片路径
        self._check_background_image()

        # 创建主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(30)

        # 创建UI组件
        self._create_ui_components()

        # 设置控件样式
        self._style_components()

        # 连接信号与槽
        self.start_btn.clicked.connect(self.on_start_clicked)

    def _check_background_image(self):
        """检查背景图片是否有效"""
        if self.background_image.isNull():
            # 如果图片加载失败，使用渐变背景作为备用方案
            gradient = QLinearGradient(0, 0, 0, self.height())
            gradient.setColorAt(0, QColor("#2c3e50"))
            gradient.setColorAt(1, QColor("#3498db"))

            palette = self.palette()
            palette.setBrush(QPalette.Window, QBrush(gradient))
            self.setPalette(palette)
            print("背景图片加载失败，已启用备用背景")

    def paintEvent(self, event):
        """重绘事件处理背景图片"""
        if not self.background_image.isNull():
            painter = QPainter(self)

            # 根据窗口大小缩放图片（保持宽高比）
            scaled_pixmap = self.background_image.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # 居中显示背景图片
            x = (self.width() - scaled_pixmap.width()) / 2
            y = (self.height() - scaled_pixmap.height()) / 2
            painter.drawPixmap(x, y, scaled_pixmap)

            # 添加半透明遮罩层（增强文字可读性）
            painter.setBrush(QColor(0, 0, 0, 180))  # 黑色半透明遮罩
            painter.drawRect(self.rect())

    def _create_ui_components(self):
        """创建界面组件"""
        self.title_label = QLabel("图片背景应用示例")
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("在此输入内容...")
        self.result_label = QLabel("处理结果将显示在这里")
        self.start_btn = QPushButton("开始处理")

    def _style_components(self):
        """设置控件样式"""
        # 通用文本样式
        text_style = """
            color: #ffffff;
            font-size: 16px;
        """

        # 标题样式
        self.title_label.setStyleSheet(f"""
            QLabel {{
                {text_style}
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                background-color: rgba(0, 0, 0, 0.3);
                border-radius: 8px;
            }}
        """)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 输入框样式
        self.input_box.setStyleSheet(f"""
            QLineEdit {{
                {text_style}
                background-color: rgba(255, 255, 255, 0.15);
                border: 2px solid #3498db;
                border-radius: 6px;
                padding: 12px;
                min-height: 40px;
            }}
            QLineEdit:focus {{
                border-color: #2980b9;
            }}
        """)

        # 结果标签样式
        self.result_label.setStyleSheet(f"""
            QLabel {{
                {text_style}
                background-color: rgba(46, 204, 113, 0.25);
                border: 2px solid #2ecc71;
                border-radius: 6px;
                padding: 15px;
            }}
        """)
        self.result_label.setAlignment(Qt.AlignCenter)

        # 按钮样式
        self.start_btn.setStyleSheet(f"""
            QPushButton {{
                {text_style}
                background-color: rgba(52, 152, 219, 0.8);
                border: none;
                padding: 15px 30px;
                border-radius: 6px;
                min-width: 120px;
            }}
            QPushButton:hover {{
                background-color: rgba(41, 128, 185, 0.9);
            }}
            QPushButton:pressed {{
                background-color: rgba(52, 152, 219, 1);
            }}
        """)

        # 添加按钮动画
        self._add_button_animation()

    def _add_button_animation(self):
        """为按钮添加悬浮动画"""
        self.btn_anim = QPropertyAnimation(self.start_btn, b"geometry")
        self.btn_anim.setDuration(300)
        self.btn_anim.setEasingCurve(QEasingCurve.OutBack)

    def enterEvent(self, event):
        """鼠标进入按钮区域时触发"""
        if self.start_btn.underMouse():
            self.btn_anim.stop()
            self.btn_anim.setStartValue(self.start_btn.geometry())
            self.btn_anim.setEndValue(self.start_btn.geometry().adjusted(-5, -5, 10, 10))
            self.btn_anim.start()

    def leaveEvent(self, event):
        """鼠标离开按钮区域时触发"""
        self.btn_anim.stop()
        self.btn_anim.setStartValue(self.start_btn.geometry())
        self.btn_anim.setEndValue(self.start_btn.geometry().adjusted(5, 5, -10, -10))
        self.btn_anim.start()

    def on_start_clicked(self):
        """处理按钮点击事件"""
        input_text = self.input_box.text()
        processed = self._process_data(input_text)
        self._show_result(processed)

    def _process_data(self, data):
        """示例处理函数"""
        return f"🔮 处理结果: {data.upper()} 🔮"

    def _show_result(self, text):
        """显示结果动画"""
        self.result_label.setText(text)
        anim = QPropertyAnimation(self.result_label, b"windowOpacity")
        anim.setDuration(1000)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置全局字体
    font = app.font()
    font.setFamily("微软雅黑")
    font.setPointSize(10)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())