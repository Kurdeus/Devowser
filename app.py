import sys
import ctypes
import win32gui
import win32process
import win32con
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == "__main__":
    # Hide console window
    if hasattr(sys, 'frozen'):
        # If running as compiled executable
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd != 0:
            ctypes.windll.user32.ShowWindow(hwnd, 0)
    else:
        # If running as script, try to hide the console window
        foreground_window = win32gui.GetForegroundWindow()
        if foreground_window:
            _, process_id = win32process.GetWindowThreadProcessId(foreground_window)
            if process_id == os.getpid():
                win32gui.ShowWindow(foreground_window, win32con.SW_HIDE)

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    try:
        # Initialize the Chrome driver with options
        driver = webdriver.Chrome(options=chrome_options)

        # Open Google search
        driver.get("https://www.google.com/")

        # Keep browser window open
        while True:
            time.sleep(1)  # Check every second if browser is still open
            try:
                # Check if browser window still exists
                driver.current_url  # This will throw an exception if browser is closed
                if not driver.service.process:
                    print("Browser process no longer running")
                    break
            except Exception:
                print("Browser window closed")
                break

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error while quitting driver: {e}", file=sys.stderr)