import subprocess
import time
import pyautogui

# Optional: Enable fail-safe (move mouse to top-left corner to abort)
pyautogui.FAILSAFE = True

# Step 1: Minimize all windows
pyautogui.hotkey('win', 'd')
time.sleep(1)

# Step 2: Launch Chrome with WhatsApp Web using profile
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
profile_option = r'--profile-directory=Profile 5'
whatsapp_url = 'https://web.whatsapp.com'
subprocess.Popen([chrome_path, profile_option, whatsapp_url])

print("🚀 Opening WhatsApp Web in Chrome...")
time.sleep(12)  # Wait for WhatsApp Web to fully load

# Step 3: Open search (Ctrl + K) and search for the contact
print("🔍 Searching for contact using Ctrl+K...")
pyautogui.hotkey('ctrl', 'alt', 'n')  # Shortcut to open chat search
time.sleep(1)
pyautogui.write("9791554199", interval=0.1)
time.sleep(1)
pyautogui.press('enter')

# Step 4: Type and send the message
print("💬 Sending the message...")
time.sleep(1)
pyautogui.write("We are testing buddy", interval=0.05)
time.sleep(0.5)
pyautogui.press('enter')

print("✅ Message sent successfully!")
