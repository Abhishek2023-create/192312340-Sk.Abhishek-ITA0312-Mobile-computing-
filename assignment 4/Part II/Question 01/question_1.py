import shutil
print('Android device evidence checklist (not device measurements):')
commands=['adb shell getprop ro.build.version.release','adb shell ps -A','adb shell dumpsys activity processes','adb shell dumpsys meminfo com.example.testapp','adb shell service list']
for cmd in commands: print('  '+cmd)
print('adb available on this runner:', bool(shutil.which('adb')))
print('No Android device/emulator connected or measured by this Python example.')
