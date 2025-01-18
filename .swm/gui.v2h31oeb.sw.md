---
title: GUI
---
## Introduction

This doc gives a high level overview of the GUI of Myra. It is located under <SwmPath>[video/](/video/)</SwmPath> and is responsible for the interface of the assistant.

## Interface

The main file containing the code for the GUI is <SwmPath>[video/VISUAL.py](/video/VISUAL.py)</SwmPath>. It initializes with <SwmToken path="/video/VISUAL.py" pos="6:2:4" line-data="def Init_Window():">`Init_Window()`</SwmToken>, which is called in <SwmPath>[execution/building/build.py](/execution/building/build.py)</SwmPath>.&nbsp;

- IMPORTANT: The initialization is multithreaded to allow the window to execute at the same time as the main assistant code. Keep this in mind while developing.

## Directory structure

In the <SwmPath>[video/](/video/)</SwmPath> folder there is the <SwmPath>[video/web/](/video/web/)</SwmPath> containing the main html, js, css files for the GUI, and <SwmPath>[video/VISUAL.py](/video/VISUAL.py)</SwmPath>.

## Changes & Expansions

Right now, there is only template code inside of the files. Code needs to be added so that the main assistant is shutdown after closing the window, and vice versa. Also, there needs to be a usable interface.

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
