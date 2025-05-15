import time
import psutil
import pygetwindow as gw
import pyautogui

# SETTINGS
TARGET_PROCESS = "valorant.exe"  # Process name for Valorant
KEY_TO_PRESS = "a"              # Key to press
PRESS_INTERVAL = 2              # Seconds between presses

def is_valorant_running():
    """Check if Valorant is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == TARGET_PROCESS:
            return True
    return False

def is_valorant_focused():
    """Check if Valorant is the active window."""
    try:
        win = gw.getActiveWindow()
        if win:
            print(f"Active window: '{win.title}'")  # Debug print
            if "valorant" in win.title.lower():  # Match 'valorant' in the title
                return True
    except Exception as e:
        print(f"Error checking window: {e}")
    return False

def main():
    print("Monitoring Valorant...")
    try:
        while True:
            if is_valorant_running() and is_valorant_focused():
                print(f"[{time.ctime()}] Valorant is focused. Pressing '{KEY_TO_PRESS}'")
                pyautogui.press(KEY_TO_PRESS)
            time.sleep(PRESS_INTERVAL)
    except Exception as e:
        print(f"Error occurred: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()