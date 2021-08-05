branchName="master"
# echo $branchName (stay as master)
username=$1
# echo $username (youremail dltronganh)
Date=`date +%d%m%y_%H%M`
# echo $date
branchName=$branchName\_$username\_$Date
echo $branchName    

git init
git config --global user.email $username@gmail.com
git add .
git commit -m "$username updated"
git checkout -b $branchName
git push -u origin $branchName
