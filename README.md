# Ipl_2023_score_predictor

This is a score predicting app for Indian premier league , kaggle was used for data then the data was filtered,cleaned,extracted ,feature extraction was performed .
The data was shaped in required shape which was needed for training data ,the data was split in training and testing data and the model was trained as keeping final score as our output
To run predictor run downlload pipe.pickle file and run main.py as(streamlit run main.py)
youll need some libraries which are mentioned in requirements.txt

### There are set of Parameters to be kept in mind
*Score predictor predicts best result for 1st innings of the match
*Atleast 5 overs has to be bowled
*Data for newer team is less which makes it difficult to train for new teams so they are excluded 

### The best r2_score and mean_absolute_error was registered 0.964 and 2.31 respectively
