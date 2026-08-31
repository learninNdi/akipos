from ui.styles.styles import DARK_THEME, LIGHT_THEME

def apply_theme(window, theme):
    window.current_theme = theme
    window.setStyleSheet(DARK_THEME if theme == "dark" else LIGHT_THEME)
    window.theme_button.setText("☀  Light" if theme == "dark" else "☾  Dark")