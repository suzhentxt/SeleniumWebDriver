from ChromeController import RegTikTokController

auto = RegTikTokController()

auto.open_chrome()

auto.watch_video(number_video=3)

# cmd:
#     cd C:\Program Files\Google\Chrome\Application
#     chrome --remote-debugging-port=4444