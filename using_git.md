Some notes adapted from:   https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html


+ Tell git who you are:
```
git config --global user.email jason@xyz.com
```

+ Check out our repository from the web:
```
git clone https://github.com/jpsember/ml.git
```

+ Make some changes to some files, then look at the status of the repo:
```
git status
```

+ Add new files, and commit changes with description.  Here, for example, I just created the file 'using_git.md', and am telling git to start including this file, and making a commit representing this change:
```
git add using_git.md

git commit -am "adding using_git.md"

```

+ Make further changes to files, and making another commit:
```
git commit -am "further changes to using_git"

