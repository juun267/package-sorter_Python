# Package Sorter

This repository contains a Python solution for sorting packages based on their dimensions and mass. The function determines where each package should be dispatched: STANDARD, SPECIAL, or REJECTED.

## Functionality

The function `sort(width, height, length, mass)` classifies packages according to the following rules:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.

### Criteria

- **Bulky**: A package is considered bulky if its volume is greater than or equal to 1,000,000 cm³, or if any of its dimensions (width, height, or length) is greater than or equal to 150 cm.
- **Heavy**: A package is considered heavy if its mass is greater than or equal to 20 kg.

### Implementation

The Python function to sort the packages is implemented in `main.py`.

### How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/package-sorter.git

2. **Navigate to the Directory**:
   cd package-sorter
   
4. **Run the Code**:
   Ensure you have Python installed. Then run:
   python main.py
   
6. **View Output**:
   The test cases will output the stack classification for each package.
