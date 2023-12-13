# Networking Conversation Note Tracker

The only tool created to track your conversation notes on LinkedIn.

## Background

In 2023, @jqwez started having many conversations on LinkedIn with potential future coworkers and found that other note-taking tools were inadequate for making sense of all the interactions. This tool is meant to both keep a record of interactions within your given network and help you better understand how your network is interconnected. At the time of conception, the best working toolset for @jqwez was a bunch of notepad managed .txt files in a directory on his desktop. Thus, it is likely we will use notepad as our default text editor.

## Features

Currently not much. Immediately, what we are going to have is the ability to add connections you're interacting with on linked in and associate notes with them. Further features to follow. Feel free to suggest features by putting in a new issue.

## Model-View-Controller

We are using this nomenclature to get us started in code organization; however, we might not stick to strict patterns. The intent is to have a working application as soon as practicable.

## Toolset

Python was chosen to enable quick development targeting the desktop. While TkInter is being used, the tools used in this project should not inhibit transforming this into a backend for a future web application. You might find that there are packages already available that would work well in this application but @jqwez sometimes like to write things himself for the fun and practice of it. However, this does not mean contributions cannot feature a new package. In the future, @jqwez might do a rewrite in Kotlin as he was 50/50 on using it versus Python.

## Contributions

Contributions are not likely to come in and certainly not expected for such this project but they are certainly welcome. The simplicity of this open source application would likely make a great first/early contribution for the budding open source developer. All new features should have tests but, at a minimum, should not break any tests. We strive to have 100% coverage but this is not currently a hard and fast rule. Formatting is enforced by python black.

## TODO:

A lot.
