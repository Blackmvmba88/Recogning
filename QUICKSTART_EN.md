# Quick Start Guide - Recogning

This guide will help you get the object recognition system up and running in 5 minutes.

## 📋 Prerequisites

- Python 3.7+
- Webcam
- 5 minutes of your time

## 🚀 Quick Installation

```bash
# Clone the repository
git clone https://github.com/Blackmvmba88/Recogning.git
cd Recogning

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Basic Tutorial

### Option 1: Simple Version (Recommended)

```bash
python reconocimiento_simple.py
```

**Follow the menu:**
1. Select option **1** to teach a new object
2. Enter object name (e.g., "cup")
3. Position object in front of camera
4. 30 samples will be captured automatically
5. Repeat for 2-3 different objects
6. Select option **2** to train the model
7. Select option **3** to see real-time recognition!

### Option 2: Advanced Version

```bash
python object_recognition.py
```

#### Step 1: Capture Samples (2 minutes)

1. **Press `c`** to enter capture mode
2. **Type** the name of an object (e.g., "cup")
3. **Position** the object in front of the camera
4. **Press SPACE** 10-15 times to capture samples from different angles

Repeat for 2-3 different objects (e.g., "book", "phone")

#### Step 2: Train the Model (30 seconds)

**Press `t`** to train the model with captured samples

#### Step 3: Recognize Objects! (real-time)

**Press `p`** to enter prediction mode and show objects in front of camera

## 💡 Tips for Better Results

### During Capture:
- ✅ Capture 15-20 samples per object
- ✅ Vary angle and distance
- ✅ Maintain good lighting
- ✅ Use simple and consistent backgrounds

### For Better Accuracy:
- ✅ Visually distinct objects
- ✅ More samples = better accuracy
- ✅ Similar conditions between training and prediction

## 🔧 Quick Commands

### Simple Version Menu
| Option | Action |
|--------|--------|
| `1` | Teach New Object |
| `2` | Train Model |
| `3` | Recognize in Real-time |
| `4` | View Learned Objects |
| `5` | Exit |

### Advanced Version Keys
| Key | Action |
|-----|--------|
| `c` | Capture Mode |
| `SPACE` | Capture Sample |
| `t` | Train Model |
| `p` | Prediction Mode |
| `l` | Load Model |
| `q` | Exit |

## 📊 Complete Example

### Using Simple Version:
```bash
# 1. Start
python reconocimiento_simple.py

# 2. In the program:
# - Select 1, enter "cup", wait for 30 captures
# - Select 1, enter "book", wait for 30 captures
# - Select 1, enter "phone", wait for 30 captures
# - Select 2 to train
# - Select 3 to see real-time recognition
# - Select 5 to exit
```

### Using Advanced Version:
```bash
# 1. Start
python object_recognition.py

# 2. In the program:
# - Press 'c', type "cup", capture 15 samples with SPACE
# - Press 'c', type "book", capture 15 samples with SPACE
# - Press 'c', type "phone", capture 15 samples with SPACE
# - Press 't' to train
# - Press 'p' to see real-time recognition
# - Press 'q' to exit
```

## 🎓 Next Steps

1. **Read the full README** for advanced features
2. **Try example_usage.py** for programmatic use
3. **Experiment** with different objects and settings
4. **Share** your results

## ❓ Common Issues

**Camera doesn't work:**
- Verify it's connected
- Close other applications using the camera
- Check access permissions

**Inaccurate predictions:**
- Capture more samples (20-30 per object)
- Improve lighting
- Use more visually distinct objects

**Module import error:**
- Run: `pip install -r requirements.txt`

## 🎉 Ready!

You now have a functional object recognition system. Have fun teaching it to recognize the world!

---

**Need more help?** Check the [full README](README.md)
