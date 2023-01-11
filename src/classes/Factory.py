from classes.readers.ExcellReader import ExcellReader
class Factory():

    acceptedFiles = ["xlsx"]

    def getReader(self,pathname):
        try:
            pathNameArray = pathname.split("/")
            fileName = pathNameArray[len(pathNameArray)-1]
            fileNameArray = fileName.split(".")
            fileExtsension = fileNameArray[len(fileNameArray)-1]
        except:
            raise TypeError("Path is incorrect")
        if (fileExtsension not in self.acceptedFiles):
            raise TypeError("Extension of file cannot be opened")
        if(fileExtsension == "xlsx"):
            return ExcellReader(pathname)



