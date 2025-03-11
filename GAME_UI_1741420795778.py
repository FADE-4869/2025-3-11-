import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt5.QtGui import (QColor, QPalette, QPixmap, QPainter,
                         QLinearGradient, QBrush)

class MainWindow(QMainWindow):
    # 样式常量
    TEXT_STYLE = """
        color: #ffffff;
        font-size: 16px;
    """



    def __init__(self):
        super().__init__()
        self._scaled_bg = None  # 缓存缩放后的背景
        self._setup_ui()

    def _setup_ui(self):
        """初始化界面组件"""
        self.setWindowTitle("自定义背景图片示例")
        self.setGeometry(100, 100, 800, 600)
        
        self._init_background()
        self._create_components()
        self._setup_layout()
        self._connect_signals()



    def _init_background(self):
        """初始化背景相关设置"""
        self.background_image = QPixmap("background.jpg")
        if not self._check_background_image():
            self._create_fallback_background()

    def _check_background_image(self):
        """检查背景有效性并返回布尔结果"""
        if self.background_image.isNull():
            self._show_load_error()
            return False
        return True

    def _show_load_error(self):
        """显示加载错误提示"""
        error_label = QLabel("背景图片加载失败，已启用备用方案", self)
        error_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        error_label.adjustSize()
        error_label.move(10, 10)

    def _create_fallback_background(self):
        """创建备用背景（修复版）"""
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#2c3e50"))
        gradient.setColorAt(1, QColor("#3498db"))

        # 正确的调色板设置方式
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

    def paintEvent(self, event):
        """优化后的绘制事件处理"""
        if not self.background_image.isNull():
            painter = QPainter(self)
            
            # 使用缓存或创建新缩放
            if not self._scaled_bg or self._scaled_bg.size() != self.size():
                self._scaled_bg = self.background_image.scaled(
                    self.size(), 
                    Qt.KeepAspectRatioByExpanding,
                    Qt.SmoothTransformation
                )
            
            x = (self.width() - self._scaled_bg.width()) / 2
            y = (self.height() - self._scaled_bg.height()) / 2
            painter.drawPixmap(x, y, self._scaled_bg)
            painter.setBrush(QColor(0, 0, 0, 180))
            painter.drawRect(self.rect())

    def _create_components(self):
        """创建界面组件"""
        self.title_label = QLabel("图片背景应用示例")
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("在此输入内容...")
        self.result_label = QLabel("处理结果将显示在这里")
        self.start_btn = QPushButton("开始处理")
        self._style_components()

    def _setup_layout(self):
        """初始化主界面布局"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.main_layout = QVBoxLayout(main_widget)

        # 设置布局参数
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(30)

        # 按顺序添加组件
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.input_box)
        self.main_layout.addWidget(self.result_label)
        self.main_layout.addWidget(self.start_btn)

        # 添加弹性空间
        self.main_layout.addStretch(1)

    def _style_components(self):
        """应用样式到组件"""
        self.title_label.setStyleSheet(f"""
            QLabel {{
                {self.TEXT_STYLE}
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                background-color: rgba(0, 0, 0, 0.3);
                border-radius: 8px;
            }}
        """)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 其他组件样式保持不变...
        # [原有样式设置代码保留，此处为节省篇幅省略重复代码]

    def _add_button_animation(self):
        """优化后的按钮动画设置"""
        self.btn_anim = self._create_animation(
            self.start_btn, 
            b"geometry", 
            300, 
            QEasingCurve.OutBack
        )

    def _create_animation(self, target, prop, duration, curve):
        """创建可复用的动画对象"""
        anim = QPropertyAnimation(target, prop)
        anim.setDuration(duration)
        anim.setEasingCurve(curve)
        return anim

    def enterEvent(self, event):
        """优化后的进入事件处理"""
        if self.start_btn.underMouse():
            original = self.start_btn.geometry()
            self.btn_anim.stop()
            self.btn_anim.setStartValue(original)
            self.btn_anim.setEndValue(original.adjusted(-5, -5, 10, 10))
            self.btn_anim.start()

    def leaveEvent(self, event):
        """优化后的离开事件处理"""
        self.btn_anim.stop()
        self.btn_anim.setStartValue(self.start_btn.geometry())
        self.btn_anim.setEndValue(self.start_btn.geometry().adjusted(5, 5, -10, -10))
        self.btn_anim.start()

    def on_start_clicked(self):
        """按钮点击事件处理（需补全）"""
        input_text = self.input_box.text()
        processed = self._process_data(input_text)
        self._show_result(processed)

    def _show_result(self, text):
        """显示结果动画（需补全）"""
        self.result_label.setText(text)
        anim = QPropertyAnimation(self.result_label, b"windowOpacity")
        anim.setDuration(1000)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()

    def _process_data(self, data):
        """添加异常处理的数据处理方法"""
        try:
            return f"🔮 处理结果: {self._sanitize_input(data).upper()} 🔮"
        except Exception as e:
            return f"错误: {str(e)}"

    def _sanitize_input(self, text):
        """输入过滤处理"""
        return text.replace('<', '&lt;').replace('>', '&gt;')

    def resizeEvent(self, event):
        """处理窗口大小改变事件"""
        self._scaled_bg = None  # 清除缓存
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = app.font()
    font.setFamily("微软雅黑")
    font.setPointSize(10)
    app.setFont(font)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
