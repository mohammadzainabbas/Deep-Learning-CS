## 🎨 Monet like Painting 👩🏻‍🎨 via Diffusion Model 👨🏻‍💻

### Table of contents

- [Introduction](#introduction)
- [Kaggle challenge](#kaggle-challenge)
- [Setup](#setup)
  * [Create new enviornment](#create-new-env)
  * [Setup `pre-commit` hooks](#setup-pre-commit)


#

<a id="introduction" />

### 1. Introduction

> _“Every artist dips his brush in his own soul, and paints his own nature into his pictures.”_
> Henry Ward Beecher

We recognize the works of artists through their unique style, such as color choices or brush strokes. The _“je ne sais quoi”_ (I do not know what) of artists like [__Claude Monet__](https://en.wikipedia.org/wiki/Claude_Monet) can now be imitated with image generation algorithms like: generative adversarial networks (GANs) and diffusion models. 

In this project, we will bring that style to the photos or recreate the style from scratch via duffion model!

#

<a id="about-course" />

### 2. About the course

A decision model provides a way to visualize the sequences of events that can occur following alternative decisions (or actions) in a logical framework.

<p align="center">
  <img alt="Decision Modelling Process" width="400" src="extra/assets/decision_modelling_process.png" />
</p>

There are two types of decision models in the literature:

1. Deterministic models
2. Probabilistic models

The purpose of this course is to study different ways to model a _deterministic_ decision model.

<a id="main-topics" />

#### 2.1. Main Topics

- [x] Introduction to Decision Modeling
- [x] Preferences as binary relations
- [x] Voting rules as Group Decision Making Models

#

<a id="labs" />

### 3. Labs

The main aim of this repository is to keep track of the work we have done in __Decision Modelling (DeM)__ labs.
#

<a id="lab-1" />

#### 3.1. Lab 01 - Testing Binary Relations

In this lab, we focused on testing binary relations (given a matrix/graph to extract binary relations). You could use [NetworkX](https://networkx.org/) to generate a graph/matrix to test different the binary relations.

Please checkout lab's details [here](https://github.com/mohammadzainabbas/DeM-Lab/tree/main/src/lab1)

<a id="lab-2" />

#### 3.2. Lab 02 - Binary Relations via Linear Programming

This lab focuses on implementing a decision model for some given constraints via _linear programming_. You could use the following python packages to solve _linear programs_:

- [x] [Linear Programming with Python and PuLP](http://benalexkeen.com/linear-programming-with-python-and-pulp/)
- [x] [scipy.optimize.linprog](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.linprog.html)

> For more details: checkout this [detailed guidline](https://realpython.com/linear-programming-python/#linear-programming-python-implementation)

Please checkout lab's details [here](https://github.com/mohammadzainabbas/DeM-Lab/tree/main/src/lab2)

#

<a id="setup" />

### 4. Setup

If you want to follow along with the lab exercises, make sure to clone and `cd` to the relevant lab's directory:

```bash
git clone https://github.com/mohammadzainabbas/DeM-Lab.git
cd DeM-Lab/src/<lab-of-your-choice>
```

> For e.g: if you want to practice lab # 1, then you should do `cd DeM-Lab/src/lab1`.

<a id="create-new-env" />

#### 4.1. Create new enviornment

Before starting, you may have to create new enviornment for the lab. Kindly, checkout the [documentation](https://github.com/mohammadzainabbas/DeM-Lab/blob/main/docs/SETUP_ENV.md) for creating an new environment.

#

Once, you have activated your new enviornment, we may have to install all the dependencies for a given lab (kindly check if `requirements.txt` file exists for a given lab before running the below command):

```bash
pip install -r requirements.txt
```

<a id="setup-pre-commit" />

#### 4.2. Setup `pre-commit` hooks

In order to setup `pre-commit` hooks, please refer to the [documentation](https://github.com/mohammadzainabbas/DeM-Lab/blob/main/docs/SETUP_PRE-COMMIT_HOOKS.md).

#
