# Contributing to YGO_Scanner

## Creating tickets 
Please feel free to create tickets, even if it's just for asking questions about YGO_Scanner. 
Issues should be descriptive and if bugs should have steps to reproduce. 

## Workflow 
The general approach to working on an issue is as follows: 
- Create a ticket if there isn't one already.
- Create a branch with `git checkout -b ###_issue_descriptor`, with `###` replaced with the issue number. 
- Make changes on branch 
- Open a pull request, comparing your branch to master 
- I will try and review the PR and suggest changes/merge it. 

## Formatting and code standards
As this is a Python project, it should follow the pep8 style, and in particular [`black`](https://github.com/psf/black) should be used. 

For linting, flake8 can be used. There is a config file in the root of the project directory and a flake8 check will be run on every travis build. 
