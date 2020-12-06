## Welcome to Counting Game
An OOP Python game which can challenge your intelligence

**Table of Contents** 
- [Rule](#rule)
- [Installation Guide](#installation-guide)
- [User Guide](#user-guide)
- [Tips to win](#tips-to-win)
- [Personal opinions](#personal-opinions)

****
### Rule
Given a goal number, for example: 30  
We will start the game with counting 1 (or 2, or 3).  
Two players (you and the computer) will take turn counting a number,  who ever reaches counting 30 first will win.  

There are some restrictions when counting:  
1. The first player will count either 1, 2, or 3.  
2. Then for each turn, a player can add 1, 2, or 3  to the current number to create a new one and count it out.  
    >For example: player 1 counts 1, player 2 can either count 2, 3, or 4.  
3. Who counts or passes 30 first will win.


****
### Installation Guide
1. Clone the repository
	<code>git clone [repo-clone-link]</code>
2. Open and run the file <code>main.py</code>
	**Note:** make sure all files are in the same repository

****
### User Guide
**Note**: make sure all files are in the same directory
- When you run the <code>main.py</code> file, the game starts and you will need to give some inputs for:
	- Your name
	- Is it the first time you play the game (if yes then a demo will be shown)?
	- Which level you want to play?
	- After finishing one game, you may want to choose to restart the game

If you want to increase the game's difficulty, check the <code>main.py</code> and change the following three variables:

1. goalNumber: a number you need to reach or pass to win
2. minStep: minimum increment for each turn counting
3. maxStep: maximum increment for each turn counting
<br/>
Then choose Hard level and try whether you can defeat the computer or not
<br/>
**Note**: goalNumber > maxStep > minStep


****
### Tips to win
There are three tips you need to know:

1. You need to know which numbers you must count to win
2. You need to know whether you should go first or not
3. Choose the EASY level first before the HARD one 

****
### Personal opinions
**Take away**

1. Apply OOP knowledge in developing a program
2. Understand more about importing and creating modules
3. Generate an algorithm allowing computer to decide which numbers to count no matter what goalNumber, minStep, or maxStep are
