# Exercise Badges

![](https://byob.yarr.is/apoorvav-github/made-template-fau/score_ex1) ![](https://byob.yarr.is/apoorvav-github/made-template-fau/score_ex2) ![](https://byob.yarr.is/apoorvav-github/made-template-fau/score_ex3) ![](https://byob.yarr.is/apoorvav-github/made-template-fau/score_ex4) ![](https://byob.yarr.is/apoorvav-github/made-template-fau/score_ex5)

# Methods of Advanced Data Engineering Project

This project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


## Project Work
### Main Question:
How is temperature change impacting the crop yield over the years and if there is any pattern that can be realized by visualization?

### Description:

The project aims to explore and understand the relationship between temperature change and crop yield in Ireland. Understanding this relationship is crucial for following reasons:

1. Selecting the appropriate crops can help to improve the overall yield.
2. Increases awareness of temperature impact on crops.


### Datasources:

#### Datasource1: Temperature change countrywise
* Metadata: https://www.fao.org/faostat/en/#data/ET/metadata
* Dataset: https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_Europe.zip
* Data Type: CSV

The CSV file contains temperature change data for Ireland from 1961 to 2023

#### Datasource2: Crop Yield (2008 - 2023) - Ireland 
* Metadata: https://data.gov.ie/dataset/aqa04-crop-yield-and-production/resource/ca2113ee-d9f3-4654-acc6-777213ae9330
* Data URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/AQA04/CSV/1.0/en
* Data Type: CSV

The CSV file contains data of crop yield in Ireland.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`
