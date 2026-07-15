import LinkExtractor
import LinkObject as LO
import LinkSorter
import os

import tkinter as tk
from tkinter import filedialog


class FolderSifter:
    def __init__(self, folder=None, recursive=False):
        """Initialize the FolderSifter.

        folder: optional path to a directory. If None, a folder picker dialog is shown.
        recursive: if True, include files in subdirectories.

        The instance will populate self.folder (path) and self.files (list of file paths).
        The object is iterable (yields file paths).
        """
        # resolve folder path or open dialog
        if folder and os.path.isdir(folder):
            self.folder = os.path.abspath(folder)
        else:
            root = tk.Tk()
            root.withdraw()
            # initialdir: default to user's home directory
            self.folder = filedialog.askdirectory(title="Select a Folder", initialdir=os.path.expanduser("~"))

        if not self.folder:
            # user cancelled or no folder; create empty file list
            self.files = []
        else:
            # build the file list
            if recursive:
                self.files = []
                for dirpath, _, filenames in os.walk(self.folder):
                    for fn in filenames:
                        if fn.lower().endswith(".docx"):
                            self.files.append(os.path.join(dirpath, fn))
            else:
                self.files = [os.path.join(self.folder, fn) for fn in os.listdir(self.folder)
                              if os.path.isfile(os.path.join(self.folder, fn))]
                

        # convenience: expose number of files
        self.count = len(self.files)

    def __iter__(self):
        return iter(self.files)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, index):
        return self.files[index]
    
    def folderList(self):
        # Print All Word Document Files found in folder 
        for docx in self.files:
            print(docx)






