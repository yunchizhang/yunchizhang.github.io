pelican content -o output -s publishconf.py
ghp-import output -r origin -b main
git push origin main
git checkout pelican