def split_logs(machines):
    
    Counts = {machine: {"INFO": 0, "WARNING": 0, "ERROR": 0} for machine in machines} 
    with open("info.log", "w") as Info_log, open("warning.log", "w") as Warning_log, open("error.log", "w") as Error_log:
        outputs = {"INFO": Info_log, "WARNING": Warning_log, "ERROR": Error_log}

        for machine, log_file in machines.items():
            with open(log_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    for blah in outputs:
                        if f"[{blah}]" in line:
                            outputs[blah].write(f"{machine} | {line}")
                            Counts[machine][blah] += 1
                            break
    return Counts

def print_report(counts, error_file="error.log"):
    print("SECURITY LOG")
    print("=" * 40)
    total_info = 0
    total_warning = 0
    total_error = 0 

    for machine, level in counts.items():
        info += level["INFO"]
        warning += level["WARNING"]
        error += level["ERROR"]
        total = info + warning + error

        if error >= 2:
            status = "CRITICAL!!!!!!"
        elif error == 1 or warning >= 1:
            status = "WARNING!"
        else:
            status = "OK"

        print(f"{machine}: {total} entries | INFO {info} | WARNING {warning} | ERROR {error} | Status: {status}")

        total_info += info
        total_warning += warning
        total_error += error

    print("-" * 40)
    print(f"TOTAL: {total_info + total_warning + total_error} entries | INFO {total_info} | WARNING {total_warning} | ERROR {total_error}")

    print("Errors (see error.log):")
    with open(error_file, "r") as f:
        for line in f:
            print(" " + line.strip())

# Test cases
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")
with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")
counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)
# {'server_a': {'INFO': 3, 'WARNING': 2, 'ERROR': 1}, 'server_b': {'INFO': 3,'WARNING': 1, 'ERROR': 2}}
with open("warning.log", "r") as f:
    print(f.read())

import json
import pickle
import os
def load_incidents(csv_file):
    incidents = []
    with open(csv_file, "r") as f:
       f.readline()
       for line in f:
           parts = line.strip().split(",")
           incidents.append({
               "id": int(parts[0]),
               "machine": parts[1],
               "severity": parts[2],
                "description": parts[3],
           })
    
    return incidents
             

def save_summary(incidents, json_file):
    summary = {"total": len(incidents),
               "by_machine": {},
                "by_severity": {},
                "high_ids": [] 
    }
    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]
        summary["by_machine"][machine] = summary["by_machine"].get(machine, 0) + 1
        summary["by_severity"][severity] = summary["by_severity"].get(severity, 0) + 1
        if severity == "high":
            summary["high_ids"].append(incident["id"])
    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)
    return summary

def archive(incidents, folder):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    by_machine = {}
    for incident in incidents:
        machine = incident["machine"]
        if machine not in by_machine:
            by_machine[machine] = []
        by_machine[machine].append(incident)

    for machine, machine_incidents in by_machine.items():
        with open(os.path.join(folder, machine + ".json"), "w") as f:
            json.dump(machine_incidents, f, indent=2)

    return sorted(os.listdir(folder))
def load_archive(folder):
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)


with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")
incidents = load_incidents("incidents.csv")
print(len(incidents))
# 5
print(incidents[0])
# {'id': 1, 'machine': 'server_a', 'severity': 'high', 'description': 'Account root locked'}
summary = save_summary(incidents, "summary.json")
print(summary)
# {'total': 5, 'by_machine': {'server_a': 2, 'server_b': 3},
# 'by_severity': {'high': 3, 'low': 1, 'medium': 1}, 'high_ids': [1, 2, 5]}
with open("summary.json", "r") as f:
    print(json.load(f) == summary)
# True
print(archive(incidents, "archive"))
# ['incidents.pkl', 'server_a.json', 'server_b.json']
with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])
# [1, 4]
restored = load_archive("archive")
print(restored == incidents)
# True