1. Which issues were the easiest to fix, and which were the hardest? Why?

  The easiest issues to fix were the spacing and naming style errors shown by flake8 and pylint. 
  Things like missing blank lines, line too long, or unused imports were simple to correct. 
  The hardest issues were related to exception handling and the use of eval() which Bandit flagged. 
  Those required changing logic and understanding safer ways to handle errors.

2. Did the static analysis tools report any false positives? If so, describe one example.

  One example of a false positive was when pylint warned about using a global variable. 
  In this small script it was intentional at first and did not really cause a bug, 
  so it felt unnecessary but I later changed the code to use a class.

3. How would you integrate static analysis tools into your actual software development workflow? 
  Consider continuous integration (CI) or local development practices.

  Static analysis tools can be added in the workflow using pre-commit hooks or CI tools like GitHub Actions. 
  Every time code is pushed or committed these tools can automatically run to catch issues early. 
  This helps maintain code quality and prevents unsafe or unclean code from being merged.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

  After applying all the fixes the code became much cleaner and easier to read. 
  The logging made it easier to debug, input validation made it safer, 
  and removing eval() removed a big security risk. 
  Overall the code now looks professional, secure, and more maintainable.
