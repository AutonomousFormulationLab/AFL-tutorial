# AFL Tutorials

| Tutorial | Description | Instructor Version | Student Version |
|----------|-------------|-------------------|-----------------|
| 01 | Introduction to small-angle scattering and the concept of phase mapping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/01-introduction-instructor.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/01-introduction-student.ipynb) |
| 02 | Building decision pipelines (AI agents) using scikit-learn | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/02-sklearn-instructor.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/02-sklearn-student.ipynb) |
| 03 | ~~Building decision agents with the AFL.double_agent library~~ | 🚧 Under Development | 🚧 Under Development |
| C1 | Build an agent that tolerates measurement noise | | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C1-challenge1.ipynb) |
| C2 | Discover the boundaries of multiple phases | | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C2-challenge2.ipynb) |
| C3 | Handle second order (continuous) phase transitions | | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C3-challenge3.ipynb) |
| CX | Ideas and inspiration for the challenges | | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/CX-inspiration.ipynb) |

## Introduction

The goal of these tutorials is to introduce the software tools developed to run the Autonomous Formulation Lab. We introduce our AI agent software (AFL.double_agent) and show how it can be used to build decision pipelines. The notebooks leverage widely used open source libraries (scikit-learn) and our new library for building decision pipelines (AFL.double_agent). We are in the process of developing tutorials for our orchestration software (AFL.automation) so check back soon

These tutorials are highly interactive, making it suitable for both self-paced learning and guided tutorial presentation settings.

## Background

The Autonomous Formulation Lab (AFL) is a National Institute of Standards and Technology (NIST) program that seeks to accelerate the discovery and optimization of soft materials through the development and application of autonomous techniques to high-value measurements. Specifically, we design robotic platforms that autonomously mix, synthesize and evaluate soft materials and we study them using small-angle scattering (SANS) and small-angle X-ray scattering (SAXS) and other techniques.

## Instructions

No installation required! All tutorials are designed to run directly in Google Colab.

⚠️ **Google Colab Kernel Warning**: The Colab kernel will automatically disconnect after periods of inactivity. If this happens, you'll need to rerun the "Setup" section at the top of the notebook to continue your work.

### Notebook Versions
- **Student Notebooks**: These notebooks are designed for guided tutorial presentations. They have sections of the code removed that are meant to be filled in by the active participants.
- **Instructor Notebooks**: These notebooks are designed for self-paced learning. They contain all the code and can be used to work through the tutorial at your own pace.

### How to Use These Tutorials
1. Click the "Open in Colab" button for the notebook version you want to use
2. Make a copy of the notebook to your own Google Drive to save your work
3. Work through the tutorials in order (01 → 02 → Challenges)

## Previous Guided Tutorials

| Date | Event | Location/Event |
|------|--------|-----------|
| February 2025 | Virtual Tutorial Lecture @ UIC| Chicago, IL |
| April 2024 | Spring MRS 2024 Tutorial | Seattle, WA |

## NIST Disclaimer

Any identification of commercial or open-source software in this document is
done so purely in order to specify the methodology adequately. Such
identification is not intended to imply recommendation or endorsement by the
National Institute of Standards and Technology, nor is it intended to imply
that the softwares identified are necessarily the best available for the
purpose.

## NIST License
This software was developed by employees of the National Institute of Standards
and Technology (NIST), an agency of the Federal Government and is being made
available as a public service. Pursuant to title 17 United States Code Section
105, works of NIST employees are not subject to copyright protection in the
United States.  This software may be subject to foreign copyright.  Permission
in the United States and in foreign countries, to the extent that NIST may hold
copyright, to use, copy, modify, create derivative works, and distribute this
software and its documentation without fee is hereby granted on a non-exclusive
basis, provided that this notice and disclaimer of warranty appears in all
copies. 

THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND, EITHER
EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY
THAT THE SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND FREEDOM FROM
INFRINGEMENT, AND ANY WARRANTY THAT THE DOCUMENTATION WILL CONFORM TO THE
SOFTWARE, OR ANY WARRANTY THAT THE SOFTWARE WILL BE ERROR FREE.  IN NO EVENT
SHALL NIST BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT,
INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR
IN ANY WAY CONNECTED WITH THIS SOFTWARE, WHETHER OR NOT BASED UPON WARRANTY,
CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS SUSTAINED BY PERSONS OR
PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE OUT
OF THE RESULTS OF, OR USE OF, THE SOFTWARE OR SERVICES PROVIDED HEREUNDER.