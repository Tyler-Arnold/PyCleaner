import os
import glob
import tkinter

#create a new window
window = tkinter.Tk()

#title the window and resize it
window.title("PyCleaner 1.0")
window.geometry("500x300")
window.configure(background = "dodger blue")

def clean():
    print("Button clicked!")
    cleanAlert.configure(text = "Cleaning!")
    cleaningDir = userDirectory.get()
    cleaningFileTypes = userFiletypes.get()
    FileTypesList = cleaningFileTypes.split(", ")
    for FT in range(len(FileTypesList)):
        FileTypesList[FT] = ("*"+FileTypesList[FT])
    print(FileTypesList)
    cleaningResultDir = userResultDir.get()
    cleaningResultDir = cleaningResultDir + "\%s"

    #does the actual "cleaning"
    try:
        os.chdir(cleaningDir)
        for a in range(len(FileTypesList)):
            os.chdir(cleaningDir)
            formattedCleaningDir = cleaningDir + "\%s"
            for file in glob.glob(FileTypesList[a]):
                print(file)
                os.rename(formattedCleaningDir%file, cleaningResultDir%file)
        cleanAlert.configure(text = "Cleaned!")

    except FileNotFoundError:
        cleanAlert.configure(text = "Please enter a valid directory: FileNotFoundError")
    except OSError:
        cleanAlert.configure(text = "Please enter a valid directory: OSError")


#creates the visual stuff
welcome = tkinter.Label(window, text = "Welcome to PyCleaner!", bg = "dodger blue")
instructions1 = tkinter.Label(window, text = "Enter the directory to be cleaned below:", bg = "dodger blue")
userDirectory = tkinter.Entry(window)
instructions2 = tkinter.Label(window, text = "Enter the filetypes you want moved below separated by a comma:", bg = "dodger blue")
userFiletypes = tkinter.Entry(window)
instructions3 = tkinter.Label(window, text = "Enter the directory you want the files to be moved to:", bg = "dodger blue")
userResultDir = tkinter.Entry(window)
btn = tkinter.Button(window, text = "Clean!", command = clean)
cleanAlert = tkinter.Label(window, text = "", bg = "dodger blue")

#adds it to the window
welcome.pack()
instructions1.pack()
userDirectory.pack()
instructions2.pack()
userFiletypes.pack()
instructions3.pack()
userResultDir.pack()
btn.pack()
cleanAlert.pack()

window.mainloop()