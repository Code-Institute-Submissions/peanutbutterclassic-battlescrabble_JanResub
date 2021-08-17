# BattleScrabble

<!-- [View the live project here.](https://story-vault.herokuapp.com/) -->

![](https://raw.githubusercontent.com/peanutbutterclassic/battlescrabble/main/assets/images/screenshot_amiresponsive.png)
The image is from [Am I responsive?](http://ami.responsivedesign.is/)

Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods.

How it will work:
* A 10x10 grid will have 3 ships of variable length randomly placed about.
* You will have 50 bullets to take down the ships that are placed down.
* You can choose a row and column such as A3 to indicate where to shoot.
* For every shot that hits or misses it will show up in the grid.
* A ship cannot be placed diagonally, so if a shot hits the rest of the ship is in one of 4 directions, left, right, up, and down.
* If all ships are unearthed before using up all bullets, you win else, you lose.


## UX
I aimed to integrate ease-of-use concept despite the limitation of the CLI.

#### Target audience:
* Over 18s only since this is a violent game.

### The game will help clients to:
* Navigate easily through the terminal
* Test their reading skills
* Improve their imagination
* Provide entertainment

## Owner Stories
1. As the owner, I want the game to be fun and make the user to keep returning.
2. As the owner, I want the game to be educational.
3. As the owner, I want to show my new learned skills with Python.

### User Stories
1. As a new visitor, I want to easily navigate the terminal to play the game.
2. As a visitor, I want to be able to exit the game when I get tired of playing.
3. As a visitor, I want to be create and read fun stories.

## The skeleton
The Game consists of only 1 page which is the terminal page. I am using Python to generate the data and create the game.
* The terminal game is not responsive and is only one page therefore wireframes were not needed this time.

## The Scope
To achieve my goal, I included the following features in my game:

### Features
1. A grid with randomised battleships placed either horizontally or vertically.
2. Limited number of shots to take.
3. Scrabble concept added to improve interactivity.


### Future features
In the future, I would like to develop this game to include the following features:
* A timer to add pressure to the player.
* A two player option so people can play online with other human users.
* A more interactive word hit coordinates features.

## The Design
The game is designed using CLI so the outlook is very basic. 
  

## Technologies Used
* This project integrates basic python concepts such as: Loops; Strings; Arrays; 2D Arrays; Global Variables; Methods.
* The following platforms have been used:
 * [Gitpod](https://gitpod.io/workspaces) for writing code to develop this game.
 * [Github](https://github.com/) Was used for hosting my repository and this readme file.
 * [Heroku](https://id.heroku.com/login) for deployment.
 * [pep8online.com](http://pep8online.com/) for validating my code and check for errors.

## Testing
As a user/player, the game shall be easy to navigate in the terminal.
* The battle grid appears as soon as the game starts.
* The player has to select the coordinates to take down the battleships and guess the word at the end to completely sink the ships.
![](https://raw.githubusercontent.com/peanutbutterclassic/battlescrabble/main/assets/images/screenshot_errors.png)

 ### Additional Testing
* [pep8online.com](http://pep8online.com/) is used to confirm my code.
* python3 run.py has been used intensively during the creation of this game.
* Automatic set up on [Heroku](https://id.heroku.com/login) which should allow me to see how the end product of the game from the code I created. However, errors occured which meant I had to abandon the development.

 ## Compatibility
To ensure that a broad range of users can successfully view/use the site, I tested it across all major browsers on both desktop and mobile.
* Chrome
* Mozila Firefox
* Edge
* Internet explorer
* Safari
Although this is a web app it is visible on a mobile and tablets, even though it is not responsive.

## Validation
<!-- Add validation snapshot -->

## Deployment
This project was developed using Gitpod, committed to git and pushed to GitHub using git commands. You can clone this repository [Here](https://github.com/peanutbutterclassic/battlescrabble)

To deploy this page to Heroku from GitHub repository, the following steps were taken:

1. In the Heroku dashboard I selected 'New' in the top right hand corner and clicked on 'Create new app'.
2. Then I Created the App name and Choose my region as Europe. Then selected 'Create app'
4. Then I selected Settings tab, and scrolled down to 'Buildpacks'. Here I added 'Python' clicked saved changes and then selected 'Node.js' and saved my changes again.
5. On top of the page I clicked on the 'Deploy' section, and I selected Github as my deployment method.
6. Then I selected 'Connect to Github, and searched for my repository name and clicked on 'Connect' to link my Heroku app to my Github repository code.
7. Scrolling down I have selected 'Enable Automatic Deploys' and after this I selected 'Deploy Branch' to deploy my project. I had to wait for it to build.
8. After it has successfully deployed a 'view' button appeared which took me to my deployed app.

## Credits
* [Austin Montgomery](https://bigmonty12.github.io/battleship) 
* I have used [S. Mengel](https://www.enseignement.polytechnique.fr/informatique/CSE101/TD/td_9/CSE101-td_9-1.html)'s materials from l'École polytechnique in Paris to better understand how to create a battleship game. 
* I have watched the following videos for inspiration:
   1. [CS Students](https://www.youtube.com/watch?v=MgJBgnsDcF0)
   2. [Jie Jenn](https://www.youtube.com/watch?v=gkglr8GID5E) 
* My Mentor Guido Cecilio Garcia Bernal was extremely helpful in breaking all the steps down for me and answering any questions I had, especially those concerning randomising words to add to the battleship game.
* I have been fortunate to get useful pointers from Code Institute's tutoring team, which I am grateful for.
* Thanks to [Twilio Blog](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) for a thorough explanation on how to work with Google Spreadsheets and Python.
* [Stack Overflow](https://stackoverflow.com/questions/18834636/random-word-generator-python)
* [Stack Overflow](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)
* [devpost](https://www.youtube.com/watch?v=zSQIGzmcp2I)
