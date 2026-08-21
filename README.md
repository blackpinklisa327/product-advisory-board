# Product Advisory Board

Bring the right product thinkers into the room for a product decision.

Product Advisory Board is a model-agnostic skill that assembles grounded expert perspectives, lets you call individual advisors by name, surfaces meaningful disagreement, and then helps you make the call.

## What you can do

- `Should Duolingo de-emphasize streaks for mature learners?`
- `Ask Elena Verna to challenge this retention strategy.`
- `Bring in three advisors who will disagree about this pricing decision.`
- `Teresa Torres, critique my discovery plan.`
- `Have April Dunford and Bob Moesta debate this positioning.`

The advisor library is grounded primarily in public source material, including Lenny's Podcast transcripts, and can be enriched with an advisor's own writing, talks, books, interviews, and other credible public sources. The goal is not celebrity role-play. The goal is to retrieve documented schools of judgment and expose a decision to multiple useful perspectives.

## Advisors ask before they advise

If your prompt is missing context that would materially change the answer, the advisor should **not invent the missing product facts**. Instead, they ask 1–3 high-information questions that reflect their own judgment style.

For example, if you say:

`Ask Elena Verna to challenge this retention strategy: We should add more streak rewards to increase D30 retention.`

A good response should first ask things like:

- What product is this and what behavior represents real user value?
- Where does retention actually break between activation and D30?
- What evidence connects streak behavior to the churn problem?

Teresa Torres, April Dunford, Annie Duke, and other advisors should ask different questions because they reason differently.

If the context is already sufficient, the advisor should skip the intake and make the call.

## Evidence rules

The skill distinguishes transcript evidence, external primary sources, external secondary sources, and synthesized inference. It should never present an inferred opinion as something an advisor actually said.

## Status

The standalone skill now includes the initial advisor-selection logic, direct-call behavior, context-sufficiency gate, and the 306-person name-resolution roster. Stored enriched profiles and source-grounded judgment cards are being expanded progressively.