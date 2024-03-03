Xpath = {
    'ajax_app': '//android.widget.TextView[@content-desc="Ajax"]',
    'login': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]',
    'email_field': '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]',
    'password_field': '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]',
    'login_button': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]',
    'logout': '(//android.view.View[@resource-id="com.ajaxsystems:id/atomTitle"])[5]',
    'create_account': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Create Account"]',
    'ajax_main': '//android.widget.LinearLayout[@resource-id="com.ajaxsystems:id/noHubs"]/android.view.ViewGroup'
}
element_id = {
    'login_error': 'com.ajaxsystems:id/snackbar_text',
    'add_hub': 'com.ajaxsystems:id/text',
    'menu': 'com.ajaxsystems:id/menuDrawer',
    'app_settings': 'com.ajaxsystems:id/settings'
}
side_bar_buttons_xpath = {
    'app_settings': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]',
    'help': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]',
    'report_a_problem': '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]',
    'add_hub': '//android.widget.Button'
}

side_bar_buttons_id = {
    'terms_of_service': 'com.ajaxsystems:id/documentation_text',
    'build': 'com.ajaxsystems:id/build',
    'build_message': 'com.ajaxsystems:id/snackbar_title'
}