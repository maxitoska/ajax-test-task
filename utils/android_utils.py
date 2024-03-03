from typing import Dict

def android_get_desired_capabilities() -> Dict[str, str]:
    return {
        "platformName": "Android",
        "deviceName": "Pixel 7 API 30 Android 11",  # Replace with your device name
        "automationName": "UiAutomator2",
        "appPackage": "com.example.myapplication",  # Replace with your app package name
        "appActivity": ".MainActivity",  # Replace with your app main activity
        "app": "C:/Users/maxit/AndroidStudioProjects/MyApplication/app/release/app-release.apk"
    }

def get_url() -> str:
    return 'http://localhost:4723/wd/hub'
