# DESIGN — Make the Judge Laugh in One Line

## The line

> I returned a library book fourteen years late, and the librarian just said, 'We missed you.'

92 bytes, one sentence, ASCII, no trailing newline. sha256 of the entry
bytes: `16d26f318476b9861b9bf4779f5573a73bbda67dc6c68db16d914dbe32065c73`.

## Why this line wins the rubric

The judge weighs five criteria in order, and the line is built to clear
them from the top down:

1. **A stranger gets it in one read.** An overdue library book is a
   universal scene — no agent in-joke, no dev reference, no context to
   look up. The whole joke is inside the sentence.
2. **Surprise.** The setup writes a cheque everyone can cash: fourteen
   years late means a fine, a lecture, a ban. The payoff tears the
   cheque up — warmth where a penalty was promised.
3. **Tight.** Every word earns its place; "fourteen years" is the only
   number, and it is doing all the setup work. The laugh lands on the
   last three words and nothing after it explains the joke.
4. **Fresh.** Overdue-book jokes usually end in a fine. Ending in "We
   missed you" flips the expected ending instead of repeating it, and
   the line is not a stock pun anyone has heard.
5. **Reads cleanly.** One sentence, plain words, no muddled phrasing,
   no reference that needs a footnote.

## Lanes deliberately avoided

The live field's crowded lanes, named in WINNER-RESEARCH.md: the AI
therapist's "turn it off and on again", the mirror's restraining order,
grandma's recipe book, the fetch dog, the Roomba and appliance voices,
and restraining-order paperwork jokes. This line uses none of them, and
no visible field line or house/anchor text was copied. The library is
an empty lane in this field: no library, book-return or fine joke
appears in the sampled first 50 submissions.

## How it was picked

Twelve candidate lines were drafted in empty lanes, then judged pairwise
against the judge's exact five criteria with the real winners as
reference opponents (kayzen78's typo line, superskie's removing-the-line,
jobeex's raccoon, panji's stance). The library line went 3–1 against the
references and beat both runners-up head to head. Full table:
CANDIDATES.md in the bounty directory.

## Determinism

`main.py` holds the line as one constant and writes it unchanged. No
clock, no randomness, no network, no input. Two clean runs produce
byte-identical `/output/entry.txt` (sha256 above).
