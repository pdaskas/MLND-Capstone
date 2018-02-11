# Machine Learning Engineer Nanodegree
## Capstone Proposal
Patrick Daskas
January 26, 2018

## Proposal


### Domain Background
     I will be using data from the Kepler telescope (2009-2013).  The Kepler mission was designed to observe thousands of stars to look for transiting planets.  The mission looks for reductions in a star's brightness, and if the reduction occurrs on a set period, then the star could be considered as having planet candidates.  From the data that it is collected, NASA has been able to detect thousands of new planets orbiting other stars.  The largest solar system detected by the Kepler mission has been 7 planets.  Just last year, Google created a convolutional neural network to detect exoplanets.  In the system that had 7 planets, Google discovered an 8th.  This finding was recently confirmed by NASA.
    This will not be using the K2 data.  After some hardware failures in 2013, the Kepler mission's progress came to a halt.  With the failing hardware, NASA repurposed the Kepler telescope to acquire data that spanned much smaller timescales.

More information describing the Kepler mission and the K2 mission can be found here:
https://www.nasa.gov/mission_pages/kepler/overview/index.html

More information about Google and NASA discovering an 8th planet by using artificial intelligence can be found here:
https://www.nasa.gov/press-release/artificial-intelligence-nasa-data-used-to-discover-eighth-planet-circling-distant-star

### Problem Statement
    The amount of data acquired by the Kepler telescope is enormous.  How  are exoplanets detected in all the data?  Almost every star observed has over 4000 data points per quarter.  There are approximately 70000 data points that describe the change in brightness and the time in which it occurred for each star.  Add to that over 100000 stars with this type of data, and one can quickly realize that manual detection of exoplanets seems absurd. There are websites today that pull this data and have a userbase analyze each of the image sets.  They are attempting to manually categorize stars as having or not having exoplanets.  I plan to build a convolutional neural network to automatically classify targets in the dataset.

### Datasets and Inputs
    I have downloaded "fits" files for roughly 5600 stars, and this data set is about 40 gigabytes.  These fits files have been provided by NASA.  With the intent to classify, I downloaded data that has already been categorized as planet candidate targets and false positive targets. 
    For the planet candidate targets, I took the data from http://archive.stsci.edu/missions/kepler/lightcurves/tarfiles/Exoplanet_KOI/.  I downloaded each long cadence tgz file (_long.tgz) for all 17 quarters.  Each contains a collection of fits files for various stars that were scanned in that quarter.
    I also need a set containing false positives.  For this, I executed wget scripts by quarter from http://archive.stsci.edu/missions/kepler/lightcurves/tarfiles/wget_scripts/ for the false positives.  These scripts downloaded long and short cadence files.  To be consistent, I removed all short cadence files (these files ended in sc.fits) and kept the long cadence files (ending in lc.fits).
    Using PyKE (https://github.com/KeplerGO/pyke), I intend to stitch together 17 quarters of data for each star.  The data will then be normalized using PyKE.  Normalization is necessary, as after each quarter, the telescope rotates (to maximize solar gains on the solar panels).  Normalization is an expensive operation and will be done by splitting the work across multiple cores on the CPU.  The normalized fits file contains datapoints that represent brightness and time.  Using this data with matplotlib, I will create a picture of the change in brightness for a given star across 17 quarters.  The file will be saved and used as inputs to the convolutional neural network.

### Solution Statement
    I will build a convolutional neural network to determine if a target star has planets.  For the scope of this project, I will not attempt to create a model which can determine the number of planets for a given star.  I will simply try to identify planet candidate stars from false positives.  To do this, I will need to preprocess a significant amount of data.  My dataset will be classified as planet candidates and false positives.  The inputs will be images, and I will split them entire set into a training, testing, and validation set.  The training set will be 80%, and 10% will go to each of the remaining.  I may explore k-fold cross validation. 

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

https://software.nasa.gov/software/ARC-17981-1 (Robovetter)
Kepler Object of Interest (KOI) Catalog - Q1–Q17 DR 25 (https://exoplanetarchive.ipac.caltech.edu/docs/Q1Q17-DR25-KOIcompanion.html)

NASA currently has a pipeline to vet stars and classify them as planet candidates or false positives.  This tool is called Robovetter and it  uses a Random Forest to achieve its goal.  It's classification is used as the ground truth for my inputs.  I hope to achieve greater than 50% accuracy on my test set.


### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
Environment
Python 3.0+
Keras
Tensorflow
Scikit-learn
Numpy
Matplotlib
PyKE

-Acquire dataset for 5000+ targets (across two categories: False Positives, Planet Candidates) for 17 quarters (2009-2013)
-Build new dataset for the 5000+ targets where the data is merged and normalized
-Convert the dataset containing the brightness and time to a graph using Matplotlib
-Save all graphs as images
-Split the dataset into training/testing/validation (80/10/10) sets.
-Build convolutional neural network starting with 5 convolutional layers with dropout, maxpooling and batch normalization between each.  The final fully connected layer will have 2 units which represents the two categories and will have a softmax activation.
--Each convolutional layer will have a relu activation
-Assess the accuracy on the training, and validation set.
-Use the model to make predictions against the test set and assess the accuracy.
-Work to improve the accuracy on the test set by altering the hyperparameters.  

