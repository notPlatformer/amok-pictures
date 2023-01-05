# python because i am not good at c++ !!!!

import random
import time

# taken from one of my modules
def format_time(seconds: float, use_millis: bool = False, padded_millis: bool = True) -> str:
    """
    Formats seconds into days, hours, minutes, seconds, (milliseconds)
    """
    if (use_millis and seconds <= 0) or (not use_millis and int(seconds) <= 0):
        return "0s"

    time_days = int(seconds / 86400)
    seconds -= time_days * 86400

    time_hours = int(seconds / 3600)
    seconds -= time_hours * 3600

    time_minutes = int(seconds / 60)
    seconds -= time_minutes * 60

    time_seconds = int(seconds)
    seconds -= time_seconds

    time_millis = int(seconds * 1000)

    date = f"{time_days}d " if time_days > 0 else ""
    date += f"{time_hours}h " if time_hours > 0 else ""
    date += f"{time_minutes}m " if time_minutes > 0 else ""
    date += f"{time_seconds}s " if time_seconds > 0 else ""
    date += f"{time_millis:0>{3 if padded_millis else 0}}ms " if use_millis and time_millis > 0 else ""

    if date.endswith(" "):
        date = date[:-1]
    return date

# frames it takes to move a picture from A to B
movetimes = {
    "12": 67,
    "13": 65,
    "14": 143,
    "15": 210,
    "16": 251,
    "17": 121,
    "18": 138,
    "19": 220,
    "23": 96,
    "24": 92,
    "25": 153,
    "26": 192,
    "27": 134,
    "28": 122,
    "29": 171,
    "34": 139,
    "35": 183,
    "36": 252,
    "37": 65,
    "38": 100,
    "39": 204,
    "45": 78,
    "46": 121,
    "47": 122,
    "48": 88,
    "49": 86,
    "56": 48,
    "57": 207,
    "58": 149,
    "59": 65,
    "67": 246,
    "68": 188,
    "69": 85,
    "78": 69,
    "79": 183,
    "89": 121,
}

# just a list of all the keys
movetimeskeys = list(movetimes)

def get_move_time(move):
    # returns the frames to move from A to B, but also sorts it
    # for example since "81" doesn't exist in the dict, returns "18" which is correct
    return movetimes["".join(sorted(str(move)))]

# positions the pictures are in at the beginning
positions = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# positions the pictures must be in to be solved
end_positions = [ 6, 9, 4, 5, 7, 8, 2, 1, 3 ]

def swap(l, i):
    # weirdness
    # swaps two variables of a list in place (no return)
    # how "i" works is basically say you have a list of l=[1,2,3] and you do swap(l, "23"), l becomes [1,3,2]
    # the reason i made it this way is because the moves i generate below are strings of two numbers
    # maybe it would've been faster to just use integers... welp, too late for that
    sa, sb = list(i)
    sa = int(sa) - 1
    sb = int(sb) - 1
    a, b = l[sa], l[sb]
    l[sa] = b
    l[sb] = a

def random_moves(count):
    return random.choices(movetimeskeys, k=count)

bestmoves = [
    # old wr strat, for comparison purposes
    (956, ["16", "68", "34", "49", "42", "74", "45"], 0),
]

# use a different file so i can run multiple instances of these at once
logfile = f"find_fastest_moves_{time.time()}.log"
def update_file():
    # basically saves the entire list of possible combinations (found so far) to a file so you can easily see what's good and what's bad
    with open(logfile, "w") as file:
        # sort entire list from slowest to fastest (so fastest is at the bottom)
        bestmoves.sort(reverse=True)
        for frames, allmoves, i in bestmoves:
            moves = f'''[{", ".join(f'"{move}"' for move in allmoves)}]'''
            speed = f"{round(frames/60,2)}s ({frames} frames)"
            file.write(f"\nMoves: {moves}\nSpeed: {speed}\nCount: {i:,}\n")
update_file()

iterations = 0
skips = 0

starttime = time.time()
while 1:
    pos = positions.copy()
    moves = random_moves(7)

    # executes all moves
    for move in moves:
        swap(pos, move)

    # checks if the combination of moves resulted in a victory royale (haha)
    if pos == end_positions:
        # yeah
        movesstr = f'''[{", ".join(f'"{move}"' for move in moves)}]'''
        speedframes = sum(get_move_time(move) for move in moves)
        speed = f"{round(speedframes/60,2)}s ({speedframes} frames)"

        # print out stuff, because why not
        print("")
        print(f"Moves: {movesstr}")
        print(f"Speed: {speed}")
        print(f"Count: {iterations:,}")
        print("")

        # store all of it in a list
        data = (speedframes, moves, iterations)
        if not data in bestmoves:
            bestmoves.append(data)

        # save it to file
        update_file()
    else:
        # skips is the amount of loops that were skipped duh
        # basically just a cool thing to see! means that that combination failed
        skips += 1
    iterations += 1

    # don't even ask, i didn't think i was gonna show this to anyone
    if (iterations-1) % 1_000_000 == 0:
        milpermin = (iterations-1) / 1_000_000 / max(0.01, (time.time() - starttime) / 60)
        print(f"Millions looped: {int((iterations-1)/1_000_000):,} ({round(milpermin, 3)} mil per min), skips: {skips-1:,}")
