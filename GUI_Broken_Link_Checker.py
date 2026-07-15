# GUI
#
# Test code written by Addy for demo only
# Haseeb is assigned this part
# 
# TODO: Implement the following
# Creates window and UI widgets (you can reference testapp.py for how to use tkinter)
# defines buttons whose command is to call LinkSorter and ExcelsheetGenerator (you can reference UI drawings)
# 
# stretch goals: (do not implement if the previous dont already work)
# allows user to select a file from their device as the input_file to be passed to LinkSorter
# also allows user to define an output file name and location to be passed to excelsheetGenerator
#
# References
# https://stackoverflow.com/questions/34689889/update-label-text-after-pressing-a-button-in-tkinter
#
from LinkObject import LinkObject
import tkinter as tk
from tkinter.filedialog import askopenfilename
from ExcelsheetGenerator import ExcelsheetGenerator
from LinkSorter import LinkChecker
from LinkExtractor import LinkExtractor

class BrokenLinkCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Broken Link Checker App")

        self.sourceFile = None
        self.linkObjs = None

        # populates window
        self.create_widgets()
        self.running = True


    def select_input_file(self):
        filename = askopenfilename() # File selecting dialog box, returns path to the selected file as string
        self.sourceFile = filename # save global
        self.variableLabel.config(text=filename)
        # no return value

    def create_widgets(self):
        # layout to specify size with
        self.root.state('zoomed')
        self.layout = tk.Frame(self.root)
        self.layout.grid()
        tk.Label(self.layout, text="Choose docx file to extract links from").grid(row=0, column=0)

        tk.Button(self.layout, text="Open File...", command=lambda: self.select_input_file()).grid(row=1, column=0, columnspan=2, pady=2)
        # to change values of this label later we have to give it a variable name to reference later
        # this variable is edited with .config() later in select_input_file() function
        # which is called on press of the previous button ^
        self.variableLabel = tk.Label(self.layout, text="No file selected...")
        self.variableLabel.grid(row=2, column=0)

        tk.Button(self.layout, text="Run the link sorter program", command=lambda: self.call_linksorter()).grid(row=3, column=0, columnspan=2, pady=2)

        tk.Button(self.layout, text="Run the Excelsheet Generator program", command=lambda: self.call_excelgenerator()).grid(row=4, column=0, columnspan=2, pady=2)

    def call_linksorter(self):
        extractor = LinkExtractor(self.sourceFile)
        self.linkObjs = extractor.extract_links()

        self.linkchecker = LinkChecker()
        for links in self.linkObjs:
            self.linkchecker.addLink(links)
        self.linkchecker.linkSortion()
        print(f"Links Extracted")
        tk.Label(self.root, text=("Links Sorted ")).grid(row=2)
        
    def call_excelgenerator(self):
        #creates list using only broken links
        broken_links = self.linkchecker.brokenList
        if len(broken_links) == 0:
            print("No broken links found")
            tk.Label(self.root, text=("No Broken Links Found")).grid(row=3)
            return
        
        output = ExcelsheetGenerator (broken_links, "brokenlinks.csv")
        print(f"Excel sheet created: {output}")
        tk.Label(self.root, text=("Excel Sheet Created")).grid(row=3)

    def on_close(self):
        self.running = False
        self.root.destroy()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = BrokenLinkCheckerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()