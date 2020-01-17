# Sudoku
Generate solvable sudoku with varying levels and Backtracking, Forward search solution.

## solve.py

Solves a given goard.  
  *solve*: Solves a given board using backtracking. Future - Forward search and constraint propagaatio to be implemented.  
  *is_valid*: Returns a bool if the given move (number in an empty slot) is valid

## generate.py  
Generate  
  *generate*: Generates a sudoku puzzle on given difficulty level and also returns the expected answer.  
      ### Difficulty Levels: 'easy', 'medium', 'hard' and 'v_hard' with 'easy' puzzle having most clues.
      The expected answer given by 'generate' function is expected to be different from an answer produced from the backtracking      solution, with the most differences in 'v_hard' and atmost two exchanges in 'easy'.  
