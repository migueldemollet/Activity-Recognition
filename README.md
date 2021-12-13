# Activity Recognition
Project which classifies the user's activity through accelerometers.

## Objective
Create a model that can predict from sensors what activity is being carried out (running, walking ...)

## DataSet
The dataset has been obtained from the following link [dataset](https://www.kaggle.com/kosovanolexandr/data-for-activity-recognition)

## Results
After having compared the following models:
* SVM witk kernel rbf
* SVM with kernel linear
* SVM with kernel poly
* SVM with kernel sigmoid
* Decision Tree
* Random Forest

We can assure you that the best is the Random Forest, with the following metrics obtained:

![metric image](https://github.com/migueldemollet/Activity-Recognition/blob/main/img/metricas.png)

With the following confusion matrix:

![metric image](https://github.com/migueldemollet/Activity-Recognition/blob/main/img/output.png)

## Repository Structure
The repository is composed as follows:

* data: contains training and test data

    * idle: idle state data

    * walking: walking state data

    * running: running state data

    * stairs: stairs state data

    * metadata: contains the data of the device on which the data was obtained

* img: contains the images of the readme

* src: It contains code of tests of the first versions

* LICENSE: file that indicates the license of the repository

* notebook.bat: script to run the notebook result with the jupyter notebook application

* requirements.txt: file that indicates the libraries that the project uses

* README md: repository documentation

* result.ipynb: notebook where the project has been developed

## Prerequisites
* Python 3.9 or later
* Have all the requirements from the file requirements.txt
    
    * seaborn
    * matplotlib
    * scikit-learn
    * pandas
    * numpy
    * scipy
    * sklearn
    * imblearn


If you don't have some of these libraries, you can install them manually or by running the following command:

    $ pip install -r requirements.txt

## User guide
1. Run the following command:

        $ git clone https://github.com/migueldemollet/Activity-Recognition.git

2. Open the file result.ipynb with your favorite editor or by executing the script notebook.bat

3. Feel free to modify the code

## Built With
* [Visual Studio Code](https://code.visualstudio.com/) - The editor used.
* [Python 3.9](https://www.python.org/) - Programming language used.

## Author
* **Miguel del Arco** - 1566698 - [migueldemollet](https://github.com/migueldemollet)

## Conclusion
After having carried out an intense search for parameters and cross-validation and solved the problems of the distribution of the data, we can affirm that we have found the best model for our problem, this is the random forest with the parameters n-estimators = 100 and min_samples_leaf = 1.

Although this model has been the best for our problem, the other models are not far behind since the metrics obtained in the cross-validation are very promising but we are interested in the random forest because it is the best.

## Ideas for future work
* Predict what sport will be performed.
* Create an application for a smartphone or smartwatch that integrates this model.

## License
This project is under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
