# Amok Runner optimized pictures puzzle

## OPTIMIZED INPUTS

i found these inputs to be the most optimized (after about 10 billion loops on my algorithm!!)
- S SPACE D SPACE
- SPACE S SPACE
- W D SPACE S A SPACE
- SPACE A W W SPACE
- D SPACE S SPACE
- SPACE A S SPACE
- D W SPACE D SPACE

here are the moves that each of them uses (see [picture numbers](https://github.com/notPlatformer/amok-pictures/blob/main/picture_numbering.jpg) for what the numbers mean)
- 3-4
- 4-9
- 6-8
- 8-1
- 2-4
- 4-7
- 4-5

### [times.json](https://github.com/notPlatformer/amok-pictures/blob/main/times.json)

this file contains the amount of frames a picture from position A takes to move to position B.

as the time a picture takes to move from position 1 to position 8 is the same as 8 to 1, only 1 to 8 is shown in the file.

### [moves.json](https://github.com/notPlatformer/amok-pictures/blob/main/moves.json)

this file contains the best (in my opinion lol) moves from position A to B. there may or may not be some bias here, but that is irrelevant.

### [picture_numbering.jpg](https://github.com/notPlatformer/amok-pictures/blob/main/picture_numbering.jpg)

this screenshot shows how i numbered the pictures, for anyone curious.
