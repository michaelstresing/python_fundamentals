'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.



CLI Commands For the steps above:

cd ~/Desktop/CodingNomads
python3 -m venv venv
source venv/bin/activate
pip install Django
pip install Flask
pip install TensorFlow
pip freeze > requirements.txt
deactivate
cd ~/Desktop/CodingNomads/
rm -r venv
python3 -m venv venv2
pip install -r requirements.txt
deactivate

'''