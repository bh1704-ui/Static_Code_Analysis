# Issues Identified and Fixes Applied

| **Issue Type** | **Tool Used** | **Line No** | **Description** | **Fix Applied** |
|----------------|---------------|--------------|------------------|-----------------|
| Missing module docstring | Pylint | 1 | No description at the top of the file. | Added a short docstring explaining the purpose of the program. |
| Function naming style (snake_case) | Pylint | Multiple | Function names like `addItem`, `removeItem`, and `getQty` were not in snake_case format. | Renamed all functions to follow snake_case naming (e.g., `add_item`, `remove_item`, `get_qty`). |
| Mutable default argument | Pylint | 8 | Used `logs=[]` as a default parameter, which can cause shared data issues. | Changed to `logs=None` and initialized inside the function. |
| Bare except | Pylint / Flake8 | 19 | Used a bare `except:` which hides all exceptions. | Replaced with specific exceptions (`KeyError`, `ValueError`, `TypeError`) and added logging. |
| Use of `eval()` | Bandit | 59 | The `eval()` function is unsafe and can execute arbitrary code. | Removed `eval()` and replaced it with a safe logging statement. |
| File not closed properly | Pylint / Bandit | 26, 32 | Files were opened using `open()` without a context manager. | Used `with open(...) as f:` to ensure safe file handling. |
| Unspecified encoding | Pylint | 26, 32 | File operations did not specify encoding, which can cause errors on some systems. | Added `encoding="utf-8"` in all file operations. |
| Use of global variable | Pylint | 27 | `stock_data` was used as a global variable, which reduces maintainability. | Refactored the code into a class-based structure (`InventorySystem`) to avoid global state. |
| Logging f-string interpolation | Pylint | 21, 32, 36 | Used f-strings inside logging statements instead of lazy `%` formatting. | Updated all logging statements to use `%s` formatting for efficiency. |
| Too many blank lines / long lines | Flake8 | Multiple | Some lines exceeded 79 characters or had extra blank lines. | Adjusted spacing and wrapped long lines to meet PEP 8 standards. |

---

### ✅ Summary

- **Total Issues Fixed:** 10  
- **Tools Used:** Pylint, Bandit, Flake8  
- **Final Results:**
  - Pylint → *Your code has been rated at 10.00/10*  
  - Bandit → *No issues identified*  
  - Flake8 → *No output (PEP 8 compliant)*  
