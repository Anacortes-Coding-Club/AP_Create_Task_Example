# README.md

# Component System Project

## Overview

This project implements a component system for managing game objects in a game environment. The component system allows for the dynamic addition and management of components that can enhance the functionality of `GameObject` instances.

## Project Structure

```
component-system-project
├── src
│   ├── componentSystem.py       # Implements the component system for managing components.
│   ├── gameObject.py            # Defines the GameObject class with properties for position and size.
│   └── components
│       ├── __init__.py          # Initializes the components package.
│       └── baseComponent.py      # Base class for all components that can be attached to GameObjects.
├── requirements.txt             # Lists the dependencies required for the project.
└── README.md                    # Documentation for the project.
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd component-system-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the component system, you can create instances of `GameObject` and attach components to them. Here is a simple example:

```python
from src.gameObject import GameObject
from src.componentSystem import ComponentSystem

# Create a GameObject
game_object = GameObject(x=0, y=0, width=50, height=50)

# Create a ComponentSystem
component_system = ComponentSystem()

# Add components to the GameObject
component_system.add_component(game_object, SomeComponent())
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.