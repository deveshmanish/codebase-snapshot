# Repository Structure and Content Dumper

This repository contains scripts to generate a single text file summarizing the entire structure and contents of another code repository. It's useful for creating a quick, flat snapshot for easy searching, sharing code contexts with LLMs, or archival purposes.

## Features

*   **Directory Tree:** Generates a visual representation of the repository's folder and file structure, similar to the Linux `tree` command.
*   **File Content Concatenation:** Iterates through all files (recursively including subdirectories) and appends their contents to the output.
*   **File Path Markers:** Each file's content is preceded by a clear comment indicating its original path (e.g., `# File: path/to/your/file.js`).
*   **Exclusion Filtering:** Automatically skips common directories (like `node_modules`, `.git`, `__pycache__`) and file types (like logs, binaries, temporary files) to keep the output focused.
*   **Robust Traversal:** Handles multi-level nested directories.
*   **Single Output File:** Combines the structure and all file contents into one convenient `.txt` file.

## Included Scripts

Choose the script that best fits your environment:

1.  **`generate_repo_summary.sh` (Bash):** For Linux or macOS systems. Requires standard shell commands (`bash`, `find`, `cat`). Attempts to use the `tree` command for a nicer structure view if available.
2.  **`generate_repo_summary.py` (Python):** Cross-platform (Linux, macOS, Windows). Requires Python 3.x. Provides a built-in tree-like structure view.

## Usage

### Bash Script (`generate_repo_summary.sh`)

1.  Save `generate_repo_summary.sh` into the root directory of the repository you want to summarize.
2.  Make the script executable (usually required once):
    ```bash
    chmod +x generate_repo_summary.sh
    ```
3.  Run the script:
    *   To summarize the **current directory**:
        ```bash
        ./generate_repo_summary.sh
        ```
    *   To summarize a **specific directory** (replace `/path/to/target/repo`):
        ```bash
        ./generate_repo_summary.sh /path/to/target/repo
        ```

### Python Script (`generate_repo_summary.py`)

1.  Save `generate_repo_summary.py` into the root directory of the repository you want to summarize.
2.  Ensure you have Python 3 installed.
3.  Run the script from the command line:
    *   To summarize the **current directory**:
        ```bash
        python generate_repo_summary.py
        ```
        or (depending on your system's Python setup)
        ```bash
        python3 generate_repo_summary.py
        ```
    *   To summarize a **specific directory** (replace `/path/to/target/repo`):
        ```bash
        python generate_repo_summary.py /path/to/target/repo
        ```
    *   To specify a **custom output filename** (replace `my_summary.txt`):
        ```bash
        python generate_repo_summary.py -o my_summary.txt
        ```

## Output

Both scripts will generate a file in the directory where you run them. The default filename is `repo_contents_summary.txt`.

The output file will contain:

1.  A section showing the directory/file structure.
2.  A section containing the contents of each file, clearly marked with its path.

Example output structure:

=== Repository Structure (tree-like) ===
.
├── package.json
├── README.md
├── src/
│   ├── index.js
│   ├── config/
│   │   └── db.js
│   └── routes/
│       ├── userRoutes.js
│       └── api/
│           └── v1/
│               └── productRoutes.js
└── tests/
    └── user.test.js

=== File Contents ===

--------------------
# File: package.json
--------------------
{
  "name": "my-project",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.2"
  }
}

--------------------
# File: README.md
--------------------
# My Project

This is the README file.

--------------------
# File: src/index.js
--------------------
const express = require('express');
const db = require('./config/db');
// ... rest of index.js

--------------------
# File: src/config/db.js
--------------------
const mysql = require('mysql2');

const pool = mysql.createPool({
  // ... db config
});

module.exports = pool.promise();

--------------------
# File: src/routes/userRoutes.js
--------------------
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ message: 'Get all users' });
});

module.exports = router;

--------------------
# File: src/routes/api/v1/productRoutes.js
--------------------
const express = require('express');
const router = express.Router();

/**
 * @swagger
 * /products:
 *   get:
 *     summary: Get all products
 *     // ... swagger details
 */
router.get('/', (req, res) => {
  res.json({ products: [] });
});

module.exports = router;

--------------------
# File: tests/user.test.js
--------------------
const { expect } = require('chai');

describe('User Tests', () => {
  it('should pass', () => {
    expect(true).to.be.true;
  });
});


## Customization

You can modify the `exclude_patterns` list in the Python script or the `find` command's `-name` and `-path` options in the Bash script to add or remove directories/files that should not be included in the summary.

---
