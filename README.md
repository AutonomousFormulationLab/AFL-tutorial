# AFL Agent Tutorial

| Tutorial | Description | Open in Colab |
|----------|-------------|----------------|
| 01 - Intro | Introduction to small-angle scattering and the concept of phase mapping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/01-introduction.ipynb) |
| 02 - Decision Pipelines | Building decision pipelines using scikit-learn | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/02-sklearn.ipynb) |
| 03 - AFL Agent | Building decision agents with the AFL.double_agent library | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/03-afl-agent.ipynb) |
| C1 - Challenge 1 | Build an agent that tolerates measurement noise | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C1-challenge1.ipynb) |
| C2 - Challenge 2 | Discover the boundaries of multiple phases | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C2-challenge2.ipynb) |
| C3 - Challenge 3 | Handle second order (continuous) phase transitions | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martintb/AFL-tutorial/blob/main/notebooks/C3-challenge3.ipynb) |

## Introduction

This goal of these tutorials is to convey a methodlogy for using machine learning to interpret experimental data for the purpose of microstructural phase identification and structure mapping. The tutorial is highly interactive, making it suitable for both self-paced learning and guided tutorial presentation settings.

## Background

The Autonomous Formulation Lab (AFL) is a National Institute of Standards and Technology (NIST) program that seeks to accelerate the discovery and optimization of soft materials through the development and application of autonomous techniques to high-value measurements. Specifically, we design robotic platforms that autonomously mix, synthesize and evaluate soft materials and we study them using small-angle scattering (SANS) and small-angle X-ray scattering (SAXS) and other techniques.

## Installation

No installation required! All tutorials are designed to run directly in Google Colab.

## Important Note

⚠️ **Google Colab Kernel Warning**: The Colab kernel will automatically disconnect after periods of inactivity. If this happens, you'll need to rerun the "Setup" section at the top of the notebook to continue your work.


## Previous Tutorials

| Date | Event | Location/Event |
|------|--------|-----------|
| April 2024 | Spring MRS 2024 Tutorial | Seattle, WA |
| February 2025 | Virtual Tutorial Lecture @ UIC| Chicago, IL |

## Contributing

We welcome contributions and feedback! Please submit any issues or suggestions using the Issues functionality on Github. 


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