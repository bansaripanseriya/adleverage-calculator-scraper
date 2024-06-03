from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import traceback

def Calculator(net_budget, bud_type, ad_sch):
    try:
        # Set up headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--log-level=3")  # Suppress logs


        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the daily budget calculator page
        driver.get("https://adleverage.com/daily-budget-calculator/")

        # Wait for the page to load
        time.sleep(2)

        # Interact with the page to fill the calculator form
        net_budget_input = driver.find_element(By.ID, "field_t05x2")
        net_budget_input.send_keys(str(net_budget))
        time.sleep(1)

        # Budget Type
        budget_options = driver.find_elements(By.CSS_SELECTOR, "select#field_vgax2 option")

        if bud_type == 1:
            budget_options[0].click()
        elif bud_type == 2:
            budget_options[1].click()
        elif bud_type == 3:
            budget_options[2].click()
        elif bud_type == 4:
            budget_options[3].click()
        time.sleep(1)

        # Ad Schedule
        ad_schedule_options = driver.find_elements(By.CSS_SELECTOR, "select#field_u7j70 option")

        if ad_sch == "a":
            ad_schedule_options[0].click()
        elif ad_sch == "b":
            ad_schedule_options[1].click()
        elif ad_sch == "c":
            ad_schedule_options[2].click()
        time.sleep(1)

        if bud_type == 1:
            # Retrieve the output
            op = driver.find_element(By.CSS_SELECTOR, "span.frm_inline_total")
            if op:
                output = op.text 
                return output
            else:
                return "Daily budget not found"
        else:
            op = driver.find_elements(By.CSS_SELECTOR, "span.frm_inline_total")
            if op:
                output = op[1].text 
                return output
            else:
                return "Daily budget not found"
    
    except Exception as e:
        print(f"Exception: {e}")
        traceback.print_exc()
        if 'driver' in locals():
            driver.quit()
        return None
    
    finally:
        if driver:
            driver.quit()

def main():
    net_budget = float(input("Enter your net budget: "))

    print("Select Budget Type:")
    print("Press [1] for Monthly")
    print("Press [2] for Equalized Weekly")
    print("Press [3] for Manual 4 weeks")
    print("Press [4] for Manual 5 weeks")

    bud_type = int(input("Enter your choice (1-4): "))

    print("Select Ad Schedule:")
    print("Press [a] for M-Sa")
    print("Press [b] for M-Su")
    print("Press [c] for M-F")

    ad_sch = input("Enter your choice (a-c): ")
    
    # Calculate daily budget
    daily_budget = Calculator(net_budget, bud_type, ad_sch)
    print(f"Daily budge: {daily_budget}")
    
if __name__ == "__main__":
    main()