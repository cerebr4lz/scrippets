# jsteeleiv 2023

# Automatically change password for a user.

user=$1
echo -e "xxxxxx" | (passwd --stdin $user)
chage -d 0 $user
echo "Done "