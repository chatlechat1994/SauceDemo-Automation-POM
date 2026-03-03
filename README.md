# SauceDemo UI Automation Framework (POM)

A UI automation suite demonstrating the Page Object Model (POM) design pattern for scalable and maintainable web testing.

### **Skills Demonstrated**
* **Framework Architecture:** Logical separation of UI locators (pages/) and test logic (tests/) to reduce maintenance.
* **Clean Code Practices:** Use of .gitignore to maintain a professional, junk-free repository.
* **Automation Logic:** Implementation of Selenium By selectors, implicit waits, and element interactions.
* **Tools:** Python 3.x, Selenium WebDriver, and Pytest.

### **Project Structure**
* **pages/**: Contains classes for the Login and Inventory pages. This acts as the source of truth for UI locators, ensuring that site updates only require changes in one file.
* **tests/**: Contains the end-to-end purchase flow test scripts and assertions.
* **.gitignore**: Configured to ignore __pycache__, .pytest_cache, and local environment files.

### **Execution and Setup**
To run this project locally:

1. **Clone the repository:**
   git clone https://github.com/chatlechat1994/SauceDemo-Automation-POM.git

2. **Install dependencies:**
   pip install selenium pytest

3. **Run the test suite:**
   pytest

### **Test Coverage**
* **Successful Login:** Verifies access with standard_user credentials.
* **Product Interaction:** Selects the "Sauce Labs Backpack" and adds it to the cart.
* **Navigation Validation:** Uses URL assertions to confirm the user reached the cart.html destination.

---
**Author:** Fred Davies – Junior QA Automation Engineer