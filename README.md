
# 🚀 Strikeout Recognition and Removal Pipeline
![Python](https://img.shields.io/badge/Python-3.12-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0-green) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.1-yellow) ![NetworkX](https://img.shields.io/badge/NetworkX-3.4.2-orange)

---

## 📌 **Project Overview**
The **Strikeout Recognition and Removal Pipeline** is a Python-based project designed to:
- ✅ Detect and remove **strikeout lines** from scanned or digital documents.  
- ✅ Use **machine learning (SVM)** and **graph-based modeling** for strike detection.  
- ✅ Provide **enhanced visualization** by comparing original and processed images side by side.  
- ✅ Perform **batch processing** for multiple images automatically.

---

## ⚙️ **Features**
- 🔍 **Automated Image Preprocessing:**  
    - Converts images to grayscale.  
    - Applies adaptive thresholding and morphological operations.  
- 🤖 **SVM Model for Classification:**  
    - Trained to identify and remove strikeout lines.  
- 📊 **Graph-based Component Analysis:**  
    - Uses **NetworkX** for graph generation and analysis.  
- 📷 **Visualization & Comparison:**  
    - Displays **before and after** images side by side.  
- 📁 **Batch Processing:**  
    - Automatically processes all images in the `raw_images` folder.  
- 🚀 **Flexible and Scalable:**  
    - Modular code with clear directory structure.

---

## ✅ **Installation Instructions**

1. **📥 Clone the Repository**
```bash
git clone https://github.com/your-username/strikeout_recognition_project.git
cd strikeout_recognition_project
```

2. **📦 Install Required Libraries**
```bash
pip install -r requirements.txt
```

✅ **`requirements.txt`:**
```
opencv-python==4.11.0.80
numpy==1.26.3
scikit-learn==1.4.1
networkx==3.4.2
matplotlib==3.8.3
```

---

## 🚀 **Usage Instructions**

1. **📁 Place Images for Processing:**  
   - Add all your raw images to the `raw_images/` folder.  
   - Supported formats: `.png`, `.jpg`, `.jpeg`.

2. **🏃 Run the Pipeline:**  
   - In the root directory, run:
```bash
run.bat
```
3. **✅ View Results:**  
   - Processed images will be saved in `output/enhanced/`.  
   - Visualizations will be saved in `output/visualizations/`.  
   - Check the `visualize_results.py` script to view before/after images side by side.

---

## 📂 **Folder Structure**

```
C:\strikeout_recognition_project\
├── models\                     # SVM and Graph models
│   ├── svm_model.pkl           # Serialized SVM model
│   ├── graph.pkl               # Graph data model
│
├── output\                      # Output folders
│   ├── enhanced\               # Preprocessed images
│   ├── visualizations\         # Images with contours highlighted
│
├── raw_images\                  # Raw images for batch processing
│
├── src\                         # Source code folder
│   ├── preprocessing.py         # Preprocessing and thresholding
│   ├── graph_builder.py         # Graph creation
│   ├── svm_classifier.py        # SVM model loading and prediction
│   ├── strikeout_removal.py     # Final strikeout removal
│   ├── visualize_results.py     # Displays side-by-side images
│
├── run.bat                      # Batch script to run the full pipeline
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
```

---

## 🔥 **Pipeline Execution Flow**
✅ When you run `run.bat`, the following steps are executed:

1. **Preprocessing:**  
   - Grayscale conversion.  
   - Adaptive thresholding.  
   - Morphological operations for better line removal.  
   - Saves enhanced images to `output/enhanced/`.

2. **Graph Generation:**  
   - Generates a graph representation of the document.  
   - Uses **NetworkX** to build and save the graph model.  
   - Saves the model as `models/graph.pkl`.

3. **SVM Classification:**  
   - Loads the pre-trained SVM model from `models/svm_model.pkl`.  
   - Predicts strikeouts and filters them.  

4. **Strikeout Removal:**  
   - Removes detected strikeout lines from the images.  
   - Saves processed images in `output/visualizations/`.

5. **Visualization:**  
   - Displays side-by-side comparison of enhanced and processed images.  
   - Saved in `output/visualizations/`.

---

## 📊 **Output Examples**
✅ **Original Image:**  
`docs/original.png`

✅ **Enhanced Image (after preprocessing):**  
`docs/enhanced.png`

✅ **Strikeout Removed Image (after processing):**  
`docs/strikeout_removed.png`

✅ **Side-by-Side Visualization:**  
`docs/visualization.png`

---

## ⚙️ **Dependencies**
To run this project, you need the following Python libraries:
- `opencv-python==4.11.0` → For image processing  
- `numpy==1.26.3` → For numerical operations  
- `scikit-learn==1.4.1` → For SVM model training  
- `networkx==3.4.2` → For graph-based modeling  
- `matplotlib==3.8.3` → For visualizing side-by-side images  

✅ Install them by running:
```bash
pip install -r requirements.txt
```

---

## 🚀 **Future Enhancements**
1. **🔍 OCR Integration:**  
    - Use `Pytesseract` to extract and validate the recovered text.  

2. **📊 Performance Metrics:**  
    - Add metrics like **precision, recall, and F1-score** to evaluate accuracy.  

3. **🖼️ Interactive GUI:**  
    - Use **Gradio or Tkinter** for a user-friendly interface.  

4. **🔧 Real-Time Processing:**  
    - Streamline the pipeline for **real-time strikeout removal**.  

---

## 🎯 **Contributors**
- 👤 **Your Name** → Project lead  
- 💻 **OpenAI's ChatGPT** → Assistant for code optimization and debugging  

---

## 💡 **Contact & Support**
📧 For questions or support, feel free to reach out:  
- Email: `your-email@example.com`  
- GitHub Issues: [Open an Issue](https://github.com/your-username/strikeout_recognition_project/issues)

---

