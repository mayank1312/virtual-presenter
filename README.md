# AI Virtual Presenter 

This project allows you to control your presentation slides using hand gestures through your webcam. It uses computer vision to track your hand, enabling you to navigate slides, draw real-time annotations, and use a virtual pointer without touching your keyboard or mouse.

##  Features

* **Gesture-based Navigation:** Move to the next or previous slide.
* **Virtual Pointer:** A red dot follows your index and middle fingers to highlight content.
* **Live Annotation:** Draw directly on your slides with your index finger.
* **Undo:** Remove the last annotation you drew.

##  Tech Stack

* **Python 3.x**
* **OpenCV:** For video capture and image processing.
* **cvzone:** A wrapper for MediaPipe, used for hand tracking.
* **MediaPipe:** The underlying technology for hand landmark detection.
* **NumPy:** For numerical operations and screen mapping.

##  Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

Clone this project to your desired directory.

```bash
git clone "https://github.com/mayank1312/virtual-presenter.git"
cd virtual-presenter
```

### 2. Prepare Your Presentation

1.Export your presentation slides (from PowerPoint, Google Slides, Keynote, etc.) as PNG images.
2.Rename the exported images sequentially: 1.png, 2.png, 3.png, and so on.
3.Replace all these renamed PNG files inside the Presentation folder with the sample images.

### 3. Install Dependencies

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required libraries
pip install opencv-python cvzone numpy
```

## How To Run 

Open Terminal

```bash
python app.py
```

## General Instructions

Place your right hand inside the box shown and then use following Gestures for the presentation
1.Previous Slide: Raise only your Thumb.
2.Next Slide: Raise only your Pinky Finger.
3.Draw: Raise only your Index Finger. (Hold to draw a continuous line).
4.Pointer: Raise your Index and Middle Fingers to move the virtual pointer.
5.Delete Annotation: Raise your Index, Middle, and Ring Fingers to remove the last drawing on the current slide.

## Screenshots 


##
Thank you for checking out this project. Feel free to fork the repository, suggest improvements, or submit pull requests!
