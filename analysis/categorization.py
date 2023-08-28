# categorization.py
def categorize_attacks(attack_log):
    attack_categories = {
        "Brute Force": [],
        "SQL Injection": [],
        "Cross-Site Scripting (XSS)": [],
        "Other": []
    }

    with open(attack_log, 'r') as log_file:
        for line in log_file:
            if "Attack from" in line:
                if "brute" in line.lower():
                    attack_categories["Brute Force"].append(line.strip())
                elif "sql injection" in line.lower():
                    attack_categories["SQL Injection"].append(line.strip())
                elif "xss" in line.lower():
                    attack_categories["Cross-Site Scripting (XSS)"].append(line.strip())
                else:
                    attack_categories["Other"].append(line.strip())

    return attack_categories

def generate_category_reports(attack_categories):
    for category, attacks in attack_categories.items():
        report_filename = f"{category.replace(' ', '_').lower()}_attacks.txt"
        with open(report_filename, 'w') as report_file:
            report_file.write(f"Category: {category}\n\n")
            for attack in attacks:
                report_file.write(f"{attack}\n")

if __name__ == "__main__":
    attack_categories = categorize_attacks('attacks.log')
    generate_category_reports(attack_categories)
