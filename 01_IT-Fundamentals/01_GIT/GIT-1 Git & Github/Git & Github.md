# Git & Github
Git is a free and open source distributed version control system. Github offers a cloud-based Git repository where developers can store, manage, track and control changes to their projects.
## Key terminology
- **Distributed Version Control System**  
A distributed version control system (DVCS) is a type of version control through which the complete repository becomes available every team member’s computer, so they can commit, branch, and merge locally. The server doesn’t have to store a physical file for each branch but rather just needs the differences between each commit.
- **Centralized Version Control System**
In a centralized version control system (CVCS), a server acts as the main repository which stores every version of code. Using centralized source control, every user commits directly to the main branch, so this type of version control often works well for small teams, because team members have the ability to communicate quickly so that no two developers want to work on the same piece of code simultaneously. In a centralized version control system there are only two data repositories that users have to monitor: the local copy and the central server.
- **Repository**  
A repository is a virtual domain where you can store data. It contains all files and the file's history on it. In doing so, it creates a place where people can see and comment on each others work, and with the right permissions, propose changes to them.
- **Main/Master**  
The main branch or master branch is the central branch of your repository. 
- **Branch**  
A branch is a version of the repository. This can be the master/main branch, or a copy of the master branch that exist parallel to it. The changes made to the copy of the main branch in the parallel branch do not affect the main branch, until such time when they are merged.
- **Commit** 
A commit is a change to a file. Whenever you 'commit' to the change you made, a hash is created to record this change. In this hash,  you can find all the information regarding the change. 
- **Push**  
Pushing means that you send the committed changes that you made on your local machine to the remote repository that exists on Github.com.
- **Pull**  
Pulling means that you are receiving the commited changes from the local machine at the remote repository.
- **Merge**  
Merging takes the changes from one branch and applies them to the branch they are merging with. These can be done either via the command line or via the GUI which in this case is the Github website.
- **Fork**  
A fork is a copy of another repository that you can keep on your account in order to make changes to it without affecting the original repository.


## Exercise
### Sources  
- https://docs.github.com/en/get-started/quickstart/github-glossary#branch  
- https://www.geeksforgeeks.org/centralized-vs-distributed-version-control-which-one-should-we-choose/   
- https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository  
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address
- https://about.gitlab.com/topics/version-control/what-is-centralized-version-control-system/#:~:text=A%20centralized%20version%20control%20system%20only%20has%20two%20data%20repositories,can%20decrease%20insight%20into%20projects  
- https://www.geeksforgeeks.org/centralized-vs-distributed-version-control-which-one-should-we-choose/
- https://www.perforce.com/blog/vcs/what-dvcs-anyway

### Overcome challenges
I had some difficulty with pushing code via GitBash, but I got it to work by use of the sources.

### Results
- Made a Github repository ![Github Repository Made](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/84c48204dab6c201d0e90d3c211fde3c7e7dc2fd/00_includes/Sprint%201/Screenshots%20Git/GIT-01%20-%20Git%20&%20Github/GIT-01%20Exercise%20%201%20-%20%231%20&%202_Account.png)
- Gave permissions to my teammates ![Permissions given to teammates](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/84c48204dab6c201d0e90d3c211fde3c7e7dc2fd/00_includes/Sprint%201/Screenshots%20Git/GIT-01%20-%20Git%20&%20Github/GIT-01%20Exercise%201%20-%20%233_Permissions.png) 
- Pushed code to the repository ![Code pushed to repository](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/84c48204dab6c201d0e90d3c211fde3c7e7dc2fd/00_includes/Sprint%201/Screenshots%20Git/GIT-01%20-%20Git%20&%20Github/GIT-01%20Exercise%201%20-%20%234_Push.png)  
- Cloned Jeena's Repository ![Cloned Jeena's Repository](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/84c48204dab6c201d0e90d3c211fde3c7e7dc2fd/00_includes/Sprint%201/Screenshots%20Git/GIT-01%20-%20Git%20&%20Github/GIT-01%20Exercise%201%20-%20%235_Clone_Jeena.png)  
- Created a new repository for a portolio ![Created a new repository for a portfolio](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/84c48204dab6c201d0e90d3c211fde3c7e7dc2fd/00_includes/Sprint%201/Screenshots%20Git/GIT-01%20-%20Git%20&%20Github/GIT-01%20Exercise%202%20-%20%231%20&%202_Portfolio.png)