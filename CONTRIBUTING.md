# Contributing
Thank you for investing your time in contributing to this project!

To contribute to this repository, please open an Issue with the details of changes you would like to make. If you have already contributed to this repository, please open a Pull Request.

## Opening an Issue
To open an issue, select "New Issue" from the [GitHub Issue tracker page](https://github.com/PamelaPajarillo/HEPQIS-LivingReview/issues). 
Please search through existing Issues before you open an Issue.

## Opening a Pull Request
Follow the folling instructions to open a Pull Request:
1. Create a [fork of the project](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
2. Install the following packages
```
sudo apt-get install latexmk texlive-full
pip install pandas urllib3
```
3. Create your Pull Request (PR) from your fork (see the FAQ below)
4. See FAQ below for instructions on adding a paper
5. Ensure that the tests in the CI are passing
6. Request that a maintainer review your PR. Your PR may be merged in once you have the sign-off of at least one maintainer

## FAQ
### How do I add a paper?

All paper additions should be submitted as a single pull request on a source branch that isn't `main`.

1. Make a new branch on your fork for the pull request
2. Find the paper on [INSPIRE](https://inspirehep.net/?ln=en). If you found the paper on [arXiv](https://arxiv.org/), the INSPIRE listing linked is linked under "References & Citations"
3. Obtain the INSPIRE control number by copying the digits at the end of the URL: `https://inspirehep.net/literature/CONTROLNUMBER`
4. Add the INSPIRE control number, HEP and QIS category identifications, and descriptions to [`HEPQIS.yaml`](https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/HEPQIS.csv) in the appropriate categories. The papers in `HEPQIS.yaml` are listed in reverse order of INSPIRE control number
5. Run `make` to update the `README`,`PDF`, and `BIB` files with the new references.
6. Add and commit `HEPQIS.bib`, `HEPQIS.yaml`, and the updated `README`,`PDF`, and `BIB` files to your pull request
8. If you haven't yet, push your branch to GitHub and open a pull request to the main project