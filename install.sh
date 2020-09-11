# INSTALL SCRIPTS
# FOR Mac OS:
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
mkdir ~/bin
touch ~/.zshrc
echo 'export PATH="~/bin":$PATH' > ~/.zshrc
brew install youtube-dl
brew install jq
curl -O https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_mac64.zip
brew install unzip
unzip chromedriver_mac64.zip 
chmod a+x chromedriver
mv chromedriver ~/bin/
rm chromedriver_mac64.zip 
python3 -m pip install --update pip
python3 -m pip install selenium
python3 -m pip install pyautogui
python3 -m pip install tensorflow
exec -l $SHELL
# NOT COMPLETE

# GET Chrome user dir for research
cp -r ~/Library/Application\ Support/Google/Chrome/Default ~/Desktop

# Will include 1-click auto setup and as much auto cloud as allowed in terms of service

# For Windows use the choco package manger

# For linux or virtual envs use similar
