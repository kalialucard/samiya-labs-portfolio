---
title: "Neural-Network-Visualizer"
date: "2024-01-01"
category: "projects"
enrich: true
image: "assets/project-thumb.png"
tags: "python, ai, visualization, tool"
description: "A real-time 3D visualization tool for neural network training processes."
summary: "Visualizing AI training in 3D."
skills: "python, three.js, tensorflow"
tools: "vscode, docker, nvidia-cuda"
github: "https://github.com/kalialucard/neural-viz"
report: ""
demo: ""
---

# Neural-Network-Visualizer

> **Status**: Completed  
> **Type**: Tooling

## Overview
Neural-Network-Visualizer fills the gap between raw loss metrics and intuitive understanding. It renders the weights and biases of a neural network as a 3D dynamic structure, allowing researchers to "watch" the network learn in real-time.

## Architecture
### System Design
The system uses a Python backend to hook into TensorFlow/PyTorch training loops and streams state data via WebSockets to a React/Three.js frontend.

```mermaid
graph LR
    A[Training Script] -->|Hooks| B[Python Agent]
    B -->|WebSocket| C[React Frontend]
    C -->|Render| D[Three.js Canvas]
```

### Key Components
*   **Agent**: A lightweight Python callback that extracts layer weights without slowing down training.
*   **Visualizer**: A WebGL-based engine capable of rendering millions of connections efficiently.

## Technical Implementation
### Challenges
Rendering dense matrices (1024x1024 layers) in the browser caused massive frame drops.

### Solutions
I implemented Instanced Mesh rendering in Three.js, reducing draw calls from thousands to just one per layer.

## Usage
```bash
pip install neural-viz
# In your training script:
from neural_viz import Visualizer
model.fit(..., callbacks=[Visualizer()])
```

## Results & Impact
*   Used by 50+ researchers to debug vanishing gradients.
*   Featured in "AI Tools Weekly".

## Future Roadmap
*   [ ] VR Support
*   [ ] Support for Transformer Attention Maps
