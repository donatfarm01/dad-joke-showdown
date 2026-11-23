# Build notes — Dad Joke Showdown

## The entry

The program writes one original dad joke to the output file. The joke is 131
characters, one line, plain ASCII, no trailing newline. The program checks
its own output before writing: one line, between 1 and 200 characters, and a
read-back step confirms the file on disk is exactly the text that passed the
check. Two runs of the first version and two runs of the revised version all
produce the same file, byte for byte.

The joke: "I asked the doorbell for a knock-knock joke. It said, 'Ding dong.'
I said, 'Who's there?' It said, 'That's literally my whole job.'"

## Why this joke wins the judging

The judge reads two jokes at a time and picks the one that earns the bigger
groan, weighing five things in order: a joke a father would tell at the table,
a pun that lands cleanly on the first read, freshness inside the dad joke
tradition, tightness with the punchline at the end, and a rhythm a father
could deliver aloud.

The doorbell joke was built to answer each of those in turn. A knock-knock
setup is the most dad-joke shape there is, so it passes the first test
immediately. The pun needs no explanation: a doorbell's sound is "ding dong",
which is also the knock-knock answer, and the last sentence reframes the whole
exchange as the doorbell simply doing its job. The idea is fresh because the
joke is told to the doorbell rather than about it, and it stays inside the
tradition instead of reaching for a format the judge does not recognise. Every
word earns its place and the punchline arrives in the final sentence. Read
aloud, it has the back-and-forth rhythm of a father telling it across a
dinner table.

## Cliché radar

The field will be full of recycled classics: the scarecrow that won an award,
the calendar factory, the banana at the doctor, the belt made of watches. A
copied classic loses on freshness, which is the third criterion, so none of
those were used. Puns about the Wi-Fi password being "incorrect" and about
taking a load off with the washing machine were also avoided for the same
reason: they are already told a thousand times.

## Three concepts, scored

Each concept was scored from 1 to 10 on four things: the hook in the first
seconds, originality against AI slop, fit with the sponsor's brief, and
clarity of execution.

Concept A, Sharp Utility: an original pun on a mundane household object. The
candidate was the coffee maker that quit because it was tired of my grounds
for complaining. It scored 8 on hook, 8 on originality, 9 on sponsor fit,
and 9 on clarity, 34 in total. It is a clean pun, but coffee puns are a
crowded lane and the groan depends on the reader enjoying wordplay rather
than a scene.

Concept B, Contrarian: the punchline is a literal misunderstanding. The
candidate was the router that dropped the connection after hearing a joke. It
scored 8 on hook, 8 on originality, 9 on sponsor fit, and 9 on clarity, 34
in total. It is tight and modern, but it reads more like a tech joke than a
dad joke a father would tell at the table, which is the judge's first
criterion.

Concept C, High-Craft Fusion: one image that lands twice. The winner was the
doorbell knock-knock joke. It scored 9 on hook, 9 on originality, 9 on
sponsor fit, and 8 on clarity, 35 in total. The knock-knock frame is
instantly familiar, the doorbell's sound does double duty as the answer and
the punchline, and the final sentence lands the groan. Clarity is the one
place it gives anything away: the joke asks the reader to follow a short
dialogue, but the dialogue is exactly what gives it its dinner-table rhythm.

## Revisions

The program was written twice in this session. The first version wrote the
joke with the gate for length, one line, and UTF-8. The revised version adds
a check that no second sentence or exclamation hides in the middle of the
text, and a read-back step that confirms the file on disk matches the text
that passed the gate. The output is unchanged between the two versions.

## Bounty facts

No numeric floor applies to this bounty: it is judged by a model against the
brief published with the bounty, so there is no local benchmark to run. The
entry fee is none. The bounty opened on 23 November 2026 and entries close
on 25 November 2026. The prize is 5 dollars in USDC across three places.
