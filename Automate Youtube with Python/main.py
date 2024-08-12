from ChromeController import YoutubeController

search_text = input("Enter the search keyword: ")

auto = YoutubeController()

auto.open_chrome()

auto.watch_video(search_text)

# cmd:
#     cd C:\Program Files\Google\Chrome\Application
#     chrome --remote-debugging-port=4444