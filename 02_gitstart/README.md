# Git or Hub

Here is a quick review of the points covered in chapter 2, "Git and GitHub Fundamentals".

I've added a few things that weren't in the text.

Here's a [Mermaidjs][mjs] version of [Figure 2.2][fig22].

[mjs]: https://mermaid.js.org/
[fig]: ./git-workflow.md

## Basic Git

- **command-line tool**
- distributed version control system
  - allows tracking of changes to files
    - what changed
    - who changed it
    - when it was changed
  - allows editing to take place in parallel
    - teams need not wait for one another to finish working on each file
  - offers options to manage the combination of revisions
    - manage synchronisation and conflicts
    - maintain various historical versions

## Basic GitHub

- **web-based** central storage for git repositories
- offers features for collaboration and communication
  - discussion boards
  - project management timelines
- GitHub Actions offers continuous integration and/or deployment (CI/CD)
- [bought by Microsoft][yuck] in 2018.
  - some competitors are [GitLab][glab] and [BitBucket][bbkt] and [Codeberg][berg]

## Install git

- Debian-based Linux, e.g. Ubuntu/Mint: `sudo apt-get install git`
  - `apt` is the flashier version, both are front-ends to [`dpkg`][dpkg]
- Red Hat-based Linux, e.g. RHEL/Fedora: `sudo dnf install git`
  - You may also see `rpm` and `yum` as alternative [package managers][rpm]
- Arch Linux: `sudo pacman -S git`
  - [Pacman][arch] is the default package manager for Arch Linux, the veganism of the Linux world
- Mac OS X: `brew install git`
  - [Homebrew][brew] is also available for Linux
- Windows: `choco install git`
  - [Chocolatey][choc] is a package manager for Windows

Official [website][gito] offers more details.

## GUI clients for git

Some third-party options are available at [the GUIs page of the official site][ggui].

## Starting with GitHub

1. Using a web browser, create an account at https://github.com/join and/or sign in
2. Click the `+` button in the top right corner.
3. Click "New repository" and complete the form.
4. You will be taken to the repository's page, e.g. https://github.com/username/myrepo - leave this window open.

## Commands

In the command-line entries below, the following syntax applies:

 - wherever you see `${name}` that means you should substitute your own value where it is necessary.
 - If any argument is surrounded by square brackets like `[${name}]`, it means that that argument is
   optional and need not be included.
 - any text after a hash sign `#` is a comment for your reference and need not be copied.

With any git command, feel free to get help on it by adding `--help` at the end or `help` after `git`:
```
git help commit
git commit --help
```

Do note that these pages can be pretty wordy, read them carefully.

### Setup

You will need a username and email address to make commits. The email need not actually work,
but it is recommended to set a working address if you intend to collaborate with others.

- Username:
  ```
  git config --global user.name ${name} # use quotes for more than one word, e.g. "my name"
  ```

- Email:
  ```
  git config --global user.email ${email} # can use quotes for safety, e.g. "username@email.com"
  ```

### New Repository

- **Initialise a directory** as a git repository:
  ```
  git init [directory name]
  ```
  If the directory name is not specified, the current directory you are in will be set up as a repository.

- Alternatively, to **clone an existing repository from a remote**:
  ```
  git clone ${remote_address} [${directory_name}]
  ```
  Here, substitute the actual address after the word `clone`. This remote address can be a URL beginning
  with https://, as above, or some other format. Here, if the directory name is not specified, git tries
  to create a new directory with the name of the repo, for example:
  ```
  git clone https://github.com/username/somework
  ```
  The above command will try to create a `somework` directory and clone the remote into it. This fails if
  the `somework` directory already exists. In addition, a remote (usually called `origin`) is automatically
  created which points to the address provided above.

### Retrieve Updates

- Fetch any commits from the same branch on a remote, and merge them:
  ```
  git pull
  ```

- Fetch all the branches from a remote, but not merge them:
  ```
  git fetch [${remote_alias}]
  ```
  Specifying the `${remote_alias}` is optional, if there is only one (e.g. `origin` as above), then there
  is only one place to fetch updates from.

### Working with Changes

- Check the **status** of the working directory to see if anything has changed:
  ```
  git status
  ```

- **Add** a file to the staging area, preparing to commit it:
  ```
  git add ${filename}
  ```
  You may want to check `git status` again to see if you have staged the right file.

- **Commit** the contents of the staging area:
  ```
  git commit [-m "${commit_message}"]
  ```
  If you supply the `-m` argument, make sure the commit message is provided in quotes.
  If the `-m` argument is left out, a text editor will open where you can work on the
  commit message. Saving that message "file" will also save the commit.

- **Push** local commit(s) to the remote, optionally specifying a branch:
  ```
  git push [${remote_alias}] [${branch_name}]
  ```
  If the names are not specified, git assumes you want to push the current branch to the default remote.

- Check that the latest commit has been added to the **log**:
  ```
  git log
  ```

### Swinging between branches

- To switch from one branch to another, `checkout` that branch:
  ```
  git checkout ${branch_name}
  ```
  You can use other IDs in place of `${branch_name}`, such as specific commit IDs.

[yuck]: https://news.microsoft.com/announcement/microsoft-acquires-github/
[glab]: https://about.gitlab.com
[bbkt]: https://bitbucket.org
[berg]: https://codeberg.org
[dpkg]: https://www.dpkg.org
[rpm]:  https://www.redhat.com/en/nblog/how-manage-packages
[arch]: https://wiki.archlinux.org/title/Pacman
[brew]: https://brew.sh
[choc]: https://community.chocolatey.org
[gito]: https://git-scm.com/downloads
[ggui]: https://git-scm.com/downloads/guis
