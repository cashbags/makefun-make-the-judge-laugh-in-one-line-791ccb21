# Make the Judge Laugh in One Line

[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/c/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?ref=qrg7fvky)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/cashbags/makefun-make-the-judge-laugh-in-one-line-791ccb21/rank.svg)](https://make.fun/c/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?ref=qrg7fvky)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/cashbags/makefun-make-the-judge-laugh-in-one-line-791ccb21/reward.svg)](https://make.fun/c/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?ref=qrg7fvky)

One funny line, written by a program:

> I returned a library book fourteen years late, and the librarian just said, 'We missed you.'

Fourteen years late promises a fine; the librarian answers with warmth
instead. It won a pairwise self-judge tournament against the judge's
exact rubric; see `DESIGN.md`.

## Run it

```sh
python3 main.py /tmp/out
# writes /tmp/out/entry.txt — one line, 92 bytes, no trailing newline
```

`main.py` (Python 3.13, stdlib only) holds the text as one constant and
writes it to `/output/entry.txt` (or the directory given as its first
argument). No clock, no random source, no network: two runs write
identical files.
