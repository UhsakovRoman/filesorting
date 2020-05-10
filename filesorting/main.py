from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "txt"):
                file = folder_track + "/" + filename
                new_path = new_folder + "/" + filename
                os.rename(file, new_path)


folder_track = r"C:\Users\Roman\Downloads"
new_folder = r"C:\Users\Roman\Desktop"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while (True):
        time.sleep(10)
        print(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
