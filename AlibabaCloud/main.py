from ChromeController import RegWebController

auto = RegWebController()

auto.open_chrome()
auto.signup()
auto.step1()
auto.step2()

# cmd:
#     cd C:\Program Files\Google\Chrome\Application
#     chrome --remote-debugging-port=4444