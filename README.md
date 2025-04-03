# RunPrepper

## Description
The ultimate route planer for your runing needs

## How to setup and run
Git clone [backen repo](https://github.com/dangosailing/aidev24_webdev_be/)  
Git clone [frontend repo](https://github.com/dangosailing/aidev24_webdev_fe/)  

### Prequisities
Install [MongoDB community edition](https://www.mongodb.com/try/download/community) if you want to run local or replace the connection string in the .env with an online cluster equivalent.    
Feel free to add [Mongo DB Conpass](https://www.mongodb.com/try/download/compass) as well! It can be added along with the MongoDB CE install.  

### In backend
  1. `python -m venv venv`
  2.  Download dependencies `pip install -r requirements.txt`
  3.  Rename .env_example to .env and fill in the proper credentials
  4.  Run backend with `python app.py`

### In frontend  
  1.  Download dependencies with `npm install`
  2.  Rename .env_example to .env and fill in the proper credentials
  3.  Run frontend with `npm run dev`

### Dependencies - BE
Flask
pymongo (https://pypi.org/project/pymongo/)  
python-dotenv  (https://pypi.org/project/python-dotenv/)  
pyjwt (https://pyjwt.readthedocs.io/en/stable//)

### Dependencies - FE
react-hook-form (https://www.npmjs.com/package/react-hook-form)  
axios (https://www.npmjs.com/package/axios)  
dotenv (https://www.npmjs.com/package/dotenv)  
leaflet (https://www.npmjs.com/package/leaflet)  
leaflet-defaulticon-compatibility (https://www.npmjs.com/package/leaflet-defaulticon-compatibility)  
react (https://www.npmjs.com/package/react)  
react-dom (https://www.npmjs.com/package/react-dom)  
react-helmet (https://www.npmjs.com/package/react-helmet)  
react-leaflet (https://www.npmjs.com/package/react-leaflet)  
react-router-dom (https://www.npmjs.com/package/react-router-dom)  



## Branch organization
**main** - production environment.  
**dev** - main development branch. Feature branches are merged into this one.  
**"feature-branches"** - developing individual features in isolation that are later merged into dev.

## Pull Request rules
- No merging of branches into main or dev without a pull request.  
- Pull requests must be reviewed and approved by at least one person before accepting merge into dev.  
- Releases/PR into main is handled under group supervision.  
- Smaller fixes or documentation updates can be made directly into the dev branch.

## Database structure
MongoDB collections:
users - username and password  
paths - Store postion data, title, distance and time for each path. Also contains a refernce to the user_id
Currently implements a validation for the users collection

## Known bugs
Possible spotify bug:
- One user reported being passed to login after spotify login. Should remain on profile

## Upcoming features
- Community features
