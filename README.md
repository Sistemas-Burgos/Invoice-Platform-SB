# Invoice-Platform-SB
Invoice platform to manage, view and generate in a comfortable way.

## Requirements
### Mandatory programs
- Python 3.9.11 x64 ([Download link](https://www.python.org/downloads/release/python-3911) | [Python installation](#python-installation))
- Git v2.40+ x64 ([Download link](https://git-scm.com/download/win))
- VSCode v1.77+ x64 ([Download link](https://code.visualstudio.com/docs/?dv=win64user))
- Chocolatey v1.3.0+ ([Chocolatey installation](#chocolatey-installation))

#### Python packages
For all packages in this section check [How to install python packages](#python-packages-installation) section.
- Flask v2.3.2+ / Werkzeug v2.3.3+
- Pdfkit v1.0.0+
- Jinja2 v3.1.2+
#### Chocolatey packages
For all packages in this section check [How to install chocolatey packages](#chocolatey-packages-installation.-example:-wkhtmltopdf) section.
- wkhtmltopdf v0.12.6+

### Optional programs (highly recommended)
- TortoiseGit v2.14+ x64 ([Download link](https://tortoisegit.org/download))
- Everything v1.4+ x64 ([Download link](https://www.voidtools.com/downloads))
- Notepad++ v8.5+ x64 ([Download link](https://notepad-plus-plus.org/downloads))

## Considerations installing tools.
Special considerations in the installation of the needed tools. If the tool is not in this section you can click on "next" to all (default installation).
### Python installation
Be sure to check the following checkboxes (they are in order of appearance):
1. Run as Administrator.
2. Check **Add Python 3.9 to PATH** then select **Customize installation**.
3. Next
4. Check **Install for all users**.
5. Install.

Disable default windows python included on system:
1. Open **Windows Settings**
2. Select **Apps**
3. Select **App execution aliases**
4. Disable **python.exe** and **python3.exe**.

Verify Python installation:
1. Enter following command in *Command Prompt (Windows Terminal)*:</br>
    <code>where python & python --version & python --version</code></br>
    ```
    C:\Program Files\Python39\python.exe
    Python 3.9.11
    Python 3.9.11
    ```
2. If some line is different trying to unistall all Python versions and re-try installing the correct one.

### Python packages installation. Example: Flask <a name="python-packages-installation"></a>
Process to install python packages using pip. This example is focused on Flask. However, it can be applied to other packages.</br>
It is mandatory to have Python installed and configured, if not the case check [Python installation](#python-installation) section.

How to install and verify:
1. Run *Command Prompt (Windows Terminal)*.
2. Type: <code>$ py -m pip install flask</code>
3. Verify the installation with this command: <code>$ py -m flask --version</code> then cmd should response with something like (or higher versions):
    ```
    Python 3.9.11
    Flask 2.3.2
    Werkzeug 2.3.3
    ```
    Some packages can show this error:</br>
    ```
    C:\Program Files\Python39\python.exe: No module named jinja2.__main__; 'jinja2' is a package and cannot be directly executed
    ```
    In that case, there is another way to check the version (replace **pdfkit** by the program to be checked):</br>
    <code>$ py -c "import pdfkit; print(pdfkit.\_\_version\_\_);"</code></br>
    The output must be something like:</br>
    ```
    1.0.0
    ```

### Chocolatey installation
For this installation is not needed download any file from Explorer. Just follow next steps:
1. Run *PowerShell* as Administrator and enter next commands:<br/>
    <code> $ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm</code>
2. Now we are going to install ***Chocolatey***, enter next command and accept all.<br/>
    <code>$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))</code>
3. Verify the installation with:<br/>
    <code> $ choco --version</code><br/>
    You must receive the installed version (or higher):
    ```
    1.3.0
    ```

### Chocolatey packages installation. Example: Wkhtmltopdf
Process to install chocolatey packages. This example is focused on Wkhtmltopdf. However, it can be applied to other packages.</br>
It is mandatory to have Chocolatey installed and configured, if not the case check [Python installation](#python-installation) section.

1. Run *PowerShell* as Administrator and enter next command and accept all:<br/>
    <code> $ choco install wkhtmltopdf</code>
2. Verify the installation with:<br/>
    <code> $ wkhtmltopdf --version</code><br/>
    You must receive the installed version (or higher):
    ```
    wkhtmltopdf 0.12.6 (with patched qt)
    ```

## Git configuration and related tools (SSH, Posh-Git and .gitconfig)
1. Create a folder in ***C:\\home*** and add ***HOME*** variable to the *Environment Variables* in Windows. For *User variables* and for *System variables* sections (for both sections).
    ```
    Variable name: HOME
    Variable value C:\home
    ```
2. Open Git Bash and run the following command to make sure that ***.gitconfig*** exists:<br/>
    <code>$ git config --global user.name "FirstName LastName"</code>.
3. Search, open and overwrite content of ***.gitconfig*** file to get configure and set aliases, usually located in: ***C:\\home\\.gitconfig*** (This is a recommended configuration, if you already have another one you can skip this step).

    **IMPORTANT:** Make sure to add your name and your email in *User* section.

    ``` ini
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
    Then a passpharese will be requested (I recommend not use any passphare so just press enter twice).
6. Register and verify the SSH Key in Git Bash:<br/>
    <code> $ eval `ssh-agent -s`</code><br/>
    Replace the github key exactly as the previous step and enter the command:<br/> 
    <code> $ ssh-add ~/.ssh/github_firsNameLastName_id</code>
7. Verify that Git was configured properly, enter next command in Git Bash:
    <code> $ ssh -T git@github.com</code><br/>
    Console must answer something like...<br/>
    ```
    Hi arathburgos05! You've successfully authenticated, but GitHub does not provide shell access.
    ```
8. Now you can clone the repo. I recommend to use another path like **Documents** or near from **C:\\**. Open *Command Prompt (Windows Terminal)* in the path where you are going to have the path, then clone it using:</br>
    <code> $ git clone git@github.com:arathburgos05/Invoice-Platform-SB.git</code><br/>
9. It's highly recommended to install *Posh-Git* which is a tool to show the repo status in PowerShell. To do that just run PowerShell as Administrator and enter next commands:<br/>
    <code> $ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm</code><br/>
    <code> $ Install-Module PowershellGet -Force</code><br/>
    <code> $ PowerShellGet\Install-Module posh-git -Scope CurrentUser -Force</code><br/>
    <code> $ Add-PoshGitToProfile -AllUsers -AllHosts</code><br/>

---

## In developing... 
## (...)

---

### Useful links:
[HTML online editor](https://html-online.com/editor)