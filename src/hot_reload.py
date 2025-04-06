from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import atexit
import time

def reload_qss(widget, qss_path):
    # Load the QSS files and apply them to the widget

    def apply_stylesheet():
        combined = ""
        try:
            for qss_file in qss_path:
                print(f"Loading QSS file: {qss_file}")  # Debugging log
                with open(qss_file, "r") as file:
                    combined += file.read()
        except FileNotFoundError:
            print(f"File not found: {qss_file}")
            return
        except Exception as e:
            print(f"Error loading the qss file: {e}")
            return
        try:
            widget.setStyleSheet(combined)
            print("Stylesheet applied.")  # Debugging log
        except Exception as e:
            print(f"Error applying stylesheet: {e}")

    class QSSFileHandler(FileSystemEventHandler):
        """Handler for file system events to reload QSS files."""
        def __init__(self, qss_files):
            super().__init__()
            self.qss_files = qss_files
            self.last_modified = 0

        def on_modified(self, event):
            current_time = time.time()
            if current_time - self.last_modified < 1:  # 1-second debounce
                return
            self.last_modified = current_time

            try:
                print(f"File modified: {event.src_path}")  # Debugging log
                if event.src_path.replace("\\", "/") in self.qss_files:
                    print(f"Detected change in {event.src_path}. Reloading styles...")
                    apply_stylesheet()
            except Exception as e:
                print(f"Error in on_modified: {e}")

    observer = Observer()
    try:
        for qss_file in qss_path:
            if not os.path.exists(qss_file):
                print(f"File not found: {qss_file}")
                return
            if not os.path.isfile(qss_file):
                print(f"Path is not a file: {qss_file}")
                return

            # Schedule the observer for the directory containing the QSS file
            directory = os.path.dirname(qss_file)
            print(f"Scheduling observer for directory: {directory}")  # Debugging log
            observer.schedule(QSSFileHandler(qss_path), path=directory, recursive=False)

        observer.start()
        print("Observer started.")  # Debugging log
        apply_stylesheet()

        # Ensure the observer stops when the program exits
        atexit.register(observer.stop)
        print("Observer registered to stop on exit.")  # Debugging log
    except Exception as e:
        print(f"Error starting observer: {e}")

