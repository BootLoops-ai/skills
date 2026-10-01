---
name: prose-lint
description: use before circulating any scientific text, human- or LLM-drafted — a clarity and integrity linter: hype vocabulary, empty sentence structures, agentless prose, number discipline, and honesty failures; one pass is never enough.
---

# prose-lint

**THE MASTER TEST, before and above every class below: read each sentence and
ask — would a specific human scientist say this, out loud, across a table to a
colleague? Not "is it grammatical," not "does it match a banned pattern" —
would a person SAY it. If you cannot hear a human saying the sentence, it
fails, whether or not any catalogued class matches. The catalogue below exists
to help you find such sentences and to name the cure; it is never the boundary
of the offense. A pass that runs every grep and skips this question is not a
lint.**

This skill improves clarity and honesty. It is not a tool for concealing AI
involvement: disclose AI assistance as your venue requires; Section E applies
to authorship statements too.

Quickly produced drafts, by people or by language models, share habits that careful readers distrust. A reader who has seen a lot of it flinches at the patterns below even when each sentence is individually fine. Run this as a dedicated pass — never assume a draft is clean because it "reads okay." Read every paragraph as if aloud; anything that sounds like a press release, a chatbot, or a social-media post gets rewritten in plain, concrete language.

**Two hard truths:**
1. **One pass is never enough.** These tells regenerate every time the text is rewritten. Scrub, then scrub again with fresh eyes, paying special attention to the opening sentence, every subheading, and every closing sentence — that is where they hide.
2. **The honesty tells (Section E) matter most.** A clunky sentence is cosmetic. A fabricated number, an inflated claim, or a mislabeled source is a lie. Hunt those first.

---

## A. Banned / suspect vocabulary

If one of these appears, it is almost always wrong. Delete or replace with a plain, specific word.

**Hype nouns/verbs:** delve, tapestry, realm, testament, underscore, leverage, unlock, unleash, navigate (figuratively), foster, embark, journey, showcase (as verb), spearhead, harness *the power of*, supercharge.
**Marketing adjectives:** seamless, robust, cutting-edge, game-changing, revolutionary, transformative, groundbreaking, multifaceted, intricate, vibrant, profound, rich (figuratively), powerful (as filler), unprecedented.
**Set phrases:** "harness the power of", "the world of", "dive into" / "deep dive", "at the forefront", "pushing the boundaries", "a paradigm shift", "the beauty of", "stands as", "serves as a testament", "a beacon of", "plays a vital/crucial/pivotal role", "boasts", "a treasure trove", "in today's world", "ever-evolving", "rapidly evolving", "needless to say", "at the end of the day", "simply put", "it goes without saying".
**Weasel openers:** "It's worth noting that", "It's important to note", "It is worth mentioning", "Notably,", "Importantly," (when it adds nothing), "Make no mistake".
**Summary throat-clearing:** "In conclusion", "In summary", "Ultimately,", "All in all", "To sum up".

*Allowed-in-context exceptions:* a word used literally (a software harness, a physical journey) or as a genuine technical term. The ban is on the cliché use, not the real one. **The defined-in-document exception:** a suspect token the document itself formally defines ("we call a value *certified* when …") is earned vocabulary from the definition onward — demote the hit to a note and check that the definition really exists and precedes the uses.

## A2. Metaphor and register classes (each with its cure)

**Commerce metaphors for information/evidence:** "the constants price the question", "a menu of methods", "what this buys", "cost" for anything other than literal compute time or literal sample size. *Cure:* state the actual quantity — "takes about 3 million samples" is fine; "the constants price the question" is not.

**Vague elevation metaphors:** "one floor up", "one level up", "one rung above", "the mathematical ladder", and kin. *Cure:* name the concrete thing — the class, or the actual dimension/order count ("the genus-two case, one step above genus one"). A *named, literal* ladder with real rungs stays allowed.

**Vague locative abstractions:** "the places where that stops are known precisely", "the point at which X breaks down", "on both sides of that boundary", "where the field currently stands" — geography metaphors standing in for specific objects. The tell: a WHERE-word (places, point, boundary, side, landscape, territory) carrying a claim about specific objects. *Cure:* name the objects — "exactly two cases are known to require more". A literal boundary (a physical region, an integration domain) is fine.

**"The field says" over-attribution:** "when the field says", "the field declared it impossible", "the field stopped trying" — generalizing one paper's or one group's statement to an entire discipline. Both a tone tell (gotcha framing toward likely referees) and an honesty tell (an attribution a source check refutes). *Cure:* attribute to the actual source, quoted or named ("Smith et al. call it 'impossible to evaluate directly'"), or scope to the actual subcommunity. If you cannot name who says it, the sentence is not ready.

**Capability-fanfare openers:** "the two theories can finally be compared", "X makes it possible to Y", "this opens the door to" — announcing that an act has become possible instead of performing it. *Cure:* do the thing — "We compare the prediction with the archival data." If the document doesn't do it, it's future work, stated as an open item, not fanfare.

**Paragraph-opening anaphora:** a new paragraph must not open on an unanchored pronoun or deictic — "We now cross it", "This changes the picture", "That is the subject of...", "It follows that..." as paragraph OPENERS force the reader back across the break to find the referent, and read as machine segues. Within a paragraph anaphora is fine. *Cure:* restate the noun. Doubly banned when combined with journey-geography verbs (cross, move to, turn to).

**Dev-subculture vocabulary in science prose:** footgun, moat, "has landed"/"lands" for results, happy path, escape hatch, guardrail (figurative), dogfood(ing), greenfield, bikeshed, yak-shaving — anything from the coding-agent/devops subculture. *The test:* would the author have used this word in a scientific paper before working with coding agents? *Cure:* ordinary English — trap, pitfall, hazard, failure mode, checker, wall, "is complete".

## A3. Agentless prose (the class the pattern lists do not catch)

Sentences that are grammatical, contain no banned vocabulary, and still read as machine/report prose because they dodge human agency or decorate structure.

**A3.1 — Abstract-agent constructions.** An inanimate abstraction performs a human verb: "The literature attaches a definite expectation to this coefficient"; "the record shows", "the analysis produced", "the section supplies", "the data argues". *Cure:* give the sentence a real subject — the people, or the plain fact: "There was every reason to expect a closed form"; "Smith and Jones showed"; "We find". **The person-subject test:** could you replace the abstract subject with a person's name and keep the verb? If not, the verb is borrowed and the sentence is fake.

**A3.1b — Pipeline vocabulary in scientific prose.** Software/devops register describing mathematics or science marks the text as machine-written. Banned on sight, each with its cure:

| banned | cure |
|---|---|
| downstream / upstream | "later results", "no later result depends on it", "the input to" |
| pipeline (for a derivation) | "the calculation", "the chain of arguments", "the method" |
| workflow | "procedure", "method" |
| hand off / handoff | "pass to", "becomes the input of" |
| flag (verb, no literal flag) | "note", "point out", "record" |
| surface (verb) | "reveal", "bring out", "expose" |
| ship / shipped (for results) | "publish", "include", "accompany the paper" |
| deploy | "apply", "use" |
| end-to-end | "complete", "from the definition onward" |
| artifact (for a result/file) | "record", "table", "computed data" |
| gate / gating (no named gate) | "check", "test", "criterion" |
| sanity check | "consistency check" |
| edge case | "degenerate case", "boundary case" |
| toolchain / tooling / stack | name the actual tools |
| bandwidth / throughput (figurative) | say the actual resource |
| iterate on (a draft/idea) | "revise", "refine" (mathematical iteration is fine) |
| blocker / pain point | "obstruction", "the difficulty" |
| load-bearing (figurative) | "essential", "the argument depends on it" |
| lane | "line of work", or name the actual activity |
| closed (completion status) | "complete", "entirely" |
| byte-identical / byte-for-byte (for exact values) | "exactly equal", "identical" — unless a literal byte comparison of files is the check, stated once |
| fail-closed / production use | "validated on cases with known answers before being applied to the real data" |
| status enums pasted verbatim (GO/NO-GO, not-gradeable-with-reason) | plain-English gloss at the definitional site, then use the defined term |

Example fixes: "nothing downstream rests on the fit" → "The fit plays no further role." "the derivation artifacts ship in the release bundle" → "the derivation records are included with the paper."
Exemption: a paper ABOUT software may use these words for the software itself (a real pipeline, a real workflow) — never for the mathematics.

**A3.2 — Contorted agentless idioms.** Constructions that twist to avoid saying who did what: "The program is named by its own titles", "admits a reading as", "attaches to", "is captured by the observation that". *Cure:* subject–verb–object with real actors.

**A3.3 — Decorated structural labels.** Run-in labels, paragraph headers, or list leads with relative clauses or editorial riders: "The geometry that explains it.", "The method, stated honestly", any "The X that Y" label; also the "Noun, participle" status rider ("The mechanism, proved"). *Cure:* labels are plain noun phrases, four words or fewer — "The theorem." — and the explanatory work moves into the paragraph's first sentence.

**A3.4 — The colleague test (mandatory, separate pass).** After the pattern hunt, run a SEPARATE pass reading as a senior person in the target field and venue: for each sentence, would that person write it? Hesitation = rewrite as subject-verb-object with a human or concrete subject. This is a different failure axis from the tell lists; pattern-matching the lists does not perform this test, and a pass that skips it WILL publish agentless prose.

---

## B. Banned sentence structures (the high-value targets)

**B1 — Negate-then-pivot ("not X, but Y" / "X, not Y" / "not X; it Y").** The single most common tell. Includes "It's not just X, it's Y", "is a feature, not a flaw", "It does not compute... it constrains". *Fix:* state the positive directly and drop the negated half. Keep at most one such construction in a whole piece, and only if the contrast is load-bearing.

**B2 — Cleft and pseudo-cleft ("It is X that…", "What … is …", "X is what …", "is exactly what/where …").** *Fix:* convert to a plain active sentence: "What carries over is the method" → "The method carries over." Three cleft sub-types that hide and must be hunted specifically:
- **Existential-there cleft:** "There is/are X … (that/who/and it is) …" — wordy throat-clearing that buries the subject. "There are many physicists who believe…" → "Many physicists believe…". Start with the real subject.
- **"it is the one/the thing/the reason …" tail**, often *mid-sentence after "and"* (clefts are not only sentence-openers — scan inside sentences too): "…, and that is what makes it work" → fold into a direct clause.
- **"what \<verb\>s … is …" with a non-"the" completion** — greps for "what … is the" miss clefts whose complement is a pronoun or possessive: "what survives of the fit is its output". Hunt ANY "what survives/remains/emerges/follows/carries/changes/works/matters … is …". Also its cousin, the **trailing-apposition flourish** — a comma tail describing the *document's* relationship to the object ("…, now the subject of a theorem") rather than the object itself. Fix both by stating the fact.
- **Specificational abstract-noun copula:** "The difference/reason/point/upshot is whether/that/how …" — a cleft with the wh-word moved into an abstract noun subject. The abstract noun adds nothing; the wh-clause is the content — let it modify the actual statement. Variants that evade greps: an interposed modifier ("The question for this note is whether…"), and the verbless colon form ("The answer to whether X: Y").

**B3 — "X changes one thing, and the one thing matters."** Fake profundity: assert something does one important thing, then declare that thing important. *Fix:* cut the self-referential second clause; just say what it does.

**B4 — Filler-emphasis flags** ("worth noting/savoring", "the key is", "what matters is") and enumerative meta-prose — a sentence whose only content is a count or a structure announcement ("Our result is then two things.", "Two points are worth making."). *Fix:* delete the flag and lead with the content; fold the count into the first content sentence.

**B4b — Participle-hedge stacks.** Two or more coordinated past participles, each carrying its own epistemic rider, in one clause: "proved modulo one lemma and validated on independent routes". Grammatical, technical, and machine to the ear — a person states one epistemic claim per clause. No pattern fires on it; hunt it by reading status sentences aloud.

**B4c — Announced significance.** Telling the reader a result is deep instead of showing it: "…and its anatomy is the deeper finding", "it is worth naming", "X is the real finding". *Fix:* delete the announcement — the demonstration follows anyway.

**B5 — "From X to Y," openers** ("From quarks to galaxies, …"). *Fix:* rewrite without the frame.

**B6 — Rhetorical-question-then-answer as a paragraph engine.** One per piece, maximum; zero in a research paper. Hook-question openers and hook-question titles are banned outright.

**B7 — "Imagine …" openers and "Enter [X]" reveals.** *Fix:* introduce the thing by name and what it does.

**B8 — Abstraction-labeling and structure narration.** "This is X in its purest form", "That number organizes the rest of the paper", "this section is the ledger". *Cure:* state what the object MEANS, not what it does to the document. Sibling: layout self-justification ("Itemized, because a grid is easy to scroll past") — the reader never needs the design defended.

**B9 — Aphorism-fragment codas.** Verbless slogan fragments as paragraph enders: "One channel, two symptoms." / "Two results, one mechanism." The content is always already in the sentence before. *Cure:* delete; if the identity needs stating, state it as a plain sentence with a verb. Siblings: the paired-gerund identity epigram ("doing X and doing Y are the same event"), vague-antecedent proof claims ("the paper proves it" — you prove statements, not causes; name the statements), compressed apposition ("at a rate the paper bounds" — give the fact its own clause), and paradox inversion ("manufactures X out of its own Y" — state the plain causal fact).

**B10 — Unhedged "the first X" flourish.** A first-claim is a factual claim: either pin it to a source and hedge ("to our knowledge, the first…") or cut it — usually the sentence works without it. One hedged first per document, maximum.

**B11 — Apposition-gloss instead of plain nouns.** A technical noun phrase glossed by a clever compressed apposition that names nothing: "the failures sit in the inference layer, the part the domain argues with". *Test:* from the sentence alone, can the reader list the concrete objects? If not, the gloss is decoration. These pass a read-aloud check — hunt them as a separate pass: for every apposition, ask what nouns it is hiding.

**B12 — Fancy phrasing instead of saying it.** "That asymmetry is where the story starts", "becomes a question with an answer", "the least of what this opens". Each performs instead of stating. *Cure:* write the sentence you would say to a colleague across a desk. If a metaphor spans more than one sentence it has become a frame — kill the frame, keep the facts.

**B13 — Stakes by pointer / reference without referent.** Reporting that a conclusion changed without saying what it was about: "reversing that part of the paper's story", "two of the source's headline claims lose support". The reader has not memorized the source. *Cure:* science forward — open with the real-world question in plain words, and give every moved number its real-world meaning in the same sentence.

**B14 — The two-beat echo.** A sentence repeating its verb or frame for cadence: "X fails, and it fails differently." / "It works, and it works everywhere." The second beat exists for rhythm, not information; treat verb-echo across a comma/conjunction as guilty by default. *Cure:* state the two facts plainly with their content. MECHANICAL SWEEP: flag every sentence where the same verb lemma appears twice joined by ", and" / "; " / "— and".

**B15 — The repeated flourish (document-scale; a per-sentence read cannot see it).** The same epigram, verdict sentence, caveat couplet, or caption formula deployed twice or more across a document: a conclusion re-asserted in near-identical words after each block of evidence; a hedge stamped verbatim in the preamble, three captions, and the close ("preliminary, a proof of principle" in the preamble, three captions, and the close); a priority claim ("the first X") told in the introduction, a caption, and three sections; consecutive captions on one superlative template ("The A, the best-described of the three…" / "The B, the most structured of the three…"); an abstract sentence recycled near-verbatim into the introduction. One instance is voice; repetition is assembly. *Cure:* give the statement its full form ONCE at the site that owns it, keep any per-figure stamp policy, and reduce the rest to a plain reference or delete. *Keep-boundary:* a scope qualifier deliberately attached to every conditional number is discipline, not a tic — before bulk-trimming an apparent chorus, check whether each instance carries its own fact; if it does, it stays. Siblings: the counted-opener template run ("Two gaps remain." / "Two conclusions follow." / "Two checks are independent…" chapter after chapter — keep at most one, fold the rest into ordinary prose) and the dramatic-opener chain (a narrative section whose paragraphs all open on a punchy sub-8-word beat: "First contact went badly." / "The reckoning came." — keep at most two).

**B16 — Credential display (validation vocabulary worn as a badge).** Method-integrity vocabulary used as a self-conferred credential rather than a defined term: certified, verified, validated, pre-registered, pre-committed, frozen protocol, blind, held-out, fail-closed, audit-grade — sprinkled through results without the document ever saying what operation confers the label. Readers experience this as protesting too much, and it buries the actual guarantee. *Cure:* define the term once, concretely, at first heavy use ("a value is *certified* to n digits when two independent evaluations agree to n digits"), after which the register is earned — or replace each use with the concrete fact ("agrees with an independent evaluation to 30 digits"). Procedural credentials ("under a frozen, preregistered protocol") are methods material, never selling points. Same family: integrity oaths stapled to facts that carry themselves — "the miss is declared, not waived", "the limitation is recorded", "disclosed at full prominence", "we note, against any suspicion of selection, that…", "right rather than convenient", "stated, not patched". The disclosure IS the preceding sentence; delete the oath. And self-congratulating checks ("the controls did their job") — state each check's outcome instead.

**B17 — Register saturation (one evocative word colonizing the document).** A single borrowed register noun or verb doing service everywhere: verdict (courtroom), referee, interrogate, campaign, battle-tested (martial), price/pays/buys (commerce), climbs (journey). One or two uses may be voice; ten is a costume. *Sweep:* count occurrences of each evocative register word; past ~4–5, translate all but the one or two load-bearing uses to the plain word (answer, result, check, cost, grows). Related: personified apparatus with communicative or judicial verbs — "the control run caught one genuine event", "the instrument proves itself", "the criterion decides", "the rule fired" — instruments and criteria are used and applied by people; recast with the mechanism ("a repeat under the control configuration revealed…") or a we-subject. Mathematical objects with natural dynamics survive (maxima split, chains converge).

---

## C. Rhythm and paragraph shape

- **C1 — Rule-of-three cadence.** The default LLM rhythm is the manufactured triple ("faster, cheaper, and more reliable"). A genuine enumeration of three real things is fine; if two of the three are padding, cut.
- **C2 — Restatement codas.** A paragraph's last sentence re-saying the paragraph in punchier words. Delete, or end on something that adds or turns forward.
- **C3 — Sentence-opening sameness.** Every sentence starting "The …" or "It …". Vary openings and lengths. Also: no epigram stacking (two flourishes back to back).
- **C4 — Em-dash stuffing.** Ration hard: at most one em-dash in an entire document. Convert asides to parentheses or commas, connective dashes to colons or new sentences.
- **C5 — Fronted-inversion openers.** Locative inversion as a dramatic pivot — "Behind the hardness sits a structural question", "One level above X sits Y" — especially as a section-opener template reused across sections. Un-invert all but at most one: "The hardness raises a structural question". Kin: the quiz-show colon ("The answer: X." — a verbless drumroll; write "The answer is that X") and colon-ended announcers ("Zero cases failed:" — the sub-8-word announcer scan covers ':' endings, not just '.').
- **C6 — Superlative self-ranking.** The document grading its own contents: "the sharpest structural question", "the strongest control", "the sharpest single fact in the data set is…" — a ranking epithet plus a specificational copula introducing evidence that speaks for itself. State the fact directly; if a ranking template repeats ("the sharpest X" twice), vary or drop one.

## D. Formatting tells

Random mid-paragraph bold; stacked hype adjectives; title clichés ("Unlocking…", "A Deep Dive into…", colon-gerund subtitles, hook-question titles); emoji; bulleted lists where prose belongs.

---

## E. Honesty tells (most important — integrity, not style)

- **E1 — Fabricated specificity.** Inventing numbers, counts, or dates and presenting them as data. Use only quantities with a real source; if something is an estimate, say so or cut it. Prefer a smaller verified claim to a bigger guessed one.
- **E2 — Importance inflation.** Claiming something is needed or matters more than it does. Claim only what is true — "at the frontier of what is computable", not "what the field needs".
- **E3 — Provenance errors.** Mislabeling who built, wrote, or discovered something. Verify against the actual repo/paper, not memory.
- **E4 — Result over-claim.** Rounding a partial or unverified result up to "done". Report the true status; never imply a check passed that didn't.
- **E5 — Confident fuzziness.** Stating a contested or approximate fact (a "first", a record, a date) flatly. Pin it against a source, or hedge precisely, never vaguely.
- **E6 — Enclosure and quotation integrity.** (a) Certified intervals round OUTWARD, always: lower endpoints down, upper endpoints up; a certified lower bound may only be rounded DOWN. (b) Quotation marks require a verbatim receipt — a fair paraphrase in quotes is a provenance error. (c) Error-bound and residual summaries may only round in the CONSERVATIVE direction (a 1.06×10⁻⁷ agreement is NOT "10⁻⁷"); trace every order-of-magnitude summary to its source value and check the rounding direction.

## N. Number discipline and cross-surface consistency

Every number appears on several surfaces — body text, table, caption, figure label, abstract — and each pair of surfaces is a place for a silent contradiction. These classes are mechanical; sweep them, don't trust the eye.

- **N1 — Rounding direction on measured counts.** Never round a measured digit/precision count UP: a measured 23.85 verified digits prints as 23, not 24. Achievement numbers round toward the weaker claim, always.
- **N2 — Subtraction-consistent display.** Numbers a reader will subtract must round consistently: 41.2 and 3.9 support "a 37-digit gap"; flooring each independently (41, 3) makes the printed arithmetic false. Same law for decomposition sums: rounded columns must recompose to the rounded total, or the display precision changes.
- **N3 — Every N/N and N-of-M carries its unit.** "812/812 exact" — entries, columns, rows, or members? A count whose noun comes from a different surface than its number is wrong until checked against the source's own definition. Sibling: a compressed count whose gloss names the wrong object ("k=6 collections" when the 6 are histogram cells).
- **N4 — The display-tie.** A value landing exactly on a rounding tie (141/400 = 0.3525) prints differently under float formatting (35.2 — float64 stores it just below the tie) and half-up display (35.3), so a generated label and the text silently disagree on the same number. Compute display labels from integer counts with exact half-up decimal arithmetic, never from the float.
- **N5 — Second-generation rounding.** A ratio or difference of already-rounded values (0.172/0.126 → 1.37) differs from the unrounded computation (1.362). Quote the source record's number verbatim; never "correct" a citable record by re-deriving from displayed values. Likewise a z-score or ratio that "fails" recomputation from displayed inputs may be exact from unrounded ones — say which convention computes it.
- **N6 — A decomposition that doesn't sum names its boundary.** When printed parts miss their printed total, the usual cause is two different boundaries in one analysis (a selection window cut by date, labels assigned by a different scheme), not a stale number. Find the boundary mismatch and state it; don't nudge a number to force the sum.
- **N7 — Non-nested denominators.** Two filters can differ by a NET count (4,201 kept vs 4,178 kept, overlap 3,900): "23 fewer" is true, "23 removed" is false. Check nesting before writing any subset clause.
- **N8 — Counterintuitive-direction numbers get a mechanism clause.** A correct number that moves the "wrong" way (power falling as the sample doubles) reads as a typo. Verify it, then attach the half-sentence mechanism at every site where it prints.
- **N9 — Two true numbers, one false parenthesis.** Two statistics sharing a parenthesis ("p=0.005; fifteen standard deviations above the mean") invite the reader to compose them into a claim neither supports. Each names its own provenance, or they separate.
- **N10 — Modals are part of the number.** "the estimate can be 1.08 times the bound" compressed to "is 1.08 times the bound" turns a possibility into a determination. When compressing or restating a claim, check the modal (can-be / is / must-be) as carefully as the numeral.
- **N11 — One symbol, one object.** Run a symbol census on collision-prone letters: the same letter as a coefficient in one section and a curve, a matrix, or a radius in another actively misleads a reader tracking it — worst when both senses appear in one argument. Rename the cheaper instance and sweep. Same class in words: one term used in a technical and an ordinary sense in the same passage — gloss or rename at first use.
- **N12 — Claim-bearing connective prose.** Relative clauses silently attribute checkable facts ("the trend that their best-fit model carries") — consistency passes must cover the connective prose around numbers, not just the numerals.
- **N13 — Identifier integrity, both directions.** A correct-looking identifier can be wrong and a wrong-looking one correct: registries migrate prefixes, so a DOI with an unfamiliar prefix may be the real one while the "canonical" form no longer resolves. Never normalize an identifier to the familiar form without resolving BOTH candidates; when the odd one wins, leave a dated do-not-fix note so a later pass doesn't undo it. Bare integers where a citation belongs may be a citation-command misfire (a numeric-style \citealp emits "(cf. 9)") — check the bibliography rendering before suspecting a hand-typed number.

---

## F. The parse and composition pass — run BEFORE the tell hunt

The tell catalogue cannot catch what it does not contain. Before any pattern hunt, read for MEANING, sentence by sentence:

1. **Grammar.** Subject and finite verb present? Topic-position fragments ("First, a change to the picture of X.") are ungrammatical, not style.
2. **Antecedent resolution (hard rule).** Every pronoun and deictic — it, this, that, "the effect", "the answer" — must resolve to ONE unambiguous referent within the previous two sentences. Section-opening deictics must survive the page turn.
3. **False agency.** No object doing what it cannot do: "the dataset returns an answer" (the fit run on it produces the answer), "the data want". MECHANICAL SWEEP: grep every inanimate-subject + agentive-verb pair — subjects like record, catalog, dataset, table, curve, model, paper, section crossed with verbs like returns, answers, tells, knows, decides, hides, insists, remembers, wants, admits. Every hit is guilty until the sentence proves the verb literal.
4. **Internal consistency.** Any sentence that APPEARS to contradict another claim anywhere in the document fails, even when both are true — put the reconciliation on the page at the first occurrence.
5. **The document-about-itself ban.** Section and paragraph openers make a claim about the WORLD, never about the document: "This section presents…", "We now turn to…", "Having established X, we…" are document furniture. The one licensed home for signposting is the introduction's roadmap paragraph.
6. **No one-sentence paragraphs.** A paragraph is a developed thought: state, support, connect. Runs of thin 2–3 sentence paragraphs fail the same way; merge thin neighbors.
7. **The skimming-reader test.** Extract every paragraph's FIRST SENTENCE and read each in isolation. Each must name its subject with full nouns and stand alone; the fast reader never traces back.
8. **The continuous read.** For any document over a few pages, one cold read cover to cover IN ORDER after the per-section passes — the only way cross-boundary reference and cross-section consistency failures get caught.
9. **Render integrity (lint the OUTPUT, not the source).** Read the rendered document, not the source file: a source-side edit can silently eat the following live text (a comment or edit tail swallowing the next sentence), leaving a subjectless fragment, a lowercase sentence start, or an unbalanced parenthesis in the render that the source read never shows. When a rendered sentence is garbled, check the adjacent comments/edit markers for the swallowed tail FIRST and restore it verbatim — never rewrite a broken sentence from memory.
10. **The twin-splice sweep.** Two identical comma-splices in one document mean an unproofed edit wave, not typos — where one sentence boundary was lost, others from the same wave usually exist. Scan the render for ", [A-Z]" after a closing parenthesis or a long clause and audit every hit.
11. **Records are tenseless.** Archival/print prose carries no lab-log deixis: "as of today", "enters no check today", a heading stamped with a run date. Chronology belongs in logs and version history, not the document's claims.

Three sharpened kin: **process-abstraction agency** ("Sampling gives no warning", "optimization promises" — process nouns never take communicative verbs; concrete objects with natural dynamics survive: maxima split, chains converge); **staccato verdict-beats** (a <8-word declarative re-asserting what the evidence just showed, or announcing the next act's theme — drama typography, usually hiding an agency defect; drop, don't rephrase); **announcement sentences** ("We give a theory of when this happens" — a vague promise with no content; cut and let the concrete contribution sentences carry).

## G. The scrub procedure

1. **Read it aloud, sentence by sentence.** Flag anything that sounds like marketing, a chatbot, or a press release.
2. **Run the parse/composition pass (F) first**, then grep the vocabulary (A) and structures (B), then run the A3 greps and the A3.4 colleague test as their own pass.
3. **Check openings and closings.** First sentence, every subheading, every paragraph's last sentence — the densest hiding spots.
4. **Read the abstract as someone who has read nothing else.** Any internal name used without an antecedent is a tell (the paper talking to itself). Run the colleague test in the abstract's register: the colleague has not read the paper.
5. **Dictated text is not exempt.** Author-supplied sketches are content specifications, not finished prose — render and lint them like everything else.
6. **Lint the linter's output.** Fixes are new prose and regenerate tells. Whoever rewrites a sentence cannot be the last to review it: sweep the DIFF of every fix pass with different eyes.
7. **Run the honesty pass (E) and the number pass (N) separately and first in priority.** Verify every number, name, date, and attribution; run the cross-surface checks (body vs table vs caption vs figure label) on the rendered text.
8. **Root-cause every external catch.** When a reader flags a sentence that passed this skill, make TWO edits: cure the sentence, AND add the pattern here with the caught quote as its type specimen. A miss without a new entry is a repeat waiting.
8b. **Verify before "fixing."** A finding is a hypothesis, not a verdict. An identical value in two roles can be a coincidence with both sides correct; an odd-looking identifier can be the real one (N13); a comment in the source stating a premise ("the source never asserts X") can be stale — comments are provenance, not law: check the cited source before obeying, and when the premise is false, supersede the comment with a dated correction. Freeze any number you cannot verify rather than "improving" it.
8c. **Respect quoted and generated material.** Locate every verbatim-quoted span (block quotes of records, licensed excerpts) BEFORE editing — a cure that lands inside quoted material gets reverted, not defended; the editable surface is the surrounding prose. Generated tables/figures/captions are cured in their GENERATOR and regenerated, never hand-edited in the output; verify the regeneration changed only what the cure intended.
9. **Fixed-point loop for ship-critical text:** lint→fix→fresh-lint until a fresh pass returns zero findings. Findings cite a named rule (no taste-only findings); prior deliberate cures are protected from re-styling; the fixer replaces verbatim and never re-flows. Never report "linted to stability" as a quality claim — a fixed point certifies only that the sweep you ran finds nothing more; report what was checked.

Final test: *would a sharp human editor with no patience for machine-sounding prose wince at any sentence here?* If yes, it is not done.

---

## Quick grep sweep (starting point, not exhaustive)

```
grep -inE "delve|tapestry|realm|testament|underscore|leverage|unlock|unleash|seamless|robust|cutting-edge|game.?chang|revolutioni|paradigm|dive into|deep dive|the world of|ever-evolving|in today's world|treasure trove|boasts|a beacon|stands as|the beauty of" FILE
grep -inE "one floor|floor up|one rung|rung above|one level up|mathematical ladder|footgun|\bmoat\b|has landed|happy path|escape hatch|guardrail|dogfood|greenfield|bikeshed|yak.shav" FILE
grep -inE "downstream|upstream|pipeline|workflow|hand.?off|end-to-end|sanity check|edge case|toolchain|tooling|\bship(s|ped)?\b|\bdeploy|iterate on|blocker|pain point|load-bearing" FILE
grep -inE "the field (says|said|declared|decided|thinks|believes|calls|stopped|gave up)|field's (own )?verdict" FILE
grep -inE "not just|is a feature, not|not a .* but|; it [a-z]|is exactly wh|is what [a-z]+s |what .* is the|worth noting|worth savoring|the key is|what matters is|in conclusion|in summary|ultimately," FILE
grep -inE "what (survives|remains|emerges|follows|carries|changes|matters|works|counts)[^.?!]* is |, now (the|a|its) [a-z]+ (of|for)|now the subject" FILE
grep -inE "The (difference|reason|point|answer|upshot|issue|trouble|question|key|trick|surprise) (is|was) (whether|that|what|how|why|in )" FILE
grep -inE "There (is|are|was|were) [a-z]|, and it is the |, and that is wh|it is the (one|thing|reason)" FILE
grep -inE "the (literature|record|analysis|program|survey|data|section|study) (attaches|shows|produced|reveals|supplies|presents|argues|records)" FILE
grep -inE "^[A-Z][^.!?]{3,60}\.$|(One|Two|Three) [a-z]+, (one|two|three) [a-z]+\.|the (first|only) [a-z-]+ (stack|tool|pipeline|method|system)|proves (it|this|that)\b" FILE
grep -inE ", (proved|adjudicated|stated)[}.]|deeper finding|is the point:|worth naming" FILE
grep -inE "is where the story|the least of what|a question with an answer|where it bites|becomes visible at all|the (paper|study|author)'?s? (story|central question|narrative)" FILE
grep -inE "\b(sampling|optimization|the analysis|the procedure|the pipeline) (gives|tells|warns|promises|assures)|We (give|present|offer|provide) a (theory|framework|picture|account) of" FILE
grep -inE "\[[0-9]+\.[0-9]+, ?[0-9]+\.[0-9]+\]" FILE   # certified intervals: endpoints must round OUTWARD vs source
grep -icE "\bverdict|\breferee|\binterrogat|\bprice[ds]?\b|\bcampaign" FILE   # register saturation: >4 hits on one register word = B17 sweep
grep -inE "byte.for.byte|byte-identical|byte-level|fail-closed|pre-committed|pre-register|frozen protocol|calibrated blind" FILE
grep -inE "declared, not|not waived|is recorded\.|disclosed (as such|in full)|against any suspicion|rather than (convenient|bury)|did (its|their) job" FILE
grep -inE "proof of principle|to our knowledge" FILE   # count the hits: repeated hedge stamps and priority claims = B15
grep -inE "(Behind|Beneath|Atop|Above) the [a-z]+ (sits|lies|stands)|The (sharpest|strongest|deepest|cleanest) [a-z]+" FILE
grep -inE "^(One|Two|Three|Four) [a-z]+ (remain|follow|complete|stand)[s]?\.|The answer: " FILE
```
Treat every hit as guilty until proven innocent. Clefts hide *inside* sentences after "and/but", not only at sentence start — read for them; do not rely on grep alone. The document-scale classes (B15 repetition, B17 saturation, N cross-surface consistency) are invisible to any per-sentence read — run their counts and cross-surface checks as their own pass on the RENDERED text.

## Parse-pass 12: broken sentences from comment edits (the swallow class)

The single most productive TRUE-DEFECT check on any LLM-edited document: **sweep the
rendered artifact for lowercase-after-period**. When an editing pass inserts a comment
(or any annotation) before existing text, the following sentence's head is routinely
absorbed into the comment or dropped outright — the render then reads "...previous
sentence. orphaned lowercase tail..." and every per-sentence prose read misses it,
because readers repair broken syntax unconsciously.

Mechanics:
- Extract text from the RENDERED artifact (not the source) and scan for `. [a-z]{3,}`
  after filtering abbreviations (al., eq., cf., i.e., e.g., vs., Fig., Sec., ref., ...).
- Expect heavy noise: table cells, figure interleaves, lowercase-styled product names,
  hyphenation, and ligature loss (extraction can render "fits" as "ts" and "chiefly" as
  "chiey" — a candidate that looks broken may be a ligature artifact, and a cure you
  can't find in the render may be hiding behind one). Verify every candidate against the
  SOURCE before calling it real: a true break shows a comment line whose tail is orphaned
  prose, or a head that is simply gone.
- Editing hygiene that prevents the class: when a replacement inserts a comment before
  existing text, include the following sentence head in BOTH the old and new strings, and
  never end a replacement on a comment line. Never let a cleanup pass delete a comment
  line whose tail is prose — that is where eaten heads live.
- Recovery oracle: the version history of the rendered artifact. Walk back to the newest
  version where the sentence is whole and restore the head verbatim; do not paraphrase a
  head you can recover exactly.
- Special hazard: a comment inserted inside a brace-delimited argument (a caption, a
  footnote) can swallow the closing brace and break the build far from the edit. Keep
  comments outside argument braces.

Two build-layer traps that masquerade as prose problems: (a) bibliography databases do
not support in-entry comment syntax, and some parse annotation characters even in the
junk between entries — keep dated notes above entries and free of special characters;
(b) a successful build exit code does not guarantee the render picked up a regenerated
bibliography — verify the RENDERED text carries the change, and force a full rebuild
when it doesn't.

**Sources and acknowledgments.** The catalogue was compiled from our own editing
record, but the vocabulary in Section A overlaps heavily with the public
studies of LLM "excess vocabulary" by Kobak, González-Márquez, Horvát and Lause
(Sci. Adv. 11 (2025) eadt3813) and Liang et al. (arXiv:2403.07183, ICML 2024)
and with the community-maintained page Wikipedia:Signs of AI writing
(WikiProject AI Cleanup), which readers should treat as the better-documented
sources; the cures are the plain-style advice of Orwell ("Politics and the
English Language", 1946) and of Gopen and Swan ("The Science of Scientific
Writing", 1990), to whom most of Section B ultimately belongs.
