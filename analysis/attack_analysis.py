# attack_analysis.py
def analyze_attack_data(attack_log):
    attack_count = 0
    attackers = {}

    with open(attack_log, 'r') as log_file:
        for line in log_file:
            if "Attack from" in line:
                attack_count += 1
                parts = line.split(" - ")
                address = parts[0].split(":")[1]
                data = parts[1]

                if address in attackers:
                    attackers[address] += 1
                else:
                    attackers[address] = 1

    return attack_count, attackers

def generate_report(attack_count, attackers):
    report = f"Total Attacks: {attack_count}\n\n"
    report += "Attackers:\n"
    for address, count in attackers.items():
        report += f"{address}: {count} attacks\n"

    with open('attack_report.txt', 'w') as report_file:
        report_file.write(report)

if __name__ == "__main__":
    attack_count, attackers = analyze_attack_data('attacks.log')
    generate_report(attack_count, attackers)
