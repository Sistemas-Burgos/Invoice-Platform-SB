# Invoice-Platform-SB
Invoice platform to manage, view and generate in a comfortable way.

## Requirements
### Mandatory programs
- VSCode v1.77+ x64 ([Download link](https://code.visualstudio.com/docs/?dv=win64user))

### Optionals programs (highly recommended)
- TortoiseGit v2.14+ x64 ([Download link](https://tortoisegit.org/download))
- Git v2.40+ x64 ([Download link](https://git-scm.com/download/win))
- Everything v1.4+ x64 ([Download link](https://www.voidtools.com/downloads))
- Notepad++ v8.5+ x64 ([Download link](https://notepad-plus-plus.org/downloads))


## Git configuration and related tools (SSH, .gitconfig and Posh-Git)
1. Create a folder in ***C:\\home*** and add ***HOME*** variable to the *Environment Variables* in Windows. For *User variables* and for *System variables* sections (for both sections).
    ```
    Variable name: HOME
    Variable value C:\home
    ```
2. Open Git Bash and run the following command to make sure that ***.gitconfig*** exists:<br/>
    <code>$ git config --global user.name "FirstName LastName"</code>.
3. Search, open and overwrite content of ***.gitconfig*** file to get configure and set aliases, usually located in: ***C:\\home\\.gitconfig*** (This is a recommended configuration, if you already have another one you can skip this step).

    **IMPORTANT:** Make sure to add your name and your email in *User* section.

    ``` ini class:"lineNo"
    [user]
        name = FirstName LastName # <-- Change by your name. 
        email = email@domain.com # <-- Change by your email.
    [alias]
        co = checkout
        br = branch
        ci = commit
        st = status
        stp = status --porcelain
        co- = checkout --
        dt = difftool
        lg = log --graph --date=relative --pretty=format:'%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%an %ad)%Creset'
        t = log --pretty=format:'%C(auto)%h %C(auto,magenta)%ad %C(auto,red)| %C(auto)%d %C(auto,reset)%s %C(auto,dim normal)[%an]' --decorate --graph --date=format:'%d.%m.%y %H:%M' --all
        oops = commit --amend --no-edit -m
        review-local = !git lg @{push}..
        mrg = merge --no-ff --no-commit
        zip = "!f() { git archive --format=zip HEAD `git diff master... --name-only`; }; f"
    [color]
        ui = auto
    [diff]
        mnemonicPrefix = true
        renames = true
        submodule = log
        tool = vscode
    [log]
        abbrevCommit = true
        follow = true
    [status]
        submoduleSummary = true
        showUntrackedFiles = all
    [tag]
        sort = version:refname
    [mergetool]
        keepbackup = false
    [core]
        editor = code --wait
        whitespace = cr-at-eol
        longpaths = true
    [filter "lfs"]
        smudge = git-lfs smudge -- %f
        process = git-lfs filter-process
        required = true
        clean = git-lfs clean -- %f
    [difftool "vscode"]
        cmd = code --wait --diff $LOCAL $REMOTE
    [merge]
        tool = vscode
    [mergetool "vscode"]
        cmd = code --wait $MERGED
    ```
4. Create ***config*** file (make sure not put any extension) and add next content:
    ``` shell
    ### How to fill - Example:
    ## Default user (Arath Burgos)
    # Host github.com
    # HostName github.com
    # User git
    # IdentityFile ~/.ssh/github_ArathBurgos_id

    ### Template:
    ## Default user (firstName lastName)
    Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_firsNameLastName_id
    #############################################################################
    ```

5. Continue in git bash following commands to start linking your SSH Key:<br/>
    Replace the email in the command by your email:<br/>
    <code> $ ssh-keygen -t rsa -b 4096 -C email@domain.com</code><br/>
    When a path to be requested edit your ***User*** according to your username in the key typed in the previous step (**IdentityFile** section) and then enter the command:<br/>
    <code>$ ~/.ssh/github_firsNameLastName_id<br/> # Example:<br/># ~/.ssh/github_ArathBurgos_id</code><br/>
    Then a passpharese will be requested (I recommend not use any passphare so just press Enter twice).
6. Register and verify the SSH Key in Git Bash:<br/>
    <code> $ eval `ssh-agent -s`</code><br/>
    Replace the github key exactly as the previous step and enter the command:<br/> 
    <code> $ ssh-add ~/.ssh/github_firsNameLastName_id</code>
7. Verify that Git was configured properly, enter next command in Git Bash:
    <code> $ ssh -T git@github.com</code><br/>
    Console must answe something like...<br/>
    ```
    Hi arathburgos05! You've successfully authenticated, but GitHub does not provide shell access.
    ```
8. Now you can clone the repo. I recommend to use another path like **Documents** or near from **C:\\**. Open *Command Prompt (Windows Terminal)* in the path where you are going to have the path, then clone it using:</br>
    <code> $ git clone git@github.com:arathburgos05/Invoice-Platform-SB.git</code><br/>
9. It's highly recommended to install *Posh-Git* which is a tool to show the repo status in PowerShell. To do that just run PowerShell as Administrator and Enter next commands:<br/>
    <code> $ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm</code><br/>
    <code> $ Install-Module PowershellGet -Force</code><br/>
    <code> $ PowerShellGet\Install-Module posh-git -Scope CurrentUser -Force</code><br/>
    <code> $ Add-PoshGitToProfile -AllUsers -AllHosts</code><br/>

# In developing...
## (...)


