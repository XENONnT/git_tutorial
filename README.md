# Git/GitHub playground

Use this repository to play around with git and github to learn by doing.

## Learn Branching
If you want to master the art of git branching, use this awesome tool: https://learngitbranching.js.org/ (if you want)

## Learn submodules
First and foremost, for any issues with submodules, the git submodules documentation is available [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### Clone a repository with submodules


When cloning the repository with a simple `git clone <repo_address>`, the submodules' directories will be present but empty, as they are not automatically initialised.
To clone the repo, recursively initialise the submodules and fetch the contents at the commit specified by the superproject (the main or upper repo), do:
```
git clone --recurse-submodules git@github.com:XENONnT/git_tutorial.git
```

If you clone the repository without initialising the submodules using the flag `--recurse-submodules`, you can still initialise and update the submodules as follows:
```
# Initialise and update (populate) submodules, including nested submodules
git submodule update --init --recursive
```

### Clone a repository with partially initialised submodules
If you want to initialise only a selected group of submodules, clone the repository using vanilla `git-clone`, then do the following

### Add a submodule to a repository
To add a submodule (for example [cutax](git@github.com:XENONnT/cutax.git)) to this repo, do the following:

- Clone this repository
```
git clone git@github.com:XENONnT/git_tutorial.git
```
- Enter the repo and go to the location you want to add the submodule
```
cd git_tutorial; mkdir submodules; cd submodules
```
- Add the submodule
```
git submodule add git@github.com:XENONnT/cutax.git
```
- Decide at which commit to checkout the submodule
- Commit
```
git commit -m "Added cutax as submodule"
```



