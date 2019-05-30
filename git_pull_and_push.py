# Loading the libraries
import os

# You can add your origin branch name instead of develop & master
git_checkout_develop = "git checkout develop"
git_pull_develop = "git pull origin develop"

git_checkout_master = "git checkout master"
git_pull_master = "git pull origin master"

git_push_develop = "git push origin develop"
git_push_master = "git push origin master"

git_branch = "git branch"
git_status = "git status"
git_add = "git add ."
git_commit = "git commit -m "

# Just enter your directory name's in list
git_repos = [
	"Python_programs",
	"PersonalAssistant",
	"turtle"
]
    
def gitPull():
    '''
        This method is used to pull from develop & master branch.        
    '''
    for i in git_repos:
        os.chdir(i)
        working_dir = os.getcwd()
	
        print("\n---------" +working_dir+"---------")   
        print("\n-----current_branch-----")
        os.system(git_branch)
        choice = int(input("\n Which branch you want to push code(\n1:Develop  \n2:Master  \n3:No pull on this branch \n[1/2/3]:"))
        if choice == 1:
            os.system(git_checkout_develop)
            os.system(git_pull_develop)
            os.chdir("..")
        elif choice == 2:
            os.system(git_checkout_master)
            os.system(git_pull_master)
            os.chdir("..")
        elif choice == 3:
            os.chdir("..")
        else:
            print("Something Went Wrong..!")
        
def gitPush():
    '''
        This method is used to push to develop & master branch.        
    '''
    for i in git_repos:
        os.chdir(i)
        working_dir = os.getcwd()
        print("\n---------" +working_dir+"---------")
        print("\n This is your current status on current branch ")
        os.system(git_branch)
        os.system(git_status)
        choice = int(input("\n Which branch you want to push code(\n1:Develop  \n2:Master  \n3:No commit on this branch \n[1/2/3]:"))
        if choice == 1:
            os.system(git_checkout_develop)
            os.system(git_add)            
            commit_msg = raw_input("\n Enter commit message here:")
            git_commit_message = git_commit + commit_msg
            os.system(git_commit_message)
            os.system(git_push_develop)
            os.chdir("..")
        elif choice == 2:
            os.system(git_checkout_master)
            os.system(git_add)
            string = " "
            commit_msg = raw_input("\n Enter commit message here:")
            git_commit_message = git_commit + commit_msg
            os.system(git_commit_message)
            os.system(git_push_master)
            os.chdir("..")
        elif choice == 3: 
            os.chdir("..")
        else:
            print("Something Went Wrong..!")
            
choice = int(input("\n What you want to do select option :\n 1. Pull \n 2. Push \n 3. Nothing \n"))
if choice == 1:
    gitPull()
elif choice == 2:
    gitPush()
elif choice == 3:
    exit()
else:
    print("Something went Wrong")

