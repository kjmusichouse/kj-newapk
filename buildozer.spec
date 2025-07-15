[app]
title = KJ Education
package.name = KJEducation
package.domain = org.kivy

source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0
orientation = portrait
fullscreen = 0

requirements = python3,kivy==2.3.0,pyjnius,requests
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
#android.ndk = 25.2.9519653
#android.sdk_path = /usr/local/lib/android/sdk
#android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.accept_sdk_license = True

# Android permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# If icon.png exists in your data/ folder
icon.filename = data/icon.png

# Optional splash (uncomment only if this file exists)
# presplash.filename = data/splash.png

# Required for GitHub CI runner
#android.sdk_path = $HOME/android-sdk

[buildozer]
log_level = 2
warn_on_root = 1
