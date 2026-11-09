---
title: "RAPTOR: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models"
collection: publications
permalink: /publication/icml-raptor
excerpt: "A train-free framework for 3D medical volumes that led the evaluated methods on 7 of 10 datasets, processed a full volume in about 6.5 seconds on a single 11 GB GPU, and enabled brain-MRI analyses identifying 126 new genetic associations while replicating 111 of 118 previously reported associations."
date: 2025-07-16
venue: ICML 2025 Spotlight
paperurl: "https://proceedings.mlr.press/v267/an25a.html"
codeurl: "https://github.com/sriramlab/raptor"
citation: #
authors: "An*, U., <u>Jeong*, M.</u>, Lee, S. A., Gorla, A., Yang, Y., and Sankararaman, S."
category: conferences
note: "*Equal contribution; Spotlight (top 2.6% of submissions)"
featured: true
featured_order: 3
figure: /images/figures/raptor.svg
figure_alt: "Pipeline: a stack of scan slices passes through a frozen two-dimensional image model and a random projection into a short embedding vector."
figure_caption: "RAPTOR: no training, one consumer graphics card, about 6.5 seconds per scan."
summary: "Applied to tens of thousands of brain scans, its embeddings found 126 new genetic associations while reproducing 111 of 118 known ones."
---
