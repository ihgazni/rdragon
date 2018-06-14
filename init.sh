username = $1
password = $2

email = $3
commituser = $4

reponame = rdragon

echo https://${username}:${password}@github.com  > $HOME/.git-credentials

git init
git remote add origin https://github.com/${username}/${reponame}.git
git pull origin master


git config --global user.email ${email}
git config --global user.name ${commituser}
git config --global credential.helper store

git add .
git commit -m "init.sh"
git push origin master
