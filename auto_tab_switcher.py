import time
import pygetwindow as gw
import pyautogui
import random
import keyboard  # pip install keyboard

# Apps to switch between
apps_to_switch = ["Google Chrome", "Visual Studio Code"]

# Time to stay on each app (seconds)
switch_interval = 5


def small_move():
    """Move mouse slightly from current position."""
    x, y = pyautogui.position()
    offset_x = random.randint(-20, 20)
    offset_y = random.randint(-20, 20)
    pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.2)


def safe_activate_window(app_name):
    """Activate window safely, fallback to ALT+TAB if needed."""
    try:
        win = gw.getWindowsWithTitle(app_name)[0]
        if win.isMinimized:
            win.restore()
        win.activate()
        win.maximize()
        time.sleep(0.5)  # ensure focus
        return True
    except Exception as e:
        print(f"Failed to activate {app_name} with pygetwindow: {e}")
        # Fallback: ALT+TAB
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.5)
        return False


print("Press ESC to stop the script at any time.")

while True:
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Stopping the script...")
        break  # exit the loop

    # Step 1: Save current mouse position
    original_x, original_y = pyautogui.position()

    # Step 2: Switch to first app
    first_app = apps_to_switch[0]
    second_app = apps_to_switch[1]

    print(f"Switching to {first_app}")
    safe_activate_window(first_app)

    # Step 3: Move mouse slightly
    small_move()

    # Step 4: Switch back to second app
    print(f"Switching back to {second_app}")
    safe_activate_window(second_app)

    # Step 5: Return mouse to original position and click
    pyautogui.moveTo(original_x, original_y, duration=0.2)
    pyautogui.click()
    print(f"Returned mouse and clicked at ({original_x}, {original_y})")

    # Wait before next cycle
    for i in range(switch_interval * 10):  # check ESC every 0.1s
        if keyboard.is_pressed('esc'):
            print("ESC pressed. Stopping the script...")
            exit()
        time.sleep(0.1)
