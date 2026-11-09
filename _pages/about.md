---
permalink: /
layout: home-modern
title: "Moonseong Jeong"
description: "Moonseong Jeong, also known as Bronson Jeong, is a computational genomics and biomedical machine learning researcher at UCLA who develops privacy-preserving, compute-efficient methods for medical imaging, genomic data, prescription records, and electronic health records."
last_modified_at: 2026-11-08T17:00:00-08:00
author_profile: false
redirect_from: 
  - /about/
  - /about.html
profile_statement: >-
  Moonseong Jeong, also known as Bronson Jeong, is a computational genomics and biomedical machine learning researcher at UCLA. He develops privacy-preserving, compute-efficient methods that let hospitals, biobanks, and public-health agencies draw clinically useful insight from medical images, genomic data, prescription records, and electronic health records inside secure environments, without centralizing raw patient-level data or repeatedly training large models.
research_areas:
  - label: "Medical imaging"
    title: "3D medical image analysis without large-scale training"
    text: "RAPTOR turns a full 3D medical volume into a compact representation using frozen 2D foundation models and random projections, with no task-specific training and on a single consumer GPU; across 10 evaluation tasks it led the evaluated methods on 7 datasets. Ongoing work applies the approach to retinal 3D scans and eye disease."
  - label: "Statistical genetics"
    title: "Genetic architecture from summary statistics, without raw genomes"
    text: "SUM-RHE and SUMMIT estimate heritability, genetic correlation, and their partition across annotations from GWAS summary statistics; SUMMIT's genome-wide LD scores keep estimates robust in structured and admixed cohorts and across ancestries, so governed biobanks can be analyzed without sharing individual-level genotypes."
  - label: "Imaging genomics"
    title: "Connecting retinal imaging phenotypes with genetic risk"
    text: "Quantitative biomarkers extracted from retinal OCT scans are combined with summary-level genetic inference to study the genetic architecture of age-related macular degeneration and other ocular disease across biobanks."
  - label: "Prescription monitoring"
    title: "Secure analytics for controlled-substance prescribing"
    text: "Interpretable, on-premises analyses of California's prescription-monitoring data (CURES), spanning more than 30 million individuals and 200 million prescriptions, to characterize opioid exposure, prescriber patterns, and the effects of policy changes under strict data-governance constraints."
  - label: "Health records"
    title: "The genetics of being diagnosed"
    text: "Diagnosis codes record whether disease was recognized, not only whether it was present. Work in UK Biobank quantifies recognition delay for measured disease and its cost to EHR case finding (ML4H 2026), and studies the heritable component of being diagnosed."
---

Moonseong Jeong, also known as Bronson Jeong, is a PhD candidate in Computer Science at UCLA, advised by Prof. [Sriram Sankararaman](http://web.cs.ucla.edu/~sriram/). His research sits at the interface of machine learning, statistics, and biomedicine, with a focus on scalable, reproducible methods for understanding the genetic basis of complex traits and diseases, and on making sensitive medical data useful under the privacy, security, and compute constraints that real institutions face.

His recent work includes SUMMIT, a summary-statistics framework that uses genome-wide LD scores to estimate heritability and genetic correlation robustly across genetic ancestries (bioRxiv, 2026; platform talk at the ASHG 2026 Annual Meeting in Montréal), and a study of recognition delay in diagnosis codes and its cost to case finding in electronic health records (ML4H 2026). He serves as technical lead of a California Department of Justice-approved collaboration analyzing the state's controlled-substance prescription data.

Moonseong earned an MS in Computer Science from UCLA in 2025 and previously completed a BS in Mathematics of Computation and a BA in Physics at UCLA. As an undergraduate, he worked on astronomical spectroscopy with Prof. [Alice Shapley](https://www.astro.ucla.edu/~aes/). That training continues to shape his approach to biomedical inference: careful modeling under noise, confounding, and limited observability.

Across these projects, his research asks how biomedical methods can remain useful when institutions cannot freely centralize sensitive records or assume access to large computing infrastructure.
