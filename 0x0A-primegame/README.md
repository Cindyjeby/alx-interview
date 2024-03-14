<h1>Prime Game</h1>
<p>For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.</p>

<h3>Concepts Needed:</h3>
<h5>1. Prime Numbers:</h5>
<li>Understanding what prime numbers are.</li>
<li>Efficient algorithms for identifying prime numbers within a range</li>

<h5>2. Sieve of Eratosthenes:</h5>
<li>An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.</li>

<h5>3. Game Theory:</h5>
<li>Basic principles of competitive games where players take turns and the concept of optimal play.</li>
<li>Understanding win conditions and strategies that lead to a win or loss</li>

<h5>4. Dynamic Programming/Memoization:</h5>
<li>Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.</li>

<h5>5. Python Programming:</h5>
<li>Loops and conditional statements for implementing game logic and algorithms.</li>
<li>Arrays and lists for storing the integers and tracking removed numbers.</li>

<h3>Resources:</h3>
<h5>Prime Numbers and Sieve of Eratosthenes:</h5>
<li><a href="https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers">Khan Academy: Prime Numbers:</a>Introduction to prime numbers.</li>
<li><a href="https://www.geeksforgeeks.org/sieve-of-eratosthenes/">Sieve of Eratosthenes in Python:</a>A step-by-step guide to implementing the sieve algorithm in Python</li>
<h5>Game Theory Basics:</h5>
<li><a href="https://www.investopedia.com/terms/g/gametheory.asp">Game Theory Introduction:</a>A simple explanation of game theory and strategic decision-making.</li>
<h5>Dynamic Programming</h5>
<li><a href="https://skerritt.blog/dynamic-programming/">What Is Dynamic Programming With Python Examples:</a>An introduction to dynamic programming with Python examples.</li>
<h5>Python Official Documentation:</h5>
<li><a href="https://docs.python.org/3/tutorial/introduction.html#lists">Python Lists: </a>Managing lists in Python, useful for tracking the game state.</li>

<p>By grasping these concepts and making use of the recommended resources, you will be well-equipped to approach the problem with a solid understanding of both the mathematical and programming challenges involved. The key to success in this project lies in applying efficient algorithms to manage the game’s state and making optimal decisions based on the game’s rules.</p>
<h3>Additional Resources</h3>
<li><a href="https://www.youtube.com/watch?feature=shared&v=Jw2pniZCLi8">Mock Technical Interview</a></li>

<h2>Task</h2>
<p>Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.</p>
<p>They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.
<li>Prototype: def isWinner(x, nums)</li>
<li>where x is the number of rounds and nums is an array of n</li>
<li>Return: name of the player that won the most rounds</li>
<li>If the winner cannot be determined, return None</li>
<li>You can assume n and x will not be larger than 10000</li>
<li>You cannot import any packages in this task</li>
</p>
<p>Example:
<li>x = 3, nums = [4, 5, 1]</li>
</p>
<p>First round: 4
<li>Maria picks 2 and removes 2, 4, leaving 1, 3</li>
<li>Ben picks 3 and removes 3, leaving 1</li>
<li>Ben wins because there are no prime numbers left for Maria to choose</li>
</p>
<p>Second round: 5
<li>Maria picks 2 and removes 2, 4, leaving 1, 3, 5</li>
<li>Ben picks 3 and removes 3, leaving 1, 5</li>
<li>Maria picks 5 and removes 5, leaving 1</li>
<li>Maria wins because there are no prime numbers left for Ben to choose</li>
</p>
<p>Third round: 1
<li>Ben wins because there are no prime numbers for Maria to choose</li>
</p>
