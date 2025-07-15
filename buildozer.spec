[app]

# App information
title = MCQ Test App
package.name = mcqapp
package.domain = org.kivy

# Source files
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Version and orientation
version = 1.0
orientation = portrait
fullscreen = 0

# Requirements
requirements = python3,kivy==2.3.0,pyjnius,requests,android

# Android SDK/NDK paths (will be set by GitHub Actions)
android.api = 33
android.ndk = 25.2.9519653
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.accept_sdk_license = True

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icons
icon.filename = data/icon.png
# presplash.filename = data/splash.png  # Uncomment if you have a splash screen

[buildozer]
log_level = 2
warn_on_root = 1
