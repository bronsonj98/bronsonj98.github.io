---
permalink: /
layout: home
title: "Moonseong Jeong"
description: "Moonseong Jeong, also known as Bronson Jeong, is a PhD candidate in Computer Science at UCLA who develops statistical and machine-learning methods for human genetics, medical imaging, and health records that work when patient data cannot leave an institution and computing is limited."
last_modified_at: 2026-11-09T12:00:00-08:00
redirect_from:
  - /about/
  - /about.html
subtitle: "Bronson Jeong · 정문성 · PhD candidate in Computer Science, UCLA"
lead: "I build statistical and machine-learning methods for human genetics, medical imaging, and health records that still work when patient data cannot leave an institution and computing is limited."
bio: "I am advised by Sriram Sankararaman and work where statistics, machine learning, and human genetics meet. My current work uses the All of Us Research Program, the UCLA ATLAS biobank, and California's prescription-monitoring data."
links:
  - title: "bronsonj@cs.ucla.edu"
    url: "mailto:bronsonj@cs.ucla.edu"
  - title: "Google Scholar"
    url: "https://scholar.google.com/citations?user=raOG4TkAAAAJ&hl=en"
  - title: "ORCID"
    url: "https://orcid.org/0009-0009-3836-2676"
  - title: "GitHub"
    url: "https://github.com/bronsonj98"
  - title: "CV (PDF)"
    url: "/files/Moonseong_Jeong_CV.pdf"
research_note: "Four themes, in plain terms."
themes:
  - title: "Genetic risk from summary data, across ancestries"
    text: "Genome-wide association studies release summary statistics for millions of variants, but rarely the genotypes of individual participants. SUM-RHE (<em>Genome Research</em>, 2024) estimates SNP heritability from summary statistics alone with the accuracy of methods that use individual genotypes. SUMMIT (bioRxiv, 2026) extends this to genetic correlation and to the heritability of genomic annotations, and replaces the local LD scores of earlier methods with genome-wide LD scores. Across 40 traits, the largest gains were in participants of South Asian and admixed African ancestry, for whom standard methods are biased. I presented this work as a platform talk at the 2026 meeting of the American Society of Human Genetics. Current work keeps related and admixed participants in the analysis rather than removing them."
  - title: "3D medical imaging without a GPU cluster"
    text: "Training a new model for each three-dimensional imaging task requires labelled scans and GPU clusters that most hospitals do not have. RAPTOR (ICML 2025, Spotlight, top 2.6% of submissions) passes the slices of a volume through a frozen two-dimensional foundation model and compresses the output with random projections. No training takes place, and a full scan is embedded in about 6.5 seconds on one consumer graphics card. Across 10 benchmark tasks, RAPTOR had the highest accuracy on 7. Applied to brain MRI, its embeddings recovered 111 of 118 known genetic associations and found 126 new ones. With collaborators in ophthalmology and genetics, I am applying the same approach to retinal scans to study age-related macular degeneration alongside genetic risk."
  - title: "What health records miss"
    text: "A health record contains a diagnosis only after a person is tested, seen, and coded, so disease that was present but not recognized leaves no trace. Among participants whose enrollment blood tests showed diabetes, kidney disease, or anemia, 19%, 32%, and 62% had no diagnosis or treatment on record, and five years later 81%, 55%, and 31% had been recognized. Case-finding models trained on recorded diagnoses found 23% to 29% fewer of the unrecognized cases than models trained on the blood tests (ML4H 2026). Whether a person is recognized is itself partly heritable, and my current work asks what this does to genetic studies that define disease from records."
  - title: "Opioid prescribing analytics inside a secure state system"
    text: "California's prescription drug monitoring program, CURES, records every controlled-substance prescription dispensed in the state. Under a collaboration approved by the California Department of Justice, I built the pipelines that turn these records, more than 200 million prescriptions to over 30 million people from about 400,000 prescribers, into analysis-ready data inside the Department's secure environment, and I analyze opioid exposure by region, prescriber specialty, and year, together with the effect of policy changes. Preliminary results were presented at the 2024 World Congress on Pain."
honors:
  - "Platform (oral) presentation, American Society of Human Genetics Annual Meeting, 2026"
  - "Spotlight paper, ICML 2025 (top 2.6% of submissions)"
  - "UCLA Computer Science Departmental Fellowship, 2022 to present"
  - "Reviewer for <em>Cell Genomics</em>, <em>Nature Communications</em>, <em>Bioinformatics</em>, <em>BMC Genomics</em>, RECOMB, ML4H, and ICLR"
teaching_note: "Teaching assistant at UCLA since 2023: computational genomics (C121/C221), introductory computer science (CS31), machine learning (M146), and machine learning in genetics (CM124/224)."
---
