# robot-pickup-line

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/nmlyz/robot-pickup-line/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/nmlyz/robot-pickup-line/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

A tiny program that writes one robot pickup line to a text file. The line is a
single sentence of at most 200 characters: a document shredder that folds one
document instead of shredding it.

## The line

> I shred 10,000 documents a day, and yours is the only one I folded instead.

75 characters, one sentence, plain ASCII. The program validates the line
before writing it (single line, 1–200 characters, one trailing period) and
reads the file back after writing to confirm the bytes match.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Running it twice produces byte-identical output.
