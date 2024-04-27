import keyboard
import pyautogui
from plyer import notification
import datetime
import os

class ScreenshotPro:
    def __init__(self):
        self.is_running = False
        self.desktop_path = self.get_desktop_path()

    def get_desktop_path(self):
        """ Return the path to the user's desktop, regardless of OS. """
        # Get the home directory
        home = os.path.expanduser("~")
        # Append 'Desktop' to the home directory path
        return os.path.join(home, 'Desktop')

    def take_screenshot(self):
        try:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Save the screenshot to the user's desktop
            screenshot_path = os.path.join(self.desktop_path, f"{current_time}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            notification.notify(
                title='Screenshot Saved',
                message=f'Screenshot saved as {screenshot_path}',
                app_icon=None,
                timeout=10
            )
            return screenshot_path
        except Exception as e:
            notification.notify(
                title='Error Taking Screenshot',
                message=f'Error: {str(e)}',
                app_icon=None,
                timeout=10
            )
            return None

    def run(self):
        self.is_running = True
        notification.notify(
            title='ScreenshotPro',
            message='ScreenshotPro is running in the background. Press Ctrl+Space to take a screenshot.',
            app_icon=None,
            timeout=10
        )
        keyboard.on_press_key('space', self.on_ctrl_space)
        keyboard.wait('esc')  # Adjust the exit key or method as needed

    def on_ctrl_space(self, event):
        if keyboard.is_pressed('ctrl'):
            return self.take_screenshot()

def run_screenshotPro():
    app = ScreenshotPro()
    return app.run()

if __name__ == "__main__":
    run_screenshotPro()
