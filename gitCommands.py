import subprocess

def gitSwitchBranch(branchName, repoDir):
    cmd = ['git', 'checkout', branchName]
    p = subprocess.Popen(cmd, cwd = repoDir)
    p.wait()

def gitCheckout(branchName, repoDir):
    cmd = ['git', 'checkout', '-b', branchName]
    p = subprocess.Popen(cmd, cwd = repoDir)
    p.wait()

def gitAdd(repoDir):
    cmd = ['git', 'add', '-A']
    p = subprocess.Popen(cmd, cwd = repoDir)
    p.wait()

def gitCommit(message, repoDir):
    cmd = ['git', 'commit', '-m', message]
    p = subprocess.Popen(cmd, cwd = repoDir)
    p.wait()

def gitDelete(branchName, repoDir):
    cmd = ['git', 'branch', '-D', branchName]
    p = subprocess.Popen(cmd, cwd = repoDir)
    p.wait()
