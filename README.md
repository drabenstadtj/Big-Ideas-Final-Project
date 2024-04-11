## Final Project

### Team name: Small Ideas

### Members:

- Jack Drabenstadt (jtd102@pitt.edu)
- Aidan Conroy (aec164@pitt.edu)

### Description

This project aims to identify the "best" neighborhood within a given area based on the number of parks, protected lanes, and transit stops. It utilizes a dataset containing information about the location and boundaries of each neighborhood, along with a Python script to determine if a point's latitude and longitude fall within a specific neighborhood.

The process involves iterating through each neighborhood, calculating counts for each metric (parks, protected lanes, and transit stops), and determining a score for each neighborhood based on these counts. These scores are then normalized and combined into an overall score of "bestness" for each neighborhood.

In summary, the project involves data analysis, geospatial processing, and scoring algorithms to evaluate and compare neighborhoods based on their amenities and infrastructure.

### Datasets:

- [Neighborhoods](https://data.wprdc.org/dataset/neighborhoods2)
- [Bike Lanes](https://data.wprdc.org/dataset/shape-files-for-bikepgh-s-pittsburgh-bike-map/resource/841de570-9de1-4568-87a1-f52dfb1b7622)
- [Parks](https://data.wprdc.org/dataset/parks1/resource/bb57d0a7-e8ee-4218-8906-0dedc903038c)
- [Bus Stops](https://data.wprdc.org/dataset/prt-of-allegheny-county-transit-stops/resource/d6e6ed6e-9220-4a0e-9796-e72d83ce8e7a?inner_span=True)

#### Repository Overview:

This repository contains geographic data processing scripts and a final project Python file, alongside associated datasets, for analyzing and evaluating neighborhood metrics.
