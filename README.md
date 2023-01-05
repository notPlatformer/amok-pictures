# Amok Runner optimized pictures puzzle
the strat times (ex. 14.05s) mean the amount of time for all of the moves to be completed. i got this time from adding up all of the moves from the [frames](https://github.com/notPlatformer/amok-pictures/blob/main/times.json) it takes to move a picture from one position to another. the frames are in 60fps

### 14.05s strat
**most optimized**

i found these inputs to be the most optimized (after about 10 billion loops on my algorithm!!)
- S SPACE D SPACE
- SPACE S SPACE
- W D SPACE S A SPACE
- SPACE A W W SPACE
- D SPACE S SPACE
- SPACE A S SPACE
- D W SPACE D SPACE

here are the moves that each of them uses (see [picture numbers](https://github.com/notPlatformer/amok-pictures/blob/main/picture_numbers.png) for what the numbers mean)
- 3-4
- 4-9
- 6-8
- 8-1
- 2-4
- 4-7
- 4-5

# files

### [times.json](https://github.com/notPlatformer/amok-pictures/blob/main/times.json)
the frames are at **_60 fps_**

this file contains the amount of frames a picture from position A takes to move to position B.
as the time a picture takes to move from position 1 to position 8 is the same as 8 to 1, only 1 to 8 is shown in the file.

### [moves.json](https://github.com/notPlatformer/amok-pictures/blob/main/moves.json)
this file contains the best (in my opinion lol) moves from position A to B. there may or may not be some bias here, but that is irrelevant.

### [picture_numbers.png](https://github.com/notPlatformer/amok-pictures/blob/main/picture_numbers.png)
this screenshot shows how i numbered the pictures, for anyone curious.



# code
i polished this a bit so they're more understandable.

### [find_fastest_moves_rand.py](https://github.com/notPlatformer/amok-pictures/blob/main/find_fastest_moves_rand.py)
the program i used to find the 14.05s strat

basically the program generates a random combination of moves (7 moves, as that is the least that can be used to solve the puzzle. yes, i brute forced ALL combinations of 6 moves, totaling `1,402,410,240` combinations. none of them worked!)

with this combination of moves, it then checks if it solves the puzzle after executing all possible moves.

if the puzzle is solved with those moves, it saves the amount of frames it took to solve it. the amount of frames is every single move's amount of frames it takes to complete that entire move added up. this is from [frames to move a picture from one position to another](https://github.com/notPlatformer/amok-pictures/blob/main/times.json).



# something technical i guess
i made another program to solve the fastest possible order of moves of a single combination of moves. this includes the time it takes to move your selection from picture A to picture B. i will not explain how this works, as it is complex. i may explain it a little bit later on!! maybe. **just maybe.** no promises.

sorry this is a bit hard to understand and i cannot think of a better way to word it so yeah. enjoy your day!
