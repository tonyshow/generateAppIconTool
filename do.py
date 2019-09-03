import os
from PIL import Image
import shutil
import imghdr
from os.path import basename
def createNewImage(inputPath,outPath,width,height):
    image = Image.open(inputPath)
    image_size = image.resize((width, height),Image.ANTIALIAS)
    image_size.save(outPath)  
def doMain():
    _outPath=os.path.join(os.getcwd(),"output/")
    if True==os.path.exists(_outPath):
        print(_outPath)
        shutil.rmtree(_outPath)
    getNeedTarget('./in',doTarget);

def getNeedTarget( path ,_cb):
    filesList=os.listdir(path) 
    for fileName in filesList:
        fileAbpath=os.path.join(path,fileName)
        if os.path.isdir(fileAbpath): 
            getNeedTarget(fileAbpath,_cb)
        else: 
            imgType = imghdr.what(fileAbpath,h=None)
            if imgType != None :
                _cb(fileAbpath,os.path.splitext(fileName)[0] ) 

def doTarget(fPath,targeFName):
    print("\n")
    print(targeFName)
    getAlldirInDiGui('./iconModule',fPath ,targeFName)
#
def moudleFileCb(moduleFPath,newFPath,width,height):
    print("moduleFilePath=%s,newFPath=%s,width=%s,height=%s" %(moduleFPath,newFPath,width,height))

def mkdir(path): 
    import os 
    path=path.strip() 
    path=path.rstrip("\\") 
    isExists=os.path.exists(path) 
    if not isExists: 
        os.makedirs(path)  
        return True
    else: 
        return False
def getAlldirInDiGui( path ,targetPath,targeFName ):
    filesList=os.listdir(path) 
    for fileName in filesList:
        fileAbpath=os.path.join(path,fileName)
        if os.path.isdir(fileAbpath): 
            getAlldirInDiGui(fileAbpath,targetPath,targeFName)
        else: 
            imgType = imghdr.what(fileAbpath,h=None)
            if imgType != None :
                im = Image.open(fileAbpath)
                width = im.size[0]
                height = im.size[1]
                newPath = fileAbpath.replace( "/iconModule","/output/"+targeFName );
                mkdir( newPath.replace(fileName,'') );
                print(newPath);
                createNewImage(targetPath,newPath,width,height)
doMain();
