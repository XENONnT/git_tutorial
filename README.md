# Git/GitHub playground

Use this repository to play around with git and github to learn by doing.

## Learn Branching
If you want to master the art of git branching, use this awesome tool: https://learngitbranching.js.org/

## Cool `aliases`
I recommend adding these lines to your `~/.gitconfig`:
```
[alias]
        lol = log --graph --decorate --pretty=oneline --abbrev-commit
        lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
[color]
        branch = auto
        diff = auto
        interactive = auto
        status = auto
```

This will allow you to use `git lol` and `git lola` to have a cool and clear view of the commit chain of your repository!
Source, related music, and further info [here](http://blog.kfish.org/2010/04/git-lola.html).

## Learn submodules
First and foremost, for any issues with submodules, the git submodules documentation is available [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

You hate reading? [Here](https://www.youtube.com/watch?v=gSlXo2iLBro)'s a useful 15 minute video that goes over the essentials.
If you use double speed, it takes half the time!

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
- Commit (submodule addition is automatically staged, together with the creation/update of the `.gitmodules` file)
```
git commit -m "Added cutax (v1.0.0) as submodule"
```
Done! 🥳💃
### Working with submodules
Submodules are nothing but git repositories within another git repository (the superproject). The directories containing the submodules will point to a specific commit of the submodule, and will not actually contain the contents of the whole submodule's repo! (That's why, when simply running `git-clone`, the submodule's dirs are empty).

Working on a submodule from within the submodule's directory is the same as working with any other repository.
If you commit some changes, you just have to tell the superproject to now point at the newest commit (or whichever commit you prefer). To do this, leave the submodule's dir and head to the superproject and commit the changes to the submodule.

For instance, say you want the `cutax` submodule we have added in the previous section to be checked-out at version v1.0.0; you can then do the following
```
# From root of git_tutorial, enter the relevant submodule
cd submodules/cutax

# Let's assume we're currently at commit #0fa392
# Do things and change commit (either by creating a new one with git-commit, or checking-out an existing one with git-checkout
git checkout v1.0.0  # e.g. commit #ab392f
```
By doing this, you have moved HEAD to point to another commit(`#ab392f`, tagged as `v1.0.0`). The superproject is however still pointing at the previous commit (`#0fa392` in the example).
Let's update the superproject to point at the new HEAD of the submodule:
```
# From submodules/cutax
cd ..

# Acknowledge changes to submodule
git add cutax

# Commit
git commit -m "Submodule cutax checked-out at v1.0.0"
```

If you `git-push` these changes, the next person to `git-pull` or `git-clone` this repo will see that the `cutax` submodule is automatically checkout at `v1.0.0` with a detached HEAD.

### Pulling
#### Pull only selected submodules
To pull content from a specific submodule, simply use `git-pull` from within the directory of the submodule.
To pull content of all submodules from the superproject directory, you can use:
```
git submodule update --remote <submodule_1> [<submodule_2> ...]
```
If they are not yet initialised, also add the `--init` flag; if they contain submodules themselves, use the `--recursive` flag.

#### Pull the superproject and all its submodules
Simply running
```
git pull
```
from the superproject will also run git-fetch on all the submodules, but will not update them!
To update them all, run
```
git submodule update
```

## Suggested use for analysiscode
The repo can be cloned without automatically cloning all submodules:
```
git clone https://github.com/XENONnT/analysiscode
```
This will leave all submodules directories uninitialised and empty.
If the user wants to work on or check the status of one or more specific submodules (e.g. `sub_1` and `sub_2`), they can do so by only initialising and updating those:
```
git submodule update --init --recursive --remote <path to sub_1> <path to sub_2>
```

Now only the directories of submodules `sub_1` and `sub_2` are initiated and populated.

When running `git-pull` from superproject, the changes to the submodules will be fetched, but will only be applied once `git-submodule-update` is run again from superproject or when `git-pull` is run directly from within the submodule.
