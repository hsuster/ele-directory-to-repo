import subprocess
import os
import shutil
import gitCommands

repoPath = "C:/Users/andrewh/Documents/DWG_to_GitLab/testRepo"
sourcePath = "C:/Users/andrewh/Documents/myDWG/DWG Copy/35-ELE10_3"
sourceDirList = os.listdir(sourcePath)
filenames = []

def createBranchArray(dirList):
    #Creates array of PDF filenames
    for file in dirList:
        if file.endswith('.pdf'):
            filenames.append(file)
    return(filenames)

def gitSequence(branches, spath, rpath):
    #Makes branch for each file in repo path and copies file
    for branchFile in branches:
        #Substring, remove extension
        branchNoExt = branchFile[:-4]
        print(branchNoExt)
        #Create from clean branch
        gitCommands.gitSwitchBranch("empty", rpath)
        gitCommands.gitCheckout(branchNoExt, rpath)
        #Copy PDF
        shutil.copy(spath + "/" + branchFile,rpath)
        gitCommands.gitAdd(rpath)
        gitCommands.gitCommit(branchNoExt, rpath)

def gitDeleteSequence(branches, rpath):
    #Deletes branch for each file in repo path
    for branchFile in branches:
        #Substring, remove extension
        branchNoExt = branchFile[:-4]
        #Switch to empty branch
        gitCommands.gitSwitchBranch("empty", rpath)
        gitCommands.gitDelete(branchNoExt, rpath)
      
#Creates branch list from source directory
branchArray = createBranchArray(sourceDirList)
#gitSequence(branchArray, sourcePath, repoPath)
#gitDeleteSequence(branchArray, repoPath)




    
    
