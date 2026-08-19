# RateMySplice

RateMySplice is an early computational biology project developed to
support experimental investigation of 5′ splice site recognition.

## Project concept

The original aim was to identify positions within a DNA sequence where
a nucleotide substitution could generate a putative GT splice donor
site.

The workflow was designed to:

1. search an input DNA sequence for candidate positions;
2. generate sequence variants containing a potential GT donor motif;
3. extract the local sequence surrounding each candidate site;
4. score the resulting putative splice sites;
5. rank candidate mutations for experimental testing.

The repository currently contains the original Python prototype used to
generate candidate mutated sequences.

A later version of the project incorporated maximum entropy splice site
scoring, developed collaboratively, but that implementation is not
contained in this repository.

## Current status

This repository preserves the original prototype as an example of my
early computational biology work.

A future redevelopment is planned as a user friendly sequence analysis
tool in which researchers could submit a DNA sequence, generate
candidate splice site mutations, score them and prioritise mutations for
experimental investigation.

## Repository structure

`legacy/` — original Python prototype from the undergraduate project.

## Planned redevelopment

Future development may include:

- user-supplied DNA sequences;
- systematic generation of candidate splice donor mutations;
- splice site strength scoring;
- ranking and visualisation of candidate mutations;
- a simple web based interface;
- documented and reproducible analysis;
- automated tests.

## Background

The project originated during my undergraduate research in splice site
recognition and experimental manipulation of splicing.
