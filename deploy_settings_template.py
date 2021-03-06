# Change these settings to match your deployment environment and
# put them in a deploy_settings.py file.

# Ubuntu Version can be 14 or 18
ubuntu_version = 14

# NOTE: Illegal user names
# root, daemon, bin, sys, sync, games, man, lp, mail, news, uucp, proxy,
# www-data, backup, list, irc, gnats, nobody, libuuid, syslog, messagebus,
# sshd
username_main = 'daniel'
ssh_keytype = 'rsa'
username_email = 'mailname'
email_address_webmaster = 'webmaster@dk-cloud.net'
django_db_name = 'django_db'
django_db_user = 'django'
django_db_test_name = 'django_db_test'
django_db_test_user = 'django_test'
ip_address = '198.58.125.218'
domain = 'dk-cloud.net'
make_new_project = False
push_existing_repo = False & (not make_new_project)
existing_repo_location = '/home/me/workspace/domain/'
app_name = 'testapp'
server_name = 'www'
dkim_selector = 'web'
python_version = '3.4'
python_req_file = None  # On local machine
postgres_version = '9.3'
password_login = 'no'
use_https = True
local_test_db = True
remove_temp_files = True