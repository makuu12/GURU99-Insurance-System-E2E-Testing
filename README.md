# 🚗 GURU99 Insurance System E2E Automation Test

This automation testing focuses on the fundamental flows of the system from the start to the finish.

🔗 You can visit this link to know about the system:  
https://demo.guru99.com/insurance/v1/index.php

---

## 📥 Download here:

You can simply download the zip file here or clone this repo using bash:

```bash
git clone https://github.com/makuu12/GURU99-Insurance-System-E2E-Testing.git

## 📁 Folder Structure

Main folder/
├── library/
│ └── components.py # My personal reusable functions to program efficiently
├── testcases/
│ ├── resources/
│ │ ├── account.json # Data for user account management
│ │ └── qoute.json # Data for quotation of car insurance details
│ ├── manageAccount.py # To manage user accounts
│ ├── modules.py # To navigate between modules
│ ├── qoutationModule.py # To add/modify quotation data
│ └── setup.py # Initializes and starts the driver
└── main.py # Executable file to run the program

---

## 🔄 Test Flow (Positive Scenario)

| 🧪 Test Case            | 🎯 Objective                          |
|------------------------|----------------------------------------|
| Navigate to the link   | Open the system in the browser         |
| Create account         | Register a new user account            |
| Login account          | Authenticate using created credentials |
| Fill out quotation form| Input car insurance details            |
| Calculate request      | Compute estimated cost                 |
| Save quotation         | Save the computed quotation            |
| Edit account profile   | Modify user details                    |
| Verify account profile | Confirm changes were saved             |
| Logout                 | End the user session                   |


---

## ⚠️ Note

There are some problems coming from the server itself such as:

- The user/test script **cannot update the account profile**
- The user profile **does not display updated information**, so accuracy cannot be fully validated
- Some **menu/module buttons glitch** or behave inconsistently

---

## 🐞 Issues as of Now

- The user needs to **scroll manually** to components during automation, as some elements can be blocked by other UI elements (e.g., nav menu)
- The user needs to **manually click modal forms** to prevent errors and allow the automation to proceed smoothly
