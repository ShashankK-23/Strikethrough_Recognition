@echo off
echo Running Automated Strikeout Recognition Pipeline...

REM Preprocessing
python src/preprocessing.py

REM Graph building
python src/graph_builder.py

REM SVM Classification
python src/svm_classifier.py

REM Strikeout Removal
python src/strikeout_removal.py

echo 🎯 Pipeline completed!
pause
