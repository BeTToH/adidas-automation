# adidas-automation
Automation of the adidas.com/us website.

# Installation
1. Download the chromedriver and add it to the PATH system variable. 
It can be downloaded at https://chromedriver.chromium.org/downloads;

2. Install python libraries by running, on the project root, 
"pip install -r requirements.txt";

3. Install the adidas-automation package by running, on the project root, 
"pip install -e .".

# Running
1. Fulfill the necessary info in the adidas_automation\tests\template.env.txt file,
 such as, EMAIL and TEST_RESULTS_PATH. Then, rename it to ".env";

2. To run, execute the following command from the project root: 
python -u "adidas_automation\tests\test_register.py"

