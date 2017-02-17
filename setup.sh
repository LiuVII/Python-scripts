#Homebrew
cd /Volumes/Storage/goinfre/$(whoami)
git clone https://github.com/Homebrew/homebrew.git
#echo 'alias brew="/Volumes/Storage/goinfre/$(whoami)/homebrew/bin/brew"' >> ~/.zshrc
#source ~/.zshrc
brew update

#install python 3
brew install python3

#install python 3 packages
pip3 install APScheduler
pip3 install dj-database-url
pip3 install Django
pip3 install django-environ
pip3 install gspread
pip3 install gunicorn
pip3 install httplib2
pip3 install matplotlib
pip3 install numpy
pip3 install oauth2client
pip3 install pandas
pip3 install requests
pip3 install scipy
pip3 install urllib3
pip3 install virtualenv

#install heroku
brew install heroku-toolbelt
heroku update
