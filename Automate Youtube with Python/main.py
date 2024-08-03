from ChromeController import RegYoutubeController

search_text = input("Enter the search keyword: ")

auto = RegYoutubeController()

auto.open_chrome()

auto.watch_video(search_text)
