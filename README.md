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
  1.  Create venv with `python -m venv venv`
  2.  Download dependencies `pip install -r requirements.txt`
  3.  Rename .env_example to .env and fill in the proper credentials
  4.  Run backend with `python app.py`

### In frontend  
  1.  Download dependencies with `npm install`
  2.  Rename .env_example to .env and fill in the proper credentials
  3.  Run frontend with `npm run dev`

### Dependencies - BE
[Flask](https://pypi.org/project/Flask/)
[pymongo](https://pypi.org/project/pymongo/)  
[python-dotenv](https://pypi.org/project/python-dotenv/)  
[pyjwt](https://pyjwt.readthedocs.io/en/stable//)

### Dependencies - FE
[react-hook-form](https://www.npmjs.com/package/react-hook-form)  
[axios](https://www.npmjs.com/package/axios)  
[dotenv](https://www.npmjs.com/package/dotenv)  
[leaflet](https://www.npmjs.com/package/leaflet)  
[leaflet-defaulticon-compatibility](https://www.npmjs.com/package/leaflet-defaulticon-compatibility)  
[react](https://www.npmjs.com/package/react)  
[react-dom](https://www.npmjs.com/package/react-dom)  
[react-helmet](https://www.npmjs.com/package/react-helmet)  
[react-leaflet](https://www.npmjs.com/package/react-leaflet)  
[react-router-dom](https://www.npmjs.com/package/react-router-dom)  

## Graphical Profile  
🎨 Visual Identity – RunPrepper   
🟦 Primary Color  
    •    Hex: #007bff  
    •    Usage: Buttons, links, icons for main CTA elements (e.g., “Get Started”, “Save Path”).  
    •    Tone: Bright blue – conveys energy, trust, and motion.  
⚫ Secondary / Dark Background  
    •    Hex: #1e1e1e / #121212  
    •    Usage: Background for Spotify section, footer, or high-contrast sections.  
    •    Tone: Deep gray / near-black – creates a clean and modern feeling.  
⚪ Light Background  
    •    Hex: #ffffff (white)  
    •    Usage: Main background for content sections for clarity and readability.  
🟡 Accent Colors  
    •    Success / Positive feedback: #28a745  
    •    Error / Alerts: #dc3545  
    •    Muted Text: #555555 – for secondary or supporting text.  
⸻  
🔤 Typography  
    •    Primary font: sans-serif  
    •    Styles:  
    •    Headings: Bold with varying sizes (e.g., h1 { font-size: 32px; })  
    •    Body text: Regular weight, around 16px with line-height: 1.5  
⸻  
🧩 Component Styles  
Buttons  
    •    .btn-primary: Blue background, white text, rounded corners  
    •    .btn-danger: Red background, white text (e.g., for delete buttons)  
    •    Hover Effects: Slight shadow or color shift on hover  
Input Fields  
    •    .primary-user-input: Rounded edges, internal padding, light background  
    •    Typically centered and matched in width with buttons for consistency  
⸻  
🧭 Layout & Responsiveness  
    •    Grid / Flexbox used for structured component alignment  
    •    Media Queries used for breakpoints (e.g., hamburger menu under 768px)  
    •    Containers: Max width 1200px, horizontally centered via margin: auto  


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

## Testing procedure
We have implemented E2E tests for some of the core features. For this to work:
- You must have the Backend and Frontend up and running
- While in the root of the Frontend repo folder run the following command: `npx cypress open`
- Navigate to the E2E test selection and just run the test you want to check

## Known bugs
Possible spotify bug:
- One user reported being passed to login after spotify login. Should remain on profile

## Upcoming features
- Community features
