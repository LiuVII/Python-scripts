apt-get update
apt-get install openssh-server openssh-client -y
CONFIG_FILE='/etc/ssh/sshd_config'
REP_VAL='51543'
sed -i.bak "s/^\(Port \).*/\1$REP_VAL/" $CONFIG_FILE
/etc/init.d/ssh reload