
from pathlib import Path

class TempFile:
    def __init__(self, filename=None):
        if not filename:
            from random import sample
            from string import ascii_letters
            filename = ''.join(sample(ascii_letters, 15))
        self.file = Path(filename)

    def __enter__(self):
        print("Entering init")
        self.file.parent.mkdir(parents=True, exist_ok=True)
        if self.file.exists():
            self.file.unlink()
        self.file.touch()
        return self.file.open('w')

    def __exit__(self, *args):
        print("Entering exit")
        self.file.unlink()


with TempFile() as tf:
    tf.write('This is test!\nThis file will be gone soon')
    tf.flush()
    import time
    time.sleep(20)