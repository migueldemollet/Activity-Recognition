# Activity Recognition
Simple project in which it tries to indicate what the user's status is from accelerometers.

## Objective
Create a model that can predict from sensors what activity is being carried out (running, walking ...)

## Results
After having compared the following models:
* SVM witk kernel rbf
* SVM with kernel linear
* SVM with kernel poly
* SVN with kernel sigmoid
* Decision Tree
* Random Forest

We can assure you that the best is the Random Forest, with the following metrics obtained:

![metric image](https://github.com/migueldemollet/Activity-Recognition/blob/main/img/metricas.png)

With the following confusion matrix:

![metric image](https://github.com/migueldemollet/Activity-Recognition/blob/main/img/output.png)

## DataSet
The dataset has been obtained from the following link [dataset](https://www.kaggle.com/kosovanolexandr/data-for-activity-recognition)

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

* README md: repository documentation

* result.ipynb: notebook where the project has been developed

## User guide
1. Run the following command:

        $ git clone https://github.com/migueldemollet/Activity-Recognition.git

2. Open the file result.ipynb with your favorite editor or by executing the script notebook.bat

3. Feel free to modify the code

## Built With
* [Visual Studio Code](https://code.visualstudio.com/) - The editor used.
* [Python](https://www.python.org/) - Programming language used.

## Author
* **Miguel del Arco** - [migueldemollet](https://github.com/migueldemollet)

## License
This project is under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
